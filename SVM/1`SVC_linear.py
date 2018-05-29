#!/usr/bin/python
# -*- coding: utf-8 -*-

from sklearn import metrics
import sys
from sklearn import svm
from cnews_loader import *
import time
from datetime import timedelta
import pandas as pd


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

x_train, y_train = x_train[:5000], l[:5000]
x_test, y_test = x_val, l2

print('start')
cls = svm.SVC(kernel='linear')
cls.fit(x_train, y_train)

print('Coefficients:%s, intercept %s'%(cls.coef_, cls.intercept_))
print('Score: %.2f'%cls.score(x_test, y_test))
