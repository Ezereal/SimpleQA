#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class NBClassifier(object):

    def __init__(self,fillNa = 1):
        
        self.fillNa = 1
        pass

    def train(self,trainSet):

        # 计算每种类别的概率
		# 保存所有tag的所有种类，及它们出现的频次
        dictTag = {}

        for subTuple in trainSet:
            dictTag[str(subTuple[1])] = 1 if str(subTuple[1]) not in dictTag.keys() else dictTag[str(subTuple[1])] + 1

        # 保存每个tag本身的概率
        tagProbablity = {}

        totalValue = sum([value for value in dictTag.values()])

        for key,value in dictTag.items():
            tagProbablity[key] = value / totalValue

        self.tagProbablity = tagProbablity

        # 计算特征的条件概率
		# 保存特征属性基本信息
        dictFeaturesBase = {}

        for subTuple in trainSet:
            for key,value in subTuple[0].items():
                if key not in dictFeaturesBase.keys():
                    dictFeaturesBase[key] = {value:1}
                else:
                    if value not in dictFeaturesBase[key].keys():
                        
