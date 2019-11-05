---
layout: post
title: "TinyOS下消息的发送和接收"
date: 2014-04-14 17:12
---
学习TinyOS也有一段时间了，消息的发送和接收算是比较基础的，直接看代码吧。

```c
#include <printf.h>

module SendAndReceiveC {
	uses {
		interface Boot;
		interface Timer<TMilli> as Timer;
		interface Leds;
		interface AMSend;
		interface AMPacket;
		interface Receive;
		interface SplitControl as AMControl;
	}
}

implementation {
	bool busy = FALSE;
	message_t pkt;
	uint16_t counter = 4;

	event void Boot.booted() {
		call AMControl.start();
	}

	event void AMControl.startDone(error_t err) {
		if (err == SUCCESS) {
			if (TOS_NODE_ID != 0) {
				call Timer.startPeriodic(2000);
				printf("This is a Sender: %d\n", TOS_NODE_ID);
				printfflush();
			}
			else {
				printf("This is a Receiver: %d\n", TOS_NODE_ID);
				printfflush();
			}
		}
		else {
			call AMControl.start();
		}
	}

	event void AMControl.stopDone(error_t err) {}

	event void Timer.fired() {
		if (!busy) {
			uint16_t * pktpl = (uint16_t *)(call AMSend.getPayload(&pkt, NULL));
			*pktpl = counter++;
			if (call AMSend.send(AM_BROADCAST_ADDR, &pkt, sizeof(uint16_t)) == SUCCESS) {
				printf("Sending...\n");
				printf("The source addr is: %d\n", call AMPacket.source(&pkt));
				printfflush();
				busy = TRUE;
			}
		}
	}

	event void AMSend.sendDone(message_t* msg, error_t err) {
		if (&pkt == msg) {
			printf("Send done!\n");
			printfflush();
			busy = FALSE;
		}
	}

	event message_t * Receive.receive(message_t* msg, void* payload, uint8_t len) {
		if (len == sizeof(uint16_t)) {
			uint16_t* pktpl = (uint16_t*)payload;
			printf("The received value is: %d\n", *pktpl);
			printfflush();
		}
		return msg;
	}
}
```

```c
configuration SendAndReceiveAppC {
}

implementation {
	components MainC;
	components new TimerMilliC() as Timer;
	components LedsC;
	components ActiveMessageC;
	components new AMSenderC(6);
	components new AMReceiverC(6);
	components SendAndReceiveC as App;
	components PrintfC, SerialStartC;

	App.Boot -> MainC;
	App.Timer -> Timer;
	App.Leds -> LedsC;
	App.AMSend -> AMSenderC;
	App.AMPacket -> AMSenderC;
	App.Receive -> AMReceiverC;
	App.AMControl -> ActiveMessageC;
}
```

```makefile
COMPONENT=SendAndReceiveAppC
include $(MAKERULES)
```
