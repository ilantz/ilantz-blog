---
title: Export-mailbox fails with error
date: 2008-08-10
categories:
- exchange-2007
showTableOfContents: true
draft: false
---


{{< lead >}}
while testing yet another ex2k7 implantation , i've encountered an error while trying to export mailboxs to pst with the Export-mailbox cmdlet.
{{< /lead >}}

I've verified full mailbox access permissions and 2007 32bit tools on xp sp2 with outlook 2007.

yet, still failed with the following error:

**Export-Mailbox : Error was found for user01 (**[**user01@mydomain.com**](mailto:user01@mydomain.com "mailto:user01@mydomain.com")**)**

**because: Error occurred in the step: Approving object. An unknown error has occurred., error code: -2147221241**

With some filtering of search results i've find a suggestion to run the cmd [fixmapi](http://msdn.microsoft.com/en-us/library/bb927655.aspx "fixmapi info") in cmd.. if your not femiliar with this utility (like i was) , this util exists in your %systemroot%system32 , along with the mapi32.dll files .. besides that 3 notes for you:

1. **FixMAPI** does not replace the current mapi32.dll file if the file is marked as read-only.
2. **FixMAPI** does not replace the current mapi32.dll if Microsoft Exchange Server is installed on the computer.
3. When **FixMAPI** makes a backup copy of the current copy of mapi32.dll on the computer, it assigns the backup copy a name different from "mapi32.dll". It then directs subsequent calls intended for that assembly to the backup copy.

oh yea, closeing all applications and running fixmapi in cmd , just like that fixed the issue.

Ilan.
