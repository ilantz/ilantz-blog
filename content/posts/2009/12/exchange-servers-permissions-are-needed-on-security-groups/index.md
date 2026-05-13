---
title: Exchange Servers Permissions are needed on Security Groups
date: 2009-12-02
categories:
- exchange-2007
showTableOfContents: true
draft: false
---


{{< lead >}}
Recently, I've encountered a situation where users that have been migrated to Exchange 2007 could not send mail to certain public folders.
{{< /lead >}}

It seems that the selected recipients were members of a security group that had inheritance disabled, and which had only few specific ACL's for Admins and such. but the " Exchange Servers " group were not included in the DACL.

The NDR reported back the recipients tried to send the email to the public folder was:

#550 5.2.0 STOREDRV.Deliver: The Microsoft Exchange Information Store service reported an error. The following information should help identify the cause of this error: "MapiExceptionNotAuthorized

To resolve this i've added Read Permissions - Allow for the Exchange Servers  group, with inheritance to all child objects.

Hope this will be useful !
