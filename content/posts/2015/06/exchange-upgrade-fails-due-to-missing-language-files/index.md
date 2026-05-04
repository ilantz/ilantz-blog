---
title: Exchange upgrade fails due to missing language files
date: 2015-06-14
categories:
- exchange-2007
- exchange-2010
- exchange-2013
- powershell
- server-2008-r2
- server-2012
showTableOfContents: true
draft: false
---


{{< lead >}}
Just to help anyone out there that might be facing this issue. I've helped troubleshoot an Exchange 2010 RTM upgrade to Exchange 2010 SP3 which kept failing due to missing language files...
{{< /lead >}}

Event ID 1603 was also thrown as per to the [KB 2784788 - "1635" or "1603" error code when you install update rollups or service packs for Exchange Server 2007 or Exchange Server 2010](https://support.microsoft.com/en-us/kb/2784788)

The MSILOG indeed showed that the setup was looking for the RTM language files in the original location where the setup files were, but they are long gone... with the RTM DVD no where to be-found (RTM trial files + the oldest Language Pack bundle are in a non compatible version) this situation was doomed to failure.

So, I've turned to manually remove any references to the Client / Server language packs on the server, this included removing a whole bunch of registry keys:

```text
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\ExchangeServer\v14\Language Packs\ <-- the whole KEY HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Installer\Products\  <-- Whatever "Microsoft Exchange ** Language Pack" I found HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\  <-- Whatever "Microsoft Exchange ** Language Pack" I found HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Installer\UserData\S-1-5-18\Products  <-- Whatever "Microsoft Exchange ** Language Pack" I found
```

Following this brutal way, I've stumbled upon a way to [Applying Small Updates by Reinstalling the Product](https://msdn.microsoft.com/en-us/library/aa367575\(v=vs.85\).aspx) this actually achieves what the installer wants:

```text
msiexec /i Server<or>ClientLanguagePack.msi REINSTALLMODE=vomus
```

And it works ! Now, I guess that with a script this would have been much quicker then the registry method, but at least now I'm (and you are) aware of this workaround , and here's the script for your usage:

\*\* edit the $setuplocation variable for your directory of the servicepack.

```powershell
$setupLocation = "c:\sp3" $allDirs = dir $setupLocation -Directory foreach ($dir in $allDirs) { if (Test-Path ($dir.FullName + "\clientlanguagepack.msi")) {Write-Host "Installing" $dir.name ; Start-Process -FilePath msiexec -ArgumentList /i, ($dir.FullName + "\clientlanguagepack.msi"), "REINSTALLMODE=vomus" -Wait } if (Test-Path ($dir.FullName + "\serverlanguagepack.msi")) {Write-Host "Installing" $dir.name ; Start-Process -FilePath msiexec -ArgumentList /i, ($dir.FullName + "\serverlanguagepack.msi"), "REINSTALLMODE=vomus" -Wait } }
```

* * *

Additional references:

[Upgrading Service pack - keep asking for language pack](https://social.technet.microsoft.com/Forums/exchange/en-US/ac03c9ff-0d49-4fd4-801e-67616cf6727c/upgrading-service-pack-keep-asking-for-language-pack?forum=exchange2010)

http://stackoverflow.com/a/7916340 - credit for the `REINSTALLMODE=vomus` trick

[How to restore the missing Windows Installer cache files and resolve problems that occur during a SQL Server update - kb 969052](https://support.microsoft.com/en-us/kb/969052)
