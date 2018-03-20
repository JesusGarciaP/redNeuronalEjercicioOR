# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:11:00 2018

@author: endJG
"""

x1=[0,0,1,1]
x2=[0,1,0,1]

def g(x,y):
    if((-1+2*x+2*y)<0):
        print("0")
    else:
        print("1")
        
for i in range(len(x1)):
    g(x1[i],x2[i])
    
    


