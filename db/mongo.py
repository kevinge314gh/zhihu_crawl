#coding:utf-8
'''
Created on 2015年9月17日

@author: root
'''

from pymongo import Connection
from config import MONGO_IP,MONGO_PORT
import time


def mongo_connection():
    return Connection(MONGO_IP, MONGO_PORT)

def save_userinfo(data, db=None):
    db.user_infos.save(data)
    
def update_userinfo(db, cond, **data):
    db.user_infos.save(data)
    
def get_userinfo(cond, db=None):
    return db.user_infos.find(cond)
    
def remove_userinfo(cond, db=None):
    db.user_infos.remove(cond)
    
    
    
    
    
if __name__ == '__main__':
    db = mongo_connection().spider
#     db.test.insert({'name':'kevin','id':14})
    db.test.update({'id':12}, {'$set':{'name':'kkkkkkkkk'}})
    ret = db.test.find()
    print [item for item in ret]
    
