---
title: Exchange Server 2010 SP2 is out!
date: 2011-12-06
categories:
- exchange-2010
showTableOfContents: true
draft: false
---


This just in !!

{{< lead >}}
Exchange Server 2010 Service Pack 2 is here ! :) I will do my best to show off some new features soon enough...
{{< /lead >}}

- [download](http://go.microsoft.com/fwlink/?LinkID=232843 "Download Exchange 2010 SP2")
- [what’s new](http://go.microsoft.com/fwlink/?LinkID=228135 "Check out what's new in Exchange 2010 SP2")
- [release notes](http://go.microsoft.com/fwlink/?LinkId=235234 "Read Exchange 2010 SP2 Release Notes")
- [prerequisites](http://go.microsoft.com/fwlink/?LinkID=194324 "Go over prerequisites for Exchange 2010 SP2")

To follow my excitement, here are the highlights of from the TechNet topic - [What's New in Exchange 2010 SP2](http://technet.microsoft.com/en-us/library/hh529924.aspx)

### Hybrid Configuration Wizard

Exchange 2010 SP2 introduces the Hybrid Configuration Wizard which provides you with a streamlined process to configure a hybrid deployment between on-premises and Office 365 Exchange organizations. Hybrid deployments provide the seamless look and feel of a single Exchange organization and offer administrators the ability to extend the feature-rich experience and administrative control of an on-premises organization to the cloud. For more information, see [Understanding the Hybrid Configuration Wizard](http://technet.microsoft.com/en-us/library/hh529921.aspx).

Address Book Policies

Exchange 2010 SP2 introduces the address book policy object which can be assigned to a mailbox user. The ABP determines the global address list (GAL), offline address book (OAB), room list, and address lists that are visible to the mailbox user that is assigned the policy. Address book policies provide a simpler mechanism to accomplish GAL separation for the on-premises organization that needs to run disparate GALs. For more information, see [Understanding Address Book Policies](http://technet.microsoft.com/en-us/library/hh529948.aspx).

### Cross-Site Silent Redirection for Outlook Web App

With Exchange 2010 SP2, you can enable a silent redirection when a Client Access server receives a client request that is better serviced by a Client Access server located in another Active Directory site. This silent redirection can also provide a single sign-on experience when forms-based authentication is enabled on each Client Access server. For more information, see [Understanding Proxying and Redirection](http://technet.microsoft.com/en-us/library/bb310763.aspx).

### Mini Version of Outlook Web App (OMA is back !)

The mini version of Outlook Web App is a lightweight browser-based client, similar to the Outlook Mobile Access client in Exchange 2003. It’s designed to be used on a mobile operating system. The mini version of Outlook Web App provides users with the following basic functionality:

- Access to e-mail, calendar, contacts, tasks and the global address list.
- Access to e-mail subfolders.
- Compose, reply to, and forward e-mail messages.
- Create and edit calendar, contact, and task items.
- Handle meeting requests.
- Set the time zone and automatic reply messages.

For more information, see [Understanding the Mini Version of Outlook Web App](http://technet.microsoft.com/en-us/library/hh529922.aspx).

### Mailbox Replication Service

In Exchange 2010 SP1, if you wanted to move mailboxes from on-premises to Outlook.com or to another forest, you had to enable MRSProxy on the remote Client Access server. To do this, you had to manually configure the web.config file on every Client Access server. In Exchange 2010 SP2, two parameters have been added to the **New-WebServicesVirtualDirectory** and **Set-WebServicesVirtualDirectory** cmdlets so that you don't have to perform the manual configuration: _MRSProxyEnabled_ and _MaxMRSProxyConnections_. For more information, see [Start the MRSProxy Service on a Remote Client Access Server](http://technet.microsoft.com/en-us/library/ee732395.aspx).

### Mailbox Auto-Mapping

In Exchange 2010 SP1, Office Outlook 2007 and Outlook 2010 clients can automatically map to any mailbox to which a user has Full Access permissions. If a user is granted Full Access permissions to another user's mailbox or to a shared mailbox, Outlook, through Autodiscover, automatically loads all mailboxes to which the user has full access. However, if the user has full access to a large number of mailboxes, performance issues may occur when starting Outlook. Therefore, in Exchange 2010 SP2, administrators can turn off the auto-mapping feature by setting the value of the new _Automapping_ parameter to $false on the **Add-MailboxPermission** cmdlets. For more information, see [Disable Outlook Auto-Mapping with Full Access Mailboxes](http://technet.microsoft.com/en-us/library/hh529943.aspx).

### Multi-Valued Custom Attributes

Exchange 2010 SP2 introduces five new multi-value custom attributes that you can use to store additional information for mail recipient objects. The _ExtensionCustomAttribute1_ to _ExtensionCustomAttribute5_ parameters can each hold up to 1,300 values. You can specify multiple values as a comma-delimited list.The following cmdlets support these new parameters:

- **Set-DistributionGroup**
- **Set-DynamicDistributionGroup**
- **Set-Mailbox**
- **Set-MailContact**
- **Set-MailPublicFolder**
- **Set-RemoteMailbox**

### Litigation Hold

In Exchange 2010 SP2, you can’t disable or remove a mailbox that has been placed on litigation hold. To bypass this restriction, you must either remove litigation hold from the mailbox, or use the new _IgnoreLegalHold_ switch parameter when removing or disabling the mailbox. The _IgnoreLegalHold_ parameter has been added to the following cmdlets:

- **Disable-Mailbox**
- **Remove-Mailbox**
- **Disable-RemoteMailbox**
- **Remove-RemoteMailbox**
- **Disable-MailUser**
- **Remove-MailUser**
