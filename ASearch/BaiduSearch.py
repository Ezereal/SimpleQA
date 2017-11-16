#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch
import requests
from bs4 import BeautifulSoup


class BSearcher(object):

    def __init__(self, query):
        query = query.replace(' ', '')
        # 向baidu提交get请求,构造Beautiful对象
        result = requests.get(url=ASearch.baidu_url+query, headers=ASearch.headers).text()
        soup = BeautifulSoup(result, "lxml")
        # 去除无关的标签
        [s.extract() for s in soup(['script', 'style', 'img'])]
        self.soup = soup
        self.answer = []
        self.exact_answer = 0

    def if_tuku(self):
        sub_soup = self.soup.find(id=1)
        if sub_soup.attrs.has_key('mu'):
            result = sub_soup.find(class_='op_exactqa_s_answer')
            if result:
                self.answer.append(result)
                self.exact_answer = 1
                return True
            return False
        return False

    def if_zhidao(self):
        for i in range(1,10):
            sub_soup = self.soup.find(id=i)
            