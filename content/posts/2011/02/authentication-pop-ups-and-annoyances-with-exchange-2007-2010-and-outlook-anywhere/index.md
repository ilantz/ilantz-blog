---
title: Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook
  Anywhere
date: 2011-02-08
slug: authentication-pop-ups-and-annoyances-with-exchange-2007-2010-and-outlook-anywhere
categories:
- exchange-2007
- exchange-2010
- outlook-mapi
showTableOfContents: true
draft: false
---


Hi again,

{{< lead >}}
This issue has came up too much, so I wanted to blog something short about this.
{{< /lead >}}

Prerequisites:

- **Update** (Added June 29th 2013) - If using Exchange 2013, check out [Exchange 2013 Outlook Anywhere Considerations](http://ilantz.com/2013/06/29/exchange-2013-outlook-anywhere-considerations/ "Exchange 2013 Outlook Anywhere Considerations") for some additional specific Exchange 2013 issues.
- Exchange 2007 or 2010
- Outlook 2003 / 2007 / 2010
- Windows XP / 7 / etc..
- Outlook Anywhere ( RPC over HTTP ) enabled - with Basic Authentication or NTLM Authentication
- Autodiscover - working correctly ;)

So, you've got it all configured, you enabled Outlook Anywhere, configured ISA 2006 / TMG / UAG to publish the Outlook Anywhere (or not), you published Autodiscover records an all is working great !

BUT ! you have this annoying user credentials pop ups, and users are going nuts ! and so do you !@ ( enough sarcasm ) it may work for a while, and then you are prompted again for user and password, or even worse - it might not work at all...

Here's what can go wrong in bullets because we have a few different issues that might cause troubles..

- Outlook Anywhere is configured to use NTLM authentication:
    - Solution 1 - Configure MSSTD or the Certificate Principle Name correctly (see below)
    - Solution 2 - Configure your clients local security policy, in specific - LmCompatiblilityLevel to 2 or 3
    - Solution 3 - If you try to pull NTLM with ISA / TMG / UAG, either configure "Kerberos Constrained Delegation" - check links below for the white-paper from Microsoft" or change the publishing rule to apply to "All Users" and in the Authentication Delegation tab choose the option "No delegation, but client may authenticate directly"
- SSL Certificates issues
    - Outlook Anywhere was enabled for - mail.company.com (ExternalHostName), but you have a wildcard certificate or the certificate subject name does not match mail.company.com
    - Solution - Configure MSSTD or the Certificate Principle Name correctly (see below)
- Outlook Anywhere continuously keep being configured automatically !%
    - Solution - Lucky for you I have already blogged about this :) [Prevent Outlook Anywhere (aka RPC over HTTP) from being automatically configured in Exchange 2007 with autodiscover](http://ilantz.com/2009/06/18/prevent-outlook-anywhere-aka-rpc-over-http-from-being-automaticly-configured-in-exchange-2007-with-autodiscover/ "Prevent Outlook Anywhere (aka RPC over HTTP) from being automaticly configured in Exchange 2007 with autodiscover")
    - **Update** (Added June 29th 2013) - If you're going to deploy Exchange 2013 anytime soon - work your way to adapt autodiscover and don't go in this path..

So what's that MSSTD or Certificate Principle Name ? well it's a method Outlook can verify that the server you are connecting to indeed holds the correct SSL certificate subject name before sending credentials to.. well yeah it ain't that secure.

{{< figure src="images/bpos-msstd.png" alt="Microsoft Exchange Proxy Settings" caption="Microsoft Exchange Proxy Settings" >}}

This setting is actually being configured automatically since Exchange 2007 and continue to be with Exchange 2010.

So here's what you can do with it - all examples follow the [Set Outlook Provider](http://technet.microsoft.com/en-us/library/bb123683.aspx) cmdlet syntax:CertPrincipalName

- You have a wildcard certificate - Run this command:

```powershell
Set-OutlookProvider EXPR -CertPrincipalName msstd:*.company.com
```

- You have a differnet subject name on your SSL certificate then the ExternalHostName you configured for Outlook anywhere on your CAS server

```powershell
Set-OutlookProvider EXPR -CertPrincipalName msstd:correctsubject.company.com
```

- You **don't** want that "only connect to proxy servers that have this principle name in their certificate" check box marked at all ! :)

`Set-OutlookProvider EXPR -CertPrincipalName none`

**New feature with Exchange 2010 -** The Set-OutlookProvider cmdlet now allows Outlook 2010 clients to connect exclusively through RPC over HTTP (Outlook Anywhere) before trying RPC over TCP connections when connecting over the Internet. !

This means you can control the check box "On fast network, connect using HTTP first, then connect using TCP/IP", here's the two options:

- Always connect using HTTP (mark "on fast networks") :

```powershell
Set-OutlookProvider EXPR -OutlookProviderFlags:ServerExclusiveConnect
```

- User TCP/IP first then HTTP (default):

```powershell
Set-OutlookProvider EXPR -OutlookProviderFlags:None
```

This should cover it, no more pop ups and hopefully Outlook Anywhere and you will be friends again !

Credits (or links) :

[When, if and how do you modify Outlook Providers?](http://msexchangeteam.com/archive/2008/09/29/449921.aspx)

[Set-OutlookProvider](http://technet.microsoft.com/en-us/library/bb123683.aspx)

[Publishing Outlook Anywhere Using NTLM Authentication With Forefront TMG or Forefront UAG](http://www.microsoft.com/download/en/details.aspx?id=22723)

[Exchange 2013 Outlook Anywhere Considerations](http://ilantz.com/2013/06/29/exchange-2013-outlook-anywhere-considerations/ "Exchange 2013 Outlook Anywhere Considerations")

ilantz
