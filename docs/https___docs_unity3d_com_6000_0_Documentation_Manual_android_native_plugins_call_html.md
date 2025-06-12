* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-call.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * [Native plug-ins for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidNativePlugins.html)
  * Call native plug-in for Android code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-import.html)
Import a native plug-in for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html)
Java and Kotlin source plug-ins
# Call native plug-in for Android code
The process to call code in native **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) for Android is the same as standard [native plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins-native.html)A platform-specific native code library that is created outside of Unity for use in Unity. Allows you can access features like OS calls and third-party code libraries that would otherwise not be available to Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Nativeplug-in).
**Note** : If you use individual C/C++ source files as plug-ins, use `__Internal` as the plug-in name in the [DllImport](https://docs.microsoft.com/en-us/dotnet/api/system.runtime.interopservices.dllimportattribute) attribute.
It’s best practice to wrap all native plug-in method calls with an additional C# code layer that:
  * Checks [Application.platform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Application-platform.html) and only calls native methods when the application is running on Android devices using the architecture that you compiled the native plug-in for. On other platforms and architectures, the additional C# code layer should return dummy values.
  * Uses [platform defines](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html) to control platform dependent code compilation and only compile code that uses the plug-in on platforms that have the plug-in available.


## Sample package
The [AndroidNativePlugin.unitypackage](https://docs.unity3d.com/6000.0/Documentation/uploads/Examples/AndroidNativePlugin.zip) zip file contains a simple example of a native code plug-in distributed as a Unity package.
The sample shows how to invoke C++ code from a Unity application. The package includes a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) which displays the sum of two values as calculated by a native plug-in. To compile the plug-in, use [Android NDK](https://developer.android.com/ndk/index.html). For information on how to install Android NDK via the Unity Hub, see [Android environment setup](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html).
To install the sample:
  1. Download the zip file.
  2. Extract the `AndroidNativePlugin.unitypackage` file.
  3. In a Unity project, click **Assets** > **Import Package** > **Custom Package**.
  4. In the **Import Package** file dialog, find and select the extracted `AndroidNativePlugin.unitypackage` file.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-import.html)
Import a native plug-in for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidJavaSourcePlugins.html)
Java and Kotlin source plug-ins
