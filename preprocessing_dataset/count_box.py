# This script outputs dataset information.
# - total images, total annotations, total objects, ratio of objects...

# usage : python count_box.py dir_root

import os,sys
import time

def count_box(dataset_root_path, info_dict):
    files = os.listdir(dataset_root_path)
    
    for file in files:
        fileName, fileExtension = os.path.splitext(file)
        path_full = os.path.join(dataset_root_path, file)
        
        # case1) dir
        if os.path.isdir(path_full):
            count_box(path_full, info_dict)

        if fileExtension.lower() in ['.jpg', '.png']:
            info_dict['total_img'] += 1

        # case2) file 
        if fileExtension == '.txt':
            info_dict['total_txt'] += 1
            
            txtFile = open(dataset_root_path + '/' + file, 'r', encoding='cp949')   # or utf-8
            lines = txtFile.readlines()
            txtFile.close() 
            
            # Delete not labeled images.
            # if len(lines) != 1:
            #     os.remove(dataset_root_path + '/' + file)
            #     os.remove(dataset_root_path + '/' + fileName + '.jpg')
                
            if len(lines) != 0:
                
                for line in lines:
                    info_dict['total_box'] += 1
                    line_split = line.split(' ')
                    try:
                        label = int(line_split[0])
                    except:
                        print(dataset_root_path + '/' + file)
                        continue             
                    
                    # Record the path of the image with a specific label.
                    # if label == 3:
                    #     #print(dataset_root_path + '/' + file)
                    #     truckfile = open(r"./list.txt", 'a')
                    #     truckfile.write(dataset_root_path + '/' +  file + '\n')
                    #     truckfile.write(dataset_root_path + '/' +  fileName + '.jpg' + '\n')
                    #     truckfile.close()

                    # count box
                    if label in info_dict['mydict'] :
                        info_dict['mydict'][label] = info_dict['mydict'][label] + 1
                    else :
                        info_dict['mydict'][label] = 1
            else : 
                info_dict['empty_img'] += 1

    return info_dict

def main(argv):
    dir_root = argv[0]
    info_dict = {'mydict':{}, 'total_box':0, 'total_img':0, 'total_txt':0, 'empty_img':0}

    start_time = time.time()
    info_dict = count_box(dir_root, info_dict)
    print("---{}s seconds---".format(time.time()-start_time))

    print('count box Done!')
    
    sort_mydict = sorted(info_dict['mydict'].items())
    print()
    
    class_index = []
    object_cnt = []

    result = ''
    for key, value in sort_mydict:
        class_index.append(str(key))
        object_cnt.append(value)
        
        percent = value / info_dict['total_box'] * 100

        result += f"class {key:2d} {value:5d} ({percent:6.2f} %)\n"
    result += ' -----'
    result += '\ntotal img : ' + str(info_dict['total_img'])
    result += '\ntotal txt : ' + str(info_dict['total_txt']) + ' (empty : ' + str(info_dict['empty_img']) + ')'
    result += '\ntotal box : ' + str(info_dict['total_box']) + ' (100 %)'

    print(result)

if __name__ == "__main__":
    argvsize = 2
    if len(sys.argv) < argvsize:
        print("usage : python count_box.py dir_root")
    else:
        main(sys.argv[1:])

