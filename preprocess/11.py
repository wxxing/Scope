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
import sys
reload(sys)
sys.setdefaultencoding('utf8')

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/exhi?charset=utf8')
engine2 = create_engine('mysql+pymysql://root:123456@127.0.0.1/demo?charset=utf8')

# df= pd.read_sql('select * from ComStandard2', engine)
#
# df[['ComSTrade', 'ComSScope']].to_sql('scope_jianmo', engine2, if_exists='append', index=False)

df= pd.read_sql('select * from 17春季天眼查a', engine2)

df.rename(columns = {u'行业':'ComSTrade', u'经营范围':'ComSScope'}, inplace=True)
print(df)
df[['ComSTrade', 'ComSScope']].to_sql('scope_jianmo', engine2, if_exists='append', index=False)

print(len(df))