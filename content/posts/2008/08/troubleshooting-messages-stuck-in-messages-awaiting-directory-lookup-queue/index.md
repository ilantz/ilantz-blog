---
title: Troubleshooting messages stuck in 'Messages awaiting directory lookup' queue
date: 2008-08-12
categories:
- exchange-2003
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
So i've got to troubleshoot this issue in a very complex multi-domain & multiple exchange organizations & servers..
{{< /lead >}}

Internal Messages from Server A in ExchangeORG A , were failing in the categorizer while being processed to be sent to Server B in ExchangeORG B.

Following [kb884996](http://support.microsoft.com/kb/884996) , resolution 2 was valid in my situation, **Allow inheritable permissions from parent to propagate to this object** check box on Server A object, was missing a Tick..

I set this via ADSIEDIT , noticed of course that the "Exchange Domain Servers" ACE entries , from the other domain were added,  and allowed for replication.

After verifying that the ACE's were propegated & fully replicated, I did a quick restart to MTA, Routing & SMTP services on both servers , and operation was succesfully restored.

Just for extra , this could be also issues with Event Sink that might have been registered and inproperly removed / integrated.. using the [smtpreg.vbs](http://msdn.microsoft.com/en-us/library/ms528023\(EXCHG.10\).aspx) , "cscript smtpreg.vbs /enum > Output.txt" i was able to verify that no 3rd party Event Sink were installed or any of Exchange Event Sinks were disabled...

More Links on the Subject:

Troubleshooting messages stuck in 'Messages awaiting directory lookup' queue [http://msexchangeteam.com/archive/2006/06/23/428114.aspx](http://msexchangeteam.com/archive/2006/06/23/428114.aspx)

How to troubleshoot messages that remain in the "Messages awaiting directory lookup" queue in Exchange Server 2003 and in Exchange 2000 Server [http://support.microsoft.com/kb/251746](http://support.microsoft.com/kb/251746)

Directory service server detection and DSAccess usage [http://support.microsoft.com/kb/250570](http://support.microsoft.com/kb/250570)
