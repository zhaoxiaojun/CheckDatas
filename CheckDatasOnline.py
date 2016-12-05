#coding=utf-8
##############################################
# Author：adolph
# Date：2016.12.05
# Description：新旧老版组合查询维度的TotalNum对比
##############################################

import urllib
import urllib2
import cookielib
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
from Mssql import MSSQL
from config import ConfigIni

# 处理cookie
filename = "cookie.txt"

cookie = cookielib.MozillaCookieJar(filename)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({})

loginurl = 'http://passport.ewt360.com/login/prelogin'

result = opener.open(loginurl,postdata)

cookie.save(ignore_discard=True,ignore_expires=True)

#新建文件对象
csv_file = open('ColMajNums.csv','wb')
csv_file.write(codecs.BOM_UTF8)
csv_writer = csv.writer(csv_file,delimiter=',')


# 初始化数据库连接
ConIns = ConfigIni()
dbinfo = eval(ConIns.get_dbinfo())
MsIns = MSSQL(dbinfo[0],dbinfo[1],dbinfo[2],dbinfo[3])
QueryDict = eval(ConIns.get_QueryDict())
GroupList = MsIns.ExecQuery("select ID,GroupName from GXT_CLPSubjectGroup")


for i in GroupList:
    # 处理新版7选3数据，根据不同的组合统计相应的院校专业总数
    clpnewurl = "http://www.ewt360.com/clpnew/subjectindex?gid={gid}"
    Gid,GroupName = i
    print Gid,GroupName
    clpnewurl = clpnewurl.format(gid=Gid)
    resnew = opener.open(clpnewurl)
    responsenew = BeautifulSoup(resnew.read())
    CollMajorNewNums = responsenew.select(".page  > div")[0].get_text()

    GID = "组合 %s" % (Gid)
    bz = "备注：7选3新版按科目组合查询"
    csv_writer.writerow([GID, GroupName,CollMajorNewNums, bz])

    #处理老版7选3数据，根据不同的组合统计相应的院校专业总数
    a = GroupName.split("+")
    km1 = QueryDict[a[0]]
    km2 = QueryDict[a[1]]
    km3 = QueryDict[a[2]]

    clpurl = "http://www.ewt360.com/CLPCheckMajor?{km1}=1&{km2}=1&{km3}=1"
    clpurl = clpurl.format(km1=km1,km2=km2,km3=km3)
    resold = opener.open(clpurl)
    responseold = BeautifulSoup(resold.read())
    CollMajorOldNums = responseold.select(".page  > div")[0].get_text()

    bzold = "备注：7选3老版按科目组合查询"
    csv_writer.writerow([GID, GroupName, CollMajorOldNums, bzold])






