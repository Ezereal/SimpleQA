#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ASearch


def get_tupu_answer(res):
    return res.get_text().strip()


def get_baike_answer(url):
    soup = ASearch.get_soup(url)
    # 获取百度百科答案
    result = soup.find(class_='lemma-summary')
    if result and result.find(class_='para'):
        return result.find(class_='para').get_text().strip()
    return None


def get_zhidao_answer(url):
    answer = []
    soup = ASearch.get_soup(url)
    # 查找百度知道最佳答案
    result = soup.find(class_="bd answer")
    if result and result.find(class_='best-text mb-10'):
        return "BestAnswer", result.find(class_='best-text mb-10').get_text().strip()
    # 查找百度知道其他答案
    result = soup.find(class_='bd-wrap')
    if result and result.find_all(class_='con'):
        result = result.find_all(class_='con')
        sentence = ''
        for res in result:
            sen = res.get_text().strip()
            sentence = sentence + sen
            if'。' in sen:
                answer.append(sentence)
                sentence = ''
        if sentence != '':
            answer.append(sentence)
        return "OtherAnswer", answer
    return "NoAnswer", None


def get_other_answer(url):
    answer = []
    sentence = ''
    soup = ASearch.get_soup(url)
    # 检索其他网页的p标签
    result = soup.find_all('p')
    if result:
        for res in result:
            sen = res.get_text().strip()
            sentence = sentence + sen
            if '。' in sen or '.' in sen:
                answer.append(sentence)
                sentence = ''
        if sentence != '':
            answer.append(sentence)
        return 'GetAnswer', answer
    # 检索其他网页的span标签
    result = soup.find_all('span')
    if result:
        for res in result:
            sen = res.get_text().strip()
            sentence = sentence + sen
            if '。' in sen or '.' in sen:
                answer.append(sentence)
                sentence = ''
        if sentence != '':
            answer.append(sentence)
        return 'GetAnswer', answer
    return "NoAnswer", None


if __name__ == '__main__':
    s = "http://m.blog.csdn.net/QWsin/article/details/51261267"
    print(get_other_answer(s))
