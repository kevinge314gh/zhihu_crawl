#coding:utf-8
'''
Created on 2015年9月15日

@author: root
'''
#!/usr/bin/python

import urllib
import urllib2
import cookielib
import re
import time
from config import ROOT_PATH,HEADERS

#set cookie
def set_cookie():
    #设置保存cookie的文件
    filename = '%s/data/cookie.txt'%ROOT_PATH
    cookie = cookielib.MozillaCookieJar(filename)
    handler = urllib2.HTTPCookieProcessor(cookie)
    opener = urllib2.build_opener(handler, urllib2.HTTPHandler)
    urllib2.install_opener(opener)
    return cookie
    
class login_zhihu():
    hosturl = 'http://www.zhihu.com'
    posturl = 'http://www.zhihu.com/login/email'
    captcha_pre = 'http://www.zhihu.com/captcha.gif?r='
    headers = HEADERS
    email = 'kevinge314wy@163.com'
    password = '123456'
    
    #get xsrf
    def get_xsrf(self):
        h = urllib2.urlopen(self.hosturl)
        html = h.read()
        xsrf_str = r'<input type="hidden" name="_xsrf" value="(.*?)"/>'
        xsrf = re.findall(xsrf_str, html)[ 0]
        return xsrf
    
    #get captcha
    def get_captcha(self):
        captchaurl = self.captcha_pre + str(int(time.time() * 1000))
        print captchaurl
        data = urllib2.urlopen(captchaurl).read()
        f = open( '%s/data/captcha.png'%ROOT_PATH, 'w')
        f.write(data)
        f.close()
        captcha = raw_input( 'captcha is: ')
        return captcha
    
    #post data
    def post_data(self,captcha,xsrf):
        postData = { '_xsrf' : xsrf,
                    'password' : self.password,
                    'captcha' : captcha,
                    'email' : self.email ,
                    'remember_me' : 'true',
                    }
    
        #request
        postData = urllib.urlencode(postData)
        request = urllib2.Request(self.posturl, postData, self.headers)
        response = urllib2.urlopen(request)
        text = response.read()
        return text
    
    def login_zhihu(self):
        #set cookie
        cookie = set_cookie()
        #post it
        captcha=self.get_captcha()
        xsrf = self.get_xsrf()
        text=self.post_data(captcha,xsrf)
        #post again
        captcha=self.get_captcha()
        text=self.post_data(captcha,xsrf)
        #index page
        request = urllib2.Request(url='http://www.zhihu.com', headers=self.headers)
        response = urllib2.urlopen(request)
        html =  response.read()
        name = re.findall( r'<span class="name">(.*?)</span>', html)
        if name == ['kevin']:
            #保存cookie到文件
            cookie.save(ignore_discard=True, ignore_expires=True)
            return True
        else:
            return False


        
if __name__ == '__main__':
    cls = login_zhihu()
    rt = cls.login_zhihu()
    if rt:
        print 'login successful'
    else:
        print 'login fial'
    
