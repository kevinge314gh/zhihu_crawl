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

def save_userinfo(db, data):
    db.user_infos.save(data)

'''
@return: 0:add new, 1:no change  change:change message
'''  
def update_userinfo(db, cond, **data):
    mongo_data = get_userinfo(db, cond)
    print mongo_data[0]
    if not len(mongo_data):
        save_userinfo(db, data)
        return 0
    agree = int(data['agree'])
    thank = int(data['thank'])
    followees = int(data['followees']['num'])
    followers = int(data['followers']['num'])
    #if the agree,thank,followees,followers changed?
    change = {}
    change['agree_change'] = agree - int(mongo_data[0]['agree'])
    change['thank_change'] = thank - int(mongo_data[0]['thank'])
    change['followees_change'] = followees - int(mongo_data[0]['followees']['num'])
    change['followers_change'] = followers - int(mongo_data[0]['followers']['num'])
    for k,v in change.items():
        #if changed, update db and return message
        if v:
            db.user_infos.update(cond, {'$set':{'agree':agree, 'thank':thank, \
                                                'followees':followees, ';followers':followers}})
            return change
        continue
    return 1
        
def get_userinfo(db, cond):
    ret = db.user_infos.find(cond)
    return [item for item in ret]
    
def remove_userinfo(db, cond):
    db.user_infos.remove(cond)
    
    
    
    
    
if __name__ == '__main__':
    db = mongo_connection().spider
    db.test.update({'id':12}, {'$set':{'name':'kkkkkkkkk'}})
    ret = db.test.find()
    print [item for item in ret]
    
