
# reduce the number of files with specific extension to 1/N.
# you can change file extension.

# python remove_files.py dir_root extension N(reduce_number)

import os,sys

global cnt
cnt = 0
global remove_cnt
remove_cnt = 0

def remove_files(dir_root, extention, N):
    global cnt
    global remove_cnt
    
    files = os.listdir(dir_root)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)        

        # case 1) dir
        if os.path.isdir(dir_root + '/' + file):
            continue
            # remove_files(dir_root + '/' + file, extention, N)

        if not '.' in extension:
            extension = '.' + extension

        # case 2) file
        if fileExtension == extention:
            cnt += 1
            if cnt % N != 0:
                remove_cnt += 1
                os.remove(dir_root+'/'+file)

def main(argv):
    global cnt
    global remove_cnt

    dir_root = argv[0]
    extension = argv[1]
    N = argv[2]
    cnt = 0
    remove_files(dir_root, extension, N) 

    print('total file : ' + str(cnt))
    print('remove file : ' + str(remove_cnt))

if __name__ == "__main__":
    argvsize = 4
    if len(sys.argv) < argvsize:
        print("usage : python remove_files.py dir_root extenstion N(reduce_number)")
    else:
        main(sys.argv[1:])
