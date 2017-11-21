#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ASearch.Asearch
import QAnalyze.Qanalyze
import AExtract.Aextract


def question_answer():
    query = input("请输入您的问题:")
    query = query.replace(' ', '')
    category = QAnalyze.Qanalyze.analyze(query)
    print("您的问题类别:" + category)
    description, cananswer = ASearch.Asearch.search(query)
    # for s in cananswer:
    #    print(s)
    # print(category)
    # 处理各种返回的答案
    print("您的答案:")
    if description == ASearch.Tupu_str:
        print(cananswer[0])
        return
    elif description == ASearch.Baike_str:
        answer = AExtract.Aextract.extract(query, cananswer, category)
        if answer is not None:
            print(answer)
            return
    elif description in [ASearch.Zhidao_str, ASearch.Other_str]:
        answer = AExtract.Aextract.extract(query, cananswer, category)
        if answer is not None:
            print(answer)
            return
    print("未找到答案QAQ")


if __name__ == '__main__':
    question_answer()
