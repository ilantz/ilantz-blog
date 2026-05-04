---
title: Exchange 2013 Outlook Anywhere Considerations
date: 2013-06-29
categories:
- exchange-2013
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
With Exchange 2013 deployments already in place, I've wanted to share with you all some "new" behaviors, tips and more to help you prevent headaches and issues :)
{{< /lead >}}

With regards to two previously posts - [Prevent Outlook Anywhere (aka RPC over HTTP) from being automatically configured in Exchange 2007 with autodiscover](http://ilantz.com/2009/06/18/prevent-outlook-anywhere-aka-rpc-over-http-from-being-automaticly-configured-in-exchange-2007-with-autodiscover/ "Prevent Outlook Anywhere (aka RPC over HTTP) from being automatically configured in Exchange 2007 with autodiscover") and also [Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook Anywhere](http://ilantz.com/2011/02/08/authentication-pop-ups-and-annoyances-with-exchange-2007-2010-and-outlook-anywhere/ "Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook Anywhere") - this post is some sort of a follow-up.

With Exchange 2013, Outlook Anywhere (aka RPC over HTTP/s) is the default method for Outlook clients connections - that is **no** more direct RPC connections to the servers for Outlook clients. Exchange 2013 will essentially require you to utilize Autodiscover and Outlook Anywhere to actually get your Outlook client connected. This is the main reason for writing this post. This information will come useful if you are getting ready or already started to deploy Exchange 2013, I'll try to keep it simple and write this down as a list of things to consider so this will be rather easy to all.

1. If you followed my post about how to prevent Outlook Anywhere from being configured and removed the EXPR outlook provider, start with restoring it. Run the following powershell command to restore it: `New-OutlookProvider -Name:EXPR`
2. If you're using any additional methods to configure Outlook Clients or Outlook Anywhere like, static XML files, Registry settings or Group Policy settings make sure to revise or even remove them. See also [http://support.microsoft.com/kb/2212902](http://support.microsoft.com/kb/2212902 "Unexpected Autodiscover behavior when you have registry settings under the \Autodiscover key")
3. Pay attention to publishing guides for Exchange 2013 - see [Publishing Exchange Server 2013 using TMG](http://blogs.technet.com/b/exchange/archive/2012/11/21/publishing-exchange-server-2013-using-tmg.aspx "Publishing Exchange Server 2013 using TMG") and also [Exchange 2013 Client Access Server Configuration](http://technet.microsoft.com/en-us/library/hh529912%28v=exchg.150%29.aspx "Exchange 2013 Client Access Server Configuration")
4. When enabling Outlook Anywhere on Exchange 2013 notice the following:
    1. Retain the current **External** authentication method (Basic,NTLM) your internal authentication method should always be NTLM. `Get-OutlookAnywhere –Server (hostname) | Set-OutlookAnywhere -InternalHostname "mail.domain.com" -InternalClientAuthenticationMethod Ntlm -InternalClientsRequireSsl $true -ExternalHostname "mail.domain.com" -ExternalClientAuthenticationMethod Basic -ExternalClientsRequireSsl $true -IISAuthenticationMethods NTLM,Basic -ssloffloading:$false`
    2. Enable NTLM on the IIS /rpc directory of your Exchange 2007/2010 servers `Get-OutlookAnywhere | ?{ $_.AdminDisplayVersion -notlike "Version 15.*"} | Set-OutlookAnywhere -IISAuthenticationMethods NTLM,Basic`
5. Plan the CertPrincipalName value you will use, that is the certificate Subject Name that your clients will use to populate the msstd:server.domain.com value - **both** internally and externally (reminding you to see the note above). My personal best practice is to use the same Subject Name on the certificate you will use on your External TMG/UAG/Juniper/F5 reverse proxy and your internal server or servers. Once you are aware of this value you can configure your Outlook Provider accordingly (you can refer to [this post](http://ilantz.com/2011/02/08/authentication-pop-ups-and-annoyances-with-exchange-2007-2010-and-outlook-anywhere/ "Authentication pop ups and annoyances with Exchange 2007 / 2010 and Outlook Anywhere") for more information on the subject).
6. If you installed a wildcard certificate on your Exchange 2013 server - you **must** perform the following:
    1. Update your EXPR setting - `Set-OutlookProvider EXPR -CertPrincipalName msstd:*.company.com`
    2. Update your EXCH setting (yes!) - `Set-OutlookProvider EXCH -CertPrincipalName msstd:*.company.com`
7. Don't freak out when you see Exchange 2013 "new" server name - it's value is actually the Mailbox GUID value, and will be unique for all users. This means that - you **must** use the Autodiscover wizard to configure outlooks from now on, Email, password and click next. If you have full mailbox access to a different mailbox - that's great- just type it's email address and enter whatever you want for password. (will work only inside the LAN...)
8. Don't forget to update your Outlook clients - or else they will **not** connect to Exchange 2013 - see [Exchange 2013 System Requirements](http://technet.microsoft.com/en-us/library/aa996719%28v=exchg.150%29.aspx) for the exact information.

That's it for now, while deployments continue I will update this topic with new "gotchas".

Hope this helps anyone out there. Ilantz
