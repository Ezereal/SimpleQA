#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import AExtract
import jieba.posseg as pseg


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
    print(get_attribute("今天张三去了北京,坐了十个小时的车"))
