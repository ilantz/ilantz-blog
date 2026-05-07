---
title: SSLChainSaver v2 - Save root certificate (and chain), the super easy way.
date: 2008-09-07
categories:
- pki
showTableOfContents: true
draft: false
slug: sslchainsaver-v2-save-root-certificate-and-chain-the-super-easy-way
---



{{< lead >}}
Well , not much to say here, read the awesome tool.
{{< /lead >}}

you need to distribute your SSL root chain , which some times more then one certificate ,and make sure your mobile likes this ..

you can use this tool to **save the whole ssl chain , and verify** if the chain is indeed presented by the web site correctly , this might some an issue too, because sometimes the server does not hold the whole chain but just the main ROOT CA public key..this helps very easy to troubleshoot it. and distribute your files easly.

[http://blogs.msdn.com/windowsmobile/archive/2008/05/18/sslchainsaver-v2-released.aspx](http://blogs.msdn.com/windowsmobile/archive/2008/05/18/sslchainsaver-v2-released.aspx "http://blogs.msdn.com/windowsmobile/archive/2008/05/18/sslchainsaver-v2-released.aspx")

- The tool can detect a common name mismatch on the cert but it doesn't parse the "SubjectAltNames" extension. If your certificates are using SubjectAltNames, the tool will report a name mismatch but the certs will really work fine.

i dont find that super problematic thu :) i just wanna save it.
