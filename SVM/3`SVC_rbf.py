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


gammas=range(1,20)
train_scores=[]
test_scores=[]
for gamma in gammas:
    print(gamma)
    cls=svm.SVC(kernel='rbf',gamma=gamma)
    cls.fit(X_train,y_train)
    train_scores.append(cls.score(X_train,y_train))
    test_scores.append(cls.score(X_test, y_test))
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.plot(gammas,train_scores,label="Training score ",marker='+' )
ax.plot(gammas,test_scores,label= " Testing  score ",marker='o' )
ax.set_title( "SVC_rbf")
ax.set_xlabel(r"$\gamma$")
ax.set_ylabel("score")
ax.set_ylim(0,1.05)
ax.legend(loc="best",framealpha=0.5)
plt.show()

