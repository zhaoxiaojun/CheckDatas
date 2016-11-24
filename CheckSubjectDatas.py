#coding=utf-8
import urllib
import urllib2
import cookielib
from bs4 import BeautifulSoup
import csv
import config


# # 处理cookie
# filename = "cookie.txt"
#
# cookie = cookielib.MozillaCookieJar(filename)
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
# postdata = urllib.urlencode({"username":"adolph004","password":"123456"})
#
# loginurl = 'http://my.233.mistong.com/login/prelogin'
#
# result = opener.open(loginurl,postdata)
#
# cookie.save(ignore_discard=True,ignore_expires=True)
#
#
# # 新建csv文件对象
# csv_file = open('SubjectDatas.csv','wb')
# csv_writer = csv.writer(csv_file,delimiter=',')
#
# # 处理数据进行拼接
# Collegeurl = 'http://172.16.7.51:81/clpnew/index?cengci=b&cid={cid}&mid=#anchor'
#
# cid = eval(config.ConfigIni.get_Cid())
# gid = eval(config.ConfigIni.get_Gid())
# for i in xrange(len(gid)):
#     urlcollege = Collegeurl.format(cid=cid[i])



# response = opener.open(urlcollege)
response = BeautifulSoup(response.read())
try:
    colleges = response.select(".anaMes")[0].string.encode("utf-8")
    print colleges
except IndexError as e:
    print e
data = response.select(".anaBg > ul > li ")
for zklist in data:
    zkl = zklist.select("b")[0]
    print zkl
    # for i in zkl:
    #     zk = i
    #     print zk
    per = zklist.select("strong")[0].string
    print per
    csv_writer.writerow([colleges,zkl,per,urlcollege])


