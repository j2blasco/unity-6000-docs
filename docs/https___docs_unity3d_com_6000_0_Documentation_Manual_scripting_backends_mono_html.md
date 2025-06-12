* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-mono.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
  * Mono overview


[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
Scripting backends
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)
IL2CPP Overview
# Mono overview
The **Mono**scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend)** compiles code at runtime, with a technique called just-in-time compilation (JIT). Unity uses a [fork](https://github.com/Unity-Technologies/mono) of the open source [Mono project](https://www.mono-project.com/).
Some platforms don’t support JIT compilation, so the Mono backend doesn’t work on every platform. Other platforms support JIT and Mono but not ahead-of-time compilation (AOT), and so can’t support the [IL2CPP backend](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html). When a platform can support both backends, Mono is the default. For more information, see [Scripting restrictions](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-restrictions.html).
Mono supports the debugging of managed code. For more information, see [Debugging C# code in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/managed-code-debugging.html).
## Building a project using Mono
You can change the scripting backend Unity uses to build your application in one of two ways:
  * Through the ****Player Settings** Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings)** menu in the Editor. Perform the following steps to change the scripting backend through the **Player** settings menu: 
    1. Go to **Edit** > **Project Settings**.
    2. Select **Player** to open the [Player](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html) settings for the current platform in the [Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
    3. Under the **Other Settings** sub-menu, navigate to **Configuration** > **Scripting Backend**.
    4. Select **Mono**.
  * Through the Editor scripting API. Use the [PlayerSettings.SetScriptingBackend](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetScriptingBackend.html) property to change the scripting backend that Unity uses.

![The Configuration section of the Player settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/backend-mono.png) The **Configuration** section of the **Player** settings
To start the build process, open the **Build Profiles** window (Menu: **File** > **Build Profiles**) and select **Build**.
Both the Mono and **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) scripting backends require a new build for each platform you want to target. For example, to support both the Android and iOS platforms, you need to build your application twice and produce two binary files, one for Android and one for iOS.
## Additional resources
  * [Unity .NET features](https://docs.unity3d.com/6000.0/Documentation/Manual/overview-of-dot-net-in-unity.html)
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
Scripting backends
[](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)
IL2CPP Overview
