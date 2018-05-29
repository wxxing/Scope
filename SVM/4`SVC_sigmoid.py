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

### 测试 gamma ，固定 coef0 为 0 ####
gammas=np.logspace(-2,1)
train_scores=[]
test_scores=[]

for gamma in gammas:
    print(gamma)
    cls=svm.SVC(kernel='sigmoid',gamma=gamma,coef0=0)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
ax=fig.add_subplot(1,2,1)
ax.plot(gammas,train_scores,label="Training score ",marker='+' )
ax.plot(gammas,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_sigmoid_gamma ")
ax.set_xscale("log")
ax.set_xlabel(r"$\gamma$")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)
### 测试 r，固定 gamma 为 0.01 ######
rs=np.linspace(0,5)
train_scores=[]
test_scores=[]

for r in rs:
    print(r)
    cls=svm.SVC(kernel='sigmoid',coef0=r,gamma=0.01)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
ax=fig.add_subplot(1,2,2)
ax.plot(rs,train_scores,label="Training score ",marker='+' )
ax.plot(rs,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_sigmoid_r ")
ax.set_xlabel(r"r")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)
plt.show()
