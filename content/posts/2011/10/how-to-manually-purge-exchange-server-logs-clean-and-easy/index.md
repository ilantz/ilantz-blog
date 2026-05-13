---
title: How to manually purge Exchange server logs - clean and easy
date: 2011-10-26
categories:
- exchange-2007
- exchange-2010
- exchange-2013
- server-2008-r2
showTableOfContents: true
draft: false
---


{{< lead >}}
Update 9/Jun/2015 - Thanks to Josh Davis for the feedback, I've added a note about making sure to include both drives (if EDB and LOG files are separated).
{{< /lead >}}

Update 21/Oct/2013 - This article suggests that you **cannot** sustain downtime or interruption for your users while battling with deleting log files or restoring your working backup solution. If you can sustain a downtime (should be around minutes or so) the easiest method will be to enable Circular Logging on your database / storage group - see more here - [http://technet.microsoft.com/en-us/library/bb331958%28v=exchg.141%29.aspx#UTL](http://technet.microsoft.com/en-us/library/bb331958%28v=exchg.141%29.aspx#UTL "http://technet.microsoft.com/en-us/library/bb331958%28v=exchg.141%29.aspx#UTL")

Update 01/May/2013 - The exchange team has written a script which helps troubleshoot and identity issues with Backups etc.. The script use the DiskShadow utility as well ! check it out @ [http://blogs.technet.com/b/exchange/archive/2013/04/29/troubleshoot-your-exchange-2010-database-backup-functionality-with-vsstester-script.aspx](http://blogs.technet.com/b/exchange/archive/2013/04/29/troubleshoot-your-exchange-2010-database-backup-functionality-with-vsstester-script.aspx "Troubleshoot your Exchange 2010 database backup functionality with VSSTester script")

* * *

Hi Again !

I often get calls and questions regarding backups and Exchange Server, since ever this issue is not always working as required or as you would expect, but that's off-topic :)

One of the most common stories is that without a working Exchange Server backup when  you perform massive mailbox moves, transaction logs will get piled and fill up the volume or disk that they reside in. and then panic starts, "hey my databases were dismounted..." then of course the administrator realizes that the space on the log drive or volume has indeed ran out and now he needs to figure out what to delete.. and here's where this post comes in...

So how can you delete or purge Exchange server logs without any risk ? well, in simple - **you cannot**, because the whole idea of restoring an Exchange or for this matter any transactional database requires you to have a first - "full" backup of the database itself and **all** transaction logs that were generated since the the date of the database creation date, or the last "successful" "full backup".

Now here's a nice method to "fake" a "full backup" or an on-demand transaction logs purge when you see you will be soon out of space, using the Exchange VSS writers and the diskshadow utility (available with Server 2008 or 2008 R2) . This procedure also "proves" that a VSS backup for your Exchange Server will work fine.

**note: This method was tested on an Exchange server with Locally Attached Disks, not storage attached LUNs.**

**Use this method on on your risk. You should preform a "Full Backup" right after this process is done.**

This example will show you how to purge the logs for a database that is located on Drive D, the log files of the databases are also located in Drive D. we will "fake backup" drive D and this will trigger the logs to be purged.

**Note:** If you have separated your log files and database file in different drives, or you want to include additional databases in the "backup" you must include the additional drives in the process, so in the example below, you will "Add volume e:" after "Add volume drive d:" and so on...

1. Open Command prompt
2. Launch Diskshadow
    1. Add volume d:
    2. (optional, add one line for each additional drive to include) Add volume X:
    3. Begin Backup
    4. Create
    5. End Backup
3. At this step you should notice the following events in the application log indicating that the backup was indeed successful and logs will now be deleted.

Here's some screenshots from the process:

{{< figure src="images/diskshadow.png" alt="Diskshadow commands for the example" caption="Diskshadow commands for the example" >}}

The Diskshadow example screenshot.

{{< figure src="images/ese-event-id-2005.png" alt="ESE Event ID 2005" caption="ESE Event ID 2005" >}}

ESE - Event ID 2005 - Starting a Full Shadow Copy Backup

{{< figure src="images/msexchangeis-event-id-9811.png" alt="MSExchangeIS Event ID 9811" caption="MSExchangeIS Event ID 9811" >}}

MSexchangeIS - Exchange VSS Writer preparation.

{{< figure src="images/ese-event-id-224.png" alt="ESE Event ID 224 - Logs being Purged" caption="ESE Event ID 224 - Logs being Purged" >}}

ESE Event ID 224 - Logs are now purged :)

{{< figure src="images/msexchangeis-event-id-9780.png" alt="MSExchangeIS Event ID 9780 - Backup complete" caption="MSExchangeIS Event ID 9780 - Backup complete" >}}

MSExchangeIS Event ID 9780 - Backup is now complete.

**side note:** although this example was tested against Exchange 2010, it should work just as fine with Exchange 2013 & 2007.

Hope this helps you !

ilantz
