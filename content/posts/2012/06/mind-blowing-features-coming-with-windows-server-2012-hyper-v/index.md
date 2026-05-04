---
title: Mind blowing features coming with Windows Server 2012 Hyper-v
date: 2012-06-06
categories:
- hyper-v
- server-2012
showTableOfContents: true
draft: false
---


{{< lead >}}
Hey Again, It seems like next year will keep me busy with visualization projects based on Hyper-V :) Many promising features are coming up with the next Windows Server version and I'm already excited !
{{< /lead >}}

Just take a look at tables below for a comparison between 2008 R2 and 2012 RC Hyper-V:

**Processor and Memory Support**

| **Processor/Memory Feature** | **W****i****ndo****w****s Server 2008 R2** | **W****i****ndo****w****s Server  2012 Release Candidate** |
| --- | --- | --- |
| **Logical processors on hardware** | 64 | 320 |
| **Physical memory** | 1 TB | 4 TB |
| **V****ir****tual processors per host** | 512 | 2,048 |
| **V****ir****tual processors per virtual machine** | 4 | 64 |
| **Me****mory per virtual machine** | 64 GB | 1 TB |
| **Active virtual machines** | 384 | 1,024 |
| **Ma****ximum Cluster Nodes** | 16 | 64 |
| **Ma****ximum Cluster Virtual machines** | 1,000 | 4,000 |

**Network**

| **N****e****twork Feature** | **W****i****ndo****w****s Server 2008 R2** | **W****i****ndo****w****s Server  2012 Release Candidate** |
| --- | --- | --- |
| **N****I****C Teaming** | Yes, through partners | Yes, Windows NIC teaming in box |
| **V****LAN Tagging** | Yes | Yes |
| **M****AC Spoofing Protection** | Yes, with R2 SP1 | Yes |
| **ARP Spoofing Protection** | Yes, with R2 SP1 | Yes |
| **S****R****\-IOV Networking** | No | Yes |
| **N****e****twork QoS** | No | Yes |
| **N****e****twork Metering** | No | Yes |
| **N****e****twork Monitor Modes** | No | Yes |
| **I****p****sec Task Offload** | No | Yes |
| **V****M Trunk Mode** | No | Yes |

**Storage**

| **S****torage Feature** | **W****i****ndo****w****s Server 2008 R2** | **W****i****ndo****w****s Server  2012 Release Candidate** |
| --- | --- | --- |
| **Live storage migration** | No, quick storage migration through System  Center Virtual Machine Manager | Yes, with no limits (as many as the hardware will allow) |
| **V****ir****tual machines on file storage** | No | Yes, Server Message Block 3.0 (SMB3) |
| **G****ue****st Fibre Channel** | No | Yes |
| **V****ir****tual disk format** | VHD up to 2 TB | VHD up to 2 TB VHDX up to 64 TB |
| **V****ir****tual machine guest clustering** | Yes, through iSCSI | Yes, through iSCSI, Fibre Channel, or Fibre  Channel over Ethernet (FCoE) |
| **N****a****tive 4 KB disk support** | No | Yes |
| **Live virtual hard disk merge** | No, offline | Yes |
| **Live new parent** | No | Yes |
| **Se****c****u****r****e offloaded data transfer** | No | Yes |

**Manageability**

| **Mana****g****eab****ili****t****y Feature** | **W****i****ndo****w****s Server 2008 R2** | **W****i****ndo****w****s Server  2012 Release Candidate** |
| --- | --- | --- |
| **Hyper-V PowerShell** | No | Yes |
| **N****e****twork PowerShell** | No | Yes |
| **S****torage PowerShell** | No | Yes |
| **REST APIs** | No | Yes |
| **S****C****ONFIG** | Yes | Yes |
| **Enable/Disable shell** | No, server core at operating system setup | Yes |
| **VM****C****onne****c****t support for RemoteFX** | No | Yes |

Additional links for your reading:

[Hyper-V Comparison Guide](http://download.microsoft.com/download/2/C/A/2CA38362-37ED-4112-86A8-FDF14D5D4C9B/WS%202012%20Feature%20Comparison_Hyper-V.pdf "Hyper-V Comparison Guide")

[Competitive Advantages of Windows Server 2012 RC Hyper-V](http://download.microsoft.com/download/5/A/0/5A0AAE2E-EB20-4E20-829D-131A768717D2/Competitive%20Advantages%20of%20Windows%20Server%202012%20RC%20Hyper-V%20over%20VMware%20vSphere%205%200%20V1%200.pdf "Competitive Advantages of Windows Server 2012 RC Hyper-V")

[Windows Server 2012 Release Candidate Server Virtualization](http://www.microsoft.com/en-us/server-cloud/windows-server/2012-server-virtualization.aspx "Windows Server 2012 Release Candidate Server Virtualization")

[Windows Server 2012 Release Candidate](http://www.microsoft.com/en-us/server-cloud/windows-server/2012-default.aspx "Windows Server 2012 Release Candidate")
