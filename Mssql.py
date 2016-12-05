#coding=utf-8
from config import ConfigIni
import pymssql

class MSSQL:
    def __init__(self,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    def __GetConnect(self):
        try:
            self.conn = pymssql.connect(host=self.host,user=self.user,password=self.pwd,database=self.db,charset="utf8")
            cur = self.conn.cursor()
        except NameError as e:
            raise e,"没有设置数据库信息，数据库连接失败"
        return cur

    def ExecQuery(self,sql):

        cur = self.__GetConnect()
        cur.execute(sql)
        resList = cur.fetchall()

        self.conn.close()
        return resList

if __name__ == "__main__":
    a = eval(ConfigIni.get_dbinfo())
    print a[0],a[1],a[2],a[3]
    print type(a[0])
    # b = MSSQL(a[0],a[1],a[2],a[3])
    # print b
    ms = MSSQL(host=a[0],user=a[1],pwd=a[2],db=a[3])
    print ms
    s = "SELECT COUNT (DISTINCT(MajorID)) * 1.0 FROM GXT_CLPMajorSubject WHERE SubjectCode IN (SELECT SubjectCode FROM dbo.GXT_CLPSubjectGroup INNER JOIN dbo.GXT_CLPSubjectGroupDetail ON dbo.GXT_CLPSubjectGroupDetail.GroupID = dbo.GXT_CLPSubjectGroup.ID WHERE GroupID = {GroupID})AND MajorID IN (SELECT ID FROM GXT_CLPMajor )AND CollegeID IN (SELECT id FROM dbo.GXT_CLPCollege WHERE LinkCode IN (SELECT LinkCode FROM dbo.GXT_College))"
    s = s.format(GroupID=1)
    c = ms.ExecQuery(s)
    print c
    d = ms.ExecQuery("SELECT COUNT(1) * 1.0 FROM GXT_CLPMajor")
    print d
    f = c[0][0]/d[0][0]
    print f
    # print c[0][0],d[0][0]
    e = c[0][0]/d[0][0]
    # f = ms.ExecQuery("SELECT GroupID,SubjectCode,GroupName FROM dbo.GXT_CLPSubjectGroup INNER JOIN dbo.GXT_CLPSubjectGroupDetail ON dbo.GXT_CLPSubjectGroupDetail.GroupID = dbo.GXT_CLPSubjectGroup.ID")
    # print len(f)
    # for (GroupID,SubjectCode,GroupName) in f:
        # print GroupID,GroupName