# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 14:31:03 2016

@author: Ryan
"""

import random
import math

step=1000

"""
If direction=1, left
If direction=2, right
If direction=3, up
If direction=4, down

"""
#  Get the disctance result
x=0
y=0
for i in range(step):            
            direction=random.randint(1, 4)
            if direction==1:
                x=x-1
            elif direction==2:
                x=x+1
            elif direction==3:
                y=y+1
            elif direction==4:
                y=y-1

        
distance=math.sqrt(x*x+y*y)
        
print (distance)

#caculate the result







