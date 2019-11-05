---
layout: post
title:  "Linux下创建虚拟网络热点"
date:   2012-1-18 00:24:58
---
引子：其实早就想写这篇文章了，不过现在在写的这篇应该会跟原先预期的有很大的不同，虽然题目是这个，但是……还是把我遇到的种种想到的跟想不到的情况一起说说吧。

原先入了kindle，wifi还是很必要的，连上wifi，书、杂志、报纸……唰唰的就过来了。而且Amazon的silk浏览器也还可以(虽然还是Experimental)，看看New York Times、瞧瞧Gmail……都很方便。而且现在冬天了，早上躺在床上都不想起来（至少我是这样的），更别说对着电脑敲键盘了。有wifi就好了，钻在被窝，掏出小机机，连上自建的AP，那速度～啧啧……而且。。。有了它，玛麻再也不用担心我每个月的流量了。不光手机，平板的话就更好了，在家到哪儿都有无线，大年夜拿着平板，连上自己房间的wifi热点，陪着父母在客厅一起看春晚，爽～

好了，我们开始吧，先从Windows开始，Windows下很简单，方法也很多，win7的话直接启动承载网络就行了，不多说了，自行Google吧（因为这不是这篇文章的重点）。另外要是够懒的话也可以使用软件：[Connectify](http://www.connectify.me)、[Visual Router](http://virtualrouter.codeplex.com)、[Bzeek](http://www.bzeek.com)……设置同样很简单，略。

好了，Windows下就这样，但是，作为一个不折腾会死星人+对瘟到死无爱星人的我来说，这显然不是我想要的。重点来了。
其实Linux下要是ad-hoc的话很简单，我也不多说了，但是问题是kindle不支持这个模式，所以没戏。

然后就只有AP咯，这里我走了不少弯路，网上很多乱七八糟的，被误导了很多次。搞清楚之后呢，其实也很简单，前提是有一枚足够给力的无线网卡（偏偏我就是没有）。

首先，对于PCI网卡，运行`lspci`（对于USB网卡的话运行`lsusb`）：

可以看到我的输出如下：

```
05:00.0 Network controller: Intel Corporation Centrino Wireless-N 1000
```

好了，下面一步比较关键，看你的无线网卡是否支持`master mode`，也就是AP模式，如果不支持的话，下面的你不用看了，基本没戏了。运行：

``` shell
sudo iwconfig wlan0 mode master
```

我的输出如下：

```
Error for wireless request "Set Mode" (8B06) :
SET failed on device wlan0 ; Invalid argument.	//悲剧掉了。
```

不过还有机会。。。有些新的网卡用的是mac80211 framework，对于这些网卡的话，用iwconfig来测试它是否支持master模式是行不通的。因为他们是使用新的nl80211接口在用户空间通信的.我们用iw这个工具来测试（没有的话就装一个）：

``` shell
iw list
```

如果`Supported interface modes`中有AP的话，那么恭喜，你的网卡支持用hostapd来架设软AP。

```
Supported interface modes:
	* IBSS
	* managed
	* monitor    # 我又悲剧了。
```

好了，对于我来说，到这儿就差不多可以了（根本就不支持AP，还捣鼓个鸟蛋啊！），但还是不甘心，于是就有了接下来的故事（如果你足够幸运的话，那么下面的斜体部分就可以直接跳过了）：

在亚马逊看中了Mercury MW150u这款无线网卡，说是采用AR9271芯片（Linux下用ath9k_htc驱动（内核自带），支持AP模式），前天发货，昨天就到了，发货到挺给力的，不过悲剧的还在后面，到手后果断插上开始“调教”，然后……这玩意儿用的是RALink的芯片，而不是Alteros的芯片，准确的说是RALink RT5370N，然后我就无奈了，算了，凑和着捣鼓吧，应该问题不是很大，然后……

插上之后压根儿就没法儿驱动啊，更别说什么架AP了，然后就是请教谷歌大大咯，这个问题好像挺普遍的样子，大部分都是国外的开源社区（貌似国内的社区没有啥学习的氛围），不过貌似挺棘手，好多都是折腾了好多天最后实在不行就再买了一块其他的网卡（这招貌似挺管用的），但是我还是说一下官方驱动的安装方法，至少让它驱动起来，能不能建AP先不管，步骤如下：

1. 首先在[这儿](http://www.ralinktech.com/en/04_support/license.php?sn=5003)下载官方的驱动并解压；
2. 修改`os/linux/config.mk`：将`HAS_WPA_SUPPLICANT`和`HAS_NATIVE_WPA_SUPPLICANT_SUPPORT`都改成`=y`并保存；
3. 修改`os/linux/usb_main_dev.c`：在`MODULE_DESCRIPTION("RT2870 Wireless Lan Linux Driver");`后面加上一句`MODULE_LICENSE("GPL");`并保存；
4. 编译安装：

   ``` shell
   sudo make
   sudo make install
   ```

   现在再`ifconfig -a`应该就可以看到ra0这个网卡了（可能需要重启）:

   ```
   ra0	Link encap:Ethernet  HWaddr 38:83:45:17:b7:44  
	   inet6 addr: fe80::3a83:45ff:fe17:b744/64 Scope:Link
	   UP BROADCAST MULTICAST  MTU:1500  Metric:1
	   RX packets:0 errors:0 dropped:0 overruns:0 frame:0
	   TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
	   collisions:0 txqueuelen:1000 
	   RX bytes:70 (70.0 B)  TX bytes:3796 (3.7 KB)
   ```

   网上说编译安装完成之后还要运行`sudo modprobe rt5370sta`来加载这个模块，不过我发现编译安装完成之后就已经加载了，所以不需要手动加载了。

5. 事情看似到这里已经结束了，可是事实却没有这么简单……这个驱动只支持infrastructure和adhoc功能，要玩Soft AP的话得用rt2800usb。而且貌似要3.0及以上内核。

   ``` shell
   sudo modprobe rt2800usb
   sudo -s
   echo 148F 5370 > /sys/bus/usb/drivers/rt2800usb/new_id
   exit
   ```

好了，网卡的问题到这儿就结束了，接下来的就简单了：

1. 安装hostapd，修改`/etc/hostapd/hostapd.conf`如下。这是一个WPA-PSK的配置，用`hostapd -d /etc/hostapd/hostapd.conf`来测试配置是否可用。

   ```
   interface=wlan1
   driver=nl80211
   ssid=vlad_is_here
   channel=6
   hw_mode=g
   ignore_broadcast_ssid=0
   auth_algs=1
   wpa=3
   wpa_passphrase=xxxxxxxx
   wpa_key_mgmt=WPA-PSK
   wpa_pairwise=TKIP
   rsn_pairwise=CCMP
   ```

2. 起hostapd服务：

   ``` shell
   sudo /etc/rc.d/hostapd start
   ```

3. 为新无线网卡指定IP：

   ``` shell
   sudo ifconfig wlan1 10.10.10.1 netmask 255.255.255.0
   ```

4. 安装配置dhcp，`/etc/dhcpd.conf`如下：

   ```
   default-lease-time 600;
   max-lease-time 7200;
   subnet 10.10.10.0 netmask 255.255.255.0 {
	   range 10.10.10.10 10.10.10.100;
	   option routers 10.10.10.1;
	   option domain-name-servers 8.8.8.8;
	   option ip-forwarding off;
	   option broadcast-address 10.10.10.255;
   }
   ```

5. 起dhcpd服务：

   ``` shell
   sudo /etc/rc.d/dhcp4 start
   ```

6. 安装iptables，增加转发规则，这里要把流量转发到wlan0：

   ``` shell
   sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
   ```

7. 启用内核转发功能：

   ``` shell
   echo net.ipv4.ip_forward=1 >> /etc/sysctl.conf
   ```

**收工！**
