#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import AExtract
import AExtract.Validate
import AExtract.SentenceTools


def get_senval(keywords, sentence, category):
    value = 0
    # 根据出现的关键词次数更新value
    words = AExtract.SentenceTools.get_words(sentence)
    value = value + len(words & keywords)
    # 根据句子中短语与问题类别词性的相近程序更新value
    cate_attr = AExtract.cate_attr_dict[category]
    attributes = AExtract.SentenceTools.get_attribute(sentence)
    for ca in cate_attr:
        if ca in attributes.keys():
            value = value + attributes[ca] * AExtract.attrvalue
    return value


def extract(query, cananswer, category):
    num = 0
    bestanswer_bias = 100
    answer_sort = {}
    keywords = AExtract.SentenceTools.get_keywords(query)
    # 计算各个候选答案的val值
    for can in cananswer:
        if can == '-----':
            bestanswer_bias = 0
            continue
        answer_sort[num] = get_senval(keywords, can, category) + bestanswer_bias
        answer_sort[num] = answer_sort[num] / len(can)
        num = num + 1
    # 根据权值排序选出val值最高的候选答案
    answerlist = sorted(answer_sort.items(), key=lambda x: x[1], reverse=True)
    answer = cananswer[answerlist[0][0]]
    if AExtract.Validate.validate(answer, category):
        return answer
    else:
        return None
