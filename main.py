#coding:utf-8
'''
Created on 2015年9月21日

@author: root
'''

import sys
from db.mongo import *
from src.spider import getUserinfos
from src.sendEmail import send_163mail

if __name__ == '__main__':
    p_name = 'zhang-jia-wei'
    db = mongo_connection().spider
    userinfo = getUserinfos(p_name)
    cond = {'p_name':p_name}
    msg = update_userinfo(db, cond, **userinfo)
    #send email
    if msg not in [0,1]:
        content = '%s的数据变化：\n赞同：%s\n感谢：%s\n关注：%s\n被关注：%s'\
        %(p_name, msg['agree_change'], msg['thank_change'], msg['followees_change'], msg['followers_change'])
        subject = '%s的知乎有更新'%p_name
        rt = send_163mail(subject, content)
	print content
        print 'send email successfull!'
        sys.exit()
    elif msg == 0:
        rt = send_163mail('you watched a new zhihu user', 'you add %s in your followees, \nyou will get email if he/her has any changes\n\
        Thank you for your subscription!'%p_name)
        print 'add a new user'
        sys.exit()
    elif msg == 1:
        print 'nothing changed'
        sys.exit()
    print 'error'
    sys.exit()
