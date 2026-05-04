---
title: Certificate autoenrollment fails with RPC server is unavailable
date: 2010-03-16
categories:
- pki
- server-2008-r2
showTableOfContents: true
draft: false
---


Hi again,

{{< lead >}}
Some of my work with Certification Authority or ADCS involves enrolling certificates for many usages, sometimes autoenrollment does not work as it should... and you get some weird errors like:
{{< /lead >}}

> Certificate enrollment for Local system failed to enroll for a DomainController certificate with request ID N/A from CA.domain.localDomain-CA (The RPC server is unavailable. 0x800706ba (WIN32: 1722)).

also along with some KDC certificate errors because the domain controller does not hold a valid domain controller certificate:

> The Key Distribution Center (KDC) cannot find a suitable certificate to use for smart card logons, or the KDC certificate could not be verified. Smart card logon may not function correctly if this problem is not resolved. To correct this problem, either verify the existing KDC certificate using certutil.exe or enroll for a new KDC certificate.

This happens when you create your CA on a Domain Controller and the "Domain Controllers" security group is missing from the "CERTSVC_DCOM_ACCESS" Domain Local Security Group.

have a look in the following post for more autoenrollment issues and how to fix'em: [http://blogs.technet.com/instan/archive/2009/12/07/troubleshooting-autoenrollment.aspx](http://blogs.technet.com/instan/archive/2009/12/07/troubleshooting-autoenrollment.aspx)

The KDC error reference: [http://technet.microsoft.com/en-us/library/cc734096%28WS.10%29.aspx](http://technet.microsoft.com/en-us/library/cc734096%28WS.10%29.aspx)
