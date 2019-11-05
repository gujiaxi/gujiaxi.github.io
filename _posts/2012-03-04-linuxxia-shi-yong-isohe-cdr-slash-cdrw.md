---
layout: post
title:  "Linux下使用ISO和CDR/CDRW"
date:   2012-03-04 17:53
---
Linux下关于刻录操作的图形化工具也有不少，不过用命令来实现也很方便，而且如果在没有控制台的服务器上使用这些图形化工具并没有多大帮助，除非远程运行X。

## 从文件制作ISO映像

```shell
mkisofs -r /home/isaac/ > /tmp/isaac.iso
```
`-r`选项可以在生成的映像文件中加入Rock Ridge扩展，

## 从CD制作ISO映像

```shell
dd if=/dev/cdrom of=image.iso
```
这样可以创建CD的ISO映像，也可以通过`dd`的`bs`参数加快创建过程：
```shell
dd if=/dev/cdrom of=image.iso bs=10k
```

## 将ISO刻录到CDR/CDRW

```shell
cdrecord -v speed=12 dev=0,0,0 -data image.iso
```
`speed=`选项用于指定刻录机的写入速度，如果在刻录之前需要擦除CDRW，可以使用`blank=`参数：
```shell
cdrecord -v speed=12 dev=0,0,0 blank=fast -data image.iso
```

## 不创建ISO地刻录CDR/CDRW

```shell
mkisofs -r /home/isaac/ | cdrecord -v speed=12 dev=0,0,0 fs=8m -data -
```
综合了前面的操作，`cdrecord`的`-`参数意味着从STDIN而不是从文件读取数据磁道。`mkisofs`默认写到STDOUT。接着通过`|`传送给`cdrecord`的STDIN，在创建ISO时实时刻录。
