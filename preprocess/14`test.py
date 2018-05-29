# coding=utf8
from __future__ import print_function

import jieba
import codecs
import pandas as pd
import parameter as pa
from sqlalchemy import create_engine
import re
import string
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from sklearn.utils import shuffle


# clus = 0
categories = ['服装', '工业', '农业', '运输', '信息', '食品', '建筑', '金融']

for clus in range(8):
    f0 = codecs.open('rnn_%s.txt'%clus, 'w', 'utf-8')

    df = pd.read_csv('./data_source/%s.csv'%clus,encoding='utf-8', header=None)

    df = shuffle(df).reset_index(drop=True)

    for i in range(len(df)):
        scopes = df.ix[i, 0]
        if scopes == None:  # 如果经营范围为空
            pass  # 跳过

            # scopes = jieba.cut(scopes)
        elif pd.isnull(scopes):  # 如果公司ID为空
            pass  # 跳过

        elif scopes == '':  # 如果经营范围为空
            pass  # 跳过

        else:



            d = {'【': '(', '】': ')', '（': '(', '）': ')', '...': '', '〓': '',
                 '**': '','＆':'','“':'','”':''}  # 替换符号
            for k, v in d.items():
                scopes = scopes.replace(k, v)  # 替换

            pattern = re.compile(r"(?<=[(])[^()]+\.*?[^()]+(?=[)])")  # 括号的正则表达式

            for ret in range(4):#防止括号内还有括号，此代码执行两次

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

                    f0.write(categories[int(clus)] + '\t' + "".join(scopes).encode('utf-8') + '\n')
    f0.close()
