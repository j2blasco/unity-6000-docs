* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-scripts.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStore.html)
  * [Develop for Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-developing.html)
  * WinRT API in C# scripts for UWP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-debug-generated-cpp.html)
Debug generated C++ code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-appcallbacks.html)
AppCallbacks class reference
# WinRT API in C# scripts for UWP
Unity includes Windows Runtime (WinRT) support when building for Universal Windows Platform with the [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) scripting backend. Use Windows Runtime support to call into both native system Windows Runtime APIs as well as custom .winmd files directly from managed (C#) **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) and plugins.
Unity automatically references Windows Runtime APIs such as `Windows.winmd` on Universal Windows Platform. To use custom .winmd files, import them into your Unity project folder together with any accompanying DLLs and configure them. For more information, refer to [Import and configure plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-in-inspector.html).
To use WinRT API in your Unity scripts:
  * Your scripts must be written in C#.
  * All the code that uses WinRT API must be under the `ENABLE_WINMD_SUPPORT` [directive](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html). This is necessary because the Editor uses [Mono](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-mono.html)A scripting backend used in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mono), which doesn’t support WinRT APIs.


The following code example gets an advertising ID using WinRT API directly:
```
using UnityEngine;
public class WinRTAPI : MonoBehaviour
{
    void Update()
    {
        auto adId = GetAdvertisingId();
        // ...
    }

    string GetAdvertisingId()
    {
        #if ENABLE_WINMD_SUPPORT
            return Windows.System.UserProfile.AdvertisingManager.AdvertisingId;
        #else
            return "";
        #endif
    }
}

```

## Additional resources
  * [Windows build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStandaloneBinaries.html)
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend)
  * [Microsoft documentation on WinRT APIs with Unity for HoloLens](https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/using-the-windows-namespace-with-unity-apps-for-hololens)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/uwp-debug-generated-cpp.html)
Debug generated C++ code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-appcallbacks.html)
AppCallbacks class reference
