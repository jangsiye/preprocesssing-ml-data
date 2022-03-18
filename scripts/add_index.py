# If there is a file with an index of 0 in yolo format, add 4 in the same coordinate.
# ex) Add an adult label if a human label exists

import os,sys

global cnt 
cnt = 0 

def addLabel(txt_folder):
    global cnt
    files = os.listdir(txt_folder)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(txt_folder, file)
        
        # case1) 폴더면 재귀
        if os.path.isdir(path_txtfile):
            print('file : ', file, '는 폴더입니다. 하위문서를 탐색합니다.')
            addLabel(path_txtfile)
        
        # case2) 파일이면 인덱스들만 읽어와서 저장
        if fileExtension == '.txt':
            txtFile = open(txt_folder + '/' + file, 'r')
            lines = txtFile.readlines()
            txtFile.close()
            
            if len(lines) != 0:                    
                for line in lines:
                    line_split = line.split(' ')
                    # 0 person 
                    # 4 adult
                    if line_split[0] == '0':
                        copyline = '4 ' + line_split[1] + ' ' + line_split[2] + ' ' + line_split[3] + ' ' + line_split[4]                   
                        txtFile = open(txt_folder + '/' + file, 'a')
                        txtFile.write(copyline)
                        txtFile.close()
                        # print(fileName)
                        cnt += 1

    print('*** cnt : ', cnt)

def main(argv):
    dir_root = argv[0]
    addLabel(dir_root)
    print('='*50)
    print("-code end-")

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python add_index.py dir_root")
    else:
        main(sys.argv[1:])

  

