# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 08:59:20 2018

@author: kristin
"""
"""
##############################
#
#   PONTE, Kristin Diane B.
#   CPE451L
#   11/10/18
#
##############################
"""
import numpy as np
import matplotlib.pyplot as plt
#declarations of variables and range
n = np.arange(-10,21)
a = []
#equation
a.append(1*(n==0) - 1*(n==7))
a.append(1*(n>=0) - 1*(n>=9))
#outside function of differential equation
def diff(a):
    a_ = np.roll(a, 1)
    a_[0] = 0
    y = a - a_

    return y
#outside function of integral equation
def inte(a):
    y = np.zeros(len(a))
    for i in range(0, len(a)):
        if i is 0:
            y[0] = a[0]
        else:
            w = y[i-1]
            y[i] = w + a[i]
    return y

#arrays
diffY = [diff(a[0]), diff(a[1])]
inteY = [inte(a[0]), inte(a[1])]

title = 'Plot 3212aDIFF y(n) = x(n)-x(n-1)'
title += '\nKDBPonte | CPE451L | Oct 11, 2018'
#plot design for differential A
f, x = plt.subplots(2)
f.suptitle(title)
x[0].stem(n, a[0])
x[1].stem(n, diffY[0])
x[0].grid()
x[1].grid()
x[1].set_xlabel('n')
x[0].set_ylabel('x(n)')
x[1].set_ylabel('y(n)')
title = title.replace('aDIFF', 'aINTE', 1) #changing of label aD to aI
title = title.replace('x(n)-x(n-1)','y(n-1)+x(n)',1) #changing of diffeq to inteq
#plot design for integral A
f, x = plt.subplots(2)
f.suptitle(title)
x[0].stem(n, a[0])
x[1].stem(n, inteY[0])
x[0].grid()
x[1].grid()
x[1].set_xlabel('n')
x[0].set_ylabel('x(n)')
x[1].set_ylabel('y(n)')
title = title.replace('aINTE', 'bDIFF', 1) #changing of label aI to bD
title = title.replace('y(n-1)+x(n)','x(n)-x(n-1)',1) #changing of inteq to diffeq
#plot design for differential B
f, x = plt.subplots(2)
f.suptitle(title)
x[0].stem(n, a[1])
x[1].stem(n, diffY[0])
x[0].grid()
x[1].grid()
x[1].set_xlabel('n')
x[0].set_ylabel('x(n)')
x[1].set_ylabel('y(n)')
title = title.replace('bDIFF', 'bINTE', 1) #changing of label bD to bI
title = title.replace('x(n)-x(n-1)','y(n-1)+x(n)',1) #changing of diffeq to inteq
#plot design for integral B
f, x = plt.subplots(2)
f.suptitle(title)
x[0].stem(n, a[1])
x[1].stem(n, inteY[1])
x[0].grid()
x[1].grid()
x[1].set_xlabel('n')
x[0].set_ylabel('x(n)')
x[1].set_ylabel('y(n)')

plt.show()

