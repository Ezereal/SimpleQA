#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch
from ASearch import BaiduSearch


def search(query):
    searcher = BaiduSearch.BSearcher(query)
    if searcher.if_tupu():
        return ASearch.Tupu_str, searcher.answer
    elif searcher.if_baike():
        return ASearch.Baike_str, searcher.answer
    elif searcher.if_zhidao():
        searcher.answer.append("-----")
        searcher.answer = searcher.answer + searcher.low_answer
        return ASearch.Zhidao_str, searcher.answer
    elif searcher.if_other():
        searcher.answer.append("-----")
        searcher.answer = searcher.answer + searcher.low_answer
        return ASearch.Other_str, searcher.answer
    else:
        return ASearch.None_str, None


if __name__ == '__main__':
    flag, answer = search("python字符串包dasdasd")
    print(flag+':')
    if flag == ASearch.Tupu_str:
        print(answer[0])
    elif flag == ASearch.Baike_str:
        print(answer[0])
    elif flag == ASearch.Zhidao_str:
        for s in answer:
            print(s)
    elif flag == ASearch.Other_str:
        for s in answer:
            print(s)

