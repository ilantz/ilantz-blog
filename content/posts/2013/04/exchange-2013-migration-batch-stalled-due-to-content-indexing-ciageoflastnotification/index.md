---
title: Exchange 2013 Migration Batch Stalled Due To Content Indexing CiAgeOfLastNotification
date: 2013-04-28
categories:
- exchange-2013
showTableOfContents: true
draft: false
---


Hi,

{{< lead >}}
I've just encountered this issue during a LAB for migrating Exchange 2010 to Exchange 2013, migration batches were getting stuck in Syncing, in addition I noticed two annoying warning messages in the application log of the server with Event ID 1009 and Event ID 1013 with source MSExchangeFastSearch
{{< /lead >}}

I've looked in the migration report using: `Get-MigrationUserStatistics -IncludeReport -Identity ilantz@lab.com | fl ...... 4/28/2013 7:44:46 AM [EX2013] The job is currently stalled due to 'Content Indexing' lagging behind on resource 'CiAgeOfLastNotification(Mailbox Database .....`

So, indeed the Content Indexing which was failing and keeping the migration back... nothing special here, Exchange 2010 had this issue as well ... Quick search showed a **very** odd solution to this...

Quoting [http://support.microsoft.com/kb/2807668](http://support.microsoft.com/kb/2807668 "Content Index status of all or most of the mailbox databases in the environment shows \"Failed\"") - Content Index status of all or most of the mailbox databases in the environment shows "Failed"

> This issue may occur if the search platform tries to check its membership in a security group that is named "ContentSubmitters." This group is not created by the search platform or by Exchange Server 2013 and is therefore not usually present. Although the check usually fails silently, without any consequences, an exception sometimes occurs. This causes the search component to fail.

Wow ... well :) .. hope this will be fixed with CU2.. go with Method 1 in the KB, worked like a charm here.

ilantz
