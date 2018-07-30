# -*- coding: utf-8 -*-
# @Time    : 18/7/27 上午10:40
# @Author  : Edward
# @Site    :
# @File    : tfidf.py
# @Software: PyCharm Community Edition

from collections import Counter

import jieba
from gensim.models import TfidfModel
from gensim.corpora.dictionary import Dictionary


class TfIdf(object):
    '''
    该类适用于文本关键词抽取或同性质特征抽取任务
    该类使用TfIdf模型抽取关键词

    >>> sentences = ['a b c d', 'a b c e', 'a c c e', 'b a e d']

    >>> tfidf = TfIdf(sentences, cutter=lambda x: x.split(' '))
    >>> ret = tfidf.get_sentence_key_words('c e f g')
    >>> ret
    [('c', 0.7071067811865476), ('e', 0.7071067811865476)]
    >>> ret = tfidf.get_key_words()
    >>> ret
    [('b', 3), ('c', 3), ('e', 3)]
    '''

    def __init__(self, sentences, stop_words=set(), cutter=jieba.cut):
        '''
        初始化TfIdf特征抽取器

        :param sentences: 文本列表
        :param stop_words: 停用词表，需要为list/set/tuple
        :param cutter: 分词方式，默认为使用jieba分词处理中文，如果要处理英文或者其他分词方式，只要丢入一个分词函数就OK
        '''
        self.stop_words = set(stop_words)
        self.cutter = cutter
        self.common_texts = [
            [word for word in cutter(sentence) if word not in self.stop_words]
            for sentence in set(sentences)
            if isinstance(sentence, str)
        ]
        self.common_dictionary = Dictionary(self.common_texts)
        self.common_corpus = [self.common_dictionary.doc2bow(text) for text in self.common_texts]

        self.tfidf = TfidfModel(self.common_corpus)
        self.vectors = [
            self.tfidf[self.common_corpus[index]]
            for index in range(len(self.common_corpus))
            if self.tfidf[self.common_corpus[index]
            ]
        ]

    def get_key_words(self, top_n=10, top_word=1):
        '''
        获取初始化文本中的关键词
        计算方式是通过获取每个句子中，tfidf值最高的top_word个词。然后统计出现次数获得的
        :param top_n: 返回前top_n个关键词
        :param top_word: 每个句子的前top_word个词
        :return: 返回列表，每一项分别为(词, 词频)
        '''
        top_word_index = [
            sorted(vector, key=lambda x: -x[1])[:top_word]
            for vector in self.vectors
        ]

        # 转化为关键词并统计出现次数
        key_words_index = []
        for line in top_word_index:
            key_words_index += [item[0] for item in line]

        key_words_index = Counter(key_words_index).items()
        key_words = [(self.common_dictionary[item[0]], item[1]) for item in key_words_index]

        return sorted(key_words, key=lambda x: (-x[1], x[0]))[:top_n]

    def get_sentence_key_words(self, sentence, top_n=3):
        '''
        获取句子关键词
        :param sentence: 待抽取的文本
        :param top_n: 抽取top_n个关键词
        :return: 返回一个列表，每一项分别为(词, 词权重)
        '''
        ret = self.transform(sentence)
        return sorted(ret, key=lambda x: (-x[1], x[0]))[:top_n]

    def transform(self, sentence):
        '''
        获取句子每个词的权重
        :param sentence: 待获取文本
        :return: 返回一个列表，每一项分别为(词, 词权重)
        '''
        words_list = list(self.cutter(sentence))
        common_corpus = self.common_dictionary.doc2bow(words_list)
        words_tfidf_value = self.tfidf[common_corpus]
        return words_tfidf_value


if __name__ == '__main__':
    import doctest
    doctest.testmod()
