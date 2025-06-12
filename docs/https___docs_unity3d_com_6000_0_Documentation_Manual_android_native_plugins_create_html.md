* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-create.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * [Native plug-ins for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidNativePlugins.html)
  * Create a native plug-in for Android


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-introducing.html)
Introducing native plug-ins for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-import.html)
Import a native plug-in for Android
# Create a native plug-in for Android
To compile a C++ **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) for Android, use the [Android NDK](https://developer.android.com/ndk/index.html) and familiarize yourself with the steps required to build a shared library or a static library.
If you use C++ to implement the plug-in, you must declare with C linkage to avoid [name mangling issues](http://en.wikipedia.org/wiki/Name_mangling). By default, only C source files that have a .c file extension in the plug-ins have C linkage (not C++).
```
extern "C" {
  float Foopluginmethod ();
}

```

**Note** : If your static library isn’t compiled with `-fno-exceptions` and `-fno-rtti` flags, compatibility issues might cause application build failure.
## Additional resources
  * [Import a native plug-in for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-import.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-introducing.html)
Introducing native plug-ins for Android
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-native-plugins-import.html)
Import a native plug-in for Android
