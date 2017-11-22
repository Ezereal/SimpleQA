#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import AExtract
import jieba.posseg as pseg
import jieba
jieba.set_dictionary("dict.txt")
jieba.initialize()


def get_wordattr(word):
    result = pseg.cut(word)
    for res in result:
        return res.flag


def get_words(sentence):
    words = set()
    result = jieba.cut(sentence)
    for res in result:
        words.add(res)
    return words


def get_keywords(sentence):
    keywords = set()
    result = pseg.cut(sentence)
    for res in result:
        if res.flag in AExtract.keyword_set:
            keywords.add(res.word)
    return keywords


def get_attribute(sentence):
    attributes = {}
    # 利用jieba分词器对句子进行词性标注
    result = pseg.cut(sentence)
    for res in result:
        if res.flag in AExtract.attribute_set:
            if res.flag in attributes.keys():
                attributes[res.flag] = attributes[res.flag] + 1
            else:
                attributes[res.flag] = 1
    return attributes


if __name__ == '__main__':
    print(get_keywords("今天张三去了北京,坐了十个小时的车"))
    print(get_attribute("今天张三去了北京,坐了十个小时的车"))
