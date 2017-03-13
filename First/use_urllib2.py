# -*- coding:utf-8 -*-

# # example1: 爬一个网页
# import urllib2
#
# # urllib2.urlopen的用法urllib2.urlopen(url, data, timeout)
# # url 即统一资源定位符
# # data 即访问url时需要使用的数据，默认值为None
# # timeout 即超时时间，默认值为socket._GLOBAL_DEFAULT_TIMEOUT
# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()

# # example2: 使用Request爬网页
# import urllib2
#
# request = urllib2.Request("http://www.baidu.com")
# # urllib2.urlopen可以接受request参数，推荐使用request，因为request可以设置很多参数
# response = urllib2.urlopen(request)
# print response.read()

# example3: 动态网页访问，关键是需要给网站传递参数
# 数据传输主要包括了POST和GET的方式，最重要的区别是GET方式是直接以链接形式访问，
# 链接中包含了所有的参数，当然如果包含了密码的话是一种不安全的选择，不过你可以直观地看到自己提交了什么内容。
# POST则不会在网址上显示所有的参数，不过如果你想直接查看提交了什么就不太方便了。

# # POST的数据传输方式
# import urllib
# import urllib2
#
# values = {"username":"yhs_cy", "password":"xxxxxx"}
# data = urllib.urlencode(values)
# url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()

# # GET的数据传输方式
import urllib
import urllib2

values = {"username": "yhs_cy", "password": "87714572"}
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?" + data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()