#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

import numpy as np;


def loopTheta(x, y, theta):
    print("123")


def fit(x, y):
    theta = np.array([0, 0])
    x = np.column_stack((np.array(np.ones(len(x))), x))

    # print(np.dot(theta,x[0]))


    times = 1
    alpha = 0.05

    while times <= 2:
        i=0
        sum = [0,0]
        while i < len(y):
            sum += np.dot((np.dot(theta.transpose(),x[i])-y[i]),x[i])
            i += 1
        theta = theta - alpha * sum
        times += 1

    return theta
