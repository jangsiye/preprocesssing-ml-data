# The script that gives a header to a image file names.

# usage : python change_filename_header.py dir_root header

import os,sys

def changeFileName_Header(directory, new_name):
    imageExtension = ['.jpg', '.JPG', '.png', '.PNG', '.jpeg']

    files = os.listdir(directory)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        onepath = os.path.join(directory, file)

        # case1) dir - recursive
        if os.path.isdir(onepath):
            print('file : ', file, 'is directory...')
            changeFileName_Header(onepath, new_name)

        # case2) 이미지 파일이면 이름 변경
        if fileExtension in imageExtension :
            file = file.replace(" ","")
            new_filename = new_name + file
            new_filepath = os.path.join(directory, new_filename)
            os.rename(onepath, new_filepath)

                
def main(argv):
    dir_root = argv[0]
    new_name = argv[1] + '_'
    changeFileName_Header(dir_root, new_name)
    print('='*50)
    print("-code end-")

if __name__ == "__main__":
    argvsize = 3
    if len(sys.argv) < argvsize:
        print("usage : python change_filename_header.py dir_root header")
    else:
        main(sys.argv[1:])
