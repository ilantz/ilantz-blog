---
title: Adding Read-only permissions to Exchange 2007 Auditing Logs
date: 2010-10-26
categories:
- exchange-2007
- server-2008-r2
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
I was asked today to add a permission to the Exchange Auditing log which is included with Exchange 2007 SP2 installations to simplify auditing, after activating [Mailbox Access Auditing](http://technet.microsoft.com/en-us/library/ee221156%28EXCHG.80%29.aspx) , I was requested to allow **read only** permissions to the IT Security group.
{{< /lead >}}

What seemed to be quite straight forward, was soon to be changed with SDDL ACL format....

Here's the quick how-to:

\- Note, this was done on a Windows 2008 server

1. Identify the SID of the user/group you wish to allow access. Using powershell you can easily find it e.g: Get-User | Select SID Get-Group | Select SID
2. Then following this KB - Which was the most simple and self-explained, add the appropriate permissions. [http://support.microsoft.com/kb/2028427](http://support.microsoft.com/kb/2028427)In-Short - each event log is located in the registry at: HKEY_LOCAL_MACHINESYSTEMCurrentControlSetServicesEventLog the Exchange Auditing log is also located there, and in that key you will find an existing CustomSD string value with the ACL's in the SDDL format ( more info in the links I added below ) I was required to add read-only permissions to the IT Audit group, which is a "regular" group, without special domain / enterprise rights, so in my case i used the following: (A;;0x1;;; [Your Group Name/user account SID]) so appended that to the existing CustomSD value.
3. **Restart** the server.
4. Now the user/group can access the Exchange Auditing log from any computer :)

Links:

[http://technet.microsoft.com/en-us/library/ee331009%28EXCHG.80%29.aspx](http://technet.microsoft.com/en-us/library/ee331009%28EXCHG.80%29.aspx) - White Paper: Configuration and Mailbox Access Auditing for Exchange 2007 Organizations [http://support.microsoft.com/kb/2028427](http://support.microsoft.com/kb/2028427) - Writing to the Windows Event Log from an ASP.NET or ASP application fails. [http://support.microsoft.com/kb/323076](http://support.microsoft.com/kb/323076) - How to set event log security locally or by using Group Policy in Windows Server 2003 - Also useful if you'd like to set this via GPO [http://blogs.technet.com/b/askds/archive/2008/05/07/the-security-descriptor-definition-language-of-love-part-1.aspx](http://blogs.technet.com/b/askds/archive/2008/05/07/the-security-descriptor-definition-language-of-love-part-1.aspx) [http://blogs.technet.com/b/askds/archive/2008/05/07/the-security-descriptor-definition-language-of-love-part-2.aspx](http://blogs.technet.com/b/askds/archive/2008/05/07/the-security-descriptor-definition-language-of-love-part-2.aspx) [http://blogs.technet.com/b/askds/archive/2008/08/12/event-logging-policy-settings-in-windows-server-2008-and-vista.aspx](http://blogs.technet.com/b/askds/archive/2008/08/12/event-logging-policy-settings-in-windows-server-2008-and-vista.aspx)

Happy Auditing !
