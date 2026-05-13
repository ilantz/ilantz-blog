---
title: Listing Office 365 Endpoints using PowerShell
date: 2019-06-20
categories:
- office-365
showTableOfContents: true
draft: false
---


{{< lead >}}
An essential part of a successful deployment of Office 365 is to make sure connectivity is optimal and that there are no restrictions being applied for the public endpoints of the service among other factors. this is all detailed on the [Office 365 Network Connectivity Principles documentation](http://aka.ms/pnc).
{{< /lead >}}

A good overview of the concept was delivered at Ignite 2019 - [BRK3000 - Strategies for building effective, optimal and future proof connectivity to Office 365 that will delight your users](http://aka.ms/brk3000)

One of the tasks is to read the list of the endpoints from the [Office 365 URLs and IP address ranges documentation page](http://aka.ms/o365endpoints), due the dynamic nature of the endpoint list a [Web Service](https://docs.microsoft.com/en-us/office365/enterprise/office-365-ip-web-service) was made available to ease automation, reporting and 3rd party solutions.

Most of the times, you'll just want to fetch the list of the URLs, and hand them over to your friendly networking team that would then do their magic. lucky enough PowerShell can be used to get that list easily, here's an  example:

```text
$endpoints = Invoke-WebRequest "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7" | ConvertFrom-Json ; $endpoints | ?{$_.serviceArea -eq "Common" -AND $_.Required -eq "True"} | select urls -ExpandProperty Urls
```

This would request the full list of endpoints from the web service, convert it PowerShell objects from Json and output only the Common Services which are also tagged as Required and list only the Urls.

Another example would be to pull the Optimize category:

```text
$endpoints = Invoke-WebRequest "https://endpoints.office.com/endpoints/worldwide?clientrequestid=b10c5ed1-bad1-445f-b386-b919946339a7" | ConvertFrom-Json ; $endpoints | ?{$_.category -eq "Optimize" }
```

Enjoy!
