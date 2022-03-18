
# The scripts to rename files in directory.
# You can specify the new name and extension.

import os,sys

global cnt 

def renameFile(directory, file, new_name, extension):
    global cnt

    filepath = os.path.join(directory, file)
    new_filename = new_name + str(cnt).zfill(1) + extension
    new_filepath = os.path.join(directory, new_filename)

    try :
        os.rename(filepath, new_filepath)
        print(str(cnt) + ' change filename.\n')
        cnt += 1    # Change file name and increase number
    except FileExistsError :    # If the file name already exists,
        print(new_name + str(cnt).zfill(1) + ' is already exist! plus number...\n')
        # rename a file by increasing the number
        cnt += 1
        renameFile(directory, file, new_name, extension)
    
def changeFileName(directory, new_name, extension):
    global cnt

    print(directory)
    files = os.listdir(directory)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        onepath = os.path.join(directory, file)

        # case1) dir - recursive
        if os.path.isdir(onepath):
            changeFileName(onepath, new_name, extension)

        # case2) Change the file name with the specified extension
        if fileExtension == extension:
            renameFile(directory, file, new_name, extension)

def main(argv):
    global cnt
    cnt = 1
    dir_root = argv[0]
    new_name = argv[1]
    extension = argv[2]

    if not '.' in extension:
        extension = '.' + extension

    changeFileName(dir_root, new_name, extension)

    print('='*50)
    print("-code end-")


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print('useage : python change_filename.py dir_root new_name extension')
    else:
        main(sys.argv[1:])
