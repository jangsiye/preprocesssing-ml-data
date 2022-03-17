
This scripts is based on the YOLO format.  
[YOLO format] class_id center_x center_y width height (normalized [0-1] / .txt anotations)  

### Usage
```
[format] python script.py  
```

- 사용법  
1. Run script.py  
2. Input the dataset root path and the maximum class number.

- 기능  
- script.py : comprehensive script for examining datasets prior to learning
- out_of_index.py : check for labels that are out of the maximum class number.
- pair_files.py : check the pairings of the image and the annotation file match.
- remove_overlap.py : remove duplicate labels. 
- check_base_label.py : check the existence of a base label in a multi-labeled annotation.
- masking_smallbox.py : If the box is too small, change the label to 99 (99 is masking label)
- count_box.py : outputs dataset information.
