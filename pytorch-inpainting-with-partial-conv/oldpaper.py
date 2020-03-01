import random
import torch
from PIL import Image
from glob import glob
from PIL import ImageFile

ImageFile.LOAD_TRUNCATED_IMAGES = True

class Oldpaper(torch.utils.data.Dataset):
    def __init__(self, img_root, mask_root, img_transform, mask_transform,
                 split='train'):
        super(Oldpaper, self).__init__()
        self.img_transform = img_transform
        self.mask_transform = mask_transform

        # use about 8M images in the challenge dataset
        if split == 'train':
            self.paths = glob('{:s}/train/annals/*.jpg'.format(img_root),
                              recursive=True)
        else:
            # split validate
            self.paths = glob('{:s}/{:s}/annals/*.jpg'.format(img_root, split))
            #self.paths = glob('./OldPaper_picture/*.jpeg')

        #self.mask_paths = glob('{:s}/*.jpg'.format(mask_root))
        #self.mask_paths = './center_mask_inverse.png'
        self.mask_paths = '/home/ubuntu/context/pytorch-inpainting-with-partial-conv-master/masks/009994.jpg'
        
        self.N_mask = len(self.mask_paths)

    def __getitem__(self, index):
        gt_img = Image.open(self.paths[index])
        gt_img = self.img_transform(gt_img.convert('RGB'))

        #mask = Image.open(self.mask_paths[random.randint(0, self.N_mask - 1)])
        # mask => center mask modified
        mask = Image.open(self.mask_paths)
        mask = self.mask_transform(mask.convert('RGB'))
        return gt_img * mask, mask, gt_img

    def __len__(self):
        return len(self.paths)
