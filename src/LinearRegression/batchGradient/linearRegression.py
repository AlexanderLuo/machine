#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

#
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import time
import batchGradient

a = time.time()
####加载数据集
diabetes = datasets.load_diabetes()
# ####仅仅使用一个特征：
diabetes_X = diabetes.data[:, np.newaxis, 2]
# ###s数据划分训练集和测试集
diabetes_X_train = diabetes_X[:-20]
# diabetes_X_test = diabetes_X[-20:]
# ###目标划分为训练集和测试集
diabetes_y_train = diabetes.target[:-20]
# diabetes_y_test = diabetes.target[-20:]
theta = batchGradient.fit(diabetes_X_train, diabetes_y_train)
print(theta)

plt.plot(diabetes_X_train, diabetes_y_train, 'rx')



x = np.linspace(-0.1, 0.18)
y = theta[1]+theta[0]*x
#
plt.plot(x,y)
plt.show()


# ###训练模型
# regr = linear_model.LogisticRegression()
# regr.fit(diabetes_X_train, diabetes_y_train)
# ###回归系数
# print('Coefficients:\n', regr.coef_)
# ##散点图
# plt.scatter(diabetes_X_test,diabetes_y_test,color='black')
# plt.plot(diabetes_X_test,regr.predict(diabetes_X_test),color='blue',linewidth=3)
# plt.xticks()
# plt.yticks()
# plt.show()
