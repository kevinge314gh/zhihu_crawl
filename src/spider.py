#!/usr/bin/env python
#coding:utf-8
'''
Created on 2015年9月15日

@author: root
'''
#!/usr/bin/python
import sys
sys.path.append('/var/app/github/zhihu_crawl')
import urllib2
import re
import cookielib
import tools

from config import ROOT_PATH,HEADERS,URL_PEOPLE

def get_html(url):
    #load cookie
    cookie = cookielib.MozillaCookieJar()
    #从文件中读取cookie内容到变量
    cookie.load('%s/data/cookie.txt'%ROOT_PATH, ignore_discard=True, ignore_expires=True)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    
    request = urllib2.Request(url= url , headers=HEADERS)
    response = urllib2.urlopen(request)
    html = response.read()
    f = open( '%s/data/indexPage.txt'%ROOT_PATH, 'w')
    f.write(html)
    f.close()
    return html

def getUserinfos(p_name):
    url = URL_PEOPLE + p_name
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
    check_oline(html)
    return userinfo

def get_answers(p_name):
    url = URL_PEOPLE + p_name + '/answers?order_by=created'
    html = get_html(url)
    check_oline(html)
    answers = []
    pattern = re.compile(r'id="mi-(.*)">\n<h2><a class="question_link" href="/question/(.*)/answer/(.*)">(.*)</a></h2>')
    rets = re.findall(pattern, html)
    for ret in rets[:3]:
        ans = {}
        ans['create_time'] = tools.time_format(int(ret[0]))
        ans['ans_id'] = ret[1] + '-' + ret[2]
        ans['ans_title'] = ret[3]
        answers.append(ans)
    return answers
    
def get_followees(p_name):
    url = URL_PEOPLE + p_name + '/followees'
    html = get_html(url)
    check_oline(html)
    users = []
    pattern = re.compile(r'<a target="_blank" href="/people/(.*)/followers" class="zg-link-gray-normal">(.*) 关注者</a>')
    rets = re.findall(pattern, html)
    for ret in rets:
        users.append({'p_name':ret[0], 'followers_num':int(ret[1]), 'big_followers':[p_name]})
    print users
    return users
    
def check_oline(html):
    name = re.findall( r'<span class="name">(.*?)</span>\n<img', html)
    if len(name):
        print name[0], " is online >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        return 1
    print 'not online xxxxxxxxxxxxxxxxxxxxxxxxx'
    return 0

    
if __name__ == '__main__':
    answers = get_followees('zhang-jia-wei')
    
    
    

    
   

