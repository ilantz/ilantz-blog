---
title: RTL Plain Text emails with Outlook 2007 - fixed
date: 2009-11-24
categories:
- exchange-2003
- exchange-2007
- outlook-mapi
showTableOfContents: true
draft: false
---


{{< lead >}}
Finally, a long term solution to a problem that have been annoying quite a while...
{{< /lead >}}

Outlook 2007 + Plain Text replies , that uses Right to Left languages , in my case Hebrew, were received reversed in order .. that is the words in the sentences were displayed literally reversed.

A quite annoying word issue actually... A workaround for this was making sure that users were sending out Rich Text (RTF) email's. then the replies were displayed correctly.

Long story short. to solve this, request and install the following patch http://support.microsoft.com/kb/973401 - Description of the Word 2007 hotfix package (Word-x-none.msp, Wordconv-x-none.msp): August 25, 2009

Additional configuration to align the text to the right could be done by following daniel's petri post regarding this :

http://www.petri.co.il/correcting-email-display-direction-in-outlook.htm

This solved my issue on the spot.

Better later then never :)
