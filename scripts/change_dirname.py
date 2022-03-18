
# Chanage sub-directory name

import os,sys

def changeName(directory):
    # imageExtension = ['.jpg', '.JPG', '.png', '.PNG', '.jpeg']
    cnt = 0

    files = os.listdir(directory)
    
    for file in files:
        # fileName, fileExtension = os.path.splitext(file)
        onepath = os.path.join(directory, file)

        # change dir name
        if os.path.isdir(onepath):
            dir = onepath[:onepath.rfind('\\')+1]
            new_filepath = 'test' + str(cnt).zfill(1)
            os.rename(onepath, dir+new_filepath)
            cnt += 1

        # Delete anything other than image files in the directory
        # if not fileExtension in imageExtension :
        #     os.remove(onepath)

def main(argv):
    dir_root = argv[0]
    changeName(dir_root)
    print('='*50)
    print("-code end-")

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python change_dirname.py dir_root")
    else:
        main(sys.argv[1:])
