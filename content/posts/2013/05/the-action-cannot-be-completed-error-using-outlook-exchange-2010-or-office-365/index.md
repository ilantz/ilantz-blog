---
title: The action cannot be completed error using Outlook - Exchange 2010 or Office
  365
date: 2013-05-05
categories:
- exchange-2010
- exchange-2013
- group-policy
- office-365
- outlook-mapi
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
Quick note from the field, if you are moving to Exchange Online / Office 365 you should double check your current office group-policy settings and registry for Outlook.
{{< /lead >}}

You should make sure that you **did not enable** the Closest GC setting, or configured a specific global catalog server with the DS Server registry entries under HKEY_CURRENT_USER\\Software\\Microsoft\\Exchange\\Exchange Provider

Both registry values, errors and methods for resolution are located at:

[http://support.microsoft.com/kb/2507626](http://support.microsoft.com/kb/2507626 "http://support.microsoft.com/kb/2507626") - Error in Outlook: "The action cannot be completed. The Bookmark is not valid"

[http://support.microsoft.com/kb/319206](http://support.microsoft.com/kb/319206 "http://support.microsoft.com/kb/319206") - How to configure Outlook to a specific global catalog server or to the closest global catalog server

And if we are on the subject, it's also a good practice to make sure the following when moving to Office 365:

- You do not have Autodiscover related registry settings also - [http://support.microsoft.com/kb/2212902](http://support.microsoft.com/kb/2212902 "http://support.microsoft.com/kb/2212902") - Unexpected Autodiscover behavior when you have registry settings under the \\Autodiscover key
- Make sure that the "Encrypt data between Microsoft Office Outlook and Microsoft Exchange Server" option under account settings of the Outlook Profile is indeed selected. Office 365 is restricting clients to encrypt MAPI traffic - see the following KB for additional information (originally written for Exchange 2010 RTM) - [http://support.microsoft.com/kb/2006508](http://support.microsoft.com/kb/2006508 "http://support.microsoft.com/kb/2006508")
