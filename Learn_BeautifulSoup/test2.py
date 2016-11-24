#coding=utf-8

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)
print soup.prettify()

print soup.title

print soup.title.string

print soup.title.parent.name

print soup.p

print soup.p['class']

print soup.a

print soup.find_all('a')

print soup.find(id="link3")

#从文档中找到所有<a>标签的链接：
for link in soup.find_all('a'):
    print (link.get('href'))

#从文档中获取所有文字内容：
print soup.get_text()

soup = BeautifulSoup("Sacr&eacute; bleu!")
print soup

# 对象种类：
"""
Tag,NavigableString,BeautifulSoup,Comment
"""

# Tag
soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b
print tag,type(tag)

"""
Tag 中最重要的属性：name 和 attributes  #name
"""

print tag.name

# change tag的name
tag.name = "blockquote"
print tag

"""
Tag 中最重要的属性：name 和 attributes  #Attributes
"""
print tag["class"]
#or
print tag.attrs

rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print rel_soup.a["rel"]

print unicode(tag.string)

print type(tag.string)

# NavigableString

# BeautifulSoup
print soup.name

# 注释及特殊字符串
markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup)
comment = soup.b.string
print comment,type(comment)

"""
Comment 对象是一个特殊类型的 NavigableString 对象
"""
print soup.b.prettify()

html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)
print type(soup.head)
print soup.body.b
print soup.find_all('a')

head_tag = soup.head
print head_tag
print head_tag.contents
title_tag = head_tag.contents[0]
print title_tag
print title_tag.contents

# for child in title_tag.children:
#     print child

print "a:",head_tag.descendants
for child in head_tag.descendants:
    print child
print '+++++'*60
print soup.children
print len(list(soup.children))
print '++++++'*60
print soup.descendants
print len(list(soup.descendants))

for string in soup.strings:
    print (repr(string))
