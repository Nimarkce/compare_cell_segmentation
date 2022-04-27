# compare_cell_segmentation (with pipeline of CellPose and DSB)

## 2018DSB_script

2018 Data Science Bowl 2nd Place Solution

Codes in utils.py, parallel_model.py, params.py, visualize.py, model_rcnn_weight.py 
are partly adapted from Matterport Mask_RCNN 
(https://github.com/matterport/Mask_RCNN) which is under MIT license. I also used its pre‐
trained weight on MS COCO (https://github.com/matterport/Mask_RCNN/releases).  

Four sources of data were used:  
1. The Revised Train set(https://github.com/lopuhin/kaggle‐dsbowl‐2018‐dataset‐fixes) 
2. 2009 ISBI (http://murphylab.web.cmu.edu/data/2009_ISBI_Nuclei.html) 
3. Weebly (https://nucleisegmentationbenchmark.weebly.com/) 
4. TNBC (https://zenodo.org/record/1175282#.Ws2n_vkdhfA)  
But some of them cannot be find. 
Some masks of the 2009ISBI data set are manually modified. 

To train from scratch
1. correct directory addresses of stage1 train set and stage2 test set accordingly in params.py
2. run eda.py  to load images&masks and save into pandas dataframe from stage1 train set and stage2 test set.
3. correct directory address and run 2009isbi.py weebly.py TNBC.py
4. run resize.py to create image pads of 256*256 size for all the datasets above.
6. run train_ext.py to train from pretrained weight on MSCOCO
7. correct directory address of weight_dir (where the model weight is saved) and run predict_auto.py to predict stage2 test set at four zooms (1/4, 1/2, 1, 2), and generate instance masks accordingly. 
8. correct directory address of weight_dir and run submission.py to combine instance masks from four zooms and mask submission file. 

Or you can use my pretrained weight in the cache folder to make predictions directly. 

#### To run it quickly:
1. correct directory addresses of stage1 train set and stage2 test set accordingly in params.py
2. run eda.py  to load images&masks and save into pandas dataframe from stage1 train set and stage2 test set.
3. correct directory address and run TNBC.py (other two datasets cannot be find)
4. run resize.py to create image pads of 256*256 size for all the datasets above.
5. correct directory address of weight_dir (where the model weight is saved) and run predict_auto.py to predict stage2 test set at four zooms (1/4, 1/2, 1, 2), and generate instance masks accordingly. ***this step is not so easy as you might face lots of problems. Good Luck!***
7. correct directory address of weight_dir and run submission.py to combine instance masks from four zooms and mask submission file. 
8. run NEWSUBMISSION.py to get the visualized results.

## Compare the results from DeepCell and CellPose
The file is in compare/. You need to put all kinds of files mentioned in the jupyter notebook file before run that. The comparing is based on the method from the package: deepcell. It also contains pipeline of CellPose too.

Remember to install comparenv.yml in Compare/ first.
