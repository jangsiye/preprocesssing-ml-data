# This script is that checks the existence of a base label in a multi-labeled annotation.
# Based on the YOLO format.
# [YOLO format] class_id center_x center_y width height (normalized [0-1] / .txt anotations)

# usage : python check_base_label.py dir_root

import os,sys

global total_add_base
total_add_base = 0
# global total_remove_file
# total_remove_file = 0
global classes_dict
global person_labels
global vehicle_labels

# example
classes_dict = {
    'person':'0',
    'male':'1',
    'female':'2',
    'adult':'3',
    'child':'4',
    'vehicle':'5',
    'smallcar':'6',
    'sedan':'7',
    'suv':'8',
    'truck':'9',
    'bus':'10',
}

# multi-labels
person_labels = ['male', 'female', 'adult', 'child']
vehicle_labels = ['smallcar', 'sedan', 'suv', 'truck', 'bus']

def check_base_label(root):
    global total_add_base
    global classes_dict
    global person_labels
    global vehicle_labels

    files = os.listdir(root)

    for file in files:
        mydict = {}
        fileName, fileExtension = os.path.splitext(file)
        path_txtfile = os.path.join(root, file)
        
        # case1) dir
        if os.path.isdir(path_txtfile):
            # print('file : ', file, 'is directory. find sub-directory...')
            check_base_label(path_txtfile)
        
        # case2) file 
        if fileExtension == '.txt':
            txtFile = open(root + '/' + file, 'r')
            lines = txtFile.readlines()
            txtFile.close() 

            if len(lines) != 0:
                mydict = {}                 # key : coordinate, value : label
                xywhList = []
                lines = list(set(lines))    # remove overlap line
                
                # seperate label, coordinate
                for line in lines:
                    line_split = line.split(' ')
                    label = line_split[0]
                    coordinate = line_split[1] + ' ' + line_split[2] + ' ' + line_split[3] + ' ' + line_split[4]

                    if not coordinate in mydict :
                        xywhList.append(coordinate)
                        mydict[coordinate] = []
                        mydict[coordinate].append(label)
                    else :
                        mydict[coordinate].append(label)
                
                
                newFile = open(root + '/' + file, 'a')
                for xywh in xywhList:
                    # person
                    for mlabel in person_labels:
                        if classes_dict[mlabel] in mydict[xywh]:
                            if not classes_dict['person'] in mydict[xywh]:
                                newline = classes_dict['person'] + ' ' + xywh
                                newFile.write(newline)
                                total_add_base += 1
                                print('add label person(0) - ' + root + '/' + file)
                    # vehicel
                    for mlabel in vehicle_labels:
                        if classes_dict[mlabel] in mydict[xywh]:
                            if not classes_dict['vehicle'] in mydict[xywh]:
                                newline = classes_dict['vehicle'] + ' ' + xywh
                                newFile.write(newline)
                                total_add_base += 1
                                print('add label vehicel(5) - ' + root + '/' + file)                   
                newFile.close()

                # [Application] 
                # If anotation file has a base-label but do not have a multi-label, delete data.
                # for xywh in xywhList:    
                #     if classes_dict['vehicle'] in mydict[xywh]:
                #         # 'smallcar', 'sedan', 'suv', 'truck', 'bus'
                #         for multilbael in vehicle_labels:
                #             if not classes_dict[multilbael] in mydict[xywh]:
                #                 os.remove(root + '/' + fileName + '.jpg')
                #                 os.remove(root + '/' + fileName + '.txt')
                #                 print('no have multi-label! Remove ' + root + '/' + file)
                #                 total_remove_file += 1
                #                 break      
    
def main(argv):
    root = argv[0]
    check_base_label(root)
    print('task Done!\n')
    print(' *** total add base label : ' + str(total_add_base))
    # print(' *** total remove file : ' + str(total_remove_file))
    print('='*50)

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python check_base_label.py dir_root")
    else:
        main(sys.argv[1:])
