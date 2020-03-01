import os
import glob
import random

import numpy as np
import cv2
from tqdm.auto import tqdm

def cropimage(img_name):
    row_list_top = []
    row_list_top_idx = []
    row_list_bottom = []
    row_list_bottom_idx = []
    img_original = cv2.imread(img_name, 0)
    H_original, W_original = img_original.shape[:2]
    img_resize = cv2.resize(img_original, (512, 512),
                            interpolation=cv2.INTER_LINEAR)
    H_resize, W_resize = img_resize.shape[:2]

    for i in range(int(H_resize/2)):
        row_top = sum(img_resize[i, :])
        row_bottom = sum(img_resize[i+int(H_resize/2), :])

        row_list_top.append(row_top)
        row_list_top_idx.append(row_top)
        row_list_bottom.append(row_bottom)
        row_list_bottom_idx.append(row_bottom)

    row_list_top.sort()
    row_list_bottom.sort()
    top_row = row_list_top[0]
    bottom_row = row_list_bottom[0]
    for i in range(len(row_list_top)):
        if row_list_top_idx[i] == top_row:
            idx_top = i
    for i in range(len(row_list_bottom)):
        if row_list_bottom_idx[i] == bottom_row:
            idx_bottom = i + int(H_resize/2)

    img_temp = img_resize[idx_top:idx_bottom, 0:512]

    return img_temp


path = os.getcwd()
print(path)

path_origin = os.path.join(path, 'oldDB')
os.chdir(path_origin)
image_list = glob.glob('*.jpg')
print(image_list[:5])

line = int(len(image_list) * 0.7)
img_train = image_list[:line]
img_test = image_list[line:]

path_cropped = '/home/ubuntu/context/context_encoder_pytorch-master_ver_1/dataset/train'

print("==============cropped=====================>")

for img in tqdm(img_train):


    img_temp = cropimage(os.path.join(path_origin, img))

#        if i < line:
    cv2.imwrite(os.path.join(path_cropped, '{}.jpg'.format(
        os.path.splitext(img)[0])), img_temp)



for img in tqdm(img_test):

    img_temp = cropimage(os.path.join(path_origin, img))

    cv2.imwrite(os.path.join(os.path.join(
        path, 'context_encoder_pytorch-master_ver_1/dataset/val'), '{}.jpg'.format(os.path.splitext(img)[0])), img_temp)
