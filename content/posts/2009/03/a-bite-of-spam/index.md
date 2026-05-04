---
title: A bite of spam
date: 2009-03-04
categories:
- misc
showTableOfContents: true
draft: false
---


{{< lead >}}
Thought I should post this to share some info and maybe even provide a simple FAQ and some basic info on how to fight the world's true evil.
{{< /lead >}}

unsolicited bulk e-mail messages...   SPAM

for start if you want some background and some basic info on what/how/why and such..i would reference you to [spamfaq.net (archive)](http://www.lumbercartel.ca/archives/spamfaq.net/) , once you are familiar with some basics terms and such, you would probably want to start and impalement (if not already) some anti-spam methods , either choose a 3rd party application for this, an hardware based relay all-in-on solution etc..

most simple solutions are rather a mail relay , with some kind of software which does a bunch of tests and lookups about the incoming message and content to measure its validity.. and so on .. my anti-spam ninja skills are mostly based with some exchange servers that either didn't implement anything other then an exchange server which is receiving mail directly from the internet, running an anti-virus solution of some kind..

I usually follow these few steps and the outcome is less SPAM being processed by the mail server , that is blocked on session connect.

1\. [Whois](http://en.wikipedia.org/wiki/WHOIS) information about each and every domain which is being used for outbound email is valid and as possible updated with relevant internal contact.

2\. Add SPF information about each and every domain which is being used for outbound email. (i define that a Fail response = reject message)

3\. Register your domains with [Sender-ID](http://www.microsoft.com/mscorp/safety/technologies/senderid/default.mspx) , the microsoft "spf" framework. (i define that a Fail response = reject message)

4\. Enable the use of DNS RBL (real time block list) provider as a first method to filter out the bad guys. this will drop most evil right here.

5\. Add SURBL, suppress sending out NDR/Out-of-Office & any other method / product you may want to use.. anti-spam is not a set-and-forget matter. you will need to take care of every solution you might choose , find dropped messages and troubleshoot false-positives and etc.. don't do any short cuts.

DNS RBL's

Choose carefully the provider which suites you and of course make sure your mail system supports using a DNS RBL look-up, most mail gateways allow this built in or either with a 3rd party add-on, for instance exchange 2003 sp2/2007 supports this built-in, so make sure you verify this. also make sure you are setting the correct RBL with the correct response code from him. that is of course so you will not just turn on blocking all your incoming email traffic :) a great compare of the major DNS RBL providers is updated weekly @ [http://www.sdsc.edu/~jeff/spam/cbc.html](http://www.sdsc.edu/~jeff/spam/cbc.html)

SURBL

another great method to even more enhance your blocking of spam is by using SURBL - "..SURBLs list web sites found in unsolicited message bodies. Those domains can be used to detect future unsolicited messages advertising the same sites. In contrast, most other lists have the IP addresses or domain names of unsolicited message senders, open relays, open proxies, etc. " [http://www.surbl.org/](http://www.surbl.org/)

because I cannot really cover it all here , here's some links to further info, utils and more..

[The anti-spam portal](http://spamlinks.net/index.html) - Super site. all over.

[DNSBL Resource](http://www.dnsbl.com/) News,info,rating's of DNSBL's and more.

[ORFilter](http://martijnjongen.com/site/) freeware , allowing microsoft smtp server to use RBLs and more.
