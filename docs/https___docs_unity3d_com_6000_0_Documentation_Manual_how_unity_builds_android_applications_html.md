* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Introducing Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-introducing.html)
  * How Unity builds Android applications


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html)
Unity Library Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
Getting started with Android
# How Unity builds Android applications
Unity uses [Gradle](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)An Android build system that automates several build processes. This automation means that many common build errors are less likely to occur. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gradle) to build Android applications so it’s useful to understand the build process and how Unity interacts with Gradle. Gradle lets you use [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) and other Unity windows to configure most aspects of the final build, however for more control, you must overwrite [manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)There are two types of manifest files: **project manifest****s** and **package manifest****s**.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Manifest) and [template](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html) files, or export your project and edit it in [Android Studio](https://developer.android.com/studio/index.html).
## The build process
To build Android applications:
  1. Unity calls [AndroidProjectFilesModifier.Setup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html) for all [AndroidProjectFilesModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html) interfaces. You can use this callback to set up prerequisites for modifying custom Android Gradle project files. For more information, refer to [AndroidProjectFilesModifier.Setup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.Setup.html).
  2. Unity collects project resources, code libraries, **plug-ins** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in), Gradle templates, and manifest templates from your Unity project and uses them to create a valid Gradle project.
  3. Unity adds and updates values inside Gradle templates and manifest files based on the Unity project’s Player settings and build settings.
  4. If you chose to export the project and not build it, and use the **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) [scripting backend](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend), Unity places C++ source files produced from your C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) into the Gradle project. Otherwise, if you chose to build the project, Unity places the `libil2cpp.so` library into the Gradle project.
  5. Unity calls [OnModifyAndroidProjectFiles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.OnModifyAndroidProjectFiles.html) for all [AndroidProjectFilesModifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.AndroidProjectFilesModifier.html) interfaces. You can use this callback to modify Gradle project file values. For more information, refer to [Modify Gradle project files with the Android Project Configuration Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-agp.html).  
**Note** : You can modify Android Gradle project files in custom modules only.
  6. Unity calls [OnPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.OnPostGenerateGradleAndroidProject.html) for all [IPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.html) interfaces. You can use this callback to modify or move files before Gradle builds the application.
  7. Unity runs Gradle to build the application from the Gradle project. Gradle merges the Unity Library Manifest, Unity Launcher Manifest, and plug-in manifests into one [Android App Manifest](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html) file.


## Incremental build pipeline
Unity uses the [incremental build pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html) when it builds the Player for Android. See the following Android-specific incremental build pipeline behaviors:
  * Unity incrementally builds/generates: 
    * [Gradle files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-gradle-overview.html)
    * [Manifest files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-manifest.html)
    * [Assets packs](https://docs.unity3d.com/6000.0/Documentation/Manual/play-asset-delivery.html)
    * [APK expansion files (obbs)](https://docs.unity3d.com/6000.0/Documentation/Manual/android-OBBsupport.html)
    * Uncompressed asset splits
    * [Android symbols zip files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html)
  * Unity incrementally copies: 
    * Player binaries
    * Gradle resources
  * The last step in the [build process](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html#the-build-process) is to run Gradle. From this point, the build process doesn’t use the incremental build pipeline and it’s up to Gradle to track dependencies.


If you implement [IPostGenerateGradleAndroidProject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Android.IPostGenerateGradleAndroidProject.html) and modify or move any Android file or asset that the incremental build pipeline uses, it can cause issues when you build your project. If you only want to [modify Gradle project files](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files.html), it’s best practice to use the [Android Project Configuration Manager](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-methods.html#agp) instead of `IPostGenerateGradleAndroidProject`. If you must use `IPostGenerateGradleAndroidProject` for your use case and need to work around incremental build pipeline issues, refer to [Creating non-incremental builds](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html#creating-non-incremental-builds).  
**Note** : You can use Android Project Configuration Manager to modify Android Gradle project files in custom modules only.
## Additional resources
  * [Build your application for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-library-manifest.html)
Unity Library Manifest
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-getting-started.html)
Getting started with Android
