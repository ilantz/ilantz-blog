---
title: Exchange Calendar Update Tool - Extract Mailboxes from Exchange 2010 fails
date: 2010-12-20
categories:
- dst
- exchange-2010
- outlook-mapi
showTableOfContents: true
draft: false
---


{{< lead >}}
Every year at December, we at Israel ( and at some other points of the year, over the world.. ) have to rebase some calendar appointments..
{{< /lead >}}

This entry is not about daylight saving bashing ;) but just a note to anyone that will use the Exchange Calendar Update Tool against Exchange 2010 mailboxes and servers.

I did not had enough time to actually find out why and what is the appropriate fix for this, but here's a workaround for the error and the empty result when extracting the mailboxes from the servers..

If you will examine the logs in the msextmz extract log, when trying to search for the mailboxes on the required servers, you will notice that the output will be empty, and zero mailboxes will be reported.

needless to say that this obviously eliminates the possibility for extracting timezones from the mailboxes - i will not cover this issue, because in Israel we need to rebase the appointments just to reflect the current daylight saving durations..

Any way here's the error:

> [20-Dec-2010 12:51:56][3684]:HrProcessMailboxTable:Please log on to a profile with administrator privileges. [20-Dec-2010 12:51:56][3684]:HrProcessMailboxTable:Unable open mailbox table for server /o=Contoso/ou=Exchange Administrative Group (FYDIBOHF23SPDLT)/cn=Configuration/cn=Servers/cn=EX-2010.  Error 0x80004005. [20-Dec-2010 12:51:56][3684]:HrProcessMailboxTable:Returning Error 0x80004005

You can easily report the mailboxes from powershell using:

Get-mailbox -ResultSize:unlimited -RecipientTypeDetails usermailbox | select ServerLegacyDN, LegacyExchangeDN | Export-Csv mailboxes.csv

Then use excel to export the data and match it with the format for the update tool which should be like this:

ServerLegacyDN <TAB> LegacyExchangeDN <TAB> TimeZone

Save that to a TXT, watch the formatting and tabs ! remove all the csv hyphens,commas etc..

 

Hope this will be fixed anytime soon, or a clarification will be published..

until then, good luck !

and Happy Holidays !

Some Links:

[Using the Exchange Calendar Update Tool to address daylight saving time changes for Exchange Server](http://support.microsoft.com/kb/930879 "Using the Exchange Calendar Update Tool to address daylight saving time changes for Exchange Server")

[December 2010 DST Cumulative Update for Windows operating systems](http://blogs.technet.com/b/dst2007/archive/2010/12/02/december-2010-dst-cumulative-update.aspx "December 2010 DST Cumulative Update for Windows operating systems")

ilantz
