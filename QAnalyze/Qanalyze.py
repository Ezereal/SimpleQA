#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import jieba
import QAnalyze
from QAnalyze import NBclassifier
from QAnalyze import traindata_read

def analyze(question,featurefile_name = QAnalyze.featurefile_name):
    #读取本地的问题关键字文本
    featureSet = set()
    with open(featurefile_name,'r') as file_object:
        for line in file_object.readlines():
            features = line.split(',')
            for feature in features:
                featureSet.add(feature)
    #利用jieba开源库对问题进行分词操作
    wordSet = set()
    words = jieba.cut(question)
    for word in words:
        wordSet.add(word)

    reader = traindata_read.dataReader()
    classifier = NBclassifier.NBClassifier()
    classifier.train(reader.trainSet)

    return classifier.classify(featureSet & wordSet)

if __name__ == '__main__':
    reader = traindata_read.dataReader()
    classifier = NBclassifier.NBClassifier()
    classifier.train(reader.trainSet)
    print(classifier.classify(analyze("这是什么东西")))





