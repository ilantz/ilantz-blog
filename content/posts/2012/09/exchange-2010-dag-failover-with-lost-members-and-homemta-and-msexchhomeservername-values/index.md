---
title: Exchange 2010 DAG failover with lost members and homeMTA and msExchHomeServerName
  values
date: 2012-09-28
categories:
- exchange-2010
- powershell
showTableOfContents: true
draft: false
---


Hi Again,

{{< lead >}}
I've recently had an unusual situation I wanted to share. A client of mine had a geographically stretched Exchange 2010 DAG cluster that crashed really bad, the original "active" servers had been lost beyond repair... luckily the databases were replicated to another location, so the data was saved. In addition the client was in between a migration from Exchange 2007 to Exchange 2010 (the 2007 servers were not effected from the disaster..).
{{< /lead >}}

Just for the sake of explaining a little more, the original "active" servers should have been restored with the setup.com /m:recoverserver , but due to the nature of the failure those servers and their names are gone and were no longer required. Those failed Exchange 2010 DAG member servers were completely deleted from Active Directory using ADSIEdit.

To recover the Exchange 2010 environment I've done a few steps, following which the Exchange DAG was online and service was restored.

1. Restored the DAG to the DR site (evict nodes from the cluster, modify the quorum, leverage AlternativeWitnessServer): Restore-DatabaseAvailabilityGroup
2. Created a new ClientAccessArray in the new AD site
3. Modified all databases with Set-MailboxDatabase so the new CAS array is now the RpcClientAccessServer
4. Made sure all databases are active within the our new site and on the correct servers with Move-ActiveMailboxDatabase
5. Removed the lost database copies on the lost DAG members with Remove-MailboxDatabseCopy
6. Forcibly removed the lost DAG members from the DAG: Remove-DatabaseAvailabilityGroupServer -ConfigurationOnly

Following the actions above, service was restored, and all was good, until we encountered an issue with users located on the Exchange 2007, they reported that they could not retrieve any free/busy information from other users (which were all located on Exchange 2010 databases).

A quick troubleshooting showed that configuration was fine (URL's were set correctly, networking access was fine, permissions were okay etc..), so I've enabled the troubleshooting log on an outlook client while logged on as an 2007 user. Looking at the xxxx-xxx-AS.log (availability service logs) generated from outlook, I was able to extract the root cause:

```powershell
<FreeBusyResponse><ResponseMessage ResponseClass="Error"><MessageText>Unable to find a Client Access server that can serve a request for an intraforest mailbox <Jhon Doe>;SMTP:Jhon.Doe@Contoso.com., inner exception: The server MBX2.contoso.com was not found in the topology.</MessageText><ResponseCode>ErrorServiceDiscoveryFailed</ResponseCode><DescriptiveLinkKey>0</DescriptiveLinkKey><MessageXml><ExceptionType xmlns="http://schemas.microsoft.com/exchange/services/2006/errors">Microsoft.Exchange.InfoWorker.Common.Availability.ServiceDiscoveryFailedException</ExceptionType><ExceptionCode xmlns="http://schemas.microsoft.com/exchange/services/2006/errors">5021</ExceptionCode></MessageXml></ResponseMessage><FreeBusyView><FreeBusyViewType xmlns="http://schemas.microsoft.com/exchange/services/2006/types">None</FreeBusyViewType></FreeBusyView></FreeBusyResponse>
```

The availability service on the Exchange 2007 server was trying to locate the users' using its msExchHomeServerName value which pointed to a **deleted** server, one of the original "active" DAG members that was lost !  Looking at the attributes values of John Doe (per my example above) reviles that the values of homeMTA and msExchHomeServerName were pointing to non existing values, the homeMTA clearly shows a deleted server value, and the msExchHomeServerName points to a server that no longer exists. here's an example of what I saw:

{{< figure src="images/homeMTA-0ADEL-300x206.png" title="homeMTA points to a deleted server value - CN=Microsoft MTA\\0DEL:" caption="homeMTA points to a deleted server value - CN=Microsoft MTA\\0DEL:" >}}

{{< figure src="images/msExchHomeServerName-deleted-server-300x241.png" title="msExchHomeServerName points to a deleted server" caption="msExchHomeServerName points to a deleted server" >}}

I've wrote a small PowerShell script that helps update the values for all affected users using a LDAP filter and the Get-User cmdlet from the Active Directory Module and the Set-Mailbox -ConfigurationOnly cmdlet.

**Use this script on your own risk, make sure to always double check your self before running on a production environment.**

```powershell
$filter = "(&(objectCategory=user)(objectClass=user)(msExchHomeServerName=/o=Contoso/ou=Exchange\20Administrative\20Group\20\28FYDIBOHF23SPDLT\29/cn=Configuration/cn=Servers/cn=MBX2*))" $strAttributes = "msExchHomeServerName, homeMTA, homeMDB" $users = get-ADUser -LDAPFilter "$filter" -ResultSetSize $null -properties $strAttributes foreach ($user in $users) { $mbx = $null; $mbx = get-mailbox -Identity $user.DistinguishedName; write-host "working on user" $user.name write-host "working on mailbox" $mbx.name set-mailbox $mbx -Database $mbx.database -confirm:$false -force -verbose }
```

Make sure you modify the LDAP filter $filter and the MBX2 per your configuration.

The conclusion from this case was very interesting to me, the scenario we had here was a "typical" cross site activation of an Exchange 2010 DAG, but due to the nature of the failure, we were forced to re-home the mailboxes as if we were using Database Portability! (excluding the actual database change of course). See the links below for more about Database Potability.

Hope you find this information useful, Ilantz

[Datacenter Switchovers](http://technet.microsoft.com/en-us/library/dd351049.aspx "Datacenter Switchovers")

[Move a Mailbox Database Using Database Portability](http://technet.microsoft.com/en-us/library/dd876926.aspx "Move a Mailbox Database Using Database Portability")
