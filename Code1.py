# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 15:29:44 2022

@author: Louis
"""
import numpy as np
import networkx as nx
import random
import matplotlib.pyplot as plt

def e_r(n,p): #creates Erdos-Renyi adjacency matrix
    M = np.array([[0]*n]*n)
    for i in range(n):
        for j in range(i):
            if random.random() < p:
                M[i][j] = 1
                M[j][i] = 1
    return M

def cmat(x,y): #creates x by y matrix of zeroes
    P = np.array([[0]*x]*y)
    return P
    


D = 1000 #number of days simulated

wA = 0.02 #death probability in school 1
wB = 0.015 #death probability in school 2
wC = 0.035 #death probability between schools
dA = 0.001 #birth probability in school 1
dB = 0.0006 #birth probability in school 2
dC = 0.00006 #birth probability between schools
eA = 0.0006 #triadic closure strength in school 1
eB = 0.0004 #triadic closure strength in school 2
eC = 0.0001 #triadic closure strength between schools

days = list(range(1,D+1))



fig, axs = plt.subplots(2, 2)
#fig.suptitle('Evolu')


for run in [(0.01,0.01), (0.1,0.1), (0.25,0.25), (0.35,0.15), (0.4, 0.05), (0.15, 0.3), (0.3,0.25),(0.4,0.4)]:
    print(run)
    A = e_r(150, run[0]) #initialise school 1
    n1 = len(A)
    B = e_r(200,run[1]) # initialise school 2
    n2 = len(B)
    C = cmat(n1, n2) #initialise empty between school connections
    Adens = []
    Bdens = []
    Cdens = []
    Totdens = []
    for k in days:
        Asq = A.dot(A)
        Bsq = B.dot(B)
        CtC = (C.transpose()).dot(C)
        CCt = C.dot(C.transpose())
        CA = C.dot(A)
        BC = B.dot(C)
        Adens.append((A.sum())/(n1*(n1-1)))
        Bdens.append((B.sum())/(n2*(n2-1)))
        Cdens.append((C.sum())/(n1*n2))
        Totdens.append((A.sum() + B.sum() + 2*C.sum())/((n1+n2)*(n1+n2-1)))
        
        for i in range(n1):
            for j in range(i):
                if A[i][j] == 1:
                    if random.random() < wA:
                        A[i][j] = 0
                        A[j][i] = 0
                else:
                    if random.random() < (dA + eA*(Asq[i][j]) + CtC[i][j]):
                        A[i][j] = 1
                        A[j][i] = 1
        for i in range(n2):
            for j in range(i):
                if B[i][j] == 1:
                    if random.random() < wB:
                        B[i][j] = 0
                        B[j][i] = 0
                else:
                    if random.random() < (dB + eB*(Bsq[i][j]) + CCt[i][j]):
                        B[i][j] = 1
                        B[j][i] = 1
        for i in range(n2):
            for j in range(n1):
                if C[i][j] == 1:
                    if random.random() < wC:
                        C[i][j] = 0
                else:
                    if random.random() < (dC + eC*(CA[i][j] + BC[i][j])):
                        C[i][j] = 1
    axs[0,0].plot(days, Adens)
    axs[0,1].plot(days, Bdens)
    axs[1,0].plot(days, Cdens)
    axs[1,1].plot(days,Totdens)
                         
axs[0,0].set_title('School 1')
axs[0,1].set_title('School 2')
axs[0,0].set(ylabel='edge density')
axs[0,1].set()
axs[1,0].set_title('Between Schools')
axs[1,1].set_title('Total System')
axs[1,0].set(xlabel='day', ylabel='edge density')
axs[1,1].set(xlabel='day')
plt.savefig('fullmodel.png', dpi = 300)

