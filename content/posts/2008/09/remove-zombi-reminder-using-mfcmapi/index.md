---
title: Remove "Zombi" reminders using MFCMAPI
date: 2008-09-16
categories:
- outlook-mapi
showTableOfContents: true
draft: false
---


{{< lead >}}
I was requested to do this the other day.. so I use the amazing [MFCMAPI](http://www.codeplex.com/MFCMAPI) tool which opens wide mailboxes and thier raw content..
{{< /lead >}}

**Be aware that i am  really deleting an appointment ! the reminder will be gone with it. (Thanks for Steve for correcting me here.)**

to do so we have a few steps:

1\. Launch MFCMAPI tool on the user’s client.

2\. Go to Session -> Logon and Display Store Table

3\. Select the outlook profile of the user and double-click “Mailbox - your user name”

4\. Expand "Root Container"

5\. Expand "Top of Information Store"

6\. Now its the tricky part , we need to find the specific reminder that does the troubles, there might be a few directory's of reminders (maybe in more then one language...).

7\. Double click the folder & start looking for the specific reminder (really the appointment)..

8\. When you find the appointment or a few together even , right click and choose "Delete Message" , in the options select “permanent deletion (deletes to deleted item retention if supported)”.

9\. close MFCMAPI & re-check in outlook.

you can use this method to delete problematic appointments, messages & all other MAPI data inside your exchange mailbox. BUT ! be careful , you can mess your mailbox up if you do something wrong ...

Reference for steps and example ...

Download MFCMAPI Latest version:

[http://www.codeplex.com/MFCMAPI](http://www.codeplex.com/MFCMAPI)

[http://exchangeshare.wordpress.com/2008/04/10/delete-corrupted-hidden-or-stale-rules-from-mailbox-with-mfcmapi/](http://exchangeshare.wordpress.com/2008/04/10/delete-corrupted-hidden-or-stale-rules-from-mailbox-with-mfcmapi/)

[http://support.microsoft.com/kb/924297](http://support.microsoft.com/kb/924297)
