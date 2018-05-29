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

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/demo?charset=utf8')

df = pd.read_sql('select * from scope_jianmo', engine)
df2 = pd.read_excel(u'/home/wu/文档/sc_ca.xlsx')

for j in range(8):
    df3 = df2[df2['cate'] == j]
    df4 = pd.DataFrame()

    for i in range(len(df3)):
        trade = list(df3['trade'])[i]

        df4 = df4.append(df[df['ComSTrade'] == trade])

        df4['ComSScope'].to_csv('%s.csv'%j, index=False)
        print('%s - %s - %s'%(j, trade, len(df4)))
