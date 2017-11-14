#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import codecs
import QAnalyze


class DataReader (object):

    def __init__(self, datafile_name=QAnalyze.datafile_name):
        trainset = []
        featureset = set()
        with open(datafile_name, 'r') as file_object:
            for line in file_object.readlines():
                # 读入构造训练集
                line = line.replace(' ', '').strip()
                features = line.split(':')[0].split(',')
                for feature in features:
                    featureset.add(feature)
                turple_item = (features, line.split(':')[1])
                trainset.append(turple_item)

        self.trainset = trainset
        self.featureset = featureset

    def getfeaturefile(self, featurefile_name=QAnalyze.featurefile_name):
        # 将特征输出到文本(Features)
        num = 0
        set_num = len(self.featureset)
        with codecs.open(featurefile_name, 'w', 'utf-8') as file_object:
            for feature in self.featureset:
                file_object.write(feature)
                num = num + 1
                if num % 10 == 0:
                    file_object.write('\n')
                elif num != set_num:
                    file_object.write(',')


if __name__ == '__main__':
    reader = DataReader()
    reader.getfeaturefile()
