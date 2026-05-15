---
title: Intune On-Premises Exchange Connector Log
date: 2015-10-22
categories:
- office-365
showTableOfContents: true
draft: false
---


{{< lead >}}
Just a quick note for everyone missing the log files location of Microsoft Intune On-Premises Exchange Connector, seems like there is no documentation on where those files exists. and they are very useful for debugging this component.
{{< /lead >}}

This info came from a support case I've had with the on-premises connector :)

Anyhow:

- Log files are here - C:\\ProgramData\\Microsoft\\Windows Intune Exchange Connector\\
- If you wish to enable verbose tracing for more advanced debugging do the following:

1. Open the Exchange Connector tracing configuration file. The file is located at: %ProgramData%\\Microsoft\\Windows Intune Exchange Connector\\TracingConfiguration.xml
2. Locate the TraceSourceLine with the following key: OnPremisesExchangeConnectorService
3. Change the SourceLevel node value from Warning ActivityTracing (the default) to Verbose ActivityTracing.

```xml
<TraceSourceLine>
  <Key xsi:type="xsd:string">OnPremisesExchangeConnectorService</Key>
  <Value xsi:type="TraceSource">
    <SourceLevel>All</SourceLevel>
    <Listeners>
      <Listener>
        <ListenerType>CircularTraceListener</ListenerType>
        <SourceLevel>Verbose ActivityTracing</SourceLevel>
        <FileSizeQuotaInBytes>10000000</FileSizeQuotaInBytes>
        <FileName>Microsoft\Windows Intune Exchange Connector\Logs\Connector.svclog</FileName>
        <FileQuota>30</FileQuota>
      </Listener>
    </Listeners>
  </Value>
</TraceSourceLine>
```

It is important to note that the ActivityTracing setting should remain or be included with ANY value that is set for the setting.

enjoy
