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


class login_zhihu():
    hosturl = 'http://www.zhihu.com'
    posturl = 'http://www.zhihu.com/login/email'
    captcha_pre = 'http://www.zhihu.com/captcha.gif?r='
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
                   'Referer' : 'http:www.zhihu.com'}
    email = 'kevinge314wy@163.com'
    password = '123456'
    
    #set cookie
    def set_cookie(self):
        cj = cookielib.CookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
    
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
        f = open('captcha.gif', "wb")
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
        self.set_cookie()
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
        return response.read()
        
if __name__ == '__main__':
    cls = login_zhihu()
    html = cls.login_zhihu()
    print html
    
