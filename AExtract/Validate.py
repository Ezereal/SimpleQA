#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import AExtract.SentenceTools


def validate(answer, category):
    words = AExtract.SentenceTools.get_words(answer)
    words = words
    cate_attr = AExtract.cate_attr_dict[category]
    for word in words:
        if AExtract.SentenceTools.get_wordattr(word) in cate_attr:
            return True
    return False
