# Copy specific index information to all txts in the directory.

import os,sys

global cnt 
cnt = 0 

def readFile(masking_txt):
    masking_info = ''
    txtFile = open(masking_txt, 'r')
    lines = txtFile.readlines()
    txtFile.close()

    for line in lines:
        masking_info += line
    
    return masking_info

def makeMasking(masking_info, one_dir):
    global cnt
    files = os.listdir(one_dir)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(one_dir, file)
        
        # case1) 폴더면 재귀
        if os.path.isdir(path_txtfile):
            # print('file : ', file, '는 폴더입니다. 하위문서를 탐색합니다.')
            makeMasking(path_txtfile)
        
        # case2) # If it's a jpg file, open a txt file with the same name and add a masking label.
        if fileExtension == '.png' or fileExtension == '.jpg':
            one_file = one_dir + '/' + fileName + '.txt'
            txtFile = open(one_file, 'a')
            txtFile.write(masking_info)
            txtFile.close() 
            cnt += 1


def main(argv):
    masking_txt = argv[0]
    img_folder = argv[1]
    masking_info = readFile(masking_txt)
    makeMasking(masking_info, img_folder)
    
    print('='*50)
    print('*** making cnt : ', cnt)
    print("-code end-")

if __name__ == "__main__":
    argvsize = 3
    if len(sys.argv) < argvsize:
        print("usage : python make_masking.py masking_txt img_folder")
    else:
        main(sys.argv[1:])
  