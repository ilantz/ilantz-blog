---
title: Grant Full Access to All Mailboxes in Exchange 2010 - even for new databases
date: 2010-11-17
categories:
- exchange-2010
- powershell
showTableOfContents: true
draft: false
---


Hi again,

{{< lead >}}
Since Exchange 2010 was released I always run into this request from administrators and help desk personnel:
{{< /lead >}}

"I want full access to all mailboxes, and also to all future mailboxes too ! uh and new mailboxes in new mailbox databases too !"

:)

The following commands will do the trick, copy the first row separately- **Exchange 2010 only**:

```powershell
$user = Read-Host -Prompt:"Enter UserName to grant permissions";
``

$organization = Get-OrganizationConfig;` `$databasesContainer = "CN=Databases,CN=Exchange Administrative Group (FYDIBOHF23SPDLT),CN=Administrative Groups," + $organization.DistinguishedName;` `Add-ADPermission -User:$user -AccessRights ExtendedRight -ExtendedRights Receive-As, Send-As, ms-Exch-Store-Admin -Identity:$databasesContainer;
```

And remember with Active Directory permissions an explicit allow overwrites an inherited deny. so this will work even if you do this to an admin user / group.

Hope this helps !
