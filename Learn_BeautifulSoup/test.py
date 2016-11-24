#coding=utf-8
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf8')

csv_file = open('yxdatas1.csv','wb')
csv_writer = csv.writer(csv_file,delimiter=',')

response = BeautifulSoup(open("test.html"))
try:
    colleges = response.select(".anaMes")[0].string
    print colleges
except IndexError as e:
    print e
data = response.select(".anaBg > ul > li ")
for zklist in data:
    zkl = zklist.select("b")[0].get_text()
    print zkl
    # for i in zkl:
    #     zk = i
    #     print zk
    per = zklist.select("strong")[0].string
    print per
    csv_writer.writerow([colleges, zkl, per])
