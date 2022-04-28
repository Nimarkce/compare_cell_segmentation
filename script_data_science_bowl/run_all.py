#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sept 11 10:13 2021

@author: ly
"""
import os
def main():
    program_to_run = ['eda','TNBC','resize','predict_auto','submission','NEWSUBMISSION']
    for program in program_to_run:
        os.system("python {}.py".format(program))
    print("MISSION COMPLETED!")
    
if __name__ == "__main__":   
    main()
        