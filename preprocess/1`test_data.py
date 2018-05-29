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

engine = create_engine('mysql+pymysql://root:123456@127.0.0.1/demo?charset=utf8')

df= pd.read_sql('select * from scope_jianmo', engine)

l2 = ['批发业', '纺织业', '橡胶和塑料制品业', '商务服务业', '纺织服装、服饰业', '印刷和记录媒介复制业', '科技推广和应用服务业', '零售业', '专业技术服务业', '通用设备制造业', '其他制造业', '其他金融业', '非金属矿物制品业', '金属制品业', '皮革、毛皮、羽毛及其制品和制鞋业', '研究和试验发展', '农、林、牧、渔服务业', '居民服务业', '造纸和纸制品业', '新闻和出版业', '化学原料和化学制品制造业', '仪器仪表制造业', '软件和信息技术服务业', '酒、饮料和精制茶制造业', '货币金融服务', '仓储业', '建筑装饰和其他建筑业', '机动车、电子产品和日用产品修理业', '化学纤维制造业', '文教、工美、体育和娱乐用品制造业', '装卸搬运和运输代理业', '土木工程建筑业', '道路运输业', '房地产业', '食品制造业', '专用设备制造业', '电气机械和器材制造业', '其他服务业', '废弃资源综合利用业', '互联网和相关服务', '金属制品、机械和设备修理业', '有色金属冶炼和压延加工业', '农业', '住宿业', '资本市场服务', '汽车制造业', '文化艺术业', '电信、广播电视和卫星传输服务', '医药制造业', '家具制造业', '铁路、船舶、航空航天和其他运输设备制造业', '娱乐业', '租赁业', '体育', '木材加工和木、竹、藤、棕、草制品业', '保险业', '教育', '煤炭开采和洗选业', '烟草制品业', '计算机、通信和其他电子设备制造业', '非金属矿采选业', '广播、电视、电影和影视录音制作业', '房屋建筑业', '黑色金属冶炼和压延加工业', '水上运输业', '邮政业', '农副食品加工业', '建筑安装业', '生态保护和环境治理业', '餐饮业', '卫生', '黑色金属矿采选业', '铁路运输业', '电力、热力生产和供应业', '畜牧业', '林业', '水的生产和供应业', '公共设施管理业', '航空运输业', '渔业', '石油加工、炼焦和核燃料加工业', '开采辅助活动', '有色金属矿采选业', '燃气生产和供应业', '社会工作']

# for j in l2:
l = []
l1=[]
for i in range(len(df)):
    st = df['ComSTrade'][i]
    sc = df['ComSScope'][i]

    if str(st) == '医药制造业':
        l1.append(sc)
        if '设备' in str(sc):
            l.append(sc)
            print(sc)


print('%s '%(len(l1)))
print(len(l)/float(len(l1)))
'''
批发业
纺织业
橡胶和塑料制品业
商务服务业
纺织服装、服饰业
印刷和记录媒介复制业
科技推广和应用服务业
零售业
专业技术服务业
通用设备制造业
其他制造业
其他金融业
非金属矿物制品业
金属制品业
皮革、毛皮、羽毛及其制品和制鞋业
研究和试验发展
农、林、牧、渔服务业
居民服务业
造纸和纸制品业
新闻和出版业
化学原料和化学制品制造业
仪器仪表制造业
软件和信息技术服务业
酒、饮料和精制茶制造业
货币金融服务
仓储业
建筑装饰和其他建筑业
机动车、电子产品和日用产品修理业
化学纤维制造业
文教、工美、体育和娱乐用品制造业
装卸搬运和运输代理业
土木工程建筑业
道路运输业
房地产业
食品制造业
专用设备制造业
电气机械和器材制造业
其他服务业
废弃资源综合利用业
互联网和相关服务
金属制品、机械和设备修理业
有色金属冶炼和压延加工业
农业
住宿业
资本市场服务
汽车制造业
文化艺术业
电信、广播电视和卫星传输服务
医药制造业
家具制造业
铁路、船舶、航空航天和其他运输设备制造业
娱乐业
租赁业
体育
木材加工和木、竹、藤、棕、草制品业
保险业
教育
煤炭开采和洗选业
烟草制品业
计算机、通信和其他电子设备制造业
非金属矿采选业
广播、电视、电影和影视录音制作业
房屋建筑业
黑色金属冶炼和压延加工业
水上运输业
邮政业
农副食品加工业
建筑安装业
生态保护和环境治理业
餐饮业
卫生
黑色金属矿采选业
铁路运输业
电力、热力生产和供应业
畜牧业
林业
水的生产和供应业
公共设施管理业
航空运输业
渔业
石油加工、炼焦和核燃料加工业
开采辅助活动
有色金属矿采选业
燃气生产和供应业
社会工作
'''