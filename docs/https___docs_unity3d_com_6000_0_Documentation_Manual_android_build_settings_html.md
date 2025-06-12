* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android.html)
  * [Building and delivering for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-building-and-delivering.html)
  * Android build settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)
Modify Gradle project files with Android Studio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)
Build your application for Android
# Android build settings reference
Use the Android build settings to configure and build your application for Android platform. The Android build settings are part of the **Platform Settings** section of the [Build Profiles window](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html).
**Property** | **Description**  
---|---  
**Texture Compression** | The texture compression format to use for the build. The options are: 
  * **Use Player Settings** : Uses the texture compression format you set in [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
  * **ETC (GLES 2.0)** : Uses ETC format.
  * **ETC2 (GLES 3.0)** : Uses ETC2 format.
  * **ASTC** : Uses ASTC format.
  * **DXT (Tegra)** : Uses DXT format.
  * **PVRTC (PowerVR)** : Uses PVRTC format (This format is deprecated. Use ASTC or ETC format instead.)

For more information about texture compression formats, refer to [Recommended, default, and supported texture compression formats, by platform](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html#android).  
  
**Notes** : 
  * If you enable [texture compression targeting](https://docs.unity3d.com/6000.0/Documentation/Manual/android-distribution-google-play.html#texture-compression-targeting), Unity disables this setting.
  * You can also change this setting from a script or using the `-setDefaultPlatformTextureFormat` [command-line argument](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html). 

  
**Export Project** | Exports the Unity project as a Gradle project that you can import into Android Studio. For more information, refer to [Export an Android project](https://docs.unity3d.com/6000.0/Documentation/Manual/android-export-process.html).  
**Symlink Sources** | Indicates whether to share Java, Kotlin, and Android Library plug-in source files between Unity and the exported Gradle project. Android Library plug-in source files can be shared only if it includes `build.gradle` file in the plug-in folder.   
  
Enable this setting to create [symbolic links](https://en.wikipedia.org/wiki/Symbolic_link) so the Gradle project references Java, Kotlin, and Android Library plug-in (.androidlib) source files in the Unity project. This helps you test and iterate Java, Kotlin, and Android Library plug-in code because it means any changes you make to these source files in the exported Gradle project persist if you re-export the Unity project.   
  
Disable this setting to make Unity copy Java, Kotlin, and Android Library plug-in source files from the Unity project into the exported Gradle project.   
  
**Note** : You can only interact with this setting if you enable **Export Project**.   
**Build App Bundle (Google Play)** | Indicates whether to build the application as an[ Android App Bundle](https://developer.android.com/platform/technology/app-bundle/) (AAB) to distribute on Google Play. If you enable this setting, Unity builds the application as an `aab`. If you disable this setting, Unity builds the application as an `apk`.   
  
**Note** : This setting is visible only if you disable **Export Project**.   
**Export for App Bundle** | Configures the exported Gradle project to build as an Android App Bundle.   
  
**Note** : This setting is visible only if you enable **Export Project**.  
**Debug Symbols** | Specifies how Unity generates a [symbols package](https://docs.unity3d.com/6000.0/Documentation/Manual/android-symbols.html) when it builds your application. The available options are: 
  * **Disabled** : Unity doesn’t generate a symbols package.
  * **Public** : Unity generates the symbols package containing only the symbol table section and not the debugging information.
  * **Debugging** : Unity generates the symbols package containing the symbol table section and debugging information.

You can upload the symbol package with your **apk** The Android Package format output by Unity. An APK is automatically deployed to your device when you select File > Build & Run. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#APK) or Android App bundle (aab) in three ways: 
  * As a separate zip file for an apk build. 
  * Embed directly in the Android App bundle. This requires you to enable the Build App Bundle option.
  * As a separate zip file for the Android App bundle. This requires you to enable the Build App Bundle option.

  
**Symbols output options** | Specifies how Unity includes the symbols with the application build. 
  * **.zip** : A separate zip file containing the symbols package. You can upload this zip file with the apk.
  * **App Bundle** : The symbols get embedded in the Android App bundle.
  * **.zip + App Bundle** : A separate zip file containing the symbols package. Additionally, the symbols get embedded in the Android App bundle.

  
**Symbol file extension** | Specifies the symbol file extension as per the selected symbols package type. You have an option to create symbol files with the legacy extension. 
  * **.so** : Specifies the legacy `.so` extension for the symbols package which you can upload on distribution services that don’t recognize the `.so.sym` or `.so.dbg` extensions.
  * **.so.sym** : Specifies the extension for the public symbols package.
  * **.so.dbg** : Specifies the extension for the debugging symbols package.

  
**Run Device** | Specifies which attached device to test the build on. Devices connected via USB appear in the list automatically. If you connect a new device or don’t find an attached device in the list, select **Refresh**. To connect a new device wirelessly over Android Debug Bridge, select the **< Enter IP>** option. For more information, refer to [Debug on Android devices](https://docs.unity3d.com/6000.0/Documentation/Manual/android-debugging-on-an-android-device.html).  
**Build to Device** | A build pipeline that doesn’t create a full build and instead deploys single files that changed since the last patch directly to the device. **Patch** deploys changed files to the devices and **Patch And Run** deploys changed files and then runs the application on the device. For more information, refer to [Application patching](https://docs.unity3d.com/6000.0/Documentation/Manual/android-AppPatching.html).   
  
You can only interact with this setting if you enable **Development Build**.   
**Development Build** | Include scripting debug symbols and the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define symbol. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  
  
For more information, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).  
**Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html).  
  
**Note** : This option is available only if you select **Development Build**.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html#deep-profiling).   
  
This property is available only if you enable **Development Build**.   
  
**Note** : Enabling **Deep Profiling** might slow down script execution.  
**Script Debugging** | Attach script debuggers to the Player remotely.   
  
This property is available only if you enable **Development Build**.  
**Wait for Managed Debugger** | Make the Player wait for a debugger to be attached before it executes any script code.  
  
This property is visible only if you enable **Script Debugging**.  
**Compression Method** | Specifies the method Unity uses to compress the data in your Project when it builds the Player. This includes [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetTypes.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset), [Scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html), and [GI data](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html). 
  * **Default** : On Windows, Mac, Linux Standalone, and iOS, there’s no default compression. On Android, the default compression is ZIP, which gives slightly better compression results than LZ4HC. However, ZIP data is slower to decompress.
  * **LZ4** : A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4.html).
  * **LZ4HC** : A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4HC.html).

  
## Additional resources
  * [How Unity builds Android applications](https://docs.unity3d.com/6000.0/Documentation/Manual/how-unity-builds-android-applications.html)
  * [Build your application for Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)
  * [BuildOptions API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-modify-gradle-project-files-android-studio.html)
Modify Gradle project files with Android Studio
[](https://docs.unity3d.com/6000.0/Documentation/Manual/android-BuildProcess.html)
Build your application for Android
