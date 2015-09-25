#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年9月18日

@author: root
'''
import base64
import re
import os
import sys
import cookielib
import urllib2
import time
from config import ROOT_PATH,HEADERS
from db.mongo import *
from src.spider import *

from PIL import Image
# import pytesseract


if __name__ == '__main__':
    db = mongo_connection().spider
    followees = get_followees('zhang-jia-wei')
    save_followees(db, cond=followees)
