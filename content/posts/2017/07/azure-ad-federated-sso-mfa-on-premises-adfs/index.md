---
title: Azure AD Federated SSO and MFA on-premises with ADFS
date: 2017-07-23
categories:
- adfs
- azure-ad
showTableOfContents: true
draft: false
---


Updates:

*2017-07-27* - I've included another important note about adding the "Authentication Methods References" claim

* * *

Hi again, this is a quick note for anyone who will try to achieve this. I'm writing this post after the topic has been raised from customers and my colleges.

Here are some of the challenges that might brought to you here

- An Azure AD tenant, with a federated domain pointing to an ADFS
- ADFS server running 2012 R2 / 2016 with a Multi Factor setup, either with Azure MFA or a 3rd party MFA provider
- A conditional access / identity protection policy in Azure AD which should enforce Multi Factor authentication
- ADFS 2016 with Azure MFA set as primary authentication
- Event ID 364 on the ADFS server - Encountered error during federation passive request. MSIS7042: The same client browser session has made '6' requests in the last '4' seconds

While configuring this, you might get multiple Multi Factor prompts, user performs MFA on-premises, but when redirected back to Azure AD - second factor prompt in cloud is presented. Here’s how you win:

- Make sure you configure the federated domain setting in Azure AD with -SupportsMFA $true – this will point Multi Factor“requests” to the ADFS:

```powershell
Set-MsolDomainFederationSettings -DomainName <name.com> -SupportsMFA $true
```

See more here - [https://docs.microsoft.com/en-us/azure/active-directory/active-directory-conditional-access-azuread-connected-apps#conditional-access-rules-with-mfa](https://docs.microsoft.com/en-us/azure/active-directory/active-directory-conditional-access-azuread-connected-apps#conditional-access-rules-with-mfa)

- In addition to the above you also need to make sure to configure -PromptLoginBehavior Disabled, this will make sure that authentication requests from Azure AD will reach the ADFS “correctly” and won’t cause it to re-authenticate your users:

```powershell
Set-MsolDomainFederationSettings -DomainName <name.com> -PromptLoginBehavior Disabled
```

See more here -  [https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-prompt-login](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/ad-fs-prompt-login)

Note that for ADFS 2012 R2, the July 2016 update rollup is required for this parameter to work.

- Make sure you create a custom rule to pass "Authentication Methods References" as a claim, follow [Secure Azure AD resources using AD FS](https://docs.microsoft.com/en-us/azure/multi-factor-authentication/multi-factor-authentication-get-started-adfs-w2k12#secure-azure-ad-resources-using-ad-fs)

* * *

With only setting Azure MFA set as Primary, you effectively do NOT perform Multi Factor. please read carefully [Configure AD FS 2016 and Azure MFA](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/configure-ad-fs-2016-and-azure-mfa) and see the notes around it.

If you have policy which will enforce Multi Factor and your setup is Azure MFA as Primary - follow the steps above first.

If you'd like to "skip" the second prompt in the cloud, you can either re-think your CA policy :) or follow [https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/create-a-rule-to-send-claims-using-a-custom-rule](https://docs.microsoft.com/en-us/windows-server/identity/ad-fs/operations/create-a-rule-to-send-claims-using-a-custom-rule) to add the following claim using a custom rule:

```text
c:[Type == "http://schemas.microsoft.com/claims/authnmethodsreferences"] => issue(Type = "http://schemas.microsoft.com/claims/authnmethodsreferences", Value = "http://schemas.microsoft.com/claims/multipleauthn");
```

This rule will effectively add all your users a static "fake" claim which states they have performed Multi Factor successfully.

ilantz
