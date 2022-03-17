# train data pre-processing

from subprocess import call
import sys
import os
import shutil

# pwd setting
pwd = os.getcwd()
pwd = pwd.replace('\\','/')

dataset_path = input('Input train_dataset_path : ')
if dataset_path.find('\\') != -1 :
    dataset_path = dataset_path.replace('\\', '/')
dataset_path += '/'

max_class = input('Input max class number : ')

print('-------------------------------------------------')
print('|     * check yourself about multi-label *      |')
print('| base label setting : person (0) / vehicle (7) |')
print('-------------------------------------------------')

check_base_label = input('=> Is it OK? [Y/N] :')
if check_base_label == 'y' or check_base_label == 'Y':
    print()
else:
    print('Please check your multi-label and come back.')
    print('If you have any change, go to "check_base_label.py" and fix labels.')
    sys.exit()

# exception
error_flag = 0
if len(dataset_path) == 0 | len(max_class) == 0 :
    print('[ERROR] Input dataset_path or max_class !!! ')
    error_flag += 1
if not os.path.isdir(dataset_path):
    print('[ERROR] dataset_path is not exist !!! ')
    error_flag += 1
if not max_class.isdigit():
    print('[ERROR] max_class is not digit !!!')
    error_flag += 1

if error_flag != 0:
    sys.exit()

# 1. masking smallbox
print('[ masking smallbox ]')
cmd = 'python masking_smallbox.py ' + dataset_path
call(cmd, shell=True)

# 2. image masking & remove masking index
print('[ image masking ]')
cmd = 'python remove_masking_new.py ' + dataset_path
call(cmd, shell=True)

# 3. check out of lable number
print('[ check out of lable number ]')
cmd = 'python out_of_index.py ' + dataset_path + ' ' + max_class
call(cmd, shell=True)

# 4. check base label
print('[ check base label ]')
cmd = 'python check_base_label.py ' + dataset_path
call(cmd, shell=True)

# 5. remove overlap box
print('[ remove overlap box ]')
cmd = 'python remove_overlap.py ' + dataset_path
call(cmd, shell=True)

# 6. check pair files (jpg&txt)
print('[ check pair files ]')
cmd = 'python pair_files.py ' + dataset_path
call(cmd, shell=True)

# 7. count label box
print('[ count label box ]')
cmd = 'python count_box.py ' + dataset_path
call(cmd, shell=True)


