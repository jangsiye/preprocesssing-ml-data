
# Average image resolution measurement of the dataset.

import os,sys
from PIL import Image, ImageDraw

global total_w
total_w = 0
global total_h
total_h = 0
global cnt
cnt = 0

def average_wh(dir_root):
    global total_w
    global total_h
    global cnt
    
    imgs = os.listdir(dir_root)
    for item in imgs:
        fileName, fileExtension = os.path.splitext(item)

        if os.path.isdir(dir_root + '/' + item):
            print('dir ' + dir_root + '/' + item + '...')
            average_wh(dir_root + '/' + item)
            
        if fileExtension == '.jpg' or fileExtension == '.JPG' or fileExtension == '.png' or fileExtension == '.PNG':
            img_path = dir_root + '/' + item
            im = Image.open(img_path)
            w,h = im.size

            total_w += w
            total_h += h
            cnt+=1

def main(argv):    
    dir_root = argv[0]
    average_wh(dir_root)
    print('*** avg width : ', total_w/cnt)
    print('*** avg height : ', total_h/cnt)

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python average_width_height.py dir_root")
    else:
        main(sys.argv[1:])
