---
title: Solving Sync Issues Error 80004005-501-4B9-560 in Exchange 2010 RTM and SP1
date: 2011-09-20
categories:
- exchange-2003
- exchange-2010
- outlook-mapi
showTableOfContents: true
draft: false
---


**Update**

{{< lead >}}
The current "Best Practice" is to upgrade your Exchange Server to Service Pack 2 and apply [Update Rollup 3 for Exchange Server 2010 Service Pack 2 (KB2685289)](http://www.microsoft.com/en-us/download/details.aspx?id=29899), as this issue has been permanently solved.
{{< /lead >}}

See [Synchronization of an organizational forms library fails when you use Outlook in Cache mode in an Exchange Server 2010](http://support.microsoft.com/kb/2572029) for additional information.

* * *

Hello Everyone,

Since the first migrations of Exchange 2003 to Exchange 2010 we've seen a really annoying error within Outlook 2003, 2007 and Outlook 2010 when trying to De-commission  legacy servers, specifically when moving all public folders replicas including the EFORMS REGISTRY system folder and it's children folders. once the organizational forms ( respectively you might see a different folder name within your organizatino ) is replicated **only** to the Exchange 2010 - a log / error message will be created in the _**Sync Issues**_ upon an Outlook Send/Receive operation:

> 11:56:54 Synchronizing Forms 11:56:54 Downloading from server 'public folder server' 11:56:54 Error synchronizing folder 11:56:54 [80004005-501-4B9-560] 11:56:54 The client operation failed. 11:56:54 Microsoft Exchange Information Store

****Notice: Use this method at your own risk ! This method is for organizations that do not use Forms !****

Many posts and different resolutions were recommended, my original "fix" for this issue was to not replicate the organizational forms folder to the new Exchange 2010 public folder when starting to De-commission the Exchange 2003 server, practically "leaving it behind".

I recently handled a situation where the Exchange 2003 server was already removed, and the forms folder was already replicated to Exchange 2010, and the error was already in place. I could not use Exchange 2003 System Manager to remove the replica, Exchange Management Shell or EXFolders. You cannot really leave an empty replica list within the tools.

[MFCMapi](http://mfcmapi.codeplex.com) to the rescue :)

1. Open MFCMapi, click the session menu, select the logon and display store table option.
2. Double click public folders, expend the public root tree, expend NON_IPM_SUBTREE, expand EFORMS REGISTRY.
3. Locate and select the organizational forms folder.
4. Scroll the property list to find the PR_REPLICA_LIST entry - double click it and clear the value inside - clear means delete the values inside the property. Setting PR_REPLICA_LIST to NULL actually leaves us with an empty replica list - which "solves" this issue.
5. Note that when you click to apply the change of the PR_REPLICA_LIST the property list will immediately shrink, this is normal :)
6. Exit Outlook, wait and see that indeed the Sync Issues folder does not include a new log with the 80004005-501-4B9-560 error.

**Use this method at your own risk ! and again - this method is for organizations that do not use Forms !**

Some references for you usage:

[Troubleshooting: Error synchronizing folder Synchronizing Forms 80004005-501-4B9-560](http://blogs.technet.com/b/agobbi/archive/2010/08/04/troubleshooting-error-synchronizing-folder-synchronizing-forms-80004005-501-4b9-560.aspx)

[Outlook synchronization error [80004005-501-4B9-560] with a Microsoft Exchange Server 2010 mailbox](http://blogs.technet.com/b/eileenor/archive/2011/05/04/outlook-synchronization-error-80004005-501-4b9-560-with-a-microsoft-exchange-server-2010-mailbox.aspx)

["80004005-501-4B9-560" synchronization error logs are generated in the Sync Issues folder in Outlook in a Business Productivity Online Suite Dedicated environment](http://support.microsoft.com/kb/2614647)
