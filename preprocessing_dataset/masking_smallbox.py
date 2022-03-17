# If the box is too small, change the label to 99 (99 is masking label)
# Criteria for boxes that are too small : width < 0.06 or height < 0.08

# usage : python masking_smallbox.py txt_folder

import os,sys

global total_smallbox
total_smallbox = 0

def smallbox(txt_folder):
    global total_smallbox 
    files = os.listdir(txt_folder)
    
    for file in files:    
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(txt_folder, file)
        
        # case1) dir
        if os.path.isdir(path_txtfile):
            # print('file : ', file, 'is directory. find sub-directory...')
            smallbox(path_txtfile)
        
        # case2) file
        if fileExtension == '.txt':
            txtFile = open(txt_folder + '/' + file, 'r')
            lines = txtFile.readlines()
            txtFile.close()

            if len(lines) != 0:
                newFile = open(txt_folder + '/' + file, 'w')
                for line in lines:
                    line_split = line.split(' ')
                    width = float(line_split[3])
                    height = float(line_split[4])
                    
                    if width > 0.06 or height > 0.08:
                        # too big box is passed
                        # if width < 0.8 and height < 0.8:
                        newFile.write(line)

                    # If the box is too small, change the label to 99
                    else:
                        print('having small box : ' + txt_folder + '/' + file)
                        masking_line = '99 ' + line_split[1] + ' ' + line_split[2] + ' ' + line_split[3] + ' ' + line_split[4]
                        newFile.write(masking_line)
                        total_smallbox += 1
                newFile.close()

def main(argv):
    txt_folder = argv[0]
    smallbox(txt_folder)
    print('task Done!\n')
    print(' *** total masking smallbox : ' + str(total_smallbox))
    print('='*50)
    
if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python masking_smallbox.py txt_folder")
    else:
        main(sys.argv[1:])
