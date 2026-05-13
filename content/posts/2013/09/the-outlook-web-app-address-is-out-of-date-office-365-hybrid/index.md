---
title: The Outlook Web App address is out of date - Office 365 Hybrid
date: 2013-09-02
categories:
- exchange-2010
- office-365
showTableOfContents: true
draft: false
---


Quick note from the field..

{{< lead >}}
I've encountered an issue with an Exchange 2010 and Office 365 Hybrid configuration, users that were moved to Office 365 and tried to reach the original On-Premise OWA URL were receiving an error - The Outlook Web App address https://owa.domain.com/owa is out of date.
{{< /lead >}}

{{< figure src="images/the-outlook-web-app-address-is-out-of-date.png" alt="The Outlook Web App Address Is Out Of Date" caption="The Outlook Web App Address Is Out Of Date" >}}

What should have happen is that the OWA will offer the users to use the URL configured on the TargetOwaUrl parameter on the Organization Relationship to the Office 365 routing domain. After some digging I've realized that this hybrid setup was performed using the manual steps that were documented for Exchange 2010 SP1, so the Hybrid Configuration Wizard did not do it's magic....

Anyhow, after comparing this setup with a **working** hybrid configuration including the OWA redirection, I've noticed that the TargetOwaUrl value did not had xxx**/owa/**xxxx in it's URL.

So instead of http://outlook.com**/owa/**domain.mail.onmicrosoft.com - I've had http://outlook.com/domain.mail.onmicrosoft.com

So after running Set-OrganizationRelationship -TargetOwaURL "http://outlook.com/owa/domain.mail.onmicrosoft.com” the redirection worked as expected.

Hope this helps out anyone,

See also: [Simplify the OWA URL for Office 365 Hybrid](http://community.office365.com/en-us/wikis/exchange/simplify-the-owa-url-for-office-365-hybrid.aspx)

ilantz
