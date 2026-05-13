---
title: This message could not be sent - Error 0x80070005 - Office 365 | Report non-inherited
  Send-As permissions script
date: 2014-06-04
categories:
- exchange-2010
- exchange-2013
- office-365
- powershell
showTableOfContents: true
draft: false
---


{{< lead >}}
After a few incidents from Office 365 deployments, I'd like to share this issue to help anyone facing it.
{{< /lead >}}

If you or anyone of your users tried to send an email and use the "From" option to send as another recipient you might face NDR's (non delivery reports) which will include these errors:

- Delivery has failed to these recipients or groups
- This message could not be sent. Try sending the message again later, or contact your network administrator.  Error is [0x80070005-00000000-00000000]

Using Exchange Server Error Code Look-up ([Download Err.exe](http://www.microsoft.com/en-us/download/details.aspx?id=985)), 0x80070005 resolves back to MAPI_E_NO_ACCESS or E_ACCESSDENIED which bring us to the actual cause of the issue.

**SendAs / Send-as** permissions are not retained in migrations to Office 365 just because it is based on an ACL set in Active Directory and ACLs are not synced to Office 365.

To add a SendAs permission use the Add-RecipientPermission cmdlet with Exchange Online Remote PowerShell or use the Exchange Admin Control Panel and add the Send As permission from the "Mailbox Delegation" menu.

```text
Add-RecipientPermission "Help Desk" -AccessRights SendAs -Trustee "Ayla Kol"
```

See the full reference about the command here - [http://technet.microsoft.com/en-us/library/ff935839(v=exchg.150).aspx](http://technet.microsoft.com/en-us/library/ff935839\(v=exchg.150\).aspx)

As a result of this issue, I've created a small script to report which recipients (of any type) have non inherited SendAs permissions ACL's.  You can later use the report to re-create the permission in 365.

Download the script here: [http://gallery.technet.microsoft.com/Report-non-inherited-Send-86ab658b](http://gallery.technet.microsoft.com/Report-non-inherited-Send-86ab658b)
