---
title: Exchange 2007 & Exchange 2003 Coexistence - CAS Proxy issues
date: 2009-03-01
categories:
- exchange-2003
- exchange-2007
showTableOfContents: true
draft: false
---


{{< lead >}}
sorry for the huge gaps , but it's been very busy and messed up lately... well anywayz
{{< /lead >}}

A CCR implementation, along with 2 HUB/CAS & 2 ISA servers to serve.

on the legacy side , an Exchange 2003 cluster based windows w2k & 2 front ends.

all seems to be working great , except that when it all came to start testing connectivity and co-existence with the 2003 backend cluster

using the new CAS servers to replace the frontend servers things went bad.

i've had error 500 when accessing 2007 mailboxes with /exchange,  404 errors when accessing /exchange and using 2003 Mailboxes.

also , event id 1000 , with source EPROX was logged in the CAS application log,  the description doesn't make much sense..except that it wrote the Backend cluster 2003 name.. " The description for Event ID 1000 from source EXPROX cannot be found. Either the component that raises this event is not installed on your local computer or the installation is corrupted. You can install or repair the component on the local computer. " If the event originated on another computer, the display information had to be saved with the event. The following information was included with the event: CLUSTER

Solving.. :)

the error 500 was solved when i double checked that all the CCR mailbox role features were installed, web-ISAPI-ext was missing, and now the 2007 mailboxes works with /exchange.

now, if you'll [read some in technet](http://technet.microsoft.com/en-us/library/bb885041.aspx) you'll find out on the hows and why and so on... BUT ! you should keep in mind that if you work with a Clustered backend , and you want to support any front end/cas

you should also follow the following KB:

["How to configure host header and authentication information in Exchange 2000 Server or Exchange Server 2003 Outlook Web Access on a Windows Server 2003 or Windows 2000 server cluster"](http://support.microsoft.com/kb/287726)

long story short now - to make this legacy proxy support , you should first check that navigating to your CAS mailboxes with /exchange WORKS to 2007 mailboxes first. rather use the default Form auth and dont change nothing to test it.

then , make sure you've added ALL the host headers you will use (eg; owa.company.com, owa.local.dom etc..) on your clustered backend 2003/2000 exchange servers.

once this works , you should not see any EPROX errors in applications log , nor Availability service errors that actually say that the CAS server cannot find your backend servers.

then you should be able to test with 2003 mailboxes through the CAS servers , and decommission any front end servers you might have.

Hope this helps!
