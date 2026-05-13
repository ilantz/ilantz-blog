---
title: Windows 8 Wakes Up From Sleep or Hibernation Unexpectedly
date: 2012-12-21
categories:
- powershell
- server-2012
- windows-8
showTableOfContents: true
draft: false
---


Hi Again,

{{< lead >}}
I've upgraded my desktop to windows 8 lately and since the upgrade I've noticed that each time the computer enters sleep mode or hibernation it keeps turning on my itself mysteriously and no apparent reason.
{{< /lead >}}

Well...no more!! Here's the actual line of events that led me to the solution:

1. Went through some event viewer entries, specifically looking at Power-Troubleshooter and Kerner-General source that did not provide me with anything... {{< figure src="images/event-id-1-source-power-troubleshooter-wake-source-unknown.png" alt="Event ID 1 Source Power-Troubleshooter Wake Source Unknown" caption="Event ID 1 Source Power-Troubleshooter Wake Source Unknown" >}}
2. Double checked that no one is touching the mouse or keyboard... :)
3. Made sure that the "Allow wake timers" option is not enabled for the active power scheme {{< figure src="images/allow-wake-timers-set-to-disabled.png" alt="Allow Wake Timers Set To Disabled" caption="Allow Wake Timers Set To Disabled" >}}
4. Disabled the "Allow this device to wake up the computer" option on the network card adapter Power Management settings tab - you can query all devices that are allowed using the following command (cmd not PowerShell): `powercfg -devicequery wake_armed`{{< figure src="images/allow-this-device-to-wake-the-computer-disabled.png" alt="Allow This Device To Wake The Computer Disabled" caption="Allow This Device To Wake The Computer Disabled" >}}

Only after being frustrated again from the computer still waking up with no apparent reason I've noticed that it keeps waking up at around specific times, which led me to the conclusion that it's probably a schedule task that was waking the computer up ! Seems like there is a Media Center task names mcupdate_scheduled that was causing all the trouble !

{{< figure src="images/wake-the-computer-to-run-this-task-enabled.png" alt="Wake The Computer To Run This Task Enabled" caption="Wake The Computer To Run This Task Enabled" >}}

So, I've written a small PowerShell script to disable the "wake the computer to run this task" option from all scheduled tasks at once, and that did the trick! This script should work fine with Windows 8 or Server 2012 and might serve as an example for manipulating scheduled tasks with PowerShell.

```powershell
Get-ScheduledTask | ? { $_.Settings.WakeToRun -eq $true -and $_.State -ne "Disabled"} | % { $_.Settings.WakeToRun = $false; Set-ScheduledTask $_ }
```

Now my computer sleeps and hibernates without waking up ! ZzzzzzzZzzzzZzzzz

Additional Links:

[http://superuser.com/questions/503786/windows-8-desktop-wakes-up-immediately-after-sleep-due-to-keyboard-mouse/522628](http://superuser.com/questions/503786/windows-8-desktop-wakes-up-immediately-after-sleep-due-to-keyboard-mouse/522628 "windows 8 desktop wakes up immediately after sleep due to keyboard/mouse")

[http://www.howtogeek.com/127818/how-to-stop-windows-8-waking-up-your-pc-to-run-maintenance/](http://www.howtogeek.com/127818/how-to-stop-windows-8-waking-up-your-pc-to-run-maintenance/ "How to Stop Windows 8 Waking Up Your PC to Run Maintenance")

Ilantz
