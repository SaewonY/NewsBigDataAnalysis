# -*- coding: utf-8 -*-

'''
@ source: https://cyc1am3n.github.io/2018/11/10/classifying_korean_movie_review.html
@ modified by Hyung-Kwon Ko
@ since: Tue Apr 30 01:26:01 2019
'''

from konlpy.tag import Okt # recommend you to install latest version
import os
from pprint import pprint
import nltk
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import numpy as np

class Preprocessing:
    def __init__(self,address):
        '''
        @const COMMON_NUM: number of vocabs
        '''
        COMMON_NUM = 100

    def tokenize(self,data):
        okt = Okt()
        # norm은 정규화, stem은 근어로 표시하기를 나타냄
        return ['/'.join(t) for t in okt.pos(data, norm=True, stem=True)]

    def tokenize2(self,data):
        doc = [(self.tokenize(row[1]), row[2]) for row in data]
        tok = [t for d in doc for t in d[0]]
        text = nltk.Text(tok, name='NMSC')
        return text # this is the tokens (ex. '그리다/Verb')

    def print_info(self,text,n):
        print("Number of tokens: ", len(text.tokens)) # Total number of tokens
        print("Without redundancy: ", len(set(text.tokens))) # 중복을 제외한 토큰의 개수
        pprint(text.vocab().most_common(n)) # 출현 빈도가 높은 상위 토큰 n개
        
    def term_frequency(self,doc):
        # 시간이 꽤 걸립니다! 시간을 절약하고 싶으면 most_common의 매개변수를 줄여보세요.
        selected_words = [f[0] for f in text.vocab().most_common(self.COMMON_NUM)]
        return [doc.count(word) for word in selected_words]

    def make_x(self,doc):
        x = [term_frequency(d) for d, _ in doc]
        return np.asarray(x).astype('float32')

    def make_y(self,doc):
        y = [c for _, c in doc]
        return np.asarray(y).astype('float32')

class EDA:
    def __init__(self,text):
        '''
        @param data: data returned from Preprocessing.tokenzie2
        '''
        self.text = text

    def show_freq(self,n):
        %matplotlib inline
        font_fname='c:/windows/fonts/malgun.ttf'
        font_name = font_manager.FontProperties(fname=font_fname).get_name()
        rc('font', family=font_name)
        plt.figure(figsize=(20,10))
        self.text.plot(n)

##usage
test_data = read_data('ratings_test.txt')
x = Preprocessing()
z = x.tokenize2(test_data[0:10])
x.printInfo(z,3)
x.show_freq(10)
x = EDA(z)


