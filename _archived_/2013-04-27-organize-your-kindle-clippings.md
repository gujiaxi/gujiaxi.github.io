---
layout: post
title: "Organize Your Kindle Clippings"
date: 2013-04-27 21:22
---
用Kindle看书也有一段时间了，积累了不少的读书笔记，但是都堆在一个文件(My Clippings.txt)里不太方便，索性写了一个脚本来导出每一本书的读书笔记到独立的文件。

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
bookList = {}
bookName = ''
clippings = open('1524.txt', 'r')
line = clippings.readline()
bookTitle = line[:-1]
bookList[bookTitle] = line
while 1:
line = clippings.readline()
bookList[bookTitle] = bookList.get(bookTitle) + line
if (line == '='*10+'\n'):
line = clippings.readline()
if not line:
break
bookTitle = line[:-1]
if not bookList.has_key(bookTitle):
bookList[bookTitle] = ''
bookList[bookTitle] = bookList.get(bookTitle) + line
clippings.close()
for title in bookList.keys():
book = open(title+'.txt', 'w')
book.write(bookList[title])
book.close()
```

后来才看到这里有个[网站](http://www.clippingsconverter.com/)可以很方便地导入并管理。。。Orz
