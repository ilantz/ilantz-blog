---
title: Schema updates docs for Exchange 2010 SP2 are here !
date: 2011-11-18
categories:
- exchange-2010
showTableOfContents: true
draft: false
---


Hey !

{{< lead >}}
Great stuff coming with Exchange 2010 SP2, along with features already mentioned at the Exchange Team Blog - [Announcing Exchange 2010 Service Pack 2](http://blogs.technet.com/b/exchange/archive/2011/05/17/announcing-exchange-2010-service-pack-2.aspx) , a major schema update will support some new stuff.
{{< /lead >}}

Quoting Michal smith's blog, here's some key points to mention:

1. The Mail-Recipient class has now gained the Company and Department attributes.
    
    This means that Groups (both security groups and distribution groups) and Contacts (mail contacts) can now be assigned values to the Company and Department attributes.
    
    From a technical perspective, the Mail-Recipient class is a system auxiliary class, for both the Group and Contact classes, and all attributes present in Mail-Recipient are available in them.
    
2. The ms-Exch-Custom-Attributes class has gained **35 new custom attributes**, from ms-Exch-Extension-Attribute-16 to ms-Exch-Extension-Attribute-45, and ms-Exch-Extension-Custom-Attribute-1 through ms-Exch-Extension-Custom-Attribute-5.
    
    This means that Contacts, Groups, Users, Public Folders, Dynamic Distribution Lists, and Recipient Policies all now have a huge number of new attributes that can be assigned arbitrary values by an organization. This is welcome news to organizations who are using many or most of the current custom attributes and are wary to extend the schema themselves.
    
    From a technical perspective, the ms-Exch-Custom-Attributes class is an auxiliary class for all the named classes above.
    
3. Many new attributes and classes were added to provide support for Address Book Policies and to enhance access to various address lists, global address lists, and offline address lists maintained by Exchange.
    
    The master class is ms-Exch-Address-Book-Mailbox-Policy.
    
4. There are several new attributes and one new class (ms-Exch-Coexistence-Relationship) that are probably designed to support the Hybrid Coexistence Wizard and to overall simplify the process of configuring hybrid coexistence with Exchange Online.
    
5. There is a new class (ms-Exch-ActiveSync-Device-Autoblock-Threshold) and a number of new attributes that are within that class that appear to be designed to support automatic throttling of ActiveSync devices.
    

Read on: [A Somewhat Detailed Look at Exchange 2010 Service Pack 2 Schema Changes](http://theessentialexchange.com/blogs/michael/archive/2011/11/06/a-somewhat-detailed-look-at-exchange-2010-service-pack-2-schema-changes.aspx)

Have a great weekend!
