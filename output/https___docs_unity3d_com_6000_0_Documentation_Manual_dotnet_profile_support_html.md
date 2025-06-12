* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
  * .NET profile support


[](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
Unity .NET features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html)
.NET system libraries
# .NET profile support
Unity supports two .NET profiles: **.NET Standard** and **.NET Framework**. Each profile provides a different set of APIs so that C# code can interact with .NET class libraries. The **Api Compatibility Level** property has two settings:
  * **.NET Standard 2.1** : .NET Standard 2.1, as published by the .NET Foundation.
  * **.NET Framework** : .NET Framework 4.8, as published by Microsoft, plus additional APIs in .NET Standard 2.1.


By default, the **Api compatibility Level** is set to **.NET Standard 2.1**. To change the .NET profile, go to **Edit** > **Project Settings** > **Player** >**Other settings**. Under the Configuration heading, set **Api Compatibility Level** to the desired setting.
## Cross-platform compatibility
If you need broad cross-platform compatibility, then set the **Api Compatibility Level** to **.NET Standard 2.1**. Where possible, Unity supports the APIs in the **.NET Standard 2.1** profile on all platforms. Although some platforms don’t fully support the **.NET Standard 2.1** profile, the **.NET Framework** profile is less suitable for cross-platform compatibility. The **.NET Framework** profile includes all APIs in the **.NET Standard 2.1** profile and additional APIs, some of which might work on few or no platforms.
## Managed plug-ins
[Managed plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html)A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Managedplug-in) are .NET assemblies that are managed outside of Unity and compiled into dynamically linked libraries (DLLs). You can use managed **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) in Unity with either the **.NET Standard 2.1** profile or the **.NET Framework** profile. The .NET profile of your Unity project determines the level of support for managed plug-ins that are compiled for different versions of .NET. The following table indicates the configurations that Unity supports:
**Managed plug-in compilation target** | **.NET Standard 2.1** | **.NET Framework 4.x**  
---|---|---  
**.NET Standard (any version)** | Supported | Supported  
**.NET Framework (any version)** | Limited support | Supported  
**.NET Core (any version)** | Not Supported | Not Supported  
Support for managed plug-ins compiled for .NET Framework is limited when you use the **.NET Standard 2.1** profile in Unity. Any .NET Framework APIs that are also present in .NET Standard are supported. However, the **.NET Framework** API contains types and methods that are not available in the **.NET Standard 2.1** profile.
## Transport Layer Security (TLS) 1.2
The UnityWebRequest API and all .NET Framework Web APIs fully support TLS 1.2 on all platforms except Web. The Web platform uses the security settings from the browser the application runs in and the web server instead. The platform-specific local certificate store automatically verifies TLS certificates if available. If access to the certificate store isn’t possible, Unity uses an embedded root certificate store.
## Additional resources
  * [.NET System libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html).
  * [Third-party .NET libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
Unity .NET features
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html)
.NET system libraries
