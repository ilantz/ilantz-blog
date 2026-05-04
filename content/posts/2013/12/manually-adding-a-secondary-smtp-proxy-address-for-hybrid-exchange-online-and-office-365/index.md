---
title: Manually adding a secondary SMTP proxy address for hybrid Exchange Online and
  Office 365
date: 2013-12-22
categories:
- exchange-2010
- exchange-2013
- office-365
- powershell
showTableOfContents: true
draft: false
---


{{< lead >}}
**Update** \- 05-02-2015 - Thanks for the feedback about this post, some more work has been done, please download the new version...
{{< /lead >}}

**Update** \- 07-30-2014 - Thanks for the feedback about this post, I've republished the code. it is now wrapped as a script and also logs results to a log file. download the new version...

I've been busy with more Office 365 and Hybrid Exchange Online deployments and came up with a script I hope will help some of you out there.

While deploying an Hybrid Exchange Online setup, one of the steps the Hybrid Configuration Wizard is doing is modifying the email address policy and adding "alias@tenant.mail.onmicrosoft.com" to the relevant EAP policies. This is great although there's a good chance you have some mailboxes that are set with EmailAddressPolicyEnabled:$false

I've written a function script that will help you add the additional secondary SMTP proxy address to those mailboxes easily :)

Here's an example on how to use the script:

`.\Add-OnMicrosoftSMTP.ps1 -Tenant:ilantz`

The script will require your "Tenant" name, for example - if your Office 365 tenant is ilantz.onmicrosoft.com, enter ilantz as the tenant name. Once entered it will find all mailboxes with the property EmailAddressPolicyEnabled:$false and have no routing SMTP address like \*@tenant.mail.onmicrosoft.com (following the default Exchange Hybrid Configuration Wizard settings). Then the script will add the required SMTP proxy address following the PrimarySmtpAdress prefix, if that SMTP proxy address is already taken, the function will add a random 5 digit number to the prefix - John.Doe12345@tenant.mail.onmicrosoft.com.

The script will catch and display any exceptions that may occur during the process. and will automatically log the results to a log file.

Get the script here - [http://gallery.technet.microsoft.com/Office-365-Add-Exchange-14c7f0c3](http://gallery.technet.microsoft.com/Office-365-Add-Exchange-14c7f0c3) Revision History --------------------------------------------------------------------------------

1.0 - Initial release

1.1 - Updated and rewritten as a script instead of a function which caused confusion

1.2 - Added Logging of successful addresses being added and failures

1.3 - Updated with server-side filtering to get all relevant users for better efficiency, an updated logging mechanism and using now the PrimarySmtpAddress prefix value for the routing address.

Enjoy !
