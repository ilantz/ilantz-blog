---
title: Local operating system boot fails when external storage is attached
date: 2010-02-14
categories:
- misc
- server-2008-r2
showTableOfContents: true
draft: false
---


{{< lead >}}
Well the topic explains this quite enough..
{{< /lead >}}

but I'd like to share little more.

A typical Exchange 2010 deployment based on Server 2008 R2, we used IBM Blade Center HS22 this time with a QLogic HBA to connect to an EMC Symmetrix storage with FC ... okay, enough hardware talk. :)

The "symptom" was that after connecting the LUN's to the and creating the partitions, well the next reboot to the server was .. unsuccessful... shocked as we were, after some quite tryouts: Drivers, Firmware upgrades, disable that and disable that ... and when all failed ...some searching, we came up with a few links... all seem to be quite "close but no cigar".

[Local operating system boot fails when external storage is attached - IBM System x3550 M2, x3650 M2 and BladeCenter HS22](http://sites.google.com/site/virtualkb/accueil/hardware/localoperatingsystembootfailswhenexternalstorageisattached-ibmsystemx3550m2x3650m2andbladecenterhs22)

[UEFI-aware OS doesn't boot after load defaults or deployment - IBM BladeCenter and System x](http://www-947.ibm.com/systems/support/supportsite.wss/docdisplay?lndocid=MIGR-5079636&brandind=5000008)

[The system becomes unbootable after you add raw disks to a Windows Server 2008 R2-based computer that has EFI enabled](http://support.microsoft.com/kb/975535) - [http://support.microsoft.com/kb/975535](http://support.microsoft.com/kb/975535)

[First real world experiences with IBM’s x3650 M2](http://projectdream.org/wordpress/2009/07/04/first-real-world-experiences-with-ibms-x3650-m2/)

The last link includes a comment by "Rudi" , which gave us a good idea. lets try it again...

well, we did ! and guess what ?? IT WORKED.

Quick wrap up:

1) HS22 BladeCenter - Server boots from local raid-1 SAS disks with a GUID Partition Table (GPT) - Server 2008 R2 EFI boot loader.

2) 21 LUN's attached with FC from a EMC Symmetrix storage (MBR).

**Solution:**

3) Make sure you initialize **all** drives with GPT - Guid Partition Table. that's it !

Smile :)

\*\* quick notice. to sum all the other links, if you use a non uefi aware OS (basically only server 2008+ is uefi aware) you need to make sure to use the "Legacy Only" method.

Hope this helps, we spent quite some time around this issue.
