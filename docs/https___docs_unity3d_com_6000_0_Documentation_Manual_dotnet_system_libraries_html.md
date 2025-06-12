* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-system-libraries.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Environment and tools](https://docs.unity3d.com/6000.0/Documentation/Manual/environment-and-tools.html)
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
  * .NET system libraries


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html)
.NET profile support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html)
Third-party .NET libraries
# .NET system libraries
Unity supports many platforms and might use different scripting back ends depending on the platform. The .NET system libraries require platform-specific implementations to work correctly in some cases. While Unity tries its best to support as much of the .NET ecosystem as possible, there are some exceptions to parts of the .NET system libraries that Unity explicitly doesn’t support.
Unity makes no performance or allocation guarantees for the .NET system libraries across Unity versions. Generally, Unity doesn’t fix any performance regressions in the .NET system libraries.
Unity doesn’t support the [System.Drawing](https://learn.microsoft.com/en-us/dotnet/api/system.drawing?view=net-8.0) library and it isn’t guaranteed to work on all platforms.
The JIT compilation that the Mono **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend) uses enables you to emit dynamic C#/.NET Intermediate Language (IL) code generation during the runtime of your application. The **AOT compilation** Ahead of Time (AOT) compilation is an optimization method used by all platforms except iOS for optimizing the size of the built player. . [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone-playerSizeOptimization.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AOTCompilation) that the **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) scripting back end uses doesn’t support dynamic code generation.
This is important to consider when you use third-party libraries, because they might have different code paths for just-in-time (JIT) and ahead-of-time (AOT), or they might use code paths that rely on dynamically generated code. For more information on how to generate code at runtime, refer to Microsoft’s [ModuleBuilder](https://docs.microsoft.com/en-us/dotnet/api/system.reflection.emit.modulebuilder?view=netcore-3.1) documentation.
Although Unity supports multiple .NET API profiles, you should use the .NET Standard [API Compatibility Level](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApiCompatibilityLevel.html) for all new projects for the following reasons:
  * .NET Standard is a smaller API surface and so has a smaller implementation. This reduces the size of your final executable file.
  * .NET Standard has better cross-platform support, so your code is more likely to work across all platforms.
  * All .NET runtimes support .NET Standard, so your code works across more VM/runtime environments (for example, .NET Framework. .NET Core, Xamarin, Unity) when you use .NET Standard.
  * .NET Standard moves more errors to compile time. A number of APIs in .NET Framework are available at compile time, but have implementations on some platforms that throw an exception at runtime.


Other profiles can be useful if, for example, you need to provide support for an older existing application. To change the **Api Compatibility Level** setting, go to **Edit** > **Project Settings** > **Player**. Under the **Other Settings** heading, set the **Api Compatibility Level** to the desired setting.
## Additional resources
  * [.NET Profile Support](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html).
  * [Third-party .NET libraries](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-support.html)
.NET profile support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-third-party-libraries.html)
Third-party .NET libraries
