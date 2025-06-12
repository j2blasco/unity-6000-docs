* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Cross-platform features and considerations](https://docs.unity3d.com/6000.0/Documentation/Manual/cross-platform-features.html)
  * Using Unity as a Library in other applications


[](https://docs.unity3d.com/6000.0/Documentation/Manual/CrossPlatformConsiderations.html)
Troubleshooting common cross-platform issues
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html)
Deep linking
# Using Unity as a Library in other applications
Unity as a Library is intended for specialist users who use native platform technologies such as Java/Android, Objective C/iOS, or Windows Win32/UWP, and want to include Unity-powered features in their games or applications.
This documentation assumes that you have experience with developing for native platform technologies such as Java/Android, Objective C/iOS, or Windows Win32/UWP, and that you are familiar with the structure of the project, language features and specific platform configuration options (for example, user permissions).
You can use Unity as a Library in other applications by integrating your content and the Unity runtime components in a native platform project. This enables you to embed content that uses 3D or 2D real-time rendering, like **AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) experiences, interaction with 3D models, and 2D mini-games. The Unity Runtime Library exposes ways to manage loading, activating, and unloading within the native application.
The following platforms currently support Unity as a Library:
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Android.html)
  * [iOS](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-iOS.html)
  * [Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Windows.html) and [Universal Windows Platform](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-UWP.html)


To determine platform versions and other dependencies, see the [system requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html) page.
## Limitations
When hosted by another application, Unity doesn’t control the runtime lifecycle, so it might not work in all scenarios. Known limitations include:
  * On Android and iOS: 
    * Only full-screen rendering is supported. However, if you are a Unity Industry customer, the limitations and features might differ.
    * When Unity is in an unloaded state (after calling [`Application.Unload`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Unload.html)), it retains some amount of memory (between 80–180Mb) to be able to instantly switch back and run again in the same process. The amount of memory that’s not released largely depends on the device’s graphics resolution.
  * On iOS, if the Unity runtime quits entirely (after calling [`Application.Quit`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application.Quit.html)), it’s not possible to reload Unity again in the same app session.
  * You can’t load more than one instance of the Unity runtime, or integrate more than one Unity runtime.
  * You might need to adapt your [native](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html) and [managed](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html) **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) to work properly.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/CrossPlatformConsiderations.html)
Troubleshooting common cross-platform issues
[](https://docs.unity3d.com/6000.0/Documentation/Manual/deep-linking.html)
Deep linking
