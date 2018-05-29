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
import parameter as pa
from sklearn import  cluster
from sklearn.metrics import adjusted_rand_score
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sqlalchemy import create_engine
import pymysql
from sklearn.utils import shuffle
import re
import string

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/demo?charset=utf8')

df = pd.read_sql('select * from scope_jianmo', engine)

f0 = codecs.open('rnn_pifa.txt', 'w', 'utf-8')

df5 = df['ComSScope']
df5 = shuffle(df5).reset_index(drop=True)

for i in range(len(df5)):
    scopes = df5.ix[i, 0]
    if scopes == None:  # 如果经营范围为空
        pass  # 跳过

        # scopes = jieba.cut(scopes)
    elif pd.isnull(scopes):  # 如果公司ID为空
        pass  # 跳过

    elif scopes == '':  # 如果经营范围为空
        pass  # 跳过

    else:

        d = {'【': '(', '】': ')', '（': '(', '）': ')', '...': '', '〓': '',
             '**': '', '＆': '', '“': '', '”': ''}  # 替换符号
        for k, v in d.items():
            scopes = scopes.replace(k, v)  # 替换

        pattern = re.compile(r"(?<=[(])[^()]+\.*?[^()]+(?=[)])")  # 括号的正则表达式

        for ret in range(4):  # 防止括号内还有括号，此代码执行两次

            l = re.findall(pattern, scopes)  # 找到括号，并存入l列表
            if len(l) == 0:  # 如果列表为空
                pass
            else:  # 如果列表不为空
                for j in range(len(l)):  # 遍历表
                    scopes = scopes.replace('(%s)' % l[j], '')  # 删除括号及内容

        add = '!?"\'**...【】（）()...〓'

        scopes = re.sub("[{}]+".format(string.punctuation + add + string.digits), "", scopes)
        if scopes == None:  # 如果经营范围为空
            pass  # 跳过

            # scopes = jieba.cut(scopes)
        elif pd.isnull(scopes):  # 如果公司ID为空
            pass  # 跳过

        elif scopes == '':  # 如果经营范围为空
            pass  # 跳过

        else:

            f0.write("".join(scopes) + '\n')
f0.close()
