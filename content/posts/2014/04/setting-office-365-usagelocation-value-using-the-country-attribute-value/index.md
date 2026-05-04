---
title: Setting Office 365 UsageLocation value using the Country attribute value
date: 2014-04-10
categories:
- office-365
- powershell
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
Since Office 365 projects started, setting users\` licenses with scripts has been somewhat of an issue.
{{< /lead >}}

There are great scripts out there to automate assigning licenses to users, but the prerequisite of assigning an Office 365 license to a user is to choose the Usage Location for that user. When dealing with several dozens or hundreds of users that might be fine, but for large scaled deployments this becomes also an issue. and I've decided to script it and share this in case anyone will need this as much as I did.

This script is has a really simple logic, trace down the Country attribute value for each user, match that with the two letter country code (required for the PowerShell Set-MsolUser command) and set that value for the user.

I've worked up to match the list from [https://www.iso.org/obp/ui](https://www.iso.org/obp/ui) to the countries available for selection within the Office 365 portal.

Keep in mind that the script will not handle any spelling errors, so be sure to maintain the country value BEFORE you run this script. If you are using Directory Synchronization this should be more productive as your Active Directory will also benefit from this move...

The script will try to find an exact match of the country value, although - case Insensitive.

grab it here: [http://gallery.technet.microsoft.com/office/Setting-Office-365-Usage-4d685175](http://gallery.technet.microsoft.com/office/Setting-Office-365-Usage-4d685175)

Please share your comments if you have any, I would love hearing this script is being used.
