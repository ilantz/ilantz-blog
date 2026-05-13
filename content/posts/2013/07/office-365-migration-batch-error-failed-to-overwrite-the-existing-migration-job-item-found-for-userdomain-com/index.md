---
title: Office 365 Migration Batch Error - Failed to overwrite the existing Migration
  Job Item found for "user@domain.com"
date: 2013-07-14
categories:
- office-365
showTableOfContents: true
draft: false
slug: office-365-migration-batch-error-failed-to-overwrite-the-existing-migration-job-item-found-for-userdomain-com
---



Hi Again,

{{< lead >}}
During a simple migration (cutoff) to Office 365 Exchange Online, I've encountered a few errors that prevented the migration batch to complete successfully, and wanted to share in case anyone is struggling with them.
{{< /lead >}}

- Active Directory operation failed on AMSPR01A001DC01.EURPR01A001.prod.outlook.com. The object 'CN=user,OU=tenant.onmicrosoft.com,OU=Microsoft Exchange Hosted Organizations,DC=EURPR01A001,DC=prod,DC=outlook,DC=com' already exists.

This error states that the migration batch failed to create a new object because that specific name is already taken. sadly enough the value for the CN=xxxx is taken from the alias property of the user/contact/group being migrated from the on-premise server.. and alias is **not** unique within (most) Exchange deployments.

To Solve this, work with the "alias" property value on your local AD to locate the conflicting objects, work with the results of the migration job and cross-reference until you will eliminate all duplicates of the alias values.

- Failed to overwrite the existing Migration Job Item found for "user@domain.com" [Mailbox]; the Job Item was created with different Recipient Type [Contact]. You may delete the newly created Mailbox and recreate the actual Contact for user@domain.com.

This error could be a result of your actions to fix duplicates issues, if for some reason the migration batch started with user@domain.com being a contact and that object has changed it will fail to "update/sync" and will continue to expect the original object type which was different in this example a contact.

To solve this [Connect to Exchange Online Using Remote PowerShell](http://technet.microsoft.com/en-us/library/jj984289%28v=exchg.150%29.aspx) and work with two commands - Get-MigrationUser and Remove-MigrationUser to remove the incorrect object from the migration batch and then resume it. This will make sure the new (correct) object will be synced successfully. Here's an example of how to use these commands:

`Get-MigrationUser -Identity User@Domain.com | FL`

Notice the output here and make sure this is indeed the incorrect object that needs to be removed, and then pipe the output to remove that user from the Migration Batch:

```powershell
Get-MigrationUser -Identity User@Domain.com | Remove-MigrationUser
```

Once removed, you can resume the migration again and it should now sync correctly your mailboxes.

Hope this helps !

ilantz
