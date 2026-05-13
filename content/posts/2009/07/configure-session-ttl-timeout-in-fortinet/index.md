---
title: Configure Session TTL / Timeout in Fortinet
date: 2009-07-23
slug: configure-session-ttl-timeout-in-fortinet
categories:
- exchange-2003
- exchange-2007
- networking
showTableOfContents: true
draft: false
---


Hey there Mobile admins..

{{< lead >}}
Recently, I've did some troubleshooting with Fortinet and ActiveSync timeout, also known as Event ID 3030 Source: Server ActiveSync with the following being output to the Application Log on an Exchange Server 2003 and 2007.
{{< /lead >}}

Event Type: Warning Event Source: Server ActiveSync Event Category: None Event ID: 3033 Description: The average of the most recent [200] heartbeat intervals used by clients is less than or equal to [9]. Make sure that your firewall configuration is set to work correctly with Exchange ActiveSync and direct push technology. Specifically, make sure that your firewall is configured so that requests to Exchange ActiveSync do not expire before they have the opportunity to be processed.

Read more on the Direct Push in Technet : [Understanding Direct Push](http://technet.microsoft.com/en-us/library/aa997252.aspx) , typically you will need to adjust your session TTL to no less then 12 minutes.

Fortinet  lists the official help on the subject in [http://kb.fortinet.com/kb/microsites/microsite.do?cmd=displayKC&externalId=FD31862](http://kb.fortinet.com/kb/microsites/microsite.do?cmd=displayKC&externalId=FD31862) - FD31862 - Customizing Session TTL in FortiOS 4.0 [](http://kb.fortinet.com/kb/microsites/microsite.do?cmd=displayKC&externalId=FD31862), FortiOS 4 also allows this in Per rule ! so for all those with FortiOS 3 , use the mentioned KB from Fortinet try the FortiOS CLI Reference..

Usually i set this time out to no less the 15 minutes or 900 seconds.. you'r call :)

\-updated the link to Fortinet KB

### [_FortiOS_ CLI Reference](http://www.isp-tools.com/uploads/media/fortigate-cli-40-mr2.pdf)
