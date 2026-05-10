---
title: my cup of checkpoint SecuRemote / SecuClient
date: 2008-12-08
slug: my-cup-of-checkpoint-securemote-secuclient
categories:
- misc
- vista-7
showTableOfContents: true
draft: false
---


{{< lead >}}
Well.. I really like checkpoint products.. with that being said it , and by the title of this post i'll rather go to business :)
{{< /lead >}}

For the record, I'm using Vista x86 with sp1 on my laptop , and mostly happy with the OS behavior.. anyways, the thing is that i have VPN-1 SecuRemote / SecureClient NGX R60 HFA2 installed on my laptop since I've installed the OS, i'm installing only SecuRemote during setup & using it a lot to connect to costumers and such .

so far os good , then comes this time when I had to connect to a client and for some reason, I had been persuaded to install the SecuClient because we had some issues to connect...!@$@

yea , from this point things went bad !

humm.. well for starts I've uninstalled , restarted & re-installed the SecuClient this time, setup got stuck.. in the part where it configures additional components or something (that gui with the wheels ...) then on the reboot... hum well the desktop fail to show up , it was pitch black with the mouse cursor only !!? so obviously something went wrong.

long story short , after battling with the install over and over again, the quick fix to the black screen is manually delete fw.sys from system32drivers each time, this fastlly broke the service binding on the network adapters & made me able to boot normally to windows and uninstall the secure client software and drivers.

finally what fixed the issue is actually binding back IPV6 which i've disabled ...added the binding to the network adapters & removedthe registry key for info on that to: [http://support.microsoft.com/kb/929852](http://support.microsoft.com/kb/929852) after that , all went great.. regarding the install of the client - securemote only !! :)

okay, now what ... some more fun to the end ! I'm lately using internet connection sharing on my laptop , so that it shares wireless to the lan adapter.. humm that got broke , unbinding the checkpoint service from the network adapter did the trick on that one.

There. nuff rumbling.
