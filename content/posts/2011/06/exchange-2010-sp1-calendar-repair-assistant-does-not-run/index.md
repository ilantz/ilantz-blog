---
title: Exchange 2010 SP1 Calendar Repair Assistant - Does not run?
date: 2011-06-23
categories:
- exchange-2010
showTableOfContents: true
draft: false
---


{{< lead >}}
So you want to use the Calendar Repair Assistant (CRA) with Exchange 2010 SP1, you've ran a few powershell commands, but nothing happens ?
{{< /lead >}}

You've missed a change Exchange 2010 SP1 introduced two new settings for Set-MailboxServer related to the Calendar Repair Assistant:

**\-CalendarRepairWorkCycle** and **\-CalendarRepairWorkCycleCheckpoint** These parameters work together. The CalendarRepairWorkCycle parameter specifies the time span in which all mailboxes on the specified server will be scanned by the CRA. For example, if you specify seven days for this parameter, the CRA will process all mailboxes on this server every seven days. Calendars that have inconsistencies will be flagged and repaired according to the interval specified by the CalendarRepairWorkCycleCheckpoint parameter. For example, if you specify one day for this parameter, the CRA will query every day for new mailboxes that require processing.

To have you exchange server schedule a daily repair schedule at 23:00 PM, while making sure this task runs each day (Cycle), and searches for new mailboxes to process every 12 hours (CycleCheckpoint) run the following:

Set-MailboxServer -Identity MBX2 -CalendarRepairSchedule 1.22:00-1.23:00, 2.22:00-2.23:00, 3.22:00-3.23:00, 4.22:00-4.23:00, 5.22:00-5.23:00, 6.22:00-6.23:00, 7.22:00-7.23:00  -CalendarRepairWorkCycle 1.00:00:00 -CalendarRepairWorkCycleCheckpoint 12:00:00

Now it will actually run ;)

Enjoy !
