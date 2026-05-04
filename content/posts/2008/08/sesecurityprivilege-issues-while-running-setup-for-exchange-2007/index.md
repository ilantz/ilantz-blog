---
title: SeSecurityPrivilege issues while running setup for Exchange 2007
date: 2008-08-12
categories:
- exchange-2007
- server-2008-r2
showTableOfContents: true
draft: false
---


{{< lead >}}
So, yet another implamentation of exchange, this time i've encounted the following error while installing the CAS role on the server.
{{< /lead >}}

Setup exited with the following error:

The process does not possess the '**SeSecurityPrivilege**' privilege which is required for this operation.

Searching the privilege showed that "**Exchange Servers**" & more accurate in our situation , the "**Domain Administrators****"** were not configured in the "**Manage auditing and security log**" , because the Default Domain Policy & Default Domain Controllers Policy GPO's was re-created and the default ones were left with the link set to off.

Easy to monitor those privileges with whoami.exe from the support tools, i love it that the server 2008 installs them all as dependencies !

Once we've added the DomainAdministrators , DomainExchange Servers to the policy , setup ran okay :)
