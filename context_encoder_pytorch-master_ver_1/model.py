import torch
import torch.nn as nn
import torch.nn.functional as F

# class PConv(nn.Conv2d):
#     def __init__(self, *args, **kwargs):
#         if 'multi_channel' in kwargs:
#             self.multi_channel = kwargs['multi_channel']
#             kwargs.pop('multi_channel')
#         else:
#             self.multi_channel = False

#         if 'return_mask' in kwargs:
#             self.return_mask = kwargs['return_mask']
#             kwargs.pop('return_mask')
#         else:
#             self.return_mask = False

#         super(PConv, self).__init__(*args, **kwargs)

#         if self.multi_channel:
#             self.weight_maskUpdater = torch.ones(
#                 self.out_channels, self.in_channels, self.kernel_size[0], self.kernel_size[1])
#         else:
#             self.weight_maskUpdater = torch.ones(
#                 1, 1, self.kernel_size[0], self.kernel_size[1])

#         self.slide_winsize = self.weight_maskUpdater.shape[1] * \
#             self.weight_maskUpdater.shape[2] * self.weight_maskUpdater.shape[3]
#         self.last_size = (None, None, None, None)
#         self.update_mask = None
#         self.mask_ratio = None

#     def forward(self, input, mask_in=None):
#         assert len(input.shape) == 4

#         if mask_in is not None or self.last_size != tuple(input.shape):
#             self.last_size = tuple(input.shape)

#             with torch.no_grad():
#                 if self.weight_maskUpdater.type() != input.type():
#                     self.weight_maskUpdater = self.weight_maskUpdater.to(input)

#                 if mask_in is None:
#                     if self.multi_channel:
#                         mask = torch.ones(
#                             input.data.shape[0], input.data.shape[1], input.data.shape[2], input.data.shape[3]).to(input)

#                     else:
#                         mask = torch.ones(
#                             1, 1, input.data.shape[2], input.data.shape[3]).cuda()

#                 else:
#                     mask = mask_in

#                 self.update_mask = F.conv2d(mask, self.weight_maskUpdater, bias=None,
#                                             stride=self.stride, padding=self.padding, dilation=self.dilation, groups=1)
#                 self.mask_ratio = self.slide_winsize / \
#                     (self.update_mask + 1e-8)
#                 self.update_mask = torch.clamp(self.update_mask, 0, 1)
#                 self.mask_ratio = torch.mul(self.mask_ratio, self.update_mask)

#         raw_out = super(PConv, self).forward(
#             torch.mul(input, mask) if mask_in is not None else input)

#         if self.bias is not None:
#             bias_view = self.bias.view(1, self.out_channels, 1, 1)
#             output = torch.mul(raw_out - bias_view,
#                                self.mask_ratio) + bias_view
#             output = torch.mul(output, self.update_mask)

#         else:
#             output = torch.mul(raw_out, self.mask_ratio)

#         if self.return_mask:
#             return output, self.update_mask
#         else:
#             return output


class _netG(nn.Module):
    def __init__(self, opt):
        super(_netG, self).__init__()
        self.ngpu = opt.ngpu
        self.main = nn.Sequential(
            # input is (nc) x 256 x 256
            # input is (nc) x 128 x 128
            nn.Conv2d(opt.nc, opt.nef, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            #PConv(opt.nc, opt.nef, 4, 2, 1, bias=False),
            nn.Conv2d(opt.nc, opt.nef, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (nef) x 64 x 64
            #PConv(opt.nc, opt.nef, 4, 2, 1, bias=False),
            nn.Conv2d(opt.nef, opt.nef, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.nef),
            nn.LeakyReLU(0.2, inplace=True),
            #PConv(opt.nc, opt.nef*2, 4, 2, 1, bias=False),
            nn.Conv2d(opt.nef, opt.nef*2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.nef*2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (nef*2) x 16 x 16
            #PConv(opt.nc*2, opt.nef*4, 4, 2, 1, bias=False),
            nn.Conv2d(opt.nef*2, opt.nef*4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.nef*4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (nef*4) x 8 x 8
            #PConv(opt.nc*4, opt.nef*8, 4, 2, 1, bias=False),
            nn.Conv2d(opt.nef*4, opt.nef*8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.nef*8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (nef*8) x 4 x 4
            #PConv(opt.nef*8, opt.nBottleneck, 4, bias=False),
            nn.Conv2d(opt.nef*8, opt.nBottleneck, 4, bias=False),

            # tate size: (nBottleneck) x 1 x 1
            nn.BatchNorm2d(opt.nBottleneck),
            nn.LeakyReLU(0.2, inplace=True),
            # input is Bottleneck, going into a convolution
            nn.ConvTranspose2d(opt.nBottleneck, opt.ngf * \
                               8, 4, 1, 0, bias=False),
            nn.BatchNorm2d(opt.ngf * 8),
            nn.ReLU(True),
            # state size. (ngf*8) x 4 x 4
            nn.ConvTranspose2d(opt.ngf * 8, opt.ngf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ngf * 4),
            nn.ReLU(True),
            # state size. (ngf*4) x 8 x 8
            nn.ConvTranspose2d(opt.ngf * 4, opt.ngf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ngf * 2),
            nn.ReLU(True),
            # state size. (ngf*2) x 16 x 16
            nn.ConvTranspose2d(opt.ngf * 2, opt.ngf, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ngf),
            nn.ReLU(True),
            # state size. (ngf) x 32 x 32
            nn.ConvTranspose2d(opt.ngf, opt.nc, 4, 2, 1, bias=False),
            nn.Tanh()
            # state size. (nc) x 64 x 64
        )

    def forward(self, input):
        if isinstance(input.data, torch.cuda.FloatTensor) and self.ngpu > 1:
            output = nn.parallel.data_parallel(
                self.main, input, range(self.ngpu))
        else:
            output = self.main(input)
        return output


class _netlocalD(nn.Module):
    def __init__(self, opt):
        super(_netlocalD, self).__init__()
        self.ngpu = opt.ngpu
        self.main = nn.Sequential(
            # input is (nc) x 64 x 64
            nn.Conv2d(opt.nc, opt.ndf, 4, 2, 1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf) x 32 x 32
            nn.Conv2d(opt.ndf, opt.ndf * 2, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ndf * 2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*2) x 16 x 16
            nn.Conv2d(opt.ndf * 2, opt.ndf * 4, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ndf * 4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*4) x 8 x 8
            nn.Conv2d(opt.ndf * 4, opt.ndf * 8, 4, 2, 1, bias=False),
            nn.BatchNorm2d(opt.ndf * 8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size. (ndf*8) x 4 x 4
            nn.Conv2d(opt.ndf * 8, 1, 4, 1, 0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        if isinstance(input.data, torch.cuda.FloatTensor) and self.ngpu > 1:
            output = nn.parallel.data_parallel(
                self.main, input, range(self.ngpu))
        else:
            output = self.main(input)

        return output.view(-1, 1)
