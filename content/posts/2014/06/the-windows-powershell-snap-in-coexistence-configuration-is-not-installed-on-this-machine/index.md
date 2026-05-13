---
title: The Windows PowerShell snap-in Coexistence-Configuration is not installed on
  this machine
date: 2014-06-10
categories:
- office-365
showTableOfContents: true
draft: false
---


{{< lead >}}
**Update 2 - February 24th 2016** - The new February AD Connect release has no schedule task anymore. So we now have a new command in the ADSync module - Start-ADSyncSyncCycle.
{{< /lead >}}

To initiate a synchronization locally or remotely (if enabled) , you could run the following command for example:

```text
Invoke-Command -ComputerName **DirSync-Server.domain.com** -ScriptBlock {& Import-Module ADSync;Start-ADSyncSyncCycle}
```

**Update - July 7th 2015** - For those who have installed the latest [AADSync - Azure Active Directory Sync](https://msdn.microsoft.com/en-us/library/azure/dn790204.aspx) or [AD Connect - Azure Active Directory Connect](https://azure.microsoft.com/en-us/documentation/articles/active-directory-aadconnect/)

There has been another change to the module name, it is now ADSync. and the great news is that forcing replication will **no longer be a PowerShell cmdlet.**

To initiate a synchronization locally or remotely (if enabled) , you could run the following command for example:

```text
Invoke-Command -ComputerName **DirSync-Server.domain.com** -ScriptBlock {& "C:\Program Files\Microsoft Azure AD Sync\Bin\DirectorySyncClientCmd.exe"}
```

If you're looking also to force a full password sync to Azure AD , visit this page - [How to Use PowerShell to Trigger a Full Password Sync in Azure AD Sync](http://social.technet.microsoft.com/wiki/contents/articles/28433.how-to-use-powershell-to-trigger-a-full-password-sync-in-azure-ad-sync.aspx)

* * *

Just noticed now that the new build of Windows Azure Directory Synchronization Tool, is missing the DirSyncConfigShell.psc1 file. Moreover, the Coexistence-Configuration PSSnapin is also gone. Trying to add the pssnapin would generate the error - The Windows PowerShell snap-in Coexistence-Configuration is not installed on this machine.

So if you've trying to use the known way to force a synchronization with DirSync, use these PowerShell commands to achieve what you were used to. `Import-Module DirSync Start-OnlineCoexistenceSync`

{{< figure src="images/import-module-dirsync.png" alt="import-module-dirsync" caption="import-module-dirsync" >}}

enjoy !
