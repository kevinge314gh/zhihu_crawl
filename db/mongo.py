#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年9月17日

@author: root
'''

from pymongo import Connection
from config import MONGO_IP,MONGO_PORT
import time
import os


def mongo_connection():
    return Connection(MONGO_IP, MONGO_PORT)

def save_userinfo(db, data):
    db.user_infos.save(data)

'''
@return: 0:add new, 1:no change  change:change message   kkkkkkkkkkkkkk
'''  
def update_userinfo(db, cond, **data):
    mongo_data = get_userinfo(db, cond)
    if not len(mongo_data):
        save_userinfo(db, data)
        return 0
    agree = int(data['agree'])
    thank = int(data['thank'])
    answers = int(data['answers'])
    posts = int(data['posts'])
    followees = int(data['followees'])
    followers = int(data['followers'])
    #if the agree,thank,followees,followers changed?
    change = {}
    change['agree_change'] = agree - int(mongo_data[0]['agree'])
    change['thank_change'] = thank - int(mongo_data[0]['thank'])
    change['answers'] = answers - int(mongo_data[0]['answers'])
    change['posts'] = posts - int(mongo_data[0]['posts'])
    change['followees_change'] = followees - int(mongo_data[0]['followees'])
    change['followers_change'] = followers - int(mongo_data[0]['followers'])
    for k,v in change.items():
        #if changed, update db and return message
        if v:
            db.user_infos.update(cond, {'$set':{'agree':agree, 'thank':thank, \
                                                'answers':answers, 'posts':posts,\
                                                'followees':followees, 'followers':followers}})
            return change
        continue
    return 1
        
def get_userinfo(db, cond):
    ret = db.user_infos.find(cond)
    return [item for item in ret]
    
def remove_userinfo(db, cond):
    db.user_infos.remove(cond)
    
'''anwsers'''  
def save_answers(db, cond):
    db.answers.insert(cond)
    
    
'''followees'''
def save_followees(db, cond):
    db.users.insert(cond)
    
    
    
    
    
    
if __name__ == '__main__':
    db = mongo_connection().spider
#     db.test.update({'id':12}, {'$set':{'name':'kkkkkkkkk'}})
#     ret = db.test.find()
#     print [item for item in ret]
#     remove_userinfo(db, {'p_name':'linan'})
    

    
