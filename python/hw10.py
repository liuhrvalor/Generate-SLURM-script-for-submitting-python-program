# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 20:26:40 2016

@author: Ryan
"""

import random
import math





pointfile_name="point.txt"
distancefile_name="distancefile.txt"

pointfile=open(pointfile_name,"w")
distancefile=open(distancefile_name,"w")

step=1000
copies=100
"""
If direction=1, left
If direction=2, right
If direction=3, up
If direction=4, down

"""
#  Get the disctance result
for j in range(copies): 
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
            else:
                print "Error"
        
        distance=math.sqrt(x*x+y*y)
        
        x_y_point="("+str(x)+","+ str(y)+ ")"
        
        distancefile.write(str(distance)+"\n")
        pointfile.write(x_y_point+"\n")
        



pointfile.close()
distancefile.close()


#caculate the result

distancepoint=open(distancefile_name,"r")

sum_dis=0.0
count=0.0

for dis in distancepoint:
    sum_dis=sum_dis+float(dis)
    count=count+1.0

average=sum_dis/count

print "grand average is: ", average