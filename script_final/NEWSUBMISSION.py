#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thr Sept 9 20:21 2021 

@author: liyang
"""

#This file must run after running submission.py, just for visualize the result and save it to a dir(../sub_img)

from load import load_from_cache
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from params import stage2_dir
def save_to_imgs(d_f,affix=' ',dirname='predimg'):
    for i in range(len(d_f.index)):
        try:
            plt.imsave(r"..//{}//{}_{}.png".format(dirname,d_f['id'][i],affix),d_f['image'][i])
        except:
            os.system("mkdir ..//{}".format(dirname))
            plt.imsave(r"..//{}//{}_{}.png".format(dirname,d_f['id'][i],affix),d_f['image'][i])
            
def main():
    weight_dir = '../cache/UnetRCNN_180410-221747'
    dat=load_from_cache(os.path.join(weight_dir, 'preds_df_scale_01'))
    preds_df=dat
    df = load_from_cache('stage2_df')
    pred_fin=pd.DataFrame()
    pred_fin['id']=df.id
    pred_fin['image']=preds_df['pred']
    test_dir=stage2_dir
    test_ids = sorted(list(os.listdir(test_dir)))
    # test_ids = list(next(os.walk(test_dir)))[1]
    test_df = []
    for id_ in test_ids:
        try:
            id_ = id_[:-4]
            path = os.path.join(test_dir, id_+'.png')
            image = cv2.imread(path)
            test_df.append({'id':id_, 'image':image, 'path': path, 
                             'shape':image.shape})
        except:
             print("the error occurs in:{}".format(id_))
    test_df = pd.DataFrame(test_df).sort_values('shape').reset_index()
    save_to_imgs(test_df,affix='original',dirname='BIGPRED_IMG')
    save_to_imgs(pred_fin,'pred',dirname='BIGPRED_IMG')
if __name__ == "__main__":   
    main()