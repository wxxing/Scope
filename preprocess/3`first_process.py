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


clus = 0

f0 = codecs.open('daa_%s.txt'%clus, 'w', 'utf-8')

df = pd.read_csv('./data_source/%s.csv'%clus,encoding='utf-8', header=None)

for i in range(len(df)):
    scopes = df.ix[i, 0]
    if scopes == None:  # 如果经营范围为空
        pass  # 跳过
    elif '建筑' in scopes:
        print(scopes)
    elif '食品' in scopes:
        print(scopes)
    elif '金融' in scopes:
        print(scopes)
    # elif '服装' in scopes:
    #     print(scopes)
    # elif '针织' in scopes:
    #     print(scopes)
    # elif '纺织' in scopes:
    #     print(scopes)
    elif '设备' in scopes:
        print(scopes)
    # elif '制造' in scopes:
    #     print(scopes)

    else:

        d = {'；': ';', '，': ',', '。': '', '【': '(', '】': ')', '（': '(', '）': ')', '...': '', '〓': '',
             '**': '','、':'','：':'','＆':'','“':'','”':''}  # 替换符号
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
        for k in pa.l3:  # 将l3中的词去掉
            scopes = scopes.replace(k, '')
        for k in pa.l:  # 将l3中的词去掉
            scopes = scopes.replace(k, '')
        for k in pa.l2:  # 将l3中的词去掉
            scopes = scopes.replace(k, '')


        add = '!,;:?"\'、**...；;:,【】（）()...〓'
        scopes = re.sub("[{}]+".format(string.punctuation + add + string.digits), "", scopes)

        scopes = jieba.cut(scopes)
        if pd.isnull(scopes):  # 如果公司ID为空
            pass  # 跳过

        elif scopes == None:  # 如果经营范围为空
            pass  # 跳过
        else:

            f0.write(str(clus) + '\t' + " ".join(scopes).encode('utf-8') + '\n')
f0.close()
