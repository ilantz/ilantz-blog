---
title: Controlling External Collaboration in Microsoft Teams
date: 2018-05-14
categories:
- azure-ad
- office-365
showTableOfContents: true
description: Learn how to control external collaboration in Microsoft Teams by using
  Azure AD and Office 365 Group settings to limit who can invite guests.
draft: false
---


{{< lead >}}
Most organizations are required these days to enable collaboration solutions and services with external parties. These may include B2B scenarios or B2C in some cases.
{{< /lead >}}

In this post I'll be specific to Office 365 Group resources, with Microsoft Teams as an example, you should be aware that [each Team in Microsoft Teams corresponds to an Office 365 group](https://docs.microsoft.com/en-us/microsoftteams/office-365-groups).

A common ask is **"We wish to enable only named people to join as a guest to our Teams, we don't want anyone from the organization to invite anyone they like - we need to control this with an internal workflow."**  to satisfy this request, we will use native capabilities within Azure Active Directory and Office 365 to enable group owners to add **existing** external guests to their team/office 365 group. In addition, we will enable **only specific people** in the organization with the permission **to create and add new guests accounts** to the directory.

{{< alert icon="circle-info" >}}
**Note:** This is the basic example, this can be adapted to more complex workflows of approval/automation to make this more customized to a specific requirement.
{{< /alert >}}

1. In Office 365 Admin Center, navigate to "Services & add-ins", select "Office 365 Groups" and enable "Let group owners add people outside the organization to groups"
            
    {{< figure src="images/enable-office-365-group-guest.png" alt="enable-office-365-group-guest" caption="Enabling the capability to add external guest accounts to Office 365 groups." >}}
    
2. To make sure your guests will also have access to the SharePoint files, enable external sharing using the SharePoint Admin Center. with alignment to our blog theme, we will enable access to Existing accounts only.
            
{{< figure src="images/enable-external-sharing-in-sharepoint.png" alt="enable-external-sharing-in-sharepoint" caption="Enabling external content sharing within SharePoint to allow guests to access the files within Microsoft Teams." >}}

3. We are now ready to limit who can invite external guests. we will configure this using the Azure Active Directory blade in the Azure portal. {{< figure src="images/Azure-AD-manage-external-collaboration.png" alt="Azure-AD-manage-external-collaboration" >}}

{{< figure src="images/2-Azure-AD-only-admins-can-invite.png" alt="Azure-AD-only-admins-can-invite" caption="Disabling the capability for non-admin or users with the guest inviter role to add new external guest accounts to the directory" >}}

Disabling "Members can invite" and "Guests can invite" will effectively achieve our goal - "Admins and users in the guest inviter role can invite"

4. Finally add assign the "Guest inviter" role to whom ever you need

{{< figure src="images/Azure-AD-assigning-guest-inviter-role.png" alt="Azure-AD-assigning-guest-inviter-role" caption="Assigning the \"Guest inviter\" role to a specific user account." >}}

The configuration is now complete, a Guest Inviter or an Admin can now add new guests to the directory, and follow whatever internal due diligence or workflow prior to that. Using the [(new) AzureAD PowerShell module](https://docs.microsoft.com/en-us/powershell/azure/active-directory/install-adv2?view=azureadps-2.0) is my personal recommendation, this way the guest user could be silently added to the directory - and an email will not be sent to him. later on an owner of an Office 365 Group or a Microsoft Teams group could add him easily like any other member - and that will trigger the email invite to the external user.

```powershell
New-AzureADMSInvitation -InvitedUserDisplayName "John Doe (External)" -InvitedUserEmailAddress "john.doe@contoso.com" -SendInvitationMessage:$false -InviteRedirectUrl "http://just.a.placeholder.local"
```

Using the Azure AD portal is also available to the guest inviter role if PowerShell is out of the question {{< figure src="images/1-Azure-AD-creating-a-guest.png" alt="Azure AD creating a guest" >}}

{{< figure src="images/2-Azure-AD-creating-a-guest.png" alt="Azure AD creating a guest" caption="Adding a new external guest account to the directory." >}}

And if you've wondered, this is the error if someone would try to add a new guest account and they don't have the proper permissions in Microsoft Teams. {{< figure src="images/Adding-guest-you-are-not-authorized-microsoft-teams.png" alt="Adding guest you are not authorized microsoft teams" >}}

Enjoy!
