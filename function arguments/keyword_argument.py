#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 14:25:10 2019

@author: root
"""

def keyword(a,r):
    if(a>r):
        print("A is greater than R");
    else:
        print("R is greater than A");
a=int(input("Enter the a value"));
b=int(input("Enter the b value"));
keyword(a,b);
keyword(a=a,r=b);
keyword(r=a,a=b);