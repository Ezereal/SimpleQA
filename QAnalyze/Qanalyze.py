#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import QAnalyze
from QAnalyze import NBclassifier
from QAnalyze import traindata_read
import jieba
jieba.set_dictionary("dict.txt")
jieba.initialize()


def getquestionkey(question, featurefile_name=QAnalyze.featurefile_name):
    # 读取本地的问题关键字文本
    featureset = set()
    with open(featurefile_name, 'r') as file_object:
        for line in file_object.readlines():
            features = line.split(',')
            for feature in features:
                featureset.add(feature)
    # 利用jieba开源库对问题进行分词操作
    wordset = set()
    words = jieba.cut(question)
    for word in words:
        wordset.add(word)

    return featureset & wordset


def analyze(question):
    reader = traindata_read.DataReader()
    classifier = NBclassifier.NBClassifier()
    classifier.train(reader.trainset)

    questionkey = getquestionkey(question)
    result = classifier.classify(questionkey)

    return result


if __name__ == '__main__':
    reader_test = traindata_read.DataReader()
    classifier_test = NBclassifier.NBClassifier()
    classifier_test.train(reader_test.trainset)
    print(classifier_test.classify(getquestionkey("黄河有多长")))





