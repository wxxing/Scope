#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import metrics
import sys
from sklearn import svm
from cnews_loader import *
import time
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt


base_dir = '/home/wu/PycharmProjects/git_scope/short-text-classify-master/data/cnews/'
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

X_train, y_train = x_train[:5000], l[:5000]
X_test, y_test = x_val, l2

print('start')

fig=plt.figure()
### 测试 degree ####
degrees=range(1,20)
train_scores=[]
test_scores=[]
for degree in degrees:
    print(degree)
    cls=svm.SVC(kernel='poly',degree=degree)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
ax=fig.add_subplot(1,3,1) # 一行三列
ax.plot(degrees,train_scores,label="Training score ",marker='+' )
ax.plot(degrees,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_poly_degree ")
ax.set_xlabel("p")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)

### 测试 gamma ，此时 degree 固定为 3####
gammas=range(1,20)
train_scores=[]
test_scores=[]
for gamma in gammas:
    print(gamma)
    cls=svm.SVC(kernel='poly',gamma=gamma,degree=3)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
ax=fig.add_subplot(1,3,2)
ax.plot(gammas,train_scores,label="Training score ",marker='+' )
ax.plot(gammas,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_poly_gamma ")
ax.set_xlabel(r"$\gamma$")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)
### 测试 r ，此时 gamma固定为10 ， degree 固定为 3######
rs=range(0,20)
train_scores=[]
test_scores=[]
for r in rs:
    print(rs)
    cls=svm.SVC(kernel='poly',gamma=10,degree=3,coef0=r)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
ax=fig.add_subplot(1,3,3)
ax.plot(rs,train_scores,label="Training score ",marker='+' )
ax.plot(rs,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_poly_r ")
ax.set_xlabel(r"r")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)
plt.show()
