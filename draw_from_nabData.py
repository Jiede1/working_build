# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 11:40:34 2018

@author: pangmingyu
"""

'''为目录的子目录下的所有数据文件生成图像并保存'''

import pandas as pd
import os
import matplotlib.pyplot as plt

dir = 'D:\RichStone_Work\data'
list = os.listdir(dir)  #查看目录下的子目录和文件
k=58
df=[]
for i in range(k):
    df.append([])
i=0
for line in list:
    path = os.path.join(dir,line)
    if os.path.isdir(path):
        for li in os.listdir(path):
            li = os.path.join(path,li)
            if os.path.isfile(li):
                file = pd.read_csv(li)
                df[i] = file
                df[i].columns = ['timestamp',li]
                plt.figure() 
                print(df[i].iloc[:,1].plot(subplots=False))
                plt.legend()
                ax = df[i].plot() 
                fig = ax.get_figure()
                fig.savefig(li[:-4]+'.png')
                i+=1
                #break
    elif os.path.isfile(path):
        pass
    #break
print(k)

            


