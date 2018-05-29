# encoding:utf-8

import os
import sys
import re
import jieba
import random
import string
import pandas as pd
from sklearn import metrics

categories = ['服装', '工业', '农业', '运输', '信息', '食品', '建筑', '金融']


def trans_res():
    data = pd.read_table('rnn_pifa.txt', header=None)
    data2 = pd.read_table('result.txt', header=None)
    print(len(data))
    print(len(data2))

    # for i in range(8):

    ff0 = open('data_abs0.txt', 'w')
    ff1 = open('data_abs1.txt', 'w')
    ff2 = open('data_abs2.txt', 'w')
    ff3 = open('data_abs3.txt', 'w')
    ff4 = open('data_abs4.txt', 'w')
    ff5 = open('data_abs5.txt', 'w')
    ff6 = open('data_abs6.txt', 'w')
    ff7 = open('data_abs7.txt', 'w')

    for i in range(len(data2)):
        print(i )
        v = data2.ix[i, 0]
        line = data.ix[i, 0]
        if str(v) == categories[0]:
            ff0.write(line + '\n')
        if str(v) == categories[1]:
            ff1.write(line + '\n')
        if str(v) == categories[2]:
            ff2.write(line + '\n')
        if str(v) == categories[3]:
            ff3.write(line + '\n')
        if str(v) == categories[4]:
            ff4.write(line + '\n')
        if str(v) == categories[5]:
            ff5.write(line + '\n')
        if str(v) == categories[6]:
            ff6.write(line + '\n')
        if str(v) == categories[7]:
            ff7.write(line + '\n')
    ff0.close()
    ff1.close()
    ff2.close()
    ff3.close()
    ff4.close()
    ff5.close()
    ff6.close()
    ff7.close()
if __name__ == '__main__':
    trans_res()
