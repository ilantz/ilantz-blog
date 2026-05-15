---
title: MSExchangeRepl 2147 / MSExchangeRepl 2104 / MSExchangeRepl 2127 occurring on
  Windows 2008 or Windows 2008 R2 with Exchange 2007 Cluster Continuous Replication
  (CCR)
date: 2010-07-12
categories:
- exchange-2007
- exchange-2010
- server-2008-r2
showTableOfContents: true
draft: false
slug: msexchangerepl-2147-msexchangerepl-2104-msexchangerepl-2127-occurring-on-windows-2008-or-windows-2008-r2-with-exchange-2007-cluster-continuous-replication-ccr
---


{{< lead >}}
As i ran into this issue this week, I've stumbled upon this thread: http://social.technet.microsoft.com/Forums/en-US/exchangesoftwareupdate/thread/eca3bbf7-ee9f-41bd-89e8-47a81780292b
{{< /lead >}}

Seems the cause for these errors, are because SMBv2 introduces status caching into the LanManWorkstation service...read more at [SMB2 Client Redirector Cache](http://technet.microsoft.com/en-us/library/ff686200(WS.10).aspx "SMB2 Client Redirector Cache")

**So to fix it I've added these registry keys under :**

```registry
HKLM\System\CurrentControlSet\Services\Lanmanworkstation\Parameters 
FileInfoCacheLifetime [DWORD] = 0 
FileNotFoundCacheLifetime [DWORD] = 0 
DirectoryCacheLifetime [DWORD] = 0
```

My errors on the server were:

```text
Event ID : 2147
Raw Event ID : 2147
Source : MSExchangeRepl
Type : Error
Machine : SERVER
Message : There was a problem with 'ActiveNode', which is an alternate name for 'ActiveNode'. The list of aliases is now 'ActiveNode', and the alias 'was' removed from the list. The specific problem is 'CreateFile(\\ActiveNodeStorageGroupGuid$LogFile.log) = 2'.
```

```text
ID:       2127
Level:    Information
Provider: MSExchangeRepl
Machine:  SERVER
Message:  The system has detected a change in the available replication networks.  The system is now using network 'ActiveNode' instead of network 'ActiveNode' for log copying from node ActiveNode.
```


Thanks a lot for JR on sharing this, check out Tim McMichael with more info on this:

http://blogs.technet.com/b/timmcmic/archive/2010/07/11/msexchangerepl-2147-msexchangerepl-2104-msexchangerepl-2127-occurring-on-windows-2008-or-windows-2008-r2-with-exchange-2007-cluster-continuous-replication-ccr.aspx