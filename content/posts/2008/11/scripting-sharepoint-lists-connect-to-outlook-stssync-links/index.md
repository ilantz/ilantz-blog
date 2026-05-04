---
title: Scripting sharepoint lists "Connect to Outlook" stssync links
date: 2008-11-02
categories:
- outlook-mapi
- sharepoint
showTableOfContents: true
draft: false
---


{{< lead >}}
I was asked to figure this out, took me a while but i found quite a nice approach to make it super easy.
{{< /lead >}}

[The official Technet on the matter](http://technet.microsoft.com/en-us/library/cc767102.aspx),  explains the how to phrase the stssync link correctly , after fighting with it..unicode etc.. i finally though of something easy.

1\. Locate the list you want to connect to.

2\. Press "connect to outlook" button.

3\. Approve in outlook...

4\. Right click the newly added list & choose share "List name"

5\. Mail the share offer to yourself .. then check out the message headers.

6\. Notice the "x-sharing-config-url" , this is the exact syssync reference link that you need :) clean and easy & without any hassle or unicode stuff...

7\. Enjoy distributing this , you can use outlook.exe /share stssync://url , or use a Link in a webpage to make the users add the lists to their outlook.

That's it :)
