
# The script that divides files into N files regardless of the extension.

# usage : python divide_files.py dir_root N(divided number)

import os,sys
import shutil

global cnt
cnt = 0
global dir_cnt
dir_cnt = 1

def divided(root, num):
    global cnt
    global dir_cnt
    
    files = os.listdir(root)

    new_dir = ''

    for file in files:
        fileName, fileExtension = os.path.splitext(file)        

        # case 1) dir
        # Skip the sub-directory
        if os.path.isdir(root + '/' + file):
            # print('file : ', file, 'is directory. find sub-directory...')
            continue

            # If you want to include sub-directory
            # divided(root + '/' + file, num)

        # case 2) files
        if cnt == 0:
            # If you want to change dir name
            new_dir = root + '/' + 'dir_' + str(dir_cnt).zfill(1)
            os.mkdir(new_dir)
            dir_cnt += 1
            cnt += 1
            print('make dir ' + new_dir)
        elif cnt < (int(num)-1):
            cnt += 1
        elif cnt == (int(num)-1):
            cnt = 0

        shutil.move(root + '/' + file, new_dir)
        
def main(argv):
    global cnt

    root = argv[0]
    num = argv[1]
    divided(root, num)

    print('* count of directory : ' + str(dir_cnt+1))
    print("* last directory\'s cnt : " + str(cnt))

if __name__ == "__main__":
    argvsize = 3
    if len(sys.argv) < argvsize:
        print("usage : python divide_files.py dir_root N(divided number)")
    else:
        main(sys.argv[1:])
