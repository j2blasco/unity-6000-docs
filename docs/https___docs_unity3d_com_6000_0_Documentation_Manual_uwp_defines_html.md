* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-defines.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * UWP scripting symbols


[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-profiler.html)
Connect the profiler to UWP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-scripting.html)
IL2CPP scripting backend for UWP
# UWP scripting symbols
Unity has a range of built-in scripting symbols which represent options that you can use in your **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) to selectively include or exclude portions of code from compilation. For more information on conditional compilation, refer to [Conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
**Note:** You can also refer to scripting symbols can as define symbols, preprocessor defines, or defines.
Unity automatically defines these scripting symbols for Universal Windows Platform (UWP):
**Scripting symbol** | **Description**  
---|---  
`UNITY_WINRT` | Defined on all scripts.  
`UNITY_WSA` | Defined on all scripts.  
`UNITY_WINRT_10_0` | Defined on all scripts.  
`UNITY_WSA_10_0` | Defined on all scripts.  
`ENABLE_IL2CPP` | Defined on all scripts when using **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend).  
`WINDOWS_UWP` | Defined on all scripts when building for UWP.  
`ENABLE_WINMD_SUPPORT` | Defined on all scripts when building for UWP.  
## Additional resources
  * [Conditional compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html)
  * [Custom scripting symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-scripting-symbols.html)
  * [Microsoft documentation on C# preprocessor directives](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/preprocessor-directives)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-profiler.html)
Connect the profiler to UWP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-scripting.html)
IL2CPP scripting backend for UWP
