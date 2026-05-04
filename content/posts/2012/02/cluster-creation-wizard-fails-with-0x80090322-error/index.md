---
title: Cluster Creation Wizard fails with 0x80090322 error
date: 2012-02-26
categories:
- hyper-v
- windows-cluster
showTableOfContents: true
draft: false
---


Hi again,

{{< lead >}}
Today I've got a call from a client regarding a new Hyper-V 2008 R2 SP1 cluster, the create cluster wizard kept failing during the forming cluster step with a timeout..
{{< /lead >}}

Well, troubleshooting..

1. Running Cluster LOG /gen
2. Doing some reading...
3. Locating the step and the error:
    
    > [NODE] Node 1: New join with node2: stage: 'Authenticate Initial Connection' status HrError(0x80090322) reason: '[SV] Authentication failed' DBG [CHANNEL 172.16.1.2:~3343~] Close(). WARN cxl::ConnectWorker::operator (): HrError(0x80090322)' because of '[SV] Authentication or Authorization Failed'
    
4. Looking up 0x80090322 with ERR.EXE means SEC_E_WRONG_PRINCIPAL
5. Lazy me , doing google for 0x80090322 cluster authentication failed
6. Read ["2 node cluster windows 2008 R2 cluster won't form"](http://social.technet.microsoft.com/Forums/en/winserverClustering/thread/5891d2aa-0dfd-41ed-9dbf-40793c391ee3)
7. Delete two users that were created to manage the servers.. node1 and node2 :)
8. Run create cluster wizard again - **SUCCESS !**
9. Retrospective understand the error... SEC_E_WRONG_PRINCIPAL seems like the wizard can't tell the difference between the user accounts and the computer accounts. ("By Design")

Nice ! I was shocked from the solution.. but hey.. it worked instantly.
