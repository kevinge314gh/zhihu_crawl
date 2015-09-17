#coding:utf-8
'''
Created on 2015年9月15日

@author: root
'''
#!/usr/bin/python

import urllib
import urllib2
import re
import pymongo

from login import login_zhihu
from urllib import localhost

URL = 'http://www.zhihu.com/'
url_linan = 'http://www.zhihu.com/people/linan'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer' : 'http:www.zhihu.com'}

def getUserinfos(url= ''):
    request = urllib2.Request(url= url , headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    f = open( 'indexPage.txt', 'w')
    f.write(html)
    f.close()
   
    userinfo = {}
    name = re.findall( r'<span class="name">(.*?)</span>' , html)
    userinfo['name'] = name
    bio = re.findall( r'<span class="bio" title=".*?">(.*)</span>', html)
    userinfo['bio' ] = bio
    location = re.findall( r'<span class="location item" title=.*?><a .*?>(.*?)</a></span>' , html)
    userinfo['location'] = location
    agree = re.findall( r'<span class="zm-profile-header-icon"></span><strong>(.*)</strong>' , html)
    userinfo['agree'] = agree[ 0]
    userinfo['thank'] = agree[ 1]
    navbar = re.findall( r'<a class="item "\nhref="(.*)">\n.*\n<span class="num">(.*)</span>', html)
    for href,num in navbar:
        href_key = href.split( '/')[3 ]
        userinfo[href_key] = { 'href':href, 'num':num}
    follow = re.findall( r'<a class="item" href="(.*)">\n.*\n<strong>(.*)</strong>' , html)
    userinfo['followees'] = {'href' :follow[0][0], 'num' :follow[0][1]}
    userinfo['followers'] = { 'href':follow[ 1][0 ], 'num' :follow[1][1]}
    print userinfo
    return userinfo

def save_userinfo(userinfo={}):
    connection = pymongo.Connection('localhost', 27017)
    db = connection.spider
    collection = db.user_infos
    collection.insert(userinfo)
    
    
if __name__ == '__main__':
    userinfo = getUserinfos(url_linan)
    save_userinfo(userinfo)
#     getUserinfos('http://www.zhihu.com/people/yangxiaoche')
#     getUserinfos('http://www.zhihu.com/people/guo-wen-kai-69')
   

