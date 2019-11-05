---
layout: post
title: "学习R语言"
date: 2014-09-07 23:34
---
其实，之前写毕业论文的时候要处理数据，接触过R语言，不过那时候比较匆忙，基本上是边用边学的状态，最近终于有空从图书馆借了点书来系统地学一学了。

* 显示当前目录文件列表
```r
list.files(all.files=TRUE)
```

* 将输出结果重定向到文件
```r
sink("filename.txt")
source("script.R")
sink() # Resume writing output to console
```

* 从文件读取数据文件
```r
data <- read.table("statisticians.txt", header=TRUE, sep=",", stringAsFactor=FALSE)
data <- read.csv("stats.csv", header=TRUE)
```

* 写入数据文件
```r
write.csv(tb1, file="test.csv", row.names=FALSE)
write.table(tb1, file="test.txt", row.names=FALSE)
```

* 向量的`names`属性
```r
v <- c(10, 20, 30)
names(v) <- c("a", "b", "c")
print(v)
```

* 实体类型和抽象类型
```r
d <- as.Date("2014-12-13")
mode(d)
class(d)
```

* 向量和列表的区别
  - 向量中所有元素必须有相同的类型；
  - 列表中的元素可以是不同的类型

* 矩阵是有维数的向量（列表）
```r
A <- 1:6
dim(A)
dim(A) <- c(2,3)
print(A)
```

* 对向量添加数据的三种方法
```r
v[length(v)+1] <- newItem # Method 1
v <- c(v, c(1, 2, 4)) # Method 2
append(1:10, 5, after=4) # Method 3
```

* 构造矩阵
```r
cbind(1:6, 1:3) # cbind means column bind
cbind(list("a", "b", "c"), list(1, 2, 3))
```

* 因子（分类向量）

比如说某个球队在上一赛季的胜负情况，那么分类向量的Levels就是"win"跟"lose"。

* 列表中 lst[[n]] 与 lst[n] 的区别

`lst[[n]]`表示lst中第n个**元素**；`lst[n]`表示仅含有lst第n个元素的一个**列表**。

* 从列表中移除元素
```r
years <- list(1, 2, 3)
years[[2]] <- NULL
```

* 将列表转换为向量
```r
scores <- list(78, 23, 43)
mean(unlist(scores))
```

* 从列表中移除空值
```r
lst <- list("Mary", NULL, "Mickey")
lst[sapply(lst, is.null)] <- NULL
```

* 矩阵初始化
```r
theData <- c(1, 2, 3, 4, 5, 6)
mat <- matrix(theData, 2, 3, byrow=T)
```

* 矩阵运算
```r
mat1 <- matrix(c(1, 2, 3, 4), 2, 2)
mat2 <- matrix(c(2, 3, 4, 2), 2, 2)
t(mat1) # 转置
solve(mat2) # 求逆
mat1 %*% mat2 # 矩阵相乘
diag(4) #一个n阶对角(单位)矩阵
```

* 矩阵的行列名称
```r
rownames(mat) <- c("Name", "Gender", "Age")
colnames(mat) <- c("Tom", "Mary", "Hellen", "Jeremy")
```

* 从矩阵中选取一行或者一列
```r
mat[1,] # 选取第一行
mat[,2] # 选取第二列
```

* 由列数据初始化数据框
```r
dfrm <- data.frame(p1=pred1, p2=pred2, p3=pred3)
```

* 将向量列表转换为一个数据框
```r
lst <- list(p1=pred1, p2=pred2, p3=pred3)
dfrm <- as.data.frame(lst)
```

* 由行数据初始化数据框
```r
obs <- list(list("Hellen", 23), list("Tom", 24))
dfrm <- do.call(rbind, obs) # rbind means row bind
```

* 添加行至数据框
```r
suburbs <- rbind(suburbs, data.frame(city="West Dundee", county="Kane"), state="IL", data.fram(city="East Dundee", couty="Kane", state="IL"))
```

* 预分配数据框
```r
N <- 100
dfrm <- data.frame(dosage=numeric(N), lab=factor(N, levels=c("NJ", "IL", "CA")), response=numeric(N))
```

* 根据条件选择行列
```r
subset(dfrm, select=c(Name, Age, Salary), subset(salary > 3000 & Gender == "Male")) # similar to the query in database
```

* 将函数运用于每个列表元素
```r
lapply(lst, mean) # mean can be any other function
sapply(lst, mean) # s means simplify, simpler than lapply
```

* 将函数应用于每行（列）
```r
apply(mat, 1, fun) # mat is a matrix, number 1 means by row, fun is a function
apply(mat, 2, fun) # mat is a matrix, number 2 means by column, fun is a function
```

* 将函数应用于组数据
```r
tapply(x, f, fun) # x is a vector, f is a grouping factor, fun is a function
```

-----

- [R语言经典实例](http://is.gd/YWtQol)
- [R语言实战](http://is.gd/JTutWc)
- [R语言编程艺术](http://is.gd/2UNOEc)
- [R for Beginners](http://is.gd/BMWAyE)
- [An Introduction to R](http://is.gd/tkTLd7)
