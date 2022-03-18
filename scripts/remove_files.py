
# Deleted all files with specific extensions.

import os,sys

global remove_cnt
remove_cnt = 0

def remove_files(root, extension):
    global remove_cnt

    dirs_src = os.listdir(root)
    
    for file in dirs_src:        
        if os.path.isdir(root + '/' + file):
            remove_files(root + '/' + file, extension)

        fileName, fileExtension = os.path.splitext(file)
        
        if not '.' in extension:
            extension = '.' + extension

        if fileExtension == extension:
            remove_cnt += 1
            os.remove(root+'/'+file)

def main(argv):    
    global remove_cnt
    root = argv[0]
    extension = argv[1]
    remove_files(root, extension)

    print('-'*10)
    print('* remove ' + extension + ' cnt : ' + remove_cnt)

if __name__ == "__main__":
    argvsize = 3
    if len(sys.argv) < argvsize:
        print("usage : python remove_files.py root extension")
    else:
        main(sys.argv[1:])
