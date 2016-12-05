#coding=utf-8
from config import ConfigIni
from Mssql import MSSQL
import csv
import codecs
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

csv_file = open('MajorPer.csv','ab+')
csv_file.write(codecs.BOM_UTF8)
csv_writer = csv.writer(csv_file,delimiter=',')

ConIns = ConfigIni()
dbinfo = eval(ConIns.get_dbinfo())
MsIns = MSSQL(dbinfo[0],dbinfo[1],dbinfo[2],dbinfo[3])



# 从基表中查询数据并计算百分比（%）
"""
按照科目查询
"""
GroupList = MsIns.ExecQuery("select ID,GroupName from GXT_CLPSubjectGroup")
for i in GroupList:
    GroupID,GroupName = i

    #从基表计算不同组合(科目)对应的专业数
    MajornumSql = "SELECT COUNT (DISTINCT(MajorID)) * 1.0 FROM GXT_CLPMajorSubject WHERE SubjectCode IN (SELECT SubjectCode FROM dbo.GXT_CLPSubjectGroup INNER JOIN dbo.GXT_CLPSubjectGroupDetail ON dbo.GXT_CLPSubjectGroupDetail.GroupID = dbo.GXT_CLPSubjectGroup.ID WHERE GroupID = {GID})AND MajorID IN (SELECT ID FROM GXT_CLPMajor )AND CollegeID IN (SELECT id FROM dbo.GXT_CLPCollege WHERE LinkCode IN (SELECT LinkCode FROM dbo.GXT_College))"
    MajornumSql = MajornumSql.format(GID=GroupID)
    Majornum = MsIns.ExecQuery(MajornumSql)

    #从专业表计算专业总数
    MajorTotalnumSql = "SELECT COUNT(1) * 1.0 FROM GXT_CLPMajor"
    # MajorTotalnumSql = MajorTotalnumSql.format()
    MajorTotalnum = MsIns.ExecQuery(MajorTotalnumSql)

    #计算百分比
    MajorPer = round(Majornum[0][0]/MajorTotalnum[0][0],3)
    print GroupID,GroupName,Majornum[0][0],MajorTotalnum[0][0],MajorPer

    # 写入CSV文件
    GID = "组合 %s"%(GroupID)
    bzhu = "按组合查询"
    csv_writer.writerow([GID,GroupName,Majornum[0][0],MajorTotalnum[0][0],MajorPer,bzhu])



    # # 从基表计算不同分类的专业数
    # MajornumSql = "SELECT COUNT (DISTINCT(MajorID)) * 1.0 FROM GXT_CLPMajorSubject WHERE SubjectCode IN (SELECT SubjectCode FROM dbo.GXT_CLPSubjectGroup INNER JOIN dbo.GXT_CLPSubjectGroupDetail ON dbo.GXT_CLPSubjectGroupDetail.GroupID = dbo.GXT_CLPSubjectGroup.ID WHERE GroupID = {GID})AND MajorID IN (SELECT ID FROM GXT_CLPMajor )AND CollegeID IN (SELECT id FROM dbo.GXT_CLPCollege WHERE LinkCode IN (SELECT LinkCode FROM dbo.GXT_College))"
    # MajornumSql = MajornumSql.format(GID=GroupID)
    # Majornum = MsIns.ExecQuery(MajornumSql)
    #
    # # 计算专业表对应不同分类的专业总数
    # MajorTotalnumSql = "SELECT COUNT(1) * 1.0 FROM GXT_CLPMajor"
    # # MajorTotalnumSql = MajorTotalnumSql.format()
    # MajorTotalnum = MsIns.ExecQuery(MajorTotalnumSql)
    #
    # # 计算百分比
    # MajorPer = round(Majornum[0][0] / MajorTotalnum[0][0],3)
    # print GroupID, GroupName, Majornum[0][0], MajorTotalnum[0][0], MajorPer
    #
    # # 写入CSV文件
    # GID = "组合 %s" % (GroupID)
    # bzhu = "按本专科查询"
    # csv_writer.writerow([GID, GroupName, Majornum[0][0], MajorTotalnum[0][0], MajorPer, bzhu])