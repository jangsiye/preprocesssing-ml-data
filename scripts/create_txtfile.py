# If the image doesn't have a txt file, create an empty text file.

# usage : python create_txtfile.py dir_root

import os,sys

global total_create_txt
global total_img
total_create_txt = 0
total_img = 0

def creat_anotation(dir_root):
    global total_create_txt
    global total_img

    image_extension = ['.jpg', '.JPG', '.png', '.PNG', '.jpeg']

    files = os.listdir(dir_root)

    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_onefile = os.path.join(dir_root, file)
        
        # case1) dir
        if os.path.isdir(path_onefile):
            creat_anotation(path_onefile)
        
        # case2) file 
        if fileExtension in image_extension:
            total_img += 1
            txt_path = dir_root + '/' + fileName + '.txt'
            # create empty txt file
            if not os.path.isfile(txt_path):
                txtFile = open(txt_path, 'w')
                txtFile.close()
                total_create_txt += 1
    
def main(argv):
    dir_root = argv[0]
    creat_anotation(dir_root)
    
    print('task Done!\n')

    print(' *** total image : ' + str(total_img))
    print(' *** total create text file : ' + str(total_create_txt))

    print('='*50)

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python create_txtfile.py dir_root")
    else:
        main(sys.argv[1:])
