---
title: Prevent users from changing the permissions settings on their mailbox folders
  in Outlook 2003/2007
date: 2009-06-03
categories:
- group-policy
- outlook-mapi
showTableOfContents: true
draft: false
---


{{< lead >}}
From a thread I've took part in, there are currently no settings in the official office 2003/2007 ADM packs to control this setting.
{{< /lead >}}

Here's the registry how to:

For Outlook 2003:

[http://support.microsoft.com/kb/948894](http://support.microsoft.com/kb/948894) 1, Click Start, click Run, type regedit, and then click OK. 2, Locate and then click the following registry subkey: HKEY_CURRENT_USERSoftwareMicrosoftOffice11.0OutlookOptionsFolders 3, On the Edit menu, point to New, and then click DWORD Value. 4, Type DisableEditPermissions, and then press ENTER. 5, Right-click DisableEditPermissions, and then click Modify. 6, In the Value data box, type 1, and then click OK. 7, Exit Registry Editor.

For Outlook 2007, that is HKEY_CURRENT_USERSoftwareMicrosoftOffice12.0OutlookOptionsFolders

Manual creation of the ADM is required, i might post it later on.[](http://support.microsoft.com/kb/948894)
