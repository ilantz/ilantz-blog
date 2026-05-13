---
title: Don't forget to modify your Windows Server Power Options
date: 2015-02-16
categories:
- exchange-2013
- misc
- server-2008-r2
- server-2012
showTableOfContents: true
draft: false
---


{{< lead >}}
Following a troubleshooting session I've had lately, I wanted to share with you an important recommended settings that most folks (myself included) often overlook.
{{< /lead >}}

With more and more virtual servers and less and less physical servers being deployed, capabilities like [SpeedStep](http://en.wikipedia.org/wiki/SpeedStep) of a CPU were forgotten. Take for example the following "modest" specifications of [Intel Xeon E5-2690 v2](http://ark.intel.com/products/75279/Intel-Xeon-Processor-E5-2690-v2-25M-Cache-3_00-GHz), with 10 cores @ 3.0 GHz this is a "fare" spec for a high load / CPU intensive profile server.

BUT ! if you forget to select the "High Performance" power option in Windows Server for example, you could end up with:

{{< figure src="images/e5-2690v2-at-half-speed.png" alt="e5-2690v2 at half speed" caption="e5-2690v2 at half speed" >}}

Notice that the speed of the CPU is less the half the speed it can run at. now to make things better, just make sure to select the "preferred" settings for your busy server:

{{< figure src="images/e5-2690v2-at-full-speed.png" alt="e5-2690v2 at full speed" caption="e5-2690v2 at full speed" >}}

Just a heads up for all you folks out there, the default "Balanced" option caused a performance issue with an Exchange 2013 server that was running on this physical hardware and once the option was changed - all was back to normal :)

ilantz
