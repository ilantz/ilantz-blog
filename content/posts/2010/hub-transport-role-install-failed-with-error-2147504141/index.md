---
title: Hub Transport Role Install Failed with error 2147504141
date: 2010-07-20
categories:
- exchange-2010
- hyper-v
- server-2008-r2
showTableOfContents: true
draft: false
---


{{< lead >}}
Wanted to share with an experience I've had with installing Exchange 2010 SP1 on Windows Server 2008 R2 in Hyper-V 2008 R2 environment.
{{< /lead >}}

When I i tried to install a fresh server for testing Exchange 2010 SP1 Beta, the setup failed when installing the Hub Transport Role:

Error: The execution of: "$error.Clear(); install-ExsetdataAtom -AtomName SMTP -DomainController $RoleDomainController", generated the following error: "An error occurred with error code '2147504141' and message 'The property cannot be found in the cache.'.".

An error occurred with error code '2147504141' and message 'The property cannot be found in the cache.'.

This issue is not "new", as IPV6 is tend to be disabled as default by many customers, and installations of Exchange 2007 and Exchange 2010 fails with the exact same error if IPV6 is **Disabled.**

My virtual machine was clean and did not had IPV6 disabled, so I've searched this up to the following thread in the Technet Social Forums : [Hub Transport Role Install Fail error # 2147504141](http://social.technet.microsoft.com/Forums/en-us/exchange2010/thread/8f6ff508-2c09-4140-ba14-eca32bc5bf1d)

A comment from Scott Landry gave a new solution for this, and seems it's now also been related to Hyper-V, as the suggested KB [http://support.microsoft.com/kb/980050](http://support.microsoft.com/kb/980050) - Error message when the Exchange Server 2010 setup on a Hyper-V virtual machine fails:“2147504141”

Anyhow, disabling the " Time synchronization " from the Integration Services settings on the Virtual Machine solved this !

Just a heads up for all of you that might encounter this.
