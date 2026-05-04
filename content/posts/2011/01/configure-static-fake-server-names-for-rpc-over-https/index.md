---
title: Configure Static "fake" server names for RPC over HTTPS
date: 2011-01-12
categories:
- exchange-2003
- exchange-2007
- exchange-2010
- forefront-isatmg
showTableOfContents: true
draft: false
---


Hi !

{{< lead >}}
This came up with a request to "fake" exchange server names, which are actually old DE-commissioned servers. users are using RPC over HTTP , and the exchange profile they use had those server names as the actual mailbox server.
{{< /lead >}}

This issue might show up when performing cross forest migration or removing servers, while manipulating name resolving using DNS CNAME records, etc..

With Exchange 2010 and Exchange 2007 Outlook Anywhere settings are applied automatically when you enable the outlook anywhere feature on a CAS server, proxy names in the registry ( HKEY_LOCAL_MACHINESOFTWAREMicrosoftRpcRpcProxy) are automatically entered, that is all back-end  servers that were enabled for RPC over HTTP (2003) and all mailbox servers 2007 / 2010.

So by default RpcProxy will only answer for existing  mailbox servers, we want to add our own "old" , "fake" exchange server names.

Here's how to manipulate the RpcProxy entry in the Exchange server make it stick.

**Use at your own risk!**

Under each CAS you will enable for Outlook Anywhere follow these steps:

1. Configure "PeriodicPollingMinutes" to 0 , this will stop automatic settings overwrite - removing the static entries you will add later.Locate the value  PeriodicPollingMinutes, under HKEY_LOCAL_MACHINESYSTEMCurrentControlSetservicesMSExchangeServiceHostRpcHttpConfigurator
 2. Configure the "fake" names, for example "email2.fake.com" will be the fake mailbox server we will add. Append ";email2.fake.com:6001-6002;email2.fake.com:6004" to the value of "ValidPorts_AutoConfig_Exchange" The String Value is under : HKEY_LOCAL_MACHINESOFTWAREMicrosoftRpcRpcProxyFor example: `EX2010:6001-6002;EX2010:6004;EX2010.test.lab:6001-6002; EX2010.test.lab:6004;ex2k3:6001-6002;ex2k3:6004; ex2k3.test.lab:6001-6002;ex2k3.test.lab:6004; email2.fake.com:6001-6002;email2.fake.com:6004`
 3. Restart the services: MSExchangeServiceHost and MSExchangeProtectedServiceHost
 4. IISReset

Done !

Now configure outlook to use the email2.fake.com server and configure Outlook Anywhere to verify it works.
