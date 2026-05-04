---
title: Lesson learned on PowerShell Modules
date: 2015-06-22
categories:
- powershell
showTableOfContents: true
draft: false
---


{{< lead >}}
Quick note, make sure you **do not forget to modify** your **PSModulePath** system variable when installing a new PowerShell module...
{{< /lead >}}

Quoting from [Installing Modules](https://msdn.microsoft.com/en-us/library/dd878350%28v=vs.85%29.aspx):

> **Effect of Incorrect Installation**
> 
> If the module is not well-formed and its location is not included in the value of the **PSModulePath** environment variable, basic discovery features of Windows PowerShell, such as the following, do not work.
> 
> - The Module Auto-Loading feature cannot import the module automatically.
> - The _ListAvailable_ parameter of the Get-Module cmdlet cannot find the module.
> - The Import-Module cmdlet cannot find the module. To import the module, you must provide the full path to the root module file or module manifest file.

In my case, I've noticed that because I did **not** modified the PSModulePath system variable, a schedule task of the PowerShell script using that module failed to import the module.... the fun part was that running it in Interactive Mode (while being logged in to the server) actually worked...

Learn from the mistakes of others...
