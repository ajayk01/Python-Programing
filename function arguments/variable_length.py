#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:16:51 2019

@author: root
"""

def length(*a):
    count=0;
    count1=0;
    for i in a:
        if(i>10):
            count+=1;
        else:
            count1+=1;
    print("The no of elements above 10 is ",count,"below 10 is ",count1);
length(56,78,2,5,100,65,7);
