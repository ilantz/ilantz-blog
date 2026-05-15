---
title: TCP/IP KeepAlive, Session Timeout, RPC Timeout, Exchange, Outlook and you
date: 2013-01-14
categories:
- exchange-2003
- exchange-2007
- exchange-2010
- exchange-2013
- forefront-isatmg
- networking
- outlook-mapi
showTableOfContents: true
draft: false
slug: tcpip-keepalive-session-timeout-rpc-timeout-exchange-outlook-and-you
---


{{< lead >}}
**Update June 21th, 2016** **-** following feedback and a (true golden) blog post by the Exchange Team - Checklist for troubleshooting Outlook connectivity in Exchange 2013 and 2016 (on-premises) I've updated the recommended values for the timeout settings, and shortened the article overall for better reading. Do read the post in general, and in topic - check the CAS & Load Balancer configuration paragraphs.
{{< /lead >}}

* * *

Hi Again,

This post will spotlight networking considerations that are mostly overlooked. I've gathered a few of these issues that might brought you here searching for an answer:

- Outlook is retrieving data from the Microsoft Exchange Server
- The connection to Microsoft Exchange is unavailable. Outlook must be online or connected to complete this action
- Sent items are stuck in Outbox or delayed
- Outlook freezes or stuck when sending a message
- Event ID 3033 regarding Exchange Server ActiveSync complaining about the most recent heartbeat intervals used by clients
- Other strange / weird issues "but PING works! / telnet to the port works great!" - my personal favorite

The mentioned issues or symptoms could take place in any network environment, thus more common in complex network setups where multiple devices are protecting / route network traffic. Some typical configurations examples could be one of the following:

- Outlook Anywhere or RPC over HTTP is being used, servers are protected or published by ISA / TMG / UAG / F5 / Juniper or any other reverse proxy / publishing solutions
- Exchange servers are located behind a firewall, router or other network device
- Clients / Remote clients are located behind a firewall, router or other network device (just to be clear on that...)
- Exchange servers are being load-balanced with an external physical / virtual appliance

If you've read this post up until here and got disappointed because the above does not fit your issue, I'd like to suggest reviewing other RPC troubleshooting topics that might help [Troubleshooting Outlook RPC dialog boxes - revisited](http://blogs.technet.com/b/exchange/archive/2008/05/02/3405434.aspx) or [Outlook RPC Dialog Box Troubleshooting](http://support.microsoft.com/kb/982913)

Exchange Server traditionally (2000 to 2010) used MAPI over RPC to communicate "natively", RPC is known to be "sensitive" and that's why Exchange Server 2013 and beyond allows **only** Outlook Anywhere (RPC over HTTP) connections from clients which in my opinion is a great change that will simplify future deployments.

Client<>Server connections in general remains active while data "flows" , mails are sent/received etc. but when the connection is Idle, we might have a situation that it will be terminated. Here comes the term KeepAlive - a "dummy" packet that makes sure the connection remain active while no data is flowing and idle.

Here's my "how-to" suggestion:

- ~~Configure the RPC timeout on Exchange servers to make sure that components which use RPC will trigger a keep alive signal within the time frame you would expect:~~

{{< strike >}}
```cmd
reg add "HKLM\Software\Policies\Microsoft\Windows NT\RPC" -v "MinimumConnectionTimeout" -t REG_DWORD -d 120
```
{{< /strike >}}

- Consider modifying the server TCP/IP KeepAlive to reduce the chance of "IDLE" connections being terminated - (Default is Two hours - **The recommended value is 30 minutes , and no less then 15 minutes**) - this controls the OS TCP behavior with idle connections, could greatly improve responsiveness and scalability - [http://support.microsoft.com/kb/314053/EN-US](http://support.microsoft.com/kb/314053/EN-US)
- Make sure that you are aware of any router, firewall or any other network device that is placed between your clients and your servers. Once you do - note their session timeout, session TTL or session ageing setting for the relevant protocol and port! (this could be tricky, so do not treat this lightly)

The trick for success here is that timeout settings should be configured without overlapping one another while following the client access "path" - for example - Client > FW > Load Balancer > Server:

- FW timeout TCP/IP timeout - 40 minutes
- Load Balancer - TCP/IP timeout - 35 minutes
- Server - TCP/IP timeout - 30 minutes

If additional network devices are placed between the server and your clients, make sure that session timeout settings continue to be configured accordingly. With today's security measures, network security has become much more complex. A typical corporate network will implement many different network appliances or software based solutions to secure data, restrict access, prevent attacks and unwanted traffic. Bottom line - don't think you are done with network considerations just because "ping works" or an email comes with a statement like "your port is now open".

I hope this post will benefit others as this issue was and will probably remain common with Exchange and other client / server services.

Don't get timed out :) Ilantz

Additional useful links and sources of data:

- Checklist for troubleshooting Outlook connectivity in Exchange 2013 and 2016 (on-premises)
- [New Best Practice for RPC Timeouts in Exchange](http://www.expta.com/2012/06/new-best-practice-for-rpc-timeouts-in.html)
- [Outlook Anywhere Network Timeout Issue](http://blogs.technet.com/b/messaging_with_communications/archive/2012/06/06/outlook-anywhere-timeout-issue-and-recommendation.aspx)
- [Sent Items delayed when publishing Outlook Anywhere through TMG](http://blogs.technet.com/b/isablog/archive/2012/08/28/sent-items-delayed-when-publishing-outlook-anywhere-through-tmg.aspx)
- [Outlook getting Stuck/disconnected occassionally with Exchange](http://www.juniperforum.com/index.php?topic=6931.0)
- [The Microsoft Outlook’s requesting data problem — a detailed analysis](http://zatz.com/outlookpower/article/the-microsoft-outlooks-requesting-data-problem-a-detailed-analysis)
- [TCP/IP and NBT configuration parameters](http://support.microsoft.com/kb/314053/EN-US)
- [RPC cancel request dialogue box due to session timeout triggered by the Network devices](http://blogs.msdn.com/b/roopeshpattan/archive/2009/06/17/rpc-cancel-request-dialogue-box-due-to-session-timeout-triggered-by-the-network-devices.aspx)
- [Troubleshooting Outlook RPC dialog boxes - revisited](http://blogs.technet.com/b/exchange/archive/2008/05/02/3405434.aspx)
- [Outlook RPC Dialog Box Troubleshooting](http://support.microsoft.com/kb/982913)
- [Direct Push - ActiveSync](http://technet.microsoft.com/en-us/library/aa997252.aspx)