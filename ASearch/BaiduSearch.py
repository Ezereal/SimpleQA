#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch
from ASearch import GetCanAnswer


class BSearcher(object):

    def __init__(self, query):
        query = query.replace(' ', '')
        self.soup = ASearch.get_soup(ASearch.baidu_url+query)
        self.answer = []
        self.low_answer = []

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
        for i in range(1, ASearch.search_num):
            sub_soup = self.soup.find(id=i)
            # 检索百度百科的答案
            result = sub_soup.find("h3").find("a")
            if result.get_text().__contains__("百度百科"):
                baike_answer = GetCanAnswer.get_baike_answer(result)
                if baike_answer:
                    self.answer.append(baike_answer)
                    return True
        return False

    def if_zhidao(self):
        if_getanswer = False
        for i in range(1, ASearch.search_num):
            sub_soup = self.soup.find(id=i)
            # 检索百度知道的答案
            result = sub_soup.find("h3").find("a")
            if result.get_text().__contains__("百度知道"):
                flag, zhidao_answer = GetCanAnswer.get_zhidao_answer(result)
                # 检索到最佳答案
                if flag == "BestAnswer":
                    if_getanswer = True
                    self.answer.append(zhidao_answer)
                # 检索到其它答案
                elif flag == "OtherAnswer":
                    if_getanswer = True
                    self.low_answer = self.low_answer + zhidao_answer
        return if_getanswer
