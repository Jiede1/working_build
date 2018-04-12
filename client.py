# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 16:25:28 2018

@author: yangzhenyu
"""

import pandas as pd
import matplotlib.pyplot as plt
import re

pattern = re.compile(r'1-step')
df = pd.read_csv('D:/Gitlab_pmy/mywork/print.csv')
print(df.head())
#plt.figure(figsize=(15,20))
#df.iloc[:,1:3].plot(subplots=1,kind='line',ylim=(-1,1),xlim=(0,50))