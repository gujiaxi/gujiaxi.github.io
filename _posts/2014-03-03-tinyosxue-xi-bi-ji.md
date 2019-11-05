---
layout: post
title: "TinyOS学习笔记"
date: 2014-03-03 10:51
---
最近在学习 TinyOS, 记了些笔记，可能比较杂，希望跟大家交流学习。

## SPI, I2C, UART 三种总线协议的区别

* SPI: Serial Peripheral Interface
* I<sup>2</sup>C: Inter Integrated Circuit
* UART: Universal Asynchronous Receiver/Transmitter

> I<sup>2</sup>C比UART、SPI更为强大，但是技术上也更加麻烦些，因为I<sup>2</sup>C需要有双向IO的支持，而且使用上拉电阻，抗干扰能力较弱，一般用于同一板卡上芯片之间的通信，较少用于远距离通信。
> SPI实现要简单一些，UART需要固定的波特率，就是说两位数据的间隔要相等，而SPI则无所谓，因为它是有时钟的协议。
> I<sup>2</sup>C的速度比SPI慢一点，协议比SPI复杂一点，但是连线也比标准的SPI要少。
> SPI和UART可以实现全双工，但I<sup>2</sup>C不行。

## TinyOS 的架构
```
             +------------------------------------------+
             |              Application                 |
             +------------------------------------------+
             +--------+   +----------+   +--------------+
             | TinyOS | + | Platform | + | Sensor board |
             +--------+   +----------+   +--------------+
                                 |
                                 V
                        +-------------------+
                        | TinyOS tool chain |
                        +-------------------+
                                 |
              Target platform    V
               +-------------------------------------+
               |  +-------+    +-----+    +-------+  |
               |  | Radio |----| MCU |----|Sensors|  |
               |  +-------+    +-----+    +-------+  |
               +-------------------------------------+
```

硬件抽象架构 Hardware Abstraction Architecture (HAA):

1. Hardware Independent Layer (HIL) - 平台无关的硬件接口
2. Hardware Adaptation Layer (HAL) - 丰富的hardware-specific接口
3. Hardware Presentation Layer (HPL) - 硬件寄存器和中断相关

```
                           +-----------------------------+
                           |                             |
                           | Cross-platform applications |
                           |                             |
                           +--------------+--------------+
 +-----------------+                      |                  +-----------------+
 |Platform-specific|                      |                  |Platform-specific|
 |  applications   |                      |                  |  applications   |
 +--------+--------+                      |                  +--------+--------+
          |          Platform-independent | hardware interface        |      
          |        +-------------+--------+----+-------------+        |
          |        |             |             |             |        |
          |  +-----+-----+ +-----+-----+ +-----+-----+ +-----+-----+  |
          |  |.----+----.| |.----+----.| |.----+----.| |.----+----.|  |
          |  ||         || ||         || ||         || ||  HIL 4  ||  |
          |  ||  HIL 1  || ||  HIL 2  || ||  HIL 3  || |`----+----'|  |
          |  ||         || |`----+----'| |`----+----'| |     |     |  |
          |  |`----+----'| |     |     | |     |     | |     |  +--+--+
          +--+--+  |     | |.----+----.| |     |     | |     |  |  |
             |  |  |     | ||         || |.----+----.| |.----+--+-.|
             |.-+--+----.| ||         || ||         || ||         ||
             ||         || ||  HAL 2  || ||         || ||         ||
             ||         || ||         || ||  HAL 3  || ||  HAL 4  ||
             ||  HAL 1  || |`----+----'| ||         || ||         ||
             ||         || |     |     | ||         || ||         ||
             ||         || |     |     | |`----+----'| |`----+----'|
             |`----+----'| |.----+----.| |     |     | |     |     |
             |     |     | ||         || |.----+----.| |     |     |
             |.----+----.| ||  HPL 2  || ||         || |.----+----.|
             ||  HPL 1  || ||         || ||  HPL 3  || ||  HPL 4  ||
             |`----+----'| |`----+----'| |`----+----'| |`----+----'|
             +-----+-----+ +-----+-----+ +-----+-----+ +-----+-----+  HW/SW
                   |             |             |             |          boundary
        ************************************************************************
            +------+-----+ +-----+-----+ +-----+-----+ +-----+-----+
            |HW Plat 1   | |HW Plat 2  | |HW Plat 3  | |HW Plat 4  |
            +------------+ +-----------+ +-----------+ +-----------+
```

平台无关的应用程序一般应用HIL层提供的接口来编写，这样的程序可以很容易地实现跨平台。如果应用程序为了对硬件特定的功能有更好的控制，而针对特定平台的HAL层进行编写，那么它将牺牲可移植性。

## 电源管理
电源管理分为两部分：微控制器的电源状态、设备的电源状态。

## 同步(Synchronous)与异步(Asynchronous)
* Synchronous - "task context"
* Asynchronous - "interrupt context"

## 计时器的基本特性
* 精确性(Precision)：根据时钟频率将一分钟分隔为指定的拍子(ticks)，比如说一秒钟等于1024ms(binary units)，也等于32768ticks(32kHz的时钟)，也等于1048576μs
* 宽度(Width)：8-bit, 16-bit, 32-bit, 64-bit，一般是32-bit
* 准确性(Accuracy)：跟时钟漂移(clock drift)、硬件限制(hardware limitations)有关

**接口**：
```c
interface Counter<precision_tag,size_type>
{
  async command size_type get();  //返回当前时间
  async command bool isOverflowPending();  //是否设置了溢出标记
  async command void clearOverflow();  //清楚溢出标记
  async event void overflow();  //发出溢出信号
}

interface Alarm<precision_tag,size_type>
{
  // basic interface
  async command void start( size_type dt );  //清除先前的计时器并开始一个新的在调用时刻dt时间之后触发的计时器
  async command void stop();  //清除先前的计时器
  async event void fired();  //计时器时间到了发出信号

  // extended interface
  async command bool isRunning();  //是否存在活跃的计时器
  async command void startAt( size_type t0, size_type dt );  //清除先前的计时器并开始一个新的计时器，从调用时刻往前推t0时间开始算起，经过dt时间触发
  async command size_type getNow();  //以时钟精确度及宽度返回当前时刻
  async command size_type getAlarm();  //返回计时器将要何时触发
}

interface BusyWait<precision_tag,size_type>
{
  async command void wait( size_type dt );  //等待dt的时间
}

interface LocalTime<precision_tag>
{
  async command uint32_t get();  //返回当前时间
}

interface Timer<precision_tag>
{
  // basic interface
  command void startPeriodic( uint32_t dt );  //清除先前的计时器并开始一个以dt为周期（自调用时刻开始计算）触发的计时器直到停止
  command void startOneShot( uint32_t dt );  //清楚先前的计时器并开始一个在dt时间之后仅触发一次的计时器
  command void stop();  //停止计时器
  event void fired();  //计时器时间到了发出信号

  // extended interface
  command bool isRunning();  //是否存在活跃的计时器
  command bool isOneShot();  //是否是单次触发的计时器
  command void startPeriodicAt( uint32_t t0, uint32_t dt );  //清除先前的计时器并开始一个新的计时器，从调用时刻往前推t0时间开始算起，经过dt时间周期性触发
  command void startOneShotAt( uint32_t t0, uint32_t dt );  //清除先前的计时器并开始一个新的计时器，从调用时刻往前推t0时间开始算起，经过dt时间单次触发
  command uint32_t getNow();  //以时钟精确度及宽度返回当前时刻
  command uint32_t gett0();  //返回计时器开始计时的时刻（如果是周期性的则是上一次触发的时刻），即t0
  command uint32_t getdt();  //返回计时器的延迟（或者是周期），即dt
}
```
