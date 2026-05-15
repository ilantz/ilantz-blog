---
title: High Resolution User Photo Synchronization to Office 365
date: 2015-11-17
categories:
- azure-ad
- office-365
showTableOfContents: true
draft: false
coverImage: fb-img.14279915541.jpg
---


{{< lead >}}
There are some known limitation and inconsistency with user photos synchronization from Active Directory (using the thumbnailPhoto attribute) to Azure AD and Office 365 apps: Exchange, SharePoint and Skype for Business (aka Lync), specifically if you want to upload high resolution photos of your users that will span across all of Office 365 services.
{{< /lead >}}

After spending some research time around this issue, here are my findings:

- "High Resolution" in our context is a 648 x 648 pixel dimension size **JPEG** photo
- The Active Directory [thumbnailPhoto attribute](https://msdn.microsoft.com/en-us/library/cc221395.aspx) value is limited to about 100KB in size - this will mostly prevent you from uploading a "high resolution" photo
- "Common knowledge" around synchronizing the thumbnailPhoto using Directory Synchronization (aka DirSync / AAD Sync/ AAD Connect) to Office 365 / Azure AD is that the attribute should not exceed 10KB, and the recommended photo dimension is 96 x 96 pixels - This is really an "Exchange" limit as far as I know..
    - [List of attributes that are synced by the Azure Active Directory Sync Tool](http://social.technet.microsoft.com/wiki/contents/articles/19901.dirsync-list-of-attributes-that-are-synced-by-the-azure-active-directory-sync-tool.aspx) aka [KB 2256198](https://support.microsoft.com/en-us/kb/2256198)
    - [Office 365: thumbnailPhoto - Obtaining Photo Sizes from Active Directory](https://gallery.technet.microsoft.com/office/Office-365-thumbnailPhoto-e2755b03)
- When User Photos are stored within Office 365 a web service handles requests for the photo with predefined allowed sizes for example - https://outlook.office365.com/owa/service.svc/s/GetPersonaPhoto?email=emailaddress@domain.com&size=HR648x648
    - Modify this to your email address to try this out
    - There are quite a few possible sizes, try for example 96x96 and 240x240 to get the idea
- SharePoint holds a separate location and also a few versions for it's images within each users profile folder and is **suppose** to synchronize those from Exchange Web Services
    - See this post for additional details around SharePoint - [Options for SharePoint User Profile Properties and Photos](http://blogs.msdn.com/b/briangre/archive/2014/03/11/options-for-sharepoint-user-profile-pictures.aspx)
- The Set-UserPhoto cmdlet from Exchange (Online **and** On-Prem) allows you to save high resolution photos, and integrates with Skype for Business Server 2015 (also for Lync 2013) and SharePoint 2013/2016 - each product with it's own flow which I'm not going into explaining.
    - See [Configure the use of high-resolution photos in Skype for Business Server 2015](https://technet.microsoft.com/en-us/library/jj688150.aspx)
    - SharePoint part is covered at [Options for SharePoint User Profile Properties and Photos](http://blogs.msdn.com/b/briangre/archive/2014/03/11/options-for-sharepoint-user-profile-pictures.aspx)

So to summarize at this point, we want to import high resolution photos to our users. If we rely on the thumbnailPhoto attribute value from Active Directory, we will end up with low resolution images (needs more JPEG effect) or inconsistent results if we look on the SharePoint case.

To upload high resolution photos to Office 365, you should use [Set-UserPhoto](https://technet.microsoft.com/en-us/library/jj218694%28v=exchg.160%29.aspx). This approach works great for Exchange Online, Skype for Business and Azure AD. Although promising, my testing (and others..) showed that if your users' photos were previously synced to SharePoint Online - they will not necessarily be updated using this method.

Here is my take on solving this, in a somewhat chronological order:

1. If you need your on-premises thumbnailPhoto attribute populated, keep your current practice of maintaining them.
    1. To avoid future inconsistencies - use "Azure AD app and attribute filtering" to **filter out** thumbnailPhoto using Azure AD Connect - [Custom installation of Azure AD Connect](https://azure.microsoft.com/en-us/documentation/articles/active-directory-aadconnect-get-started-custom)
2. Utilize the [Set-UserPhoto](https://technet.microsoft.com/en-us/library/jj218694%28v=exchg.160%29.aspx) cmdlet in Exchange Online PowerShell to upload your users high resolutions (648x648 px) photos
    1. Note [Uploading High Resolution Photos using PowerShell for Office 365](http://blogs.technet.com/b/cloudtrek365/archive/2014/12/31/uploading-high-resolution-photos-using-powershell-for-office-365.aspx) to workaround - “The remote server returned an error: (413) Request Entity Too Large” error if you get this.
3. To upload your users high resolution photos to SharePoint online use the [Core.ProfilePictureUploader](https://github.com/OfficeDev/PnP/tree/master/Samples/Core.ProfilePictureUploader) sample app from the OfficeDev PnP GitHub repo.
    1. To make this easier to non coders :) I've complied the code sample for your usage - [http://ilantz.com/files/Core.ProfilePictureUploader.zip](http://ilantz.com/files/Core.ProfilePictureUploader.zip)
        1. Get the source code here and also make sure to **read the FAQ** - [https://github.com/OfficeDev/PnP/tree/master/Samples/Core.ProfilePictureUploader](https://github.com/OfficeDev/PnP/tree/master/Samples/Core.ProfilePictureUploader)
        2. Follow the explanations in the GitHub page link above around how to run the utility (configuration.xml , the CSV input file and the command syntax).
        3. Make sure your pictures are JPEG files...
    2. This sample app is also documented here, with some additional explanations - [Upload user profile pictures sample app for SharePoint](https://msdn.microsoft.com/en-us/library/office/dn894691.aspx)

That's it !

Hope this helps anyone, please comment if it did.

ilantz
