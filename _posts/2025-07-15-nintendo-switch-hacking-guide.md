---
layout: post
title:  "Nintendo Switch Hacking Guide"
date:   2025-07-15
---
## 准备工作

1. 通过序列号确认是否可以通过注入器进行破解。
2. 准备MicroSD卡，容量至少是64GB，推荐128GB，可以根据游戏安装需求选择。
3. 下载相关文件，确认版本，尽量选择最新的版本。
  - [Atmosphère](https://github.com/Atmosphere-NX/Atmosphere): Switch自制操作系统。
  - [Hekate](https://github.com/CTCaer/hekate): Switch引导文件。
  - [sys-patch](https://github.com/impeeza/sys-patch): 补丁，以支持安装非官方签名版本的游戏/软件，替代sigpatches。
  - [dbi](https://github.com/rashevskyv/dbi/tree/main): 多功能文件管理器，支持多种格式的游戏文件安装（NSP, NSZ, XCI and XCZ），可以通过HTTP/FTP/MTP连接，也能做存档管理。
  - [Lockpick_RCM](https://github.com/s1204IT/Lockpick_RCM): 获取本机密钥，在处理Switch文件或者变砖修复的时候会用到，如果担心出问题最好提前备份。
  - [impeeza/linkalho](https://github.com/impeeza/linkalho): 用于离线伪造Nintendo在线账号关联，部分游戏强制绑定账号时需要。

## 安装

### MicroSD卡制作

1. MicroSD卡格式化，推荐FAT32。
2. 下载并解压Atmosphère到MicroSD卡根目录，同时复制`fusee.bin`到`/bootloader/payloads/`.
3. 下载并解压hekate，包含两个: `bootloader`, `hekate_ctcaer_xxx.bin`
  - `bootloader`文件夹放到MicroSD卡根目录。
  - `hekate_ctcaer_xxx.bin`重命名为`payload.bin`放到RCM注入器的`ATMOSPHERE_HEKATE`目录下（这里还有一种更一劳永逸的方案是把SX Loader-payload放到RCM注入器，它会拉起MicroSD卡根目录下的`payload.bin`，因此不需要单独再更新RCM注入器中的文件）。
4. 下载并解压Lockpick_RCM到指定位置，用来备份系统keys.
5. 下载并解压dbi到指定位置，用来游戏安装。
6. 配置文件
  - `sdmc:/atmosphere/hosts/`: 屏蔽任天堂服务器相关的DNS解析。
  - `sdmc:/atmosphere/config/system_settings.ini`: 参考配置模板`sdmc:/atmosphere/config_templates/system_settings.ini`加入相关字段[启用USB 3.0](https://github.com/rashevskyv/dbi/blob/main/README_ENG.md#usb-30).
  - `sdmc:/atmosphere/exosphere.ini`: 参考配置模板`sdmc:/atmosphere/config_templates/exosphere.ini`，设置`blank_prodinfo_emummc=1`迫使虚拟系统隐藏序列号（`blank_prodinfo_sysmmc=1`对应的是真实系统隐藏序列号）。
  - `sdmc:/switch/DBI/dbi.config`: dbi的配置，详细字段可以参考官网解释。
7. 启动项自定义，配置文件`sdmc:/bootloader/hekate_ipl.ini`，其中需要引用`sdmc:/bootloader/res/`目录下的资源，以下是一个示例：

    ```
[config]
autoboot=0
autoboot_list=0
bootwait=3
customlogo=1
backlight=100
autohosoff=0
autonogc=0
[CFW-auto]
payload=bootloader/payloads/fusee.bin
icon=bootloader/res/icon_auto.bmp
[CFW-emuMMC]
fss0=atmosphere/package3
emummcforce=1
icon=bootloader/res/icon_emummc.bmp
[CFW-sysMMC]
fss0=atmosphere/package3
emummc_force_disable=1
icon=bootloader/res/icon_sysmmc.bmp
[Stock-sysMMC]
fss0=atmosphere/package3
emummc_force_disable=1
stock=1
icon=bootloader/res/icon_stock.bmp
    ```

### 引导启动

1. 拆下Switch右手柄，插入短接期间，Type-C口连接注入器。
2. 按住音量+键，期间再按一下电源键启动，以进入自制系统启动流程。

### 系统备份

1. 进入Hekate引导界面，点击Payloads，点击`Lockpick_RCM.bin`，按照指引执行SysNAND密钥导出。
2. 回到Hekate引导界面，进入Tools页签，点击`Backup eMMC`进入备份界面。
3. 点击`eMMC BOOT0 & BOOT1`执行BOOT物理分区备份。
4. 点击`eMMC RAW GPP`执行GPP物理分区备份。
5. 复制相关backup资料（包含以上三部分：密钥、BOOT0&BOOT1、RAW GPP）到外部存储后MicroSD卡上的可以删除。

### 创建虚拟系统

虚拟系统完全安装在MicroSD卡内，可以保证不污染Switch内部存储，是比较推荐的安装方式。目前安装方式有两种，SD File和SD Partition，推荐后者，因为后者的读取速度更快。

1. 打开Hekate，选择Tools，然后点击Partition SD Card.
2. 请保证MicroSD卡的使用容量在1GB以下，因为只有这样它才会提示自动备份和恢复数据（不然以上的配置可能需要重新做）。
3. 调整emuMMC (RAW)到29 GiB，界面上会显示`29 Full`，后续按照指引完成分区。
4. 返回Home，点击`emuMMC`，选择`Create emuMMC`，选择`SD Partition`，选择`Part 1`，等待完成即可按照指引进入虚拟系统。

## 基本使用

### 游戏安装

1. dbi有2种启动模式：点击相册进入Applet Mode; 按住`R`键同时启动任一游戏进入Application Mode（更高权限）。
2. 安装游戏比较简单的方式是MTP模式（快捷键是`X`），通过数据线连接电脑即可将Switch模拟为Android设备挂载（macOS下可以用AndroidFileTransfer进行文件传输）。
3. 启动MTP后，会显示几个挂载点，可以将游戏文件拖放至`MicroSD install`中即可启动安装，Switch屏幕显示进度及安装信息。
4. 由于新版的dbi只有俄语版，下面是几个常用的菜单翻译：

    ```
Главное меню                  Main Menu
============                  =========
Просмотр SD карты             Browse SD card
Просмотр установленных игр    Browse installed applications
Инструменты                   Tools
Запустить МТР соединение      Run MTP responder
Выход                         Exit
Инструменты                   Tools
===========                   =====
Очистка системы от мусора     Cleanup orphaned files
Удаление Wi-Fi профиля...     Deleting Wi-Fi profile...
Информация системе            System info
    ```

### 系统升级

1. 先升级Atmosphère, Hekate, Sys-Patch，升级方法很简单下载最新版本到MicroSD卡上（可能需要更新注入器的payload.bin）。⚠️注意保留`Nintendo`及`emuMMC`这两个文件夹，`Nintendo`是正版系统的数据，`emuMMC`是虚拟系统的数据；此外还有一些插件及自定义配置也需要注意按需保留避免覆盖。
2. 从[Switch Firmwares](https://darthsternie.net/switch-firmwares/)下载最新固件。并解压到MicroSD卡根目录。
3. 使用Daybreak来安装更新，选择Install，然后选择固件的安装目录。（如果Daybreak校验失败，可能是macOS添加隐藏文件的问题，可以通过`dot_clean`命令来清除隐藏文件。）
4. 如果固件校验通过，点击Continue选择Preserve settings, 如果可以选择Install (FAT32 + exFAT)就选这个，否则就选Install (FAT32)。
5. 安装完成之后，点击重启就完成升级了。

## 相关链接

* [acgotaku/switch: Switch安装Atmosphère手册](https://github.com/acgotaku/switch)
* [NH Switch Guide](https://switch.hacks.guide/)
* [Sigmapatches](https://sigmapatches.su)
* [impeeza/sys-patch](https://github.com/impeeza/sys-patch)
* [Atmosphere-NX/Atmosphere](https://github.com/Atmosphere-NX/Atmosphere)
* [CTCaer/hekate](https://github.com/CTCaer/hekate)
* [rashevskyv/dbi](https://github.com/rashevskyv/dbi/tree/main)
* [s1204IT/Lockpick_RCM](https://github.com/s1204IT/Lockpick_RCM)
* [impeeza/linkalho](https://github.com/impeeza/linkalho)
