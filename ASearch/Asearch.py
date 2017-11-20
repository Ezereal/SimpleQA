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
    description, answer = search("一年有多少周")
    print(description+':')
    if description == ASearch.Tupu_str:
        print(answer[0])
    elif description == ASearch.Baike_str:
        print(answer[0])
    elif description == ASearch.Zhidao_str:
        for s in answer:
            print(s)
    elif description == ASearch.Other_str:
        for s in answer:
            print(s)

