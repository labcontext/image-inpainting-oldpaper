import os
import glob
import random

import numpy as np
import cv2
from tqdm.auto import tqdm

import torch
from torch.autograd import Variable
import torchvision.transforms as transforms


class ImageChunker(object):

    def __init__(self, rows, cols, overlap):
        self.rows = rows
        self.cols = cols
        self.overlap = overlap

    def perform_chunking(self, img_size, chunk_size):
        """
        Given an image dimension img_size, return list of (start, stop) 
        tuples to perform chunking of chunk_size
        """
        chunks, i = [], 0
        while True:
            chunks.append((i*(chunk_size - self.overlap/2), i *
                           (chunk_size - self.overlap/2)+chunk_size))
            i += 1
            if chunks[-1][1] > img_size:
                break
        n_count = len(chunks)
        chunks[-1] = tuple(x - (n_count*chunk_size - img_size -
                                (n_count-1)*self.overlap/2) for x in chunks[-1])
        chunks = [(int(x), int(y)) for x, y in chunks]
        return chunks

    def get_chunks(self, img, scale=1):
        """
        Get width and height lists of (start, stop) tuples for chunking of img.
        """
        x_chunks, y_chunks = [(0, self.rows)], [(0, self.cols)]
        if img.shape[0] > self.rows:
            x_chunks = self.perform_chunking(img.shape[0], self.rows)
        else:
            x_chunks = [(0, img.shape[0])]
        if img.shape[1] > self.cols:
            y_chunks = self.perform_chunking(img.shape[1], self.cols)
        else:
            y_chunks = [(0, img.shape[1])]
        return x_chunks, y_chunks

    def dimension_preprocess(self, img, padding=True):
        """
        In case of prediction on image of different size than 512x512,
        this function is used to add padding and chunk up the image into pieces
        of 512x512, which can then later be reconstructed into the original image
        using the dimension_postprocess() function.
        """

        # Assert single image input
        assert len(img.shape) == 3, "Image dimension expected to be (H, W, C)"

        # Check if we are adding padding for too small images
        if padding:

            # Check if height is too small
            if img.shape[0] < self.rows:
                padding = np.ones(
                    (self.rows - img.shape[0], img.shape[1], img.shape[2]))
                img = np.concatenate((img, padding), axis=0)

            # Check if width is too small
            if img.shape[1] < self.cols:
                padding = np.ones(
                    (img.shape[0], self.cols - img.shape[1], img.shape[2]))
                img = np.concatenate((img, padding), axis=1)

        # Get chunking of the image
        x_chunks, y_chunks = self.get_chunks(img)

        # Chunk up the image
        images = []
        for x in x_chunks:
            for y in y_chunks:
                images.append(
                    img[x[0]:x[1], y[0]:y[1], :]
                )
        images = np.array(images)
        return images

    def dimension_postprocess(self, chunked_images, original_image, scale=1, padding=True):
        """
        In case of prediction on image of different size than 512x512,
        the dimension_preprocess  function is used to add padding and chunk 
        up the image into pieces of 512x512, and this function is used to 
        reconstruct these pieces into the original image.
        """

        # Assert input dimensions
        assert len(
            original_image.shape) == 3, "Image dimension expected to be (H, W, C)"
        assert len(
            chunked_images.shape) == 4, "Chunked images dimension expected to be (B, H, W, C)"

        # Check if we are adding padding for too small images
        if padding:

            # Check if height is too small
            if original_image.shape[0] < self.rows:
                new_images = []
                for img in chunked_images:
                    new_images.append(
                        img[0:scale*original_image.shape[0], :, :])
                chunked_images = np.array(new_images)

            # Check if width is too small
            if original_image.shape[1] < self.cols:
                new_images = []
                for img in chunked_images:
                    new_images.append(
                        img[:, 0:scale*original_image.shape[1], :])
                chunked_images = np.array(new_images)

        # Put reconstruction into this array
        new_shape = (
            original_image.shape[0]*scale,
            original_image.shape[1]*scale,
            original_image.shape[2]
        )
        reconstruction = np.zeros(new_shape)

        # Get the chunks for this image
        x_chunks, y_chunks = self.get_chunks(original_image)

        i = 0
        s = scale
        for x in x_chunks:
            for y in y_chunks:

                prior_fill = reconstruction != 0
                chunk = np.zeros(new_shape)
                chunk[x[0]*s:x[1]*s, y[0]*s:y[1]*s, :] += chunked_images[i]
                chunk_fill = chunk != 0

                reconstruction += chunk
                reconstruction[prior_fill &
                               chunk_fill] = reconstruction[prior_fill & chunk_fill] / 2

                i += 1

        return reconstruction

