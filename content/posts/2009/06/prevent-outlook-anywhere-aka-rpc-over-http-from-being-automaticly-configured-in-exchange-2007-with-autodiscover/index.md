---
title: Prevent Outlook Anywhere (aka RPC over HTTP) from being automatically configured
  in Exchange 2007 with autodiscover
date: 2009-06-18
categories:
- exchange-2007
- exchange-2010
- outlook-mapi
showTableOfContents: true
draft: false
---


**Update #2** - July 28th 2014 -

{{< lead >}}
Removing the EXPR while Autodiscover is being utilized (which is probably the case in most deployments) will achieve preventing Outlook Anywhere from being used.
{{< /lead >}}

With that being said, a few commentators stated that they would like to continue using Outlook Anywhere and with Autodiscover enabled and the EXPR removed this will result in constant "removal" of the Outlook Anywhere settings that were statically configured.

If you want only specific users to be able to use Outlook Anywhere while others don’t I would advice considering the `Set-CasMailbox -MAPIBlockOutlookRpcHttp:$true` cmdlet to allow/block specific users.

**Update -** June 29th 2013 -

If you're going to deploy Exchange 2013 anytime soon - work your way to adapt autodiscover, and bring back the EXPR value. See [Exchange 2013 Outlook Anywhere Considerations](http://ilantz.com/2013/06/29/exchange-2013-outlook-anywhere-considerations/ "Exchange 2013 Outlook Anywhere Considerations") for more.

**This is an unsupported method, use at your own risk!**

Once “Outlook Anywhere” is configured on a client access server an EXPR entry is created. Then the autodiscover application picks up the change and publish it, along with the url’s for OAB,EWS & Availability. This basically “force” the automatic propagation of settings into the profile, including the checkbox for “Connect to Microsoft Exchange using HTTP” and filling the information for the HTTP proxy and authentication methods.

Microsoft documented Deployment Considerations for the Autodiscover Service in:

[http://technet.microsoft.com/en-us/library/aa997633(EXCHG.80).aspx](http://technet.microsoft.com/en-us/library/aa997633%28EXCHG.80%29.aspx "http://technet.microsoft.com/en-us/library/aa997633(EXCHG.80).aspx") - Where only Site Affinity is can be configured.

The Outlook provider setting and autodiscover relation are referenced quite good in the Exchange team blog:

[http://msexchangeteam.com/archive/2008/09/26/449908.aspx](http://msexchangeteam.com/archive/2008/09/26/449908.aspx)

A client of mine needed the possibility to disable the automatic propagation of the  "Connect to Microsoft Exchange using HTTP" setting in an Exchange 2007 environment . he did of course wanted to keep the ability to connect using "Outlook Anywhere"  if desired when configuring that manually.

Because autodiscover was made to auto-configure clients that are inside & outside the corporate network disabling this feature disables the ability for external outlook clients, that not domain joined to automatically connect using “Outlook Anywhere” . it does, however does not affect the configuration of a profile.

Within the exchange shell: `Get-outlookprovider –identity EXPR | remove-outlookprovider` Once this is done, recycle the application pool of AutoDiscover in IIS.

This solution will keep the outlook clients from automatically propagate the settings for “Outlook Anywhere” , but retains the possibility for configuring it manually. All web services and autodiscover information other then the proxy information itself are intact.

Updates (Thanks for all commentators)

- I've written another article related on the subject, highly recommended reading: [Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook Anywhere](http://ilantz.com/2011/02/08/authentication-pop-ups-and-annoyances-with-exchange-2007-2010-and-outlook-anywhere/ "Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook Anywhere")
- The above applies also for Exchange 2010
- To restore the EXPR provider, run the following:

`New-OutlookProvider -Name:EXPR`

I have done the required testing to make sure this solution works.

**This is an unsupported method, use at your own risk!**
