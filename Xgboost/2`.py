import numpy as np
#2. 数据集
from sklearn import datasets

#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import metrics
import sys
from sklearn import svm
from Xgboost.cnews_loader import *
import time
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.datasets import load_boston
from sklearn.cross_validation import train_test_split
from sklearn.metrics import r2_score, auc

base_dir = '/home/wu/文档/modeling/Scope_data/cnews/'
train_dir = os.path.join(base_dir, 'cnews.train.txt')
test_dir = os.path.join(base_dir, 'cnews.test.txt')
val_dir = os.path.join(base_dir, 'cnews.val.txt')
vocab_dir = os.path.join(base_dir, 'cnews.vocab.txt')

categories, cat_to_id = read_category()
words, word_to_id = read_vocab(vocab_dir)

x_train, y_train = process_file(train_dir, word_to_id, cat_to_id)
x_val, y_val = process_file(val_dir, word_to_id, cat_to_id)
l = []
l2 = []
for i in y_train:
    a = list(i).index(1)
    l.append(a)
for i in y_val:
    a = list(i).index(1)
    l2.append(a)

X_train, y_train = x_train, l
X_test, y_test = x_val, l2


train_x, test_x, train_y, test_y = X_train, X_test, y_train, y_test

print(len(test_x))
print(len(test_y))
print(len(train_x))
print(len(train_y))
print('start')
#4. Xgboost建模
#4.1 模型初始化设置
import xgboost as xgb
dtrain=xgb.DMatrix(train_x,label=train_y)
dtest=xgb.DMatrix(test_x)

params={'booster':'gbtree',
    'objective': 'multi:softmax',
    'eval_metric': 'auc',
    'max_depth':4,
    'lambda':10,
    'subsample':0.75,
    'colsample_bytree':0.75,
    'min_child_weight':2,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1
        }

watchlist = [(dtrain,'train')]

#4.2 建模与预测
bst=xgb.train(params,dtrain,num_boost_round=100,evals=watchlist)
#print(dtest)
d=xgb.DMatrix(np.array([5.1,0.5,6.4,2]).reshape(1,4))
print(bst.predict(d))
#ypred=bst.predict(dtest)
#print(ypred)
# 设置阈值, 输出一些评价指标
#y_pred = (ypred >= 0.5)*1
'''
from sklearn import metrics
print('AUC: %.4f' % metrics.roc_auc_score(test_y,ypred))
print('ACC: %.4f' % metrics.accuracy_score(test_y,y_pred))
print('Recall: %.4f' % metrics.recall_score(test_y,y_pred))
print('F1-score: %.4f' %metrics.f1_score(test_y,y_pred))
print('Precesion: %.4f' %metrics.precision_score(test_y,y_pred))
print(metrics.confusion_matrix(test_y,y_pred))
'''
#4.3 可视化输出

#4.3.1 得分
ypred = bst.predict(dtest)
#print(ypred)

#4.3.2 所属的叶子节点
ypred_leaf = bst.predict(dtest, pred_leaf=True)
#print(ypred_leaf)

#xgb.to_graphviz(bst, num_trees=0)
#bst.dump_model("model.txt")

ypred_contribs = bst.predict(dtest, pred_contribs=True)
#print(ypred_contribs)
score_a = sum(ypred_contribs[0])
#print(score_a)
# -1.38121373579
score_b = sum(ypred_contribs[1])
#print(score_b)
# 1.41094945744