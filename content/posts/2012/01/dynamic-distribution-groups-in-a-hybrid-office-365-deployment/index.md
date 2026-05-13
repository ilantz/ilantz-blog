---
title: Dynamic Distribution Groups in a Hybrid Office 365 Deployment
date: 2012-01-05
categories:
- office-365
showTableOfContents: true
draft: false
---


Happy new year everyone !

{{< lead >}}
I've been very busy lately lots of work, especially with Office 365 Hybrid deployments, Office 365 is really a growing demand and presents new technical perspectives which comes down to know knowledge :)
{{< /lead >}}

Well yeah I am a geek that likes to keep learning new stuff...

Long story short, you have deployed your Hybrid Office 365 topology to your current Exchange 2003, 2007 or 2010 organization and now you move a mailbox enabled user to the cloud (25 GB mailboxes rocks) , everyone is happy, then the CEO sends a "Happy New Year" email to "All Company" DL and for some reason the user which was moved to the cloud did not receive that memo....

So what happened ?

Most "All Company" distribution lists are Dynamic Distribution Groups AKA Query Based Distribution Group , and as such they have a LDAP filter which populates the members auto-magically - most members are Users with Exchange Mailbox, but when you move a user mailbox to Office 365 the original user was transformed to Mail-Enabled user - **With an external address !**

Yeah, you will need to modify those groups now to have "Users with External e-mail addresses" also checked :)

{{< figure src="images/enable-users-with-external-e-mail-addesses.jpg" alt="Enable Users With External E-Mail Addesses" caption="Enable Users With External E-Mail Addesses" >}}

Problem solved - Happy new year !

ilantz
