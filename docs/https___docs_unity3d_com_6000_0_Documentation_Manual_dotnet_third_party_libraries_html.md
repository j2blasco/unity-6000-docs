* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
  * Third-party .NET libraries


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html)
.NET system libraries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html)
Referencing additional class library assemblies
## Third-party .NET libraries
You should only use third-party .NET libraries that have been extensively tested on a wide range of Unity configurations and platforms.
The performance characteristics of just-in-time (JIT) and ahead-of-time (AOT) code paths in third-party libraries might be significantly different. AOT generally reduces startup times and is suited to larger applications for this reason but increases the binary file size to accommodate the compiled code. AOT also takes longer to build during development.
JIT adjusts at runtime based on the platform it’s running on, which can increase running performance at the cost of a potentially longer application startup time. As such, you should profile your application in both the Editor, and on your target platform. For more information, see [Profiler overview](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html).
You should profile the usage of your .NET system libraries on all target platforms because their performance characteristics might vary depending on the **scripting backends** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend), .NET versions, and profiles you use.
When you review a third-party library, consider the following areas:
  * Compatibility: Third-party libraries might not be compatible with some Unity platforms and scripting backends.
  * Performance: Third-party libraries might have vastly different performance characteristics in Unity compared to other .NET runtimes.
  * AOT binary size: Third-party libraries might increase AOT binary size significantly because of the number of dependencies the library uses.


## Additional resources
  * [.NET Profile Support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html).
  * [.NET System libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html).
  * [Referencing additional class library assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html)
.NET system libraries
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html)
Referencing additional class library assemblies
