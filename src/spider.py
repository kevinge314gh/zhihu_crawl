#coding:utf-8
'''
Created on 2015年9月15日

@author: root
'''
#!/usr/bin/python

import urllib2
import re

from config import ROOT_PATH


URL = 'http://www.zhihu.com'
url_people = 'http://www.zhihu.com/people/'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer' : 'http:www.zhihu.com'}

def get_html(url):
    request = urllib2.Request(url= url , headers=headers)
    response = urllib2.urlopen(request)
    html = response.read()
    f = open( '%s/data/indexPage.txt'%ROOT_PATH, 'w')
    f.write(html)
    f.close()
    return html

def getUserinfos(p_name):
    url = url_people + p_name
    html = get_html(url)
    userinfo = {}
    userinfo['user_url'] = url
    userinfo['p_name']= p_name
    name = re.findall( r'<span class="name">(.*?)</span>，<span' , html)[0]
    userinfo['user_name'] = name
    bio = re.findall( r'<span class="bio" title=".*?">(.*)</span>', html)
    userinfo['bio' ] = bio
    location = re.findall( r'<span class="location item" title=.*?><a .*?>(.*?)</a></span>' , html)
    userinfo['location'] = location
    agree = re.findall( r'<span class="zm-profile-header-icon"></span><strong>(.*)</strong>' , html)
    userinfo['agree'] = agree[0]
    userinfo['thank'] = agree[1]
    navbar = re.findall( r'<a class="item "\nhref="(.*)">\n.*\n<span class="num">(.*)</span>', html)
    for href,num in navbar:
        href_key = href.split( '/')[3]
        userinfo[href_key] = num
    follow = re.findall( r'<a class="item" href=.*>\n.*\n<strong>(.*)</strong>' , html)
    userinfo['followees'] = follow[0]
    userinfo['followers'] = follow[1]
    for k,v in userinfo.items():
        print k, ':', v
    return userinfo




    
if __name__ == '__main__':
    html = get_html(url_people+'linan')
    name = re.findall( r'<span class="name">(.*?)</span>，<span' , html)
    print name

    
   

