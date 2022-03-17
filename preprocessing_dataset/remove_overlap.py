# This script removes duplicate labels.

# usage : python remove_overlap.py txt_folder

import os,sys

def overlap(txt_folder):
    files = os.listdir(txt_folder)
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(txt_folder, file)
        
        # case1) dir
        if os.path.isdir(path_txtfile):
            # print('file : ', file, 'is directory. find sub-directory...')
            overlap(path_txtfile)
        
        # case2) file 
        if fileExtension == '.txt':
            txtFile = open(txt_folder + '/' + file, 'r')
            lines = txtFile.readlines()
            txtFile.close() 

            if len(lines) != 0:
                # remove overlap line
                lines = list(set(lines))
                newFile = open(txt_folder + '/' + file, 'w')
                for line in lines :
                    newFile.write(line)
                newFile.close()
    
def main(argv):
    txt_folder = argv[0]
    print('removing overlap line start...')
    overlap(txt_folder)
    print('task Done!\n')
    print('='*50)

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python remove_overlap.py txt_folder")
    else:
        main(sys.argv[1:])
