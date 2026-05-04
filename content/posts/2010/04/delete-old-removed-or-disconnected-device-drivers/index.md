---
title: Delete old removed or disconnected device drivers
date: 2010-04-11
categories:
- misc
- server-2008-r2
- vista-7
showTableOfContents: true
draft: false
---


{{< lead >}}
So you've plugged a harddrive / disk-on-key or any other hot plugged device, and oops BSOD :(
{{< /lead >}}

or, you want to install a new driver for a device that you have removed, but windows magic plug-and-play installed the driver automatically.... but you don't want that do you ?

Anyway there's an old method that works great.

You open device management, and click , view "show hidden devices"... but you **fail** to see your disconnected devices...

FIX - Show **all** disconnected devices, open System Properties, click Environment Variables and click to add a New System Variable.

[![Configure a New System Variable](images/configure.png "Configure a New System Variable")](images/configure.png)

After this you will be able to launch Device Manager again and when you'll click to Show Hidden Devices, you **will** see all those removed or disconnected device drivers !

[![Device Manger Before-After](images/before-after.png "Device Manger Before-After")](images/before-after.png)

That's it ! Enjoy
