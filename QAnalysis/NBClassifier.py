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
            for feature in subTuple[0]:
                if feature not in dictFeaturesBase.keys():
                    dictFeaturesBase[feature] = 1
                else:
                    dictFeaturesBase[feature] += 1

        dictFeatures = {}.fromkeys([key for key in dictTag])

        for key in dictFeatures.keys():
            dictFeatures[key] = {}.fromkeys([key for key in dictFeaturesBase])

        for subTuple in trainSet:
            for feature in subTuple[0]:
                dictFeatures[subTuple[1]][feature] = 1 if dictFeatures[subTuple[1]][feature] == None else dictFeatures[subTuple[1]][feature] + 1

        # 将训练样本中没有的项目，由None改为一个非常小的数值，表示其概率极小而并非是零
        for tag,feature in dictFeatures.items():
            for key,value in feature.items():
                if value == None:
                    feature[key] = 0

        # 由特征频率计算特征的条件概率P(feature|tag)
        for tag,fearure in dictFeatures.items():
            totalValue = sum([x for x in feature.values() if x != None])
            for key,value in feature.items():
                feature[key] = value / totalValue if value != None else None

        self.featuresProbablity = dictFeatures


    def classify(self,features):
        resultDict = {}

        # 计算每个tag的条件概率
        for key,value in self.tagProbablity.items():

            iNumList = []
            for feature in features:
                if self.featuresProbablity[key][feature]:
                    iNumList.append(self.featuresProbablity[key][feature])

            conditionPr = 1
            for iNum in iNumList:
                conditionPr *= iNum
            resultDict[key] = value * conditionPr

        resultList = sorted(resultDict.items(),key = lambda x:x[1],reverse=True)
        return resultList[0][0]

if __name__ == '__main__':

    trainSet = [
        ({"是","谁"},"人物"),
        ({"在","哪"},"地点"),
        ({"哪里"}, "地点"),
        ({"什么","地方"}, "地点"),
        ({"多少"}, "数字"),
        ({"多长"}, "数字"),
        ({"多","宽"}, "数字"),
        ({"什么","时候"}, "时间"),
        ({"何时"}, "时间"),
        ({"什么","东西"}, "实体"),
        ({"是","什么"}, "实体"),
        ({"因为","什么"}, "描述"),
        ({"为什么"}, "描述"),
        ({"原因","是"}, "描述")
    ]

    classifier = NBClassifier()
    classifier.train(trainSet)
    result = classifier.classify({"多少"})
    print(result)
