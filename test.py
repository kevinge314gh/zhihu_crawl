#coding:utf-8
'''
Created on 2015年9月18日

@author: root
'''
import base64
import re
import os
import cookielib
import urllib2
from config import ROOT_PATH,HEADERS

from PIL import Image
import pytesseract


if __name__ == '__main__':
    
    print pytesseract.image_to_string(Image.open('captcha.png'))

    