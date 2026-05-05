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

| **Processor/Memory Feature** | **Windows Server 2008 R2** | **Windows Server  2012 Release Candidate** |
| --- | --- | --- |
| **Logical processors on hardware** | 64 | 320 |
| **Physical memory** | 1 TB | 4 TB |
| **Virtual processors per host** | 512 | 2,048 |
| **Virtual processors per virtual machine** | 4 | 64 |
| **Memory per virtual machine** | 64 GB | 1 TB |
| **Active virtual machines** | 384 | 1,024 |
| **Maximum Cluster Nodes** | 16 | 64 |
| **Maximum Cluster Virtual machines** | 1,000 | 4,000 |

**Network**

| **Network Feature** | **Windows Server 2008 R2** | **Windows Server  2012 Release Candidate** |
| --- | --- | --- |
| **NIC Teaming** | Yes, through partners | Yes, Windows NIC teaming in box |
| **VLAN Tagging** | Yes | Yes |
| **MAC Spoofing Protection** | Yes, with R2 SP1 | Yes |
| **ARP Spoofing Protection** | Yes, with R2 SP1 | Yes |
| **SR\-IOV Networking** | No | Yes |
| **Network QoS** | No | Yes |
| **Network Metering** | No | Yes |
| **Network Monitor Modes** | No | Yes |
| **Ipsec Task Offload** | No | Yes |
| **VM Trunk Mode** | No | Yes |

**Storage**

| **Storage Feature** | **Windows Server 2008 R2** | **Windows Server  2012 Release Candidate** |
| --- | --- | --- |
| **Live storage migration** | No, quick storage migration through System  Center Virtual Machine Manager | Yes, with no limits (as many as the hardware will allow) |
| **Virtual machines on file storage** | No | Yes, Server Message Block 3.0 (SMB3) |
| **Guest Fibre Channel** | No | Yes |
| **Virtual disk format** | VHD up to 2 TB | VHD up to 2 TB VHDX up to 64 TB |
| **Virtual machine guest clustering** | Yes, through iSCSI | Yes, through iSCSI, Fibre Channel, or Fibre  Channel over Ethernet (FCoE) |
| **Native 4 KB disk support** | No | Yes |
| **Live virtual hard disk merge** | No, offline | Yes |
| **Live new parent** | No | Yes |
| **Secure offloaded data transfer** | No | Yes |

**Manageability**

| **Manageability Feature** | **Windows Server 2008 R2** | **Windows Server  2012 Release Candidate** |
| --- | --- | --- |
| **Hyper-V PowerShell** | No | Yes |
| **Network PowerShell** | No | Yes |
| **Storage PowerShell** | No | Yes |
| **REST APIs** | No | Yes |
| **SCONFIG** | Yes | Yes |
| **Enable/Disable shell** | No, server core at operating system setup | Yes |
| **VMConnect support for RemoteFX** | No | Yes |

Additional links for your reading:

[Hyper-V Comparison Guide](http://download.microsoft.com/download/2/C/A/2CA38362-37ED-4112-86A8-FDF14D5D4C9B/WS%202012%20Feature%20Comparison_Hyper-V.pdf "Hyper-V Comparison Guide")

[Competitive Advantages of Windows Server 2012 RC Hyper-V](http://download.microsoft.com/download/5/A/0/5A0AAE2E-EB20-4E20-829D-131A768717D2/Competitive%20Advantages%20of%20Windows%20Server%202012%20RC%20Hyper-V%20over%20VMware%20vSphere%205%200%20V1%200.pdf "Competitive Advantages of Windows Server 2012 RC Hyper-V")

[Windows Server 2012 Release Candidate Server Virtualization](http://www.microsoft.com/en-us/server-cloud/windows-server/2012-server-virtualization.aspx "Windows Server 2012 Release Candidate Server Virtualization")

[Windows Server 2012 Release Candidate](http://www.microsoft.com/en-us/server-cloud/windows-server/2012-default.aspx "Windows Server 2012 Release Candidate")
