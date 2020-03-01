import requests
import urllib.request
import os
import pickle
import argparse


# file read folder
path = 'http://db.itkc.or.kr//data/imagedb/BOOK/ITKC_{0}/ITKC_{0}_{1}A/ITKC_{0}_{1}A_{2}{5}_{3}{4}.JPG'

# Manual
label = ['BT', 'MO']
middle = 1400
last = ['A', 'V']  # A ~400 V ~009
num = 10
num1 = 400

fin = ['A', 'B', 'H', 'L']


# file path, save path

# pad for number
def pad(num, width):
    return '%0{}d'.format(width) % num


def save_picture(file_name, save_dir):
    return urllib.request.urlretrieve(file_name, save_dir)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument('-l', '--label', default='BT', type=str, help='BT, MO')
    parser.add_argument('-f', '--fin', default='A', type=str, help='A,B,H,L')

    opt = parser.parse_args()

    # make directory
    if not os.path.exists('oldDB'):
        os.mkdir('oldDB')

    if opt.label == 'BT':
    	for i in range(0, middle+1):
            for k in range(num + 1):
                for j in range(num1 + 1):

                    try:
                        p = path.format(opt.label, pad(i, 4),
                                        'V', pad(j, 3), opt.fin, pad(k, 3))
                        print(p)
                        save_picture(p, './oldDB/{0}_{1}_{2}_{3}_{4}.jpg'.format(
                            opt.label, i, 'V', j, opt.fin))

                    except Exception as e:
                        print(str(e))
                        continue

    elif opt.label == 'MO':        
     	for i in range(0, middle+1):
            for k in range(num1 + 1):
                for j in range(num1 + 1):

                    try:
                        p = path.format(opt.label, pad(i, 4),
                                        'A', pad(j, 3), opt.fin, pad(k, 3))
                        print(p)
                        save_picture(p, './oldDB/{0}_{1}_{2}_{3}_{4}.jpg'.format(
                            opt.label, i, 'A', j, opt.fin))

                    except Exception as e:
                        print(str(e))
                        continue


if __name__ == '__main__':
    main()
