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




print('start')
clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
clf_res = clf.fit(x_train, l)

print('testing')
train_pred = clf_res.predict(x_train)

result_train = metrics.accuracy_score(l, train_pred)

test_pred = clf_res.predict(x_val)

result_test = metrics.accuracy_score(l2, test_pred)

print(dict({"train": result_train, "test": result_test}))
#{'test': 0.6815052776502983, 'train': 0.831793460454754}