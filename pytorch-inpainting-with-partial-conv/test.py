import argparse
import torch
from torchvision import transforms

import opt
from oldpaper import Oldpaper
from evaluation import evaluate
from net import PConvUNet
from util.io import load_ckpt

parser = argparse.ArgumentParser()
# training options
parser.add_argument('--root', type=str, default='./data/')
parser.add_argument('--snapshot', type=str, default='./snapshots/0817/ckpt/950000.pth')
parser.add_argument('--image_size', type=int, default=256)
args = parser.parse_args()

device = torch.device('cuda:0')

size = (args.image_size, args.image_size)

img_transform = transforms.Compose(
    [transforms.Resize(size=size), transforms.ToTensor(),
     transforms.Normalize(mean=opt.MEAN, std=opt.STD)])
     
mask_transform = transforms.Compose(
    [transforms.Resize(size=size), transforms.ToTensor()])

dataset_val = Oldpaper(args.root, 'masks', img_transform, mask_transform, 'validation')
#a, b, c = dataset_val.__getitem__(0)
#print(a,b,c)
model = PConvUNet().to(device)
load_ckpt(args.snapshot, [('model', model)])


model.eval()
evaluate(model, dataset_val, device, 'result_random_val.jpg')
