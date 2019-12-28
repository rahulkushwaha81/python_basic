# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 18:21:26 2019

@author: rahul kushwaha
"""

import pandas as pd
import numpy as np
#import matplotlib as mp
import sys as sys

print('python version=>',sys.version)
print('pandas version-> ',pd._version)

print(np.random.randn(5))
s= pd.Series(np.random.randn(5))
print('s=> \n',s)
s= pd.Series(np.random.randn(5),index=list('rahul'))
print('s with index=> \n',s)
print(pd.Series(5,index=list(range(5,15,2))))
d= {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
print(pd.DataFrame(d))

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = list(zip(names,births))
df = pd.DataFrame(data = BabyDataSet, columns=['Names', 'Births'])
print(df)
df.to_csv('births1880.csv',index=False,header=False)

df_read = pd.read_csv('Employee_Sample_100_Copy.csv')
print(df_read)
df_read.info()
df_read.dtypes
print('shape=',df_read.shape)

long_series = pd.Series(np.random.randn(1000))
print(long_series)
print(long_series.head(10))
print(long_series.tail(10))