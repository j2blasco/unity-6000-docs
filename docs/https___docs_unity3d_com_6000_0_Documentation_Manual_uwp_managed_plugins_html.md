* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-managed-plugins.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * [IL2CPP scripting backend for UWP](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-scripting.html)
  * [Use UWP plug-ins with IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-plugins.html)
  * Use managed UWP plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-plugins.html)
Use UWP plug-ins with IL2CPP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-native-plugins-call.html)
Call and implement native UWP plug-ins
# Use managed UWP plug-ins
Managed **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) are managed .NET assemblies that are managed outside of Unity and compiled into dynamically-linked libraries (DLLs). For information about how to create and use managed plug-ins, refer to [Managed plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html)A managed .NET assembly that is created with tools like Visual Studio for use in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Managedplug-in).
The **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend) exposes the same .NET API surface as the Unity Editor and standalone Player. As a result, you can use the same plug-ins and you don’t have to compile separate versions to target different .NET APIs for Universal Windows Platform (UWP).
## Additional resources
  * [Managed plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html)
  * [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html)
  * [Microsoft documentation on Managed code](https://learn.microsoft.com/en-us/dotnet/standard/managed-code)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-il2cpp-plugins.html)
Use UWP plug-ins with IL2CPP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-native-plugins-call.html)
Call and implement native UWP plug-ins
