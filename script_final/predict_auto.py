#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:41:27 2018

@author: work
"""
import os, glob
from predict_test import predict_test_rcnn_two, predict_test_rcnn, \
                        predict_test_rcnn_half, predict_test_rcnn_quarter, \
                        get_mask, get_mask_scale, get_cons_scale, get_cons
                        #First you should exam these Function carefully.
                        
from params import DsbConfig
from load import load_from_cache_multi, save_to_cache_multi, load_from_cache, \
                    save_to_cache

def main():
    config = DsbConfig()
    df_name = 'stage2_df'               #df might means a DataFrame in RAM
    save_name = 'stage2'
    ###################################################################################
    weight_dir = '..//cache//UnetRCNN_180410-221747'
    #correct directory address where model weight for prediction is saved
    ##################################################################################
    
    ##ATT that the weight may be the pertrained weight by the file maker
    predict_test_rcnn(df_name, weight_dir)
    print("predict_test_rcnn_ finished ")
    predict_test_rcnn_half(df_name, weight_dir)
    print("pre_half")
    predict_test_rcnn_quarter(df_name, weight_dir)
    print("pre_quarter")
    predict_test_rcnn_two(df_name, weight_dir)
    print("pre_two")
    #combine predictions for zoom 2
    ##the following code means only get stage2_df_two_1,2,3....25.dat if there are stage2_df_two_1_1,2,3 then combine it to stage2_df_two_1 and delete the original, but where is the stage2_df_two???##
    for nb in range(25):
        try:
            fl = os.path.join(weight_dir, 'stage2_df_two_{}.dat'.format(nb))
            if os.path.exists(fl):
                continue
            else:
                fls = glob.glob(os.path.join(weight_dir, 'stage2_df_two_{}_*.dat'.format(nb)))
                preds_df = load_from_cache_multi(fl[:-4], len(fls))
                save_to_cache(preds_df, fl)
                for fl in fls:
                    os.remove(fl)
        except:
            print("-----------------an error occurs in nb=={}---------------------".format(nb))

                
                
    get_mask(df_name, config, weight_dir, save_name)
    print("get_mask-successed")
    get_mask_scale(df_name, config, weight_dir, save_name, tag='half')
    print("getmaskscale tag=='half'successed")
    get_mask_scale(df_name, config, weight_dir, save_name, tag='quarter')
    print("get_masksccale tag=='quarter'successed")
    get_mask_scale(df_name, config, weight_dir, save_name, tag='two')

    print("tag=two s")

    get_cons(df_name, weight_dir)
    print("get_cons successed")
    get_cons_scale(df_name, weight_dir, tag='half')
    print("getconsscale tag='half' suc")
    get_cons_scale(df_name, weight_dir, tag='quarter')
    print("tag='quarter',s")
    get_cons_scale(df_name, weight_dir, tag='two')
    print("all succeed")
if __name__ == '__main__': 
    main()

