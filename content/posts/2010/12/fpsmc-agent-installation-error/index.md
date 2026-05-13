---
title: FPSMC Agent Installation Error
date: 2010-12-22
categories:
- exchange-2010
- forefront-protection
showTableOfContents: true
draft: false
---


{{< lead >}}
Forefront Protection Server Managment Console 2010 was latly been released, see the [FSS blog entry](http://blogs.technet.com/b/fss/archive/2010/12/17/forefront-protection-server-management-console-2010-has-been-released.aspx "Forefront Protection Server Management Console 2010 has been released!")
{{< /lead >}}

So a quick install, reveled some issues with the Deplay Agent task on some servers.. failing with this error:

Failed to deploy the Agent. Could not connect to net.tcp://ex-cas.contoso.com:8816/PushInstaller. The connection attempt lasted for a time span of 00:00:21.0157595. TCP error code 10060: A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond 192.168.5.20:8816.

Quick workaround, just configure the Firewall State for the specific failed servers for the domain profile to off :) or, configure the inbound port 8816 from the FPSMC consle server to that server..

Just a heads up for anyone who sees this.

Happy holidays !

Ilantz
