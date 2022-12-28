# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 01:10:53 2022

@author: Louis
"""

import numpy as np
import matplotlib.pyplot as plt



D = 1000
a = 0.3
n1 = 150 
b = 0.3
n2 = 200
c = 0



wA = 0.02
wB = 0.015
wC = 0.035
dA = 0.001
dB = 0.0006
dC = 0.00006
eA = 0.0006
eB = 0.0004
eC = 0.0001

days = list(range(1,D+1))
alist = []
blist = []
clist = []
totlist = []

for k in days:
    alist.append(a)
    blist.append(b)
    clist.append(c)
    totlist.append((a*n1*(n1 - 1) + b*n2*(n2 - 1) + c*n1*n2*2)/(n1*(n1 - 1) + n2*(n2 - 1) + n1*n2*2))
    anew = (1 - wA)*a + (1 - a)*(dA + eA*((n1 - 2)*a**2 + n2*c**2))
    bnew = (1 - wB)*b + (1 - b)*(dB + eB*((n2 - 2)*b**2 + n1*c**2))  
    cnew = (1 - wC)*c + (1 - c)*(dC + eC*((n1 - 1)*a*c + (n2 - 1)*b*c))
    a = anew
    b = bnew
    c = cnew
    
fig, axs = plt.subplots(2, 2)
axs[0,0].plot(days, alist)
axs[0,1].plot(days, blist)
axs[1,0].plot(days, clist)
axs[1,1].plot(days, totlist)
axs[0,0].set_title('School 1')
axs[0,1].set_title('School 2')
axs[0,0].set(ylabel='edge density')
axs[0,1].set()
axs[1,0].set_title('Between Schools')
axs[1,1].set_title('Total System')
axs[1,0].set(xlabel='day', ylabel='edge density')
axs[1,1].set(xlabel='day')

