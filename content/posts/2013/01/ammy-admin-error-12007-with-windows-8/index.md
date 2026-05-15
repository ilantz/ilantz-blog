---
title: Ammy Admin Error 12007 with Windows 8
date: 2013-01-29
categories:
- misc
- windows-8
showTableOfContents: true
draft: false
aliases:
- /2013/01/29/549/
---


Hi again,

{{< lead >}}
I've been using [Ammyy Admin](http://www.ammyy.com "Ammyy Admin") to support family members and friends for a while now, but since I've upgraded to Windows 8, the program seems to fail it's initial connection to it's public servers upon start up.
{{< /lead >}}

It keeps popping out an error window:

> Error {12007} occured while connecting to server "http://rl.ammyy.com" Would you like to change proxy settings?

{{< figure src="images/Ammy-Admin-Error-12007-Windows-8.png" alt="Ammy Admin Error 12007 Windows 8" caption="Ammy Admin Error 12007 Windows 8" >}}

To solve this, just open the Ammyy Admin setting menu and un-check the "Run under SYSTEM account on Windows Vista/7/2003/2008" check-box.

{{< figure src="images/Uncheck-Run-under-SYSTEM-account.png" alt="Uncheck Run under SYSTEM account" caption="Uncheck Run under SYSTEM account" >}}

hope you find this useful.

ilantz