# cv Version


def load_img(filename, size=None, scale=None):
    img = cv2.imread(filename)
    if size is not None:
        img = img.resize(size, size)
    elif scale is not None:
        img = img.resize((int(img.size[0] / scale), int(img.size[1] / scale)))

    return img


# PIL version

def load_image(filename, size=None, scale=None):
    img = Image.open(filename)
    if size is not None:
        img = img.resize((size, size), Image.ANTIALIAS)
    elif scale is not None:
        img = img.resize(
            (int(img.size[0] / scale), int(img.size[1] / scale)), Image.ANTIALIAS)
    return img


def show_image(img, key=1, ver='file'):
    # cv2.destroyAllWindows()
    assert key is int
    if ver == 'file':
        origin = cv2.imread(img, cv2.IMREAD_COLOR)
        cv2.imshow('origin', origin)
        cv2.waitKey(key)

    else:  # img
        cv2.imshow('origin', img)
        cv2.waitKey(key)


def save_image(filename, data):
    img = data.clone().add(1).div(2).mul(255).clamp(0, 255).numpy()
    img = img.transpose(1, 2, 0).astype("uint8")
    img = Image.fromarray(img)
    img.save(filename)


# local path setting
path = '/home/ubuntu/context/data'
print(path)

path_cropped = '/home/enliai/Desktop/context_encoder_pytorch-master_ver_1/dataset/train'

# original data path
os.chdir(path)
file_list = os.listdir(os.getcwd())

path_origin = os.path.join()
print(path_origin)

for l in file_list:
    # a,b,...
    os.chdir(os.path.join(path, l))
    image_list = glob.glob('*.jpg')
    print(image_list[:6])

    for i, img in tqdm(enumerate(image_list)):

    try:
        img_temp = cropimage(os.path.join(path_cropped, img))

        cv2.imwrite(os.path.join(path_origin, '{}.jpg'.format(
            os.path.splitext(img)[0])), img_temp)


os.chdir(path_cropped)

line = int(len(image_list) * 0.7)


for i, img in tqdm(enumerate(image_list)):

    try:
        img_temp = cropimage(os.path.join(path_cropped, img))

        if i < line:
        cv2.imwrite(os.path.join(path_origin, '{}.jpg'.format(
            os.path.splitext(img)[0])), img_temp)
#        else:
 #           cv2.imwrite(os.path.join(os.path.join(
  #              path, 'context_encoder_pytorch-master_ver_1/dataset/val'), '{}.jpg'.format(os.path.splitext(img)[0])), img_temp)
    except ValueError as e:
        print(str(e))


# def cropimage(img_name):
#     row_list_top = []
#     row_list_top_idx = []
#     row_list_bottom = []
#     row_list_bottom_idx = []
#     img_original = cv2.imread(img_name, 0)
#     H_original, W_original = img_original.shape[:2]
#     img_resize = cv2.resize(img_original, (256, 256),
#                             interpolation=cv2.INTER_LINEAR)
#     H_resize, W_resize = img_resize.shape[:2]

#     for i in range(int(H_resize/2)):
#         row_top = sum(img_resize[i, :])
#         row_bottom = sum(img_resize[i+int(H_resize/2), :])

#         row_list_top.append(row_top)
#         row_list_top_idx.append(row_top)
#         row_list_bottom.append(row_bottom)
#         row_list_bottom_idx.append(row_bottom)

#     row_list_top.sort()
#     row_list_bottom.sort()
#     top_row = row_list_top[0]
#     bottom_row = row_list_bottom[0]
#     for i in range(len(row_list_top)):
#         if row_list_top_idx[i] == top_row:
#             idx_top = i
#     for i in range(len(row_list_bottom)):
#         if row_list_bottom_idx[i] == bottom_row:
#             idx_bottom = i + int(H_resize/2)

#     img_temp = img_resize[idx_top:idx_bottom, 0:512]

#     return img_temp
