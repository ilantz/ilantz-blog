---
title: Stopping PowerShell from truncating values in tables
date: 2017-09-12
categories:
- powershell
showTableOfContents: true
draft: false
---


A quick PowerShell Tip.

{{< lead >}}
I've just stumbled upon this within the scripting guy blog, and I felt I must (re)share it.
{{< /lead >}}

Don't we all hate it when values are displayed and being truncated with "..." ?

```powershell
PS C:\> Get-Service -Name winmgmt | ft name, DependentServices -AutoSize Name    DependentServices ----    ----------------- winmgmt {wscsvc, vmms, SUService, SharedAccess**...**}
```

It turns out that the system variable **$FormatEnumerationLimit** is controlling this behavior and there's a way to properly eliminate these. the article suggests setting to "4" but "-1" will be also a good option.

[https://blogs.technet.microsoft.com/heyscriptingguy/2013/02/19/powertip-change-powershell-to-display-more-info-by-default/](https://blogs.technet.microsoft.com/heyscriptingguy/2013/02/19/powertip-change-powershell-to-display-more-info-by-default/)

Enjoy ! ( I know I did )
