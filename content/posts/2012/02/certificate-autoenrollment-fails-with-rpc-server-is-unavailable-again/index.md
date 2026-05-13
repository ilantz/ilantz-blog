---
title: Certificate autoenrollment fails with RPC server is unavailable - Again
date: 2012-02-02
categories:
- pki
showTableOfContents: true
draft: false
---


Hey Again !

{{< lead >}}
I've blogged in the past about this issue - [Certificate autoenrollment fails with RPC server is unavailable](http://ilantz.com/2010/03/16/certificate-autoenrollment-fails-with-rpc-server-is-unavailable/ "Certificate autoenrollment fails with RPC server is unavailable") , but following a session today, we've encountered a new situation when trying to Auto-Enroll certificates, also with manual enrollment using MMC. The error code was **0x800706ba** -  The RPC server is unavailable
{{< /lead >}}

If you read my previous blog, you'll see I've explained a situation with Auto-Enrollment on domain controllers when the CA is installed on a DC. Solution was actually adding the "Domain Controllers" security group to the CERTSVC_DCOM_ACCESS security group, but what happens when the CERTSVC_DCOM_ACCESS was deleted ?

Well, easy ( so it seems )

1. Create the CERTSVC_DCOM_ACCESS group - Domain Local, Security Group in the Users container
2. Populate the group with "Domain Users" , "Domain Computers" , "Domain Controllers"
3. Log on to the CA server and run the following commands:
    1. certutil -setreg SetupStatus -SETUP_DCOM_SECURITY_UPDATED_FLAG
    2. net stop certsvc && net start certsvc
4. Restart your effected computers / DC's , because they have a new computer group membership
5. Successfully auto-enroll your certificate

Have fun !

Reference links:

[http://support.microsoft.com/kb/927066](http://support.microsoft.com/kb/927066)

Also (Again): [http://blogs.technet.com/instan/archive/2009/12/07/troubleshooting-autoenrollment.aspx](http://blogs.technet.com/instan/archive/2009/12/07/troubleshooting-autoenrollment.aspx)
