# -*- coding: utf-8 -*-
"""Question 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mwMU4w5C9hk1d5iLQLPSeCER-b_z6ohs
"""

import random
import math

def CreateLists(n):
  y = [[], []]

  for i in range (n):
    y[0].append(random.randint(0, 1))
    y[1].append(random.random())

  return y  

def CrossEntropyLoss(lst, n):
  CEL = 0

  for i in range (n):
    CEL += y[0][i] * math.log2(y[1][i])
    CEL += (1 - y[0][i]) * math.log2(1 - y[1][i])

  CEL /= (-1 * n)

  return CEL

y = CreateLists(100)
CEL = CrossEntropyLoss(y, 100)

print("Cross Entropy Loss Calculated is", CEL)