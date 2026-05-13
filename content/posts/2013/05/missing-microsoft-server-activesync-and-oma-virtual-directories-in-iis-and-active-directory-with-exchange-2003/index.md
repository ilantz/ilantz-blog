---
title: Missing Microsoft-Server-ActiveSync and OMA virtual directories in IIS and
  Active Directory with Exchange 2003
date: 2013-05-06
categories:
- exchange-2003
- exchange-2010
showTableOfContents: true
draft: false
---


Hi Again,

{{< lead >}}
I've encountered a situation today with an Exchange 2003 to 2010 migration, The Exchange 2003 Back-End server was missing the virtual directories in IIS, but this issue had an interesting twist ... both vdirs were missing also in the Active Directory !
{{< /lead >}}

Missing or corrupt virtual directories with Exchange are common and can be easily solved with KB 883380 - [How to reset the default virtual directories that are required to provide Outlook Web Access, Exchange ActiveSync, and Outlook Mobile Access services in Exchange Server 2003](http://support.microsoft.com/kb/883380 "How to reset the default virtual directories that are required to provide Outlook Web Access, Exchange ActiveSync, and Outlook Mobile Access services in Exchange Server 2003")

Exchange Server setup creates each virtual directory in the AD forest configuration partition under services, microsoft Exchange, administrative groups, administration group name, server name, protocols, http, virtual server name (usually 1).

In this case, both ActiveSync and OMA virtual directories were missing from Active Directory and as a result were also missing from the System Manager MMC, so performing a Repair Setup or the Reset virtual directories method will render useless.. both will not **write** anything new to the AD.. we had to re-create the two virtual directories both in AD and the IIS, so using System Manager, we try to create a new virtual directory, but the ActiveSync and OMA is greyed out !

{{< figure src="images/microsoft-server-activesync-and-oma-missing-from-active-directory.png" alt="Microsoft-Server-ActiveSync and  OMA Missing From Active Directory" caption="Microsoft-Server-ActiveSync and  OMA Missing From Active Directory" >}}

{{< figure src="images/creating-new-virtual-directories-with-system-manager-grayed-out.png" alt="Creating New Virtual Directory With System Manager Grayed out" caption="Creating New Virtual Directory With System Manager Grayed out" >}}

With some searching I've reached a solution that worked perfectly (dated back to 2007 from the Microsoft Exchange newsgroup), this will enable the options within the System Manager and allow us to re-create the virtual directories and restore order :)

1\. Using ADSIEDIT locate the Exchange 2003 server container - services, microsoft Exchange, administrative groups, administration group name and right click the server name to open it's properties. 2. Locate the Heuristics attribute and note the current value (just in-case...) our value in this case was 805310468. 4. Change the value to 270012416 , click apply and ok. 5. Refresh the Exchange System Manager or close and re-open it. 6. Now, locate the server name within the tree, expend it, expend protocols, expend HTTP, expend the virtual server name and right click to create a new Virtual Directory. You should now be able to recreate the Microsoft-Server-ActiveSync and OMA virtual directory.

**Note** \- This will also reset your RPC over HTTP and other "server specific" settings that you configured on the server using the System Manager GUI. so make sure to note all configurations under the server properties page and re-enable any changes after setting the value.

Credits - [http://microsoft.newsgroups.archived.at/public.exchange.setup/200702/07021815421.html](http://microsoft.newsgroups.archived.at/public.exchange.setup/200702/07021815421.html "http://microsoft.newsgroups.archived.at/public.exchange.setup/200702/07021815421.html")

I hope this helps anyone struggling with this,

Ilantz
