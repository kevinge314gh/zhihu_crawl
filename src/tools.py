#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年9月22日

@author: root
'''

import time


def time_format(timestamp):
    t = time.localtime(timestamp)
    return time.strftime('%Y/%m/%d %H:%M:%S', t)


if __name__ == '__main__':
    print time_format(1442827492)