---
title: 432-4.3.2 STOREDRV and Store Driver throttling
date: 2011-04-10
slug: 432-4-3-2-storedrv-and-store-driver-throttling
categories:
- exchange-2010
showTableOfContents: true
draft: false
---



Hi again,

{{< lead >}}
Wanted to share with you a situation I've encountered with Exchange 2010 SP1.
{{< /lead >}}

The subject mail system suffered from an extensive downtime. The mailbox server role had it's databases unavailable due to a storage outage, but as any major mail system - SMTP does not just "stop".. and after a long 24+ hours of downtime, there were quite a few messages that were waiting to be delivered to the system's recipients... counted ruffly around 5000+

Once the storage system issue was solved, and the mailbox databases were back up, the queue viewer showed that all 20 databases had around 100+ messages to deliver, which triggered the Exchange 2010 SP1 Store Driver throttling, more "verbose" information was also found at the Hub Transport connectivity log @ TransportRolesLogsConnectivity directory showing the exact error is:

> 432-4.3.2 STOREDRV; mailbox server is too busy

In a few words, throttling makes sure that a single client or a "specific issue" could effect the whole mail system, and it works in several aspects with Exchange 2010, some might be client, protocol and server role throttling.

In our case, the Mailbox Store engine throttling was triggered due the overwhelming messages per seconds, per recipient and the connection the hub transport servers was issuing to the mailbox server role.

Now, we could have "accept" this by-design behavior, but once the service was backup, it's expected to have all queues zeroed-out, that is "where's all the emails from today??!"

So, the goal was - let's turn the throttling off , in regards to the Hub Transport <> Mailbox Server connections and once all queues are empty we will turn it on, sounds logical ? well, after quite a few searches I've noticed that the documentation is missing...

The Hub Transport throttling ( advanced ) settings are controlled in the throttling configuration on the edgetransport.exe.config file under the Bin directory, but the setting to disable the throttling all together is nowhere to be found.. the only references found were: `<add key="RecipientThreadLimit" value="2" /> <add key="MaxMailboxDeliveryPerMdbConnections" value="3" />`

even setting these values to ridicules numbers did not help, we still had 100+ messages waiting at each database delivery queue.

Only after a more furious search I've stumbled upon the following "hidden" magic setting: `<add key="MailboxDeliveryThrottlingEnabled" value="False" />`

Restarted the Hub Transport service, waited a few seconds and... here's the result:

{{< figure src="images/hub-transport-throttling-disabled.png" alt="Hub-Transport-Throttling-Disabled" caption="Hub-Transport-Throttling-Disabled" >}}

:)

Of course, once all queues were zeroed-out, took around 5 minutes, I've enabled throttling to the original value "True" and restarted the Hub Transport services again.

Hope this helps you out!

Links for the enthusiasts:

[Exchange 2010 SP1 Store Driver throttling - Tony Redmond's blog](http://thoughtsofanidlemind.wordpress.com/2010/12/07/exchange-2010-sp1-store-driver-throttling/)

[Understanding Message Throttling - Technet](http://technet.microsoft.com/en-us/library/bb232205.aspx)

[Understanding the EdgeTransport.exe.Config File - Technet](http://technet.microsoft.com/en-us/library/ee681659.aspx)
