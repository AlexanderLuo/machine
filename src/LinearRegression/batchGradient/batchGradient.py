#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

import numpy as np;

def loopTheta(x,y,theta):


    print("123")



def fit(x, y):
    theta=np.array([0,0])
    x = np.column_stack((np.array(np.ones(len(x))), x))
    x = x.transpose()
    times=1
    alpha=0.5


    while times<=1:
        batch=times
        sum=0
        while batch<=len(y):
            sum+=np.dot(theta,x[:,batch-1:batch])-y[batch-1]
            batch+=1
        theta=theta-alpha*sum*x[:,times-1:times]
        times+=1


    return theta


