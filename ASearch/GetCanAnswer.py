#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch


def get_tupu_answer(res):
    return res.get_text().strip()


def get_baike_answer(res):
    url = res['href']
    soup = ASearch.get_soup(url)
    # 获取百度百科答案
    result = soup.find(class_='lemma-summary').find(class_='para')
    if result:
        return result.get_text().strip()
    return None


def get_zhidao_answer(res):
    url = res['href']
    soup = ASearch.get_soup(url)
    # 查找百度知道最佳答案
    result = soup.find(class_="bd answer").find(class_='best-text mb-10')
    if result:
        return "BestAnswer", result.get_text().strip()
    # 查找百度知道其他答案
    result = soup.find(class_='bd-wrap').find_all(class_='con')
    if result:
        answer = []
        for r in result:
            answer.append(r.get_text().strip())
        return "OtherAnswer", answer
    return "NoAnswer", None


if __name__ == '__main__':
    s = {'href': "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6/6699?fr=aladdin"}
    print(get_baike_answer(s))
