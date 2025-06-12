* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-project-and-aar-plugins-introducing.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Developing for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-developing.html)
  * [Create and use plug-ins in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/PluginsForAndroid.html)
  * [Android plug-in types](https://docs.unity3d.com/6000.0/Documentation/Manual/android-plugin-types.html)
  * [Android Library and Android Archive plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html)
  * Introducing Android Library and Android Archive plug-ins


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html)
Android Library and Android Archive plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-plugin-create.html)
Create an Android Library plug-in
# Introducing Android Library and Android Archive plug-ins
Android Archives are a compiled version of Android Libraries, and are the recommended way to format plug-ins that you want to distribute. However, while you create a **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), it’s faster to work with the Android Library format since that doesn’t require you to compile the plug-in outside of Unity and re-import the result. If you plan to modify the plug-in at all in the future, or want to iterate over it often, use an Android Library. After you finish development for the plug-in, compile it into an Android Archive.
## Android Library plug-ins
An Android Library is a directory with a specific structure that contains all the plug-in assets and the manifest.
When Unity creates the final **Gradle** An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) project during the build or export process, it automatically includes all Android Library plug-ins in it and builds them together. Unity does this in the same way that Android Studio projects build when they have multiple subprojects.
## Android Archive plug-ins
An Android Archive (AAR) plug-in is a compiled version of an Android Library plug-in that you can use as a dependency for an Android app module. The `.aar` file itself is a `.zip` archive that contains all the compiled code, assets, and plug-in manifest. For more information on the structure of an AAR, refer to [Anatomy of an AAR file](https://developer.android.com/studio/projects/android-library.html#aar-contents).
## Providing additional Android Assets and resources
If you need to add Assets to your Unity application that should be copied as they are into the output package, include the raw assets in an Android Library plug-in or AAR. To access these assets, call the [getAssets](https://developer.android.com/reference/android/content/res/Resources.html#getAssets\(\)) Android API from your Java code.
## Additional resources
  * [Create an Android Library plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-plugin-create.html)
  * [Import an Android Library plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-project-import.html)
  * [Import an Android Archive plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/android-aar-import.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AndroidAARPlugins.html)
Android Library and Android Archive plug-ins
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-plugin-create.html)
Create an Android Library plug-in
