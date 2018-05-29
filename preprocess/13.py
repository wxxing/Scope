from sklearn.utils import shuffle



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

df= pd.read_sql('select * from scope_jianmo', engine)
print(df)

df = shuffle(df).reset_index(drop=True)
print(df)