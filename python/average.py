# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:35:12 2016

@author: Ryan
"""

infile=open("totaldistance.txt","r")

count=0.0
sumdis=0.0

def FloatOrZero(value):
    try:
        return float(value)
    except:
        return 0.0

for f in infile:
          
        dis=FloatOrZero(f)
        sumdis=sumdis+dis
        count=count+1.0
        
    
average=sumdis/count

print average

infile.close()