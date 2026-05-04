---
title: Adjust allowed attachment size for EWS
date: 2012-05-06
categories:
- exchange-2007
- exchange-2010
showTableOfContents: true
draft: false
---


Hey again,

{{< lead >}}
If you you have any MAC users working against your Exchange 2007 or Exchange 2010 servers, you've probably already solved this issue, so this is just for future reference and general knowledge.
{{< /lead >}}

Following the Microsoft reference on the subject: [Set Message Size Limits for Exchange Web Services](http://technet.microsoft.com/en-us/library/hh529949.aspx "Set Message Size Limits for Exchange Web Services") the below example is for Exchange **2007**

1. Configure the application to receive requests 50 MB:
    1. Open CMD
    2. %windir%system32inetsrvappcmd set config "Default Web SiteEWS" -section:requestFiltering -requestLimits.maxAllowedContentLength:69905067
2. Edit web.config to allow 50 MB requests:
    1. Backup %ProgramFiles%MicrosoftExchange ServerV14ClientAccessexchwebewsweb.config
    2. Edit the web.config file , search for maxRequestLength
    3. Change the value from its default 13280 to 51200
3. IISReset to make sure configurations take place

**Notes:**

maxAllowedContentLenght value is entered as Bytes, calculate 50MB Base64 encoded size: =((1024\*50)\*1024)\*4/3 maxRequestLenght value is entered as Kilo Bytes, calculate 50MB =1024\*50

Hope this post  helped you
