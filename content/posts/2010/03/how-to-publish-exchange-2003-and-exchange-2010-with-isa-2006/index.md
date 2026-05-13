---
title: How to publish Exchange 2003 and Exchange 2010 with ISA 2006
date: 2010-03-12
categories:
- exchange-2003
- exchange-2010
- forefront-isatmg
showTableOfContents: true
draft: false
---


Hi,

First Step-By-Step !

{{< lead >}}
This guide will show you how to configure ISA 2006 for coexistence of Exchange 2003 with Exchange 2010 remote connectivity services, including:
{{< /lead >}}

- Outlook Web Access & Outlook WebApp
- Microsoft ActiveSync
- RPCoverHTTP - Outlook Anywhere
- Publishing Exchange 2010 FARM - two client access servers

This guide assumes that:

- ISA 2006 is configured to publish OWA 2003 and all additional services
- SSL is configured for the Exchange 2003 server
- Windows Integrated Authentication is enabled on the ActiveSync Vdir in the Exchange 2003 **Back-End** server ( [http://support.microsoft.com/?kbid=937031](http://support.microsoft.com/?kbid=937031) )
- RPC-over-HTTP was working for for 2003 mailboxes, and the 2003 back-end is configured as an RPC-over-HTTP
- The current configuration works ;)

- This guide will not cover scenarios when exchange is directly exposed to the internet. which I personally do not recommend in generally....

Okay here we go:

1. Configure redirection for Exchange 2003 OWA: Exchange 2010 will redirect a user that holds a mailbox in exchange 2003, this will be possible when the following cmdlet will be run on the Exchange 2010 Client Access server: `Get-OwaVirtualDirectory -server cas01-2010 | Set-OwaVirtualDirectory -Exchange2003Url https://owa.ext.com/exchange`
2. Publish Exchange 2010 client access web farm with ISA 2006, OWA first:

{{< figure src="images/1-new-rule-owa.png" alt="New OWA 2010 Publishing Rule" caption="New OWA 2010 Publishing Rule" >}} {{< figure src="images/2-rule-owa.png" alt="Outlook Web Access Publishing" caption="Outlook Web Access Publishing" >}}

\- Notice ISA 2006 does not provide a wizard (or the new form) for OWA 2010 - for that you need TMG

{{< figure src="images/3-farm-publish.png" alt="Publish 2010 Client Access Farm" caption="Publish 2010 Client Access Farm" >}} {{< figure src="images/4-bridge-options-to-cas-servers.png" alt="Choose SSL bridging options to CAS farm" caption="Choose SSL bridging options to CAS farm" >}}

{{< figure src="images/5-to-farm-2010.png" alt="Enter one of the CAS server internal name" caption="Enter one of the CAS server internal name" >}}

\- Now we need to create the Web Farm and select it as the target for the publishing rule

{{< figure src="images/6-newfarm.png" alt="Name the new Web Farm" caption="Name the new Web Farm" >}} {{< figure src="images/7-farm-connectivity-verification.png" alt="Choose Web Farm connectivity verification method" caption="Choose Web Farm connectivity verification method" >}}

 {{< figure src="images/8-confirm-isa-system-rule-for-verification.png" alt="Confirm isa system rule for verification" caption="Confirm isa system rule for verification" >}}{{< figure src="images/9-select-the-farm.png" alt="Select the created Web Farm" caption="Select the created Web Farm" >}}

\- Configure the web listener and authentication delegation option

\- The web listener should be already configured for Form Authentication and a valid SSL certificate

{{< figure src="images/10-public-name-for-rule.png" alt="Enter the Public DNS name for the rule" caption="Enter the Public DNS name for the rule" >}} {{< figure src="images/11-listerner.png" alt="Select the Listener ( should be already configured for 2003 publishing )" caption="Select the Listener ( should be already configured for 2003 publishing )" >}}

{{< figure src="images/12-delegation.png" alt="Select Basic Authentication for Credentials Delegation" caption="Select Basic Authentication for Credentials Delegation" >}} {{< figure src="images/13-user-sets.png" alt="Leave All Authenticated Users for Web Publishing ( ISA authenticates our users )" caption="Leave All Authenticated Users for Web Publishing ( ISA authenticates our users )" >}}

\- The publishing rule for the Web Farm is now complete.

\- Two additional configurations are now required:

1. Edit the new "exchange2010" Rule: **Remove** the legacy virtual directory's - /Exchange, /Exchweb and /Public they will continue to be published to your original 2003 rule. **Add** /ecp/\* as this is the new "options" applications for users, and a powerful administration web console with Exchange 2010. {{< figure src="images/14-edit-owa-rule.png" alt="Edit the new rule - remove all OWA 2003 vdir's" caption="Edit the new rule - remove all OWA 2003 vdir's" >}}
2. Edit the original OWA 2003 publishing rule and remove Microsoft-Server-ActiveSync path, we will next create ActiveSync publishing rule for Exchange 2010. {{< figure src="images/15-edit-owa-2003-rule.png" alt="Edit the original OWA 2003 publishing rule and remove Microsoft-Server-ActiveSync vdir" caption="Edit the original OWA 2003 publishing rule and remove Microsoft-Server-ActiveSync vdir" >}}

Now we have three last steps to finish our Exchange 2010 publishing:

1. Create a new Exchange Web Client Access rule - and select ActiveSync - Repeat most of part 1 except we select ActiveSync, publish the webfarm, enter the same info, and select the same listener.
2. Now as same for ActiveSync, we need to move the RPCoverHTTP (Outlook Anywhere) from the 2003 publishing rule to 2010 publishing rule. Delete the existing rule. Next you we will create a new publishing rule for Outlook Anywhere based on Exchange 2010.
3. Create a new Exchange Web Client Access rule - and select Outlook Anywhere - Repeat most of part 1 except we select Outlook Anywhere, publish the webfarm, enter the same info, and select the same listener.

That's it :)

if you kept up with all the requirements, all should be fine and you are now able to migrate your 2003 users to 2010 with ease, while both systems are allowed for external connectivity.

Enjoy!

More relevant links on the subject:

[Upgrading Outlook Web App to Exchange 2010](http://msexchangeteam.com/archive/2009/12/02/453367.aspx)

[Transitioning Client Access to Exchange Server 2010](http://msexchangeteam.com/archive/2009/11/20/453272.aspx)
