# -*- coding: utf-8 -*-
# @Time    : 18/4/11 上午11:33
# @Author  : Edward
# @Site    :
# @File    : information_gain.py
# @Software: PyCharm Community Edition

import re
from collections import defaultdict, Counter

import jieba
from sklearn.feature_selection import mutual_info_classif
from sklearn.feature_extraction.text import CountVectorizer


class InformationGain(object):

    def __init__(self, sentences, labels, cutter=jieba.cut):
        """
        初始化ig
        :param sentences: 句子列表
        :param labels: 每个句子的类别
        :param cutter: 分词器，默认为jieba，如果处理英文文本传入 lambda x: x.split(' ')即可
        """
        self.cutter = cutter
        self.sentences = [re.sub('[\n\t\r\b ]', '', sentence) for sentence in sentences]
        self.labels = labels
        self.sentences_words_list = [self.sentence2words(sentence) for sentence in sentences]

        label_words = defaultdict(list)
        for index in range(len(self.labels)):
            label_words[self.labels[index]] += self.sentences_words_list[index]
        self.labels_words_dict = {key: Counter(label_words[key]) for key in label_words.keys()}

        self.label_dict = dict(zip(list(set(self.labels)), range(len(set(self.labels)))))
        self.X = [' '.join(words) for words in self.sentences_words_list]
        self.y = [self.label_dict.get(item) for item in self.labels]
        self.X_vec = None
        self.ig_score = None
        self.cal_ig(self.X, self.y)

    def sentence2words(self, sentence):
        """
        将句子转化为词列表
        :param sentence: 句子
        :return: [w1, w2, ...]
        """
        return [word for word in self.cutter(sentence)]

    def cal_ig(self, x, y):
        """
        计算information gain值
        :param x: 用空格隔开的词列表的列表
        :param y: X每一项的类别
        """
        cv = CountVectorizer(
            max_df=0.95,
            min_df=1,
            max_features=100000,
            # 抽取规则，默认是只抽取两个字以上的词
            token_pattern=r'(?u)\b\w+\b',
        )
        self.X_vec = cv.fit_transform(x)
        res = dict(zip(
            cv.get_feature_names(),
            mutual_info_classif(self.X_vec, y, discrete_features=True)
        ))
        self.ig_score = res

    def get_top(self, top_n=100, label=None, sort_by_count=False):
        """
        获取信息增益最高的词
        :param top_n: 返回前n个，默认为100
        :param label: 指定某个label里的关键词
        :param sort_by_count: 是否在指定的前n个词中按照出现次数进行排序
        :return: [[w1, s1], [w2, s2], ...]
        """
        
        if label is None:
            return sorted(self.ig_score.items(), key=lambda x: -x[1])[:top_n]
        elif label in self.labels_words_dict:
            leave_items = [
                item for item in self.ig_score.items()
                if self.labels_words_dict[label][item[0]] == max(
                    map(lambda x: self.labels_words_dict[x][item[0]], self.labels_words_dict.keys())
                )
            ]
            ret = sorted(leave_items, key=lambda x: -x[1])[:top_n]

            if sort_by_count:
                new_ret = []
                for one in ret:
                    new_ret.append((one[0], one[1], self.labels_words_dict[label][one[0]]))
                return sorted(new_ret, key=lambda x: -x[-1])
            else:
                return ret


if __name__ == '__main__':
    sentences = [
        u'我想吃红烧牛肉',
        u'我想吃牛肉拉面',
        u'我想要去旅游',
        u'我旅游去的大理了',
        u'那个牛肉挺好吃的',
        u'下次去玩想去海南'
    ]

    labels = [
        u'饮食',
        u'饮食',
        u'旅行',
        u'旅行',
        u'饮食',
        u'旅行'
    ]

    ig = InformationGain(sentences, labels)

    for each in ig.get_top(10):
        print (each[0], each[1])
