* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/AppleMac.html)
  * [Building and delivering for macOS](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-delivery.html)
  * macOS build settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building.html)
Build a macOS application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building-notarization.html)
Code sign and notarize your macOS application
# macOS build settings reference
Use these settings to configure how Unity builds your application for macOS platform. You can update your macOS build settings from the **Platform Settings** section of the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.
**Property** | **Description**  
---|---  
**Architecture** | Select the CPU to build for (only applies to Build And Run). 
  * **Intel 64-bit** : Use Intel/AMD 64-bit CPU architecture.
  * **Apple Silicon** : Use Apple’s Silicon architecture.
  * **Intel 64-bit + Apple Silicon** : Use both architectures.

  
**Create Xcode Project** | Enable this setting to generate an Xcode project so you can build your final application bundle in Xcode. Xcode has built-in support for code signing and uploading the application to the Mac App Store.  
**Run in Xcode as** | Select whether Xcode runs your Project as a **Release** or **Debug** build. 
  * **Release** : Builds an optimized version of your app.
  * **Debug** : Builds a testing version of your app that contains additional code that helps with debugging.

  
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
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings), and [GI data](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html). 
  * **Default** : On Windows, Mac, Linux Standalone, and iOS, there’s no default compression. On Android, the default compression is ZIP, which gives slightly better compression results than LZ4HC. However, ZIP data is slower to decompress.
  * **LZ4** : A fast compression format that is useful for development builds. For more information, refer to [BuildOptions.CompressWithLz4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4.html).
  * **LZ4HC** : A high compression variant of LZ4 that is slower to build but produces better results for release builds. For more information, refer to [BuildOptions.CompressWithLz4HC](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.CompressWithLz4HC.html).

  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building.html)
Build a macOS application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/macos-building-notarization.html)
Code sign and notarize your macOS application
