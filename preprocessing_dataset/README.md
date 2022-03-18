
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
- script.py : checking the suitability of a dataset
- out_of_index.py : checking for labels that are out of the maximum class number.
- pair_files.py : checking the pairings of the image and the annotation file match.
- remove_overlap.py : removing duplicate labels. 
- check_base_label.py : checking the existence of a base label in a multi-labeled annotation.
- masking_smallbox.py : If the box is too small, change the label to 99 (99 is masking label)
- count_box.py : output dataset information.
