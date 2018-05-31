# encoding:utf-8
from __future__ import print_function

import jieba
import logging
import sys
import codecs
import traceback
import pandas as pd
import numpy as np
from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn import  cluster
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sqlalchemy import create_engine
import pymysql
import os
import io


def save_file(dirname):
    """
    将多个文件整合并存到3个文件中
    dirname: 原数据目录
    文件内容格式:  类别\t内容
    """
    f_train = io.open('/home/wu/文档/modeling/Scope_data/cnews.train.txt', 'w', encoding='utf-8')
    f_test = io.open('/home/wu/文档/modeling/Scope_data/cnews.test.txt', 'w', encoding='utf-8')
    f_val = io.open('/home/wu/文档/modeling/Scope_data/cnews.val.txt', 'w', encoding='utf-8')
    for cur_file in os.listdir(dirname):   # 分类目录
        filename = os.path.join(dirname, cur_file)
        print(filename)
        content = pd.read_table(filename, 'r', encoding='utf-8', header=None, delimiter="\n")
        n = len(content)
        for i in range(n):
            if i < n * 0.75:
                f_train.write(content.ix[i, 0] + '\n')
            elif i < n * 0.92:
                f_test.write(content.ix[i, 0] + '\n')
            else:
                f_val.write(content.ix[i, 0] + '\n')


    f_train.close()
    f_test.close()
    f_val.close()


if __name__ == '__main__':
    # save_file('/home/wu/PycharmProjects/Scope2/data')
    print(len(io.open('/home/wu/文档/modeling/Scope_data/CNN_RNN/data/cnews/cnews.train.txt', 'r', encoding='utf-8').readlines()))
    print(len(io.open('/home/wu/文档/modeling/Scope_data/CNN_RNN/data/cnews/cnews.test.txt', 'r', encoding='utf-8').readlines()))
    print(len(io.open('/home/wu/文档/modeling/Scope_data/CNN_RNN/data/cnews/cnews.val.txt', 'r', encoding='utf-8').readlines()))
