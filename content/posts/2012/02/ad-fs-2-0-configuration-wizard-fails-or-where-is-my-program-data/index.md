---
title: AD FS 2.0 Configuration Wizard Fails - or where is my Program Data ?
date: 2012-02-21
categories:
- adfs
- office-365
showTableOfContents: true
draft: false
slug: ad-fs-2-0-configuration-wizard-fails-or-where-is-my-program-data
---



Hi Again,

{{< lead >}}
I've encountered a funny situation the other day with a new Office 365 hybrid deployment with an initial install of ADFS 2.0 for Federation with Office 365 and SSO.
{{< /lead >}}

The first attempt of running the "AD FS 2.0 Federation Server Configuration Wizard" ended with a failure:

> You do not have sufficient privileges to create a container in Active Directory at location CN=46bd8c28-c299-475b-9853-8176010f4273,CN=ADFS,CN=Microsoft,CN=Program Data,DC=Domain,DC=com for use with sharing certificates. Verify that you are logged on as a Domain Admin or have sufficient privileges to create this container, and try again.

{{< figure src="images/1-create-active-directory-container-for-sharing-certificates.png" alt="Create Active Directory container for sharing certificates - Error" caption="Create Active Directory container for sharing certificates - Error" >}}

Well, I've double checked my logged on user credentials, the built-in Administrator - we have all the required permissions. I've opened ADSIedit and looked for the Program Data container under the domain partition, just to make sure no permissions issues are indeed preventing this wizard to complete.

Guess what - **no Program Data container !!?**

I had the feeling that the container was moved rather then deleted or removed completely.. so I decided made a little search, a custom search for containers with a description starting with the string "default"

{{< figure src="images/2-search-program-data-container.png" alt="Search Program Data Container" caption="Search Program Data Container" >}}

{{< figure src="images/3-program-data-container-found.png" alt="Program Data Container Found" caption="Program Data Container Found" >}}

Found it (!) and moved it to the root of the Domain tree, then I've started the the ADFS configuration wizard again.

{{< figure src="images/4-adfs-configuration-successful.png" alt="Adfs Configuration Successful" caption="Adfs Configuration Successful" >}}

Case closed :) happy ADFS and a working federation with Office 365
