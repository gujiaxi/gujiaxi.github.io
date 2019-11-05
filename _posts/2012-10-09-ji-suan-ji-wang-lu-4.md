---
layout: post
title: "計算機網路(4)"
date: 2012-10-09 13:31
---
通過 [Socket](http://en.wikipedia.org/wiki/Network_socket) 來達到進程間通信目的編程叫做 Network Programming。網路程序和普通的程序有一個最大的區別是網路程序是由兩個部分組成的——客戶端和服務器端。

Socket 是 [IPC](http://en.wikipedia.org/wiki/Inter-process_communication)( Inter-process communication )所使用的一種[API](http://en.wikipedia.org/wiki/Application_programming_interface)。

Connection-oriented socket ( TCP )

![](/assets/img/20121009-1.png)

Connectionless socket ( UDP )

![](/assets/img/20121009-2.png)

主程式呼叫副程式傳遞資料(參數)的主要方式有：

* call by address
* call by reference
* call by value

Application protocol defines:

* Type of messages: request, response
* Message syntax: fields, format, length
* Message semantics: meaning of fields
* Actions

Network Program Performance Index:

* delay( time-sensitive )
* loss( reliable )
* throughput( bandwith )

## 撰寫程式
開啟主程式輸入10筆資料交由副程式排序，排序後在交由主程式印出。
```c
#include <stdio.h>
void BubbleSort(int * a, int n)
{
	int i, j, t;
	for(i = n; i > 0; i--)
	{
		for (j = 0; j < i - 1; j++)
		{
			if(a[j] > a[j+1])
			{
				t = a[j];
				a[j] = a[j+1];
				a[j+1] = t;
			}
		}
	}
}

void main()
{
	int a[10], i;
	for (i = 0; i < 10; i++) scanf("%d",&a[i]);
	BubbleSort(a, 10);
	for (i = 0; i < 10; i++) printf("%d ", a[i]);
	printf("\n");
}
```

## 程式說明
搜尋任一socket program，並解釋說明之：
```c
#include <stdlib.h>
#include <sys/types.h>
#include <stdio.h>
#include <sys/socket.h>
#include <linux/in.h>
#include <string.h>

int main()
{
	int sfp,nfp;	/* 定义两个描述符 */
	struct sockaddr_in s_add,c_add;
	int sin_size;
	unsigned short portnum=0x8888;	/* 服务端使用端口 */

	printf("Hello,welcome to my server !\r\n");
	sfp = socket(AF_INET, SOCK_STREAM, 0);
	if(-1 == sfp)
	{
		printf("socket fail ! \r\n");
		return -1;
	}
	printf("socket ok !\r\n");

	/* 填充服务器端口地址信息，以便下面使用此地址和端口监听 */
	bzero(&s_add,sizeof(struct sockaddr_in));
	s_add.sin_family=AF_INET;
	s_add.sin_addr.s_addr=htonl(INADDR_ANY);	/* 这里地址使用全0，即所有 */
	s_add.sin_port=htons(portnum);
	/* 使用bind进行绑定端口 */
	if(-1 == bind(sfp,(struct sockaddr *)(&s_add), sizeof(struct sockaddr)))
	{
		printf("bind fail !\r\n");
		return -1;
	}
	printf("bind ok !\r\n");
	/* 开始监听相应的端口 */
	if(-1 == listen(sfp,5))
	{
		printf("listen fail !\r\n");
		return -1;
	}
	printf("listen ok\r\n");

	while(1)
	{
		sin_size = sizeof(struct sockaddr_in);
	/* accept服务端使用函数，调用时即进入阻塞状态，等待用户进行连接，在没有客户端进行连接时，
	 * 程序停止在此处，不会看到后面的打印，当有客户端进行连接时，程序马上执行一次，然后再次循环到此处继续等待。
	 * 此处accept的第二个参数用于获取客户端的端口和地址信息。 
	 */
		nfp = accept(sfp, (struct sockaddr *)(&c_add), &sin_size);
		if(-1 == nfp)
		{
			printf("accept fail !\r\n");
			return -1;
		}
		printf("accept ok!\r\nServer start get connect from %#x : %#x\r\n",ntohl(c_add.sin_addr.s_addr),ntohs(c_add.sin_port));

		/* 这里使用write向客户端发送信息，也可以尝试使用其他函数实现 */
		if(-1 == write(nfp,"hello,welcome to my server \r\n",32))
		{
			printf("write fail!\r\n");
			return -1;
		}
		printf("write ok!\r\n");
		close(nfp);
	}
	close(sfp);
	return 0;
}
```

```c
#include <stdlib.h>   
#include <sys/types.h>   
#include <stdio.h>   
#include <sys/socket.h>   
#include <linux/in.h>   
#include <string.h>   
  
int main()
{
	int cfd; /* 文件描述符 */
	int recbytes;
	int sin_size;
	char buffer[1024]={0};    /* 接受缓冲区 */
	struct sockaddr_in s_add,c_add; /* 存储服务端和本端的ip、端口等信息结构体 */
	unsigned short portnum=0x8888;  /* 服务端使用的通信端口，可以更改，需和服务端相同 */
  
	printf("Hello,welcome to client !\r\n");
	/* 建立socket 使用因特网，TCP流传输 */
	cfd = socket(AF_INET, SOCK_STREAM, 0);
	if(-1 == cfd)
	{
		printf("socket fail ! \r\n");
		return -1;
	}
	printf("socket ok !\r\n");
	/* 构造服务器端的ip和端口信息，具体结构体可以查资料 */
	bzero(&s_add,sizeof(struct sockaddr_in));
	s_add.sin_family=AF_INET;
	s_add.sin_addr.s_addr= inet_addr("192.168.1.104"); /* ip转换为4字节整形，使用时需要根据服务端ip进行更改 */
	s_add.sin_port=htons(portnum); 
	/* 这里htons是将short型数据字节序由主机型转换为网络型，其实就是将2字节数据的前后两个字节倒换，
	 * 和对应的ntohs效果、实质相同，只不过名字不同。htonl和ntohl是操作的4字节整形。
	 * 将0x12345678变为0x78563412，名字不同，内容两两相同，
	 * 一般情况下网络为大端，PPC的cpu为大端，x86的cpu为小端，arm的可以配置大小端，需要保证接收时字节序正确。
	 */

	printf("s_addr = %#x ,port : %#x\r\n",s_add.sin_addr.s_addr,s_add.sin_port); /* 这里打印出的是小端和我们平时看到的是相反的。 */

	/* 客户端连接服务器，参数依次为socket文件描述符，地址信息，地址结构大小 */
	if(-1 == connect(cfd,(struct sockaddr *)(&s_add), sizeof(struct sockaddr)))
	{
		printf("connect fail !\r\n");
		return -1;
	}
	printf("connect ok !\r\n");
	/*连接成功,从服务端接收字符*/
	if(-1 == (recbytes = read(cfd,buffer,1024)))
	{
		printf("read data fail !\r\n");
		return -1;
	}
	printf("read ok\r\nREC:\r\n");

	buffer[recbytes]='\0';
	printf("%s\r\n",buffer);

	getchar(); /* 此句为使程序暂停在此处，可以使用netstat查看当前的连接 */
	close(cfd); /* 关闭连接，本次通信完成 */
	return 0;
}
```
