---
title: EMS license assignment to all users made easy
date: 2016-01-20
categories:
- azure-ad
- ems
- office-365
- powershell
showTableOfContents: true
draft: false
---


{{< lead >}}
So you've purchased Microsoft's Enterprise Mobility Suite (EMS) licenses, now you need to assign them to users within your organization. A typical situation will be that you already have Office 365 licensed users, and it make sense that all of them will get EMS licenses too.
{{< /lead >}}

To achieve this, I would suggest using an Azure AD group with Dynamic Group membership. in this example, the group will include accounts that match ALL these conditions:

- Enabled users accounts
- Users with an email address
- Users with a-non empty Usage Location
- Synchronized user accounts

Within the Azure AD management portal ([http://manage.windowsazure.com](http://manage.windowsazure.com)) navigate to your Active Directory tenant, and perform the following:

1. Create a group in Azure AD
2. Enable it for Dynamic Membership
3. Enter the advanced rule: (user.accountEnabled -eq "true") AND (user.mail -ne $null) AND (user.usageLocation -ne $null) AND (user.dirSyncEnabled -eq true)
4. Assign EMS licenses to the Group

You can read more about Dynamic Group Membership here:

[http://blogs.technet.com/b/ad/archive/2015/03/09/attribute-based-dynamic-group-membership-for-azure-ad-premium-is-now-in-preview.aspx](http://blogs.technet.com/b/ad/archive/2015/03/09/attribute-based-dynamic-group-membership-for-azure-ad-premium-is-now-in-preview.aspx)

[https://azure.microsoft.com/en-us/documentation/articles/active-directory-accessmanagement-groups-with-advanced-rules/](https://azure.microsoft.com/en-us/documentation/articles/active-directory-accessmanagement-groups-with-advanced-rules/)

You can also assign licenses with the following methods:

1. Using the Office 365 Portal - like you would add Office 365 licenses.  This was made available late 2015 - [http://blogs.technet.com/b/microsoftintune/archive/2015/09/01/intune-and-ems-subscriptions-now-available-in-the-office-365-portal.aspx](http://blogs.technet.com/b/microsoftintune/archive/2015/09/01/intune-and-ems-subscriptions-now-available-in-the-office-365-portal.aspx)
2. Using Azure AD PowerShell - [http://blogs.technet.com/b/treycarlee/archive/2013/11/01/list-of-powershell-licensing-sku-s-for-office-365.aspx](http://blogs.technet.com/b/treycarlee/archive/2013/11/01/list-of-powershell-licensing-sku-s-for-office-365.aspx) ,you can use the following example to assign EMS licenses (with all options) **only** to users with an Office 365 E3 license: `$EMSSKU = (Get-MsolAccountSku | ? { $_.AccountSkuID -like "*:EMS"})[0].accountSkuId Get-MsolUser -All | ? { $_.licenses.accountsku.SkuPartNumber -eq "ENTERPRISEPACK"} | Set-MsolUserLicense -AddLicenses $EMSSKU`
3. Azure AD Graph API - [https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/users-operations#FunctionsandactionsonusersAssignalicensetoauser](https://msdn.microsoft.com/en-us/library/azure/ad/graph/api/users-operations#FunctionsandactionsonusersAssignalicensetoauser)

Enjoy

ilantz
