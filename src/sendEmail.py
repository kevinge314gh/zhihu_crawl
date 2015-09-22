#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年9月20日

@author: root
'''
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formatdate

def send_email(server, fro, to, subject, text, files=[]):
    assert type(server) == dict 
    assert type(to) == list 
    assert type(files) == list
    
    msg = MIMEMultipart()
    msg['From'] = ';'.join(fro)
    msg['To'] = ';'.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))
    try:
        smtp = smtplib.SMTP()
        smtp.connect(server['server_name'])
        smtp.login(server['user'], server['passwd'])
        smtp.sendmail(fro, to, msg.as_string())
        smtp.quit()
        return True
    except Exception, e:
        print str(e)
        return False
    
def send_163mail(subject, content):
    server = {}
    server['server_name'] = 'smtp.163.com'
    server['user'] = 'kevinge314wy@163.com'
    server['passwd'] = 'wy206144kevin'
    fro = ['kevinge314wy@163.com']
    to = ['912023833@qq.com']
    send_email(server, fro, to, subject, content)
    
    
if __name__ == '__main__':
    
    server = {}
    server['server_name'] = 'smtp.163.com'
    server['user'] = 'kevinge314wy@163.com'
    server['passwd'] = 'wy206144kevin'
    fro = ['kevinge314wy@163.com']
    to = ['912023833@qq.com']
    subject = 'Changes from guowenkai'
    text = '你好吧我是郭文凯呢,asdfjasdlfjadlfksjdffasddddddddddddddddddddddddddddddddasdfasdasdsdfsdfds\
    sadfdsfsdfasdfsadfsdfsdfsdfsdfsnfasdfjdsifds'
    send_email(server, fro, to, subject, text)
    
    
