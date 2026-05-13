---
title: 50 GB of Exchange database logs are filling up my server
date: 2012-04-19
categories:
- exchange-2003
- exchange-2007
- exchange-2010
showTableOfContents: true
draft: false
---


Hey again,

{{< lead >}}
Today I wanted to share with you another field report regarding a troubleshooting case I've had with Exchange 2010.
{{< /lead >}}

A while back in 2009 I've re-posted a blog post from the Exchange Team Blog- [Troubleshooting Exchange 2003 and 2007 Store Log/Database growth issues](http://ilantz.com/2009/07/18/troubleshooting-exchange-2003-and-2007-store-logdatabase-growth-issues/ "http://ilantz.com/2009/07/18/troubleshooting-exchange-2003-and-2007-store-logdatabase-growth-issues/") - it included a link to [Mike Lagase](http://blogs.technet.com/b/mikelag/ "http://blogs.technet.com/b/mikelag/")'s blog and massive troubleshooting guide on this matter.

This week I've been called to help with an Exchange server 2010 that was creating tremendous amounts of log files for a specific database, with regards to the blog post I've mentioned, ExMon - Exchange Server User Monitor came to the rescue, real fast.

Fired it up with an interval of 15 minutes, and located the user that is responsible for the issue, note the screen shot, sorting by "Log Bytes" the top user created **800 MB in 15 minutes !!**

{{< figure src="images/log-bytes-winner.png" alt="ExMon Screen Shot - Log Bytes Winner" caption="ExMon Screen Shot - Log Bytes Winner" >}}

 

 

From this point forward it was easy to solve this issue, disabling both MAPI And Active Sync feature for the user, and detected the cause.

Case closed :)

**Update - Apr-2013**

The Exchange Team has a new post with lots of additions from the original post from 2009 - [Troubleshooting Rapid Growth in Databases and Transaction Log Files in Exchange Server 2007 and 2010](http://blogs.technet.com/b/exchange/archive/2013/04/18/troubleshooting-rapid-growth-in-databases-and-transaction-log-files-in-exchange-server-2007-and-2010.aspx "Troubleshooting Rapid Growth in Databases and Transaction Log Files in Exchange Server 2007 and 2010")
