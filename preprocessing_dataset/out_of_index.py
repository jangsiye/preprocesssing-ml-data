
# This script checks for labels that are out of the maximum class number.

# usage : python out_of_index.py dir_root classes_max_num

import os,sys

global total_out
total_out = 0

def find_out_index(dir_root, classes_max_num):
    global total_out
    
    files = os.listdir(dir_root)

    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(dir_root, file)
        
        # case1) dir
        if os.path.isdir(path_txtfile):
            # print('file : ', file, 'is directory. find sub-directory...')
            find_out_index(path_txtfile, classes_max_num)
        
        # case2) file 
        if fileExtension == '.txt':
            txtFile = open(dir_root + '/' + file, 'r')
            lines = txtFile.readlines()
            txtFile.close() 

            if len(lines) != 0:
                # check out of index
                for line in lines:
                    line_split = line.split(' ')
                    if int(line_split[0]) > int(classes_max_num):
                        print('out of label - ' + line_split[0] + ' : ' + dir_root + '/' + file)
                        total_out += 1
    
def main(argv):
    dir_root = argv[0]
    classes_max_num = argv[1]
    print('-- classes_max_num : ' + classes_max_num)
    find_out_index(dir_root, classes_max_num)
    print('task Done!\n')
    print(' *** total out of lable : ' + str(total_out))
    print('='*50)

if __name__ == "__main__":
    argvsize = 3
    if len(sys.argv) < argvsize:
        print("usage : python out_of_index.py dir_root classes_max_num")
    else:
        main(sys.argv[1:])

