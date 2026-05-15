---
title: How to reset OneDrive for Business when it's crashing constantly
date: 2014-12-27
categories:
- office-365
showTableOfContents: true
draft: false
---


{{< lead >}}
Recently I've messed with my Windows 8.1 profile account, and shortly after my OneDrive for business client started crashing in a loop... it just went crazy, filling my notification area with icons failing to stop. I had no way to reach any menu or remove the folders I'm syncing.
{{< /lead >}}

I've tried the easy (lazy) way of repairing / uninstalling / removing Office 365 ProPlus (in my case) which turned out useless.. did some manual clean up of registry entries, removed caching files and obviously looked-up forum threads and KB's which also turned out as you've guessed it - useless...

Almost desperate, I've turned to the all mighty [Process Monitor](http://technet.microsoft.com/en-us/sysinternals/bb896645.aspx) and started debugging the errors.

Thru closely examining the endless output of entries, I've spotted an **undocumented** registry entry that was being checked by the Groove.exe (which is your OneDrive sync process) upon start-up.

So there I was, crossing fingers,  editing the registry hoping... and BINGO! I have performed a reset to the OneDrive for Business client, and it behaved like the first time I've opened it up.

Here it is, Add/Modify these two DWORD values: 

```registry
[HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Groove]
"FirstSyncComplete"=dword:00000000

[HKEY_CURRENT_USER\Software\Microsoft\Office\15.0\Groove\Development]
"IsResyncEnabled"=dword:00000001
```

Hope this post will help more good folks out there.

ilantz