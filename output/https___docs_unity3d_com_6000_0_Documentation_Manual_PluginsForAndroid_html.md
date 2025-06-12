* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * Create and use plug-ins in Android


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-large-screen-and-foldable-support.html)
Large screen and foldable device support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
Android plug-in types
# Create and use plug-ins in Android
You can use plug-ins to deliver resources and call Java and C++ code created outside of Unity from your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts). They enable you to access features, like third-party code libraries and operating systems calls, that would otherwise not be available to Unity. For more information about plug-ins with Unity, see [Plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in).
This section describes how to create your own plug-ins and use them in Android projects. The information on these pages assumes you already know how to create native plug-ins for Unity. For more information about native plug-ins and their uses, see [Native plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in).
**Topic** | **Description**  
---|---  
[Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html) | Understand the different plug-in types available for Unity Android applications.  
[Call Java and Kotlin plug-in code from C# scripts](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugins-java-code-from-c-sharp.html) | Interact with Java and Kotlin plug-in code from your C# scripts.  
## Unity as a Library
If you upgrade your project to Unity 2019.4 or above, the introduction of Unity as a Library might require you to adapt your [native](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html) and [managed](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-managed.html) plug-ins to work properly for Android.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-large-screen-and-foldable-support.html)
Large screen and foldable device support
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
Android plug-in types
