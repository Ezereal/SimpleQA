#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch
from ASearch import GetCanAnswer


class BSearcher(object):

    def __init__(self, query):
        self.soup = ASearch.get_soup(ASearch.baidu_url+query)
        self.answer = []
        self.low_answer = []
        self.search_numset = set(range(1, ASearch.search_num+1))

    def if_tupu(self):
        sub_soup = self.soup.find(id=1)
        if 'mu' in sub_soup.attrs.keys():
            # 检索百度知识图谱的答案
            result = sub_soup.find(class_='op_exactqa_s_answer')
            if result:
                self.answer.append(GetCanAnswer.get_tupu_answer(result))
                return True
            return False
        return False

    def if_baike(self):
        numset = set(self.search_numset)
        for i in numset:
            sub_soup = self.soup.find(id=i)
            # 检索百度百科的答案
            result = sub_soup.find("h3").find("a")
            if result.get_text().__contains__("百度百科"):
                self.search_numset.remove(i)
                baike_answer = GetCanAnswer.get_baike_answer(result['href'])
                if baike_answer:
                    self.answer.append(baike_answer)
                    return True
        return False

    def if_zhidao(self):
        if_getanswer = False
        numset = set(self.search_numset)
        for i in numset:
            sub_soup = self.soup.find(id=i)
            # 检索百度知道的答案
            result = sub_soup.find("h3").find("a")
            if result.get_text().__contains__("百度知道"):
                self.search_numset.remove(i)
                flag, zhidao_answer = GetCanAnswer.get_zhidao_answer(result['href'])
                # 检索到最佳答案
                if flag == "BestAnswer":
                    if_getanswer = True
                    self.answer.append(zhidao_answer)
                # 检索到其它答案
                elif flag == "OtherAnswer":
                    if_getanswer = True
                    self.low_answer = self.low_answer + zhidao_answer
        return if_getanswer

    def if_other(self):
        if_getanswer = False
        for i in self.search_numset:
            sub_soup = self.soup.find(id=i)
            # 检索其他网页的答案
            result = sub_soup.find("h3").find("a")
            if result.get_text().__contains__("百度知道"):
                continue
            flag, other_answer = GetCanAnswer.get_other_answer(result['href'])
            if flag == 'GetAnswer':
                if_getanswer = True
                self.low_answer = self.low_answer + other_answer
        return if_getanswer
