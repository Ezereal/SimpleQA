#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class NBClassifier(object):

    def __init__(self):
        self.tagprobablity = {}
        self.featuresprobablity = {}
        pass

    def train(self, trainset):

        # 计算每种类别的概率
        # 保存所有tag的所有种类,及它们出现的频次
        
        dicttag = {}

        for subTuple in trainset:
            if str(subTuple[1]) not in dicttag.keys():
                dicttag[str(subTuple[1])] = 1
            else:
                dicttag[str(subTuple[1])] = dicttag[str(subTuple[1])] + 1

        # 保存每个tag本身的概率
        tagprobablity = {}

        totalvalue = sum([value for value in dicttag.values()])

        for key, value in dicttag.items():
            tagprobablity[key] = value / totalvalue

        self.tagprobablity = tagprobablity

        # 计算特征的条件概率
        # 保存特征属性基本信息
        dictfeaturesbase = {}

        for subTuple in trainset:
            for feature in subTuple[0]:
                if feature not in dictfeaturesbase.keys():
                    dictfeaturesbase[feature] = 1
                else:
                    dictfeaturesbase[feature] += 1

        dictfeatures = {}.fromkeys([key for key in dicttag])

        for key in dictfeatures.keys():
            dictfeatures[key] = {}.fromkeys([key for key in dictfeaturesbase])

        for subTuple in trainset:
            for feature in subTuple[0]:
                if dictfeatures[subTuple[1]][feature] is None:
                    dictfeatures[subTuple[1]][feature] = 1
                else:
                    dictfeatures[subTuple[1]][feature] = dictfeatures[subTuple[1]][feature] + 1

        # 将训练样本中没有的项目，由None改为零
        for tag, feature in dictfeatures.items():
            for key, value in feature.items():
                if value is None:
                    feature[key] = 0

        # 由特征频率计算特征的条件概率P(feature|tag)
        for tag, feature in dictfeatures.items():
            totalvalue = sum([x for x in feature.values() if x is not None])
            for key, value in feature.items():
                feature[key] = value / totalvalue if value is not None else None

        self.featuresprobablity = dictfeatures

    def classify(self, features):
        resultdict = {}

        # 计算每个tag的条件概率
        for key, value in self.tagprobablity.items():
            numlist = []
            for feature in features:
                numlist.append(self.featuresprobablity[key][feature])
            condition = 1
            for iNum in numlist:
                condition *= iNum
            resultdict[key] = value * condition

        resultlist = sorted(resultdict.items(), key=lambda x: x[1], reverse=True)
        return resultlist[0][0]


if __name__ == '__main__':

    trainset_test = [
        ({"是", "谁"}, "人物"),
        ({"哪一位"}, "人物"),
        ({"在", "哪"}, "地点"),
        ({"哪里"}, "地点"),
        ({"什么", "地方"}, "地点"),
        ({"多少"}, "数字"),
        ({"多长"}, "数字"),
        ({"多", "宽"}, "数字"),
        ({"是", "什么", "时候"}, "时间"),
        ({"何时"}, "时间"),
        ({"多久"}, "时间"),
        ({"什么", "东西"}, "实体"),
        ({"是", "什么"}, "实体"),
        ({"因为", "什么"}, "描述"),
        ({"为什么"}, "描述"),
        ({"原因", "是"}, "描述")
    ]

    classifier = NBClassifier()
    classifier.train(trainset_test)
    result = classifier.classify(input().split(','))
    print(result)
