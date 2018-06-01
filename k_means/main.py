# encoding:utf-8
from __future__ import print_function

import jieba
import logging
import codecs
import traceback
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans
from collections import Counter
from sklearn import metrics
import parameter as pa


class TextCluster(object):
    # 初始化函数,重写父类函数
    def __init__(self):
        pass

    def seg_words(self, sentence):
        seg_list = jieba.cut(sentence)  # 默认是精确模式
        return " ".join(seg_list)       # 分词，然后将结果列表形式转换为字符串

    # 加载用户词典
    def load_userdictfile(self, dict_file):
        jieba.load_userdict(dict_file)

    def load_processfile(self, process_file):
        corpus_list = []
        try:
            fp = open(process_file, "r")
            for line in fp:
                conline = line.strip()
                corpus_list.append(conline)
            return True, corpus_list
        except:
            logging.error(traceback.format_exc())
            return False, "get process file fail"

    def output_file(self, out_file, item):

        try:
            fw = open(out_file, "a")
            fw.write('%s' % (item.encode("utf-8")))
            fw.close()
        except:
            logging.error(traceback.format_exc())
            return False, "out file fail"

    # 释放内存资源
    def __del__(self):
        pass

    def process(self, process_file, tf_ResFileName, tfidf_ResFileName, num_clusters, cluster_ResFileName):
        try:
            sen_seg_list = []
            flag, lines = self.load_processfile(process_file)
            if flag == False:
                logging.error("load error")
                return False, "load error"
            for line in lines:
                for k in pa.l:
                    line = line.replace(k, '')

                sen_seg_list.append(self.seg_words(line))

            # 该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
            tf_vectorizer = CountVectorizer(min_df=0.01)

            # fit_transform是将文本转为词频矩阵
            tf_matrix = tf_vectorizer.fit_transform(sen_seg_list)
            # tf_weight = tf_matrix.toarray()

            # 该类会统计每个词语的tf-idf权值
            # tfidf_transformer = TfidfTransformer()

            # fit_transform是计算tf-idf
            # tfidf_matrix = tfidf_transformer.fit_transform(tf_matrix)
            # print(tfidf_matrix)

            # 获取词袋模型中的所有词语

            # 将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

            # 打印特征向量文本内容

            # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for遍历某一类文本下的词语权重

            # 输出tfidf矩阵

            # 打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重
            # vocab_frame = pd.DataFrame(tf_matrix)

            # 聚类分析
            clusterRes = codecs.open(cluster_ResFileName, 'w', 'utf-8')

            km = KMeans(n_clusters=num_clusters)
            km.fit(tf_matrix)
            order_centroids = km.cluster_centers_.argsort()[:, ::-1]

            for i in range(num_clusters):
                print("Cluster %d words:" % i, end='')

                for ind in order_centroids[i, :6]:  # 每个聚类选 6 个词
                    print(ind)
                    # print(' %s' % tf_matrix.ix[tf_matrix[ind].split(' ')].values.tolist()[0][0].encode('utf-8', 'ignore'),
                    #       end=',')


            print('or : %s'%order_centroids)
            print (metrics.silhouette_score(tf_matrix, km.labels_, metric='euclidean'))
            print (Counter(km.labels_))  # 打印每个类多少人
            # 中心点

            # 每个样本所属的簇
            print(km.inertia_)
            count = 1
            while count <= len(km.labels_):
                clusterRes.write(str(count) + '\t' + str(km.labels_[count - 1]))
                clusterRes.write('\r\n')
                count = count + 1
            clusterRes.close()



        except:
            logging.error(traceback.format_exc())
            return False, "process fail"


# 类似于主函数
if __name__ == "__main__":
    # 获取TextProcess对象
    tc = TextCluster()
    tc.process("data2.txt", "tf_Result.txt", "tfidf_Result.txt", 2, "cluster_Result.txt")
