---
layout: post
title: "R语言连接MySQL数据库"
date: 2014-09-19 22:45
---
首先把MySQL相关的软件安装完毕（包括**MySQL Connector/ODBC**），然后开始配置数据源。定位到`控制面板->系统和安全->管理工具->数据源(ODBC)`，添加一个数据源，驱动程序选择**MySQL ODBC**，然后<del>如下图，</del>填写数据源的信息。

接下来就是R的事情了。

首先当然是装上RODBC这个包，然后是创建连接，这里第一个参数`mysql_data`指的是刚才创建的数据源的名称，`uid`即数据库用户名，`pwd`是密码：

```
install.packages("RODBC")
conn <- odbcConnect("mysql_data", uid="root", pwd="2014");
sqlTables(conn);
dfrm <- sqlFetch(conn, "city")
```
