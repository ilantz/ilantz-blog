---
title: Troubleshooting Windows Task Scheduler
date: 2008-09-28
categories:
- misc
showTableOfContents: true
draft: false
---


{{< lead >}}
Had a nice issue with this, a few tasks were set to run on a server, running .bat files.
{{< /lead >}}

okay so ? all simple till now ;)

here's what i found:

1 - the task was set to run under a specific user.

2 - that user was given "Log on as a batch job" security assignment on that server.

3 - the bat was failing to start in task scheduler.

4 - there were other jobs , running VBS and running okay !

now .. i've scratched my head a bit a found this great article about how to toubleshoot:

[http://www.shijaz.com/windows/taskscheduler.htm](http://www.shijaz.com/windows/taskscheduler.htm) a great article , check it out ! the site also has some great stuff for ISA Server & Exchange if you into it..

in section 2.b it referenced my **Part 1 solution**, the bat file had a reference to a MAPPED drive ! **running non-interactive = no mapped drives.**

**Part 2 solution**

going back to point 4 , i've figured its a security issue , although the user had the "log on as batch job" right .. CMD.EXE was manually edited with security permissions, BUILTINBATCH group was missing the read/execute security permission on it.

There .. now it works :)
