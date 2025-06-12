* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)
  * Build Profiles window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html)
Introduction to build types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html)
Incremental build pipeline
# Build Profiles window reference
The following sections provide an overview of the **Build Profiles** window and its settings. Access the **Build Profiles** window in the Unity Editor from **File > Build Profiles**. 
  * [Asset Import Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#AssetImportOverride)
  * [Build options](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#build-options)
  * [Build Data](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#build-data)
  * [Platform Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#platform-settings)
  * [Player Settings Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#player-settings-overrides)


## Asset Import Overrides
To speed up the time it takes to import assets and change platforms, you can locally override all texture import settings. During development, asset overrides can be useful to speed up iteration time by using lower quality assets.
**Note** : To set asset import overrides for initial project imports, use the Editor [command line arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/CommandLineArguments.html) `-overrideMaxTextureSize` and `-overrideTextureCompression`.
**Property** | **Description**  
---|---  
**Max Texture Size** | Override the maximum imported texture size. Unity imports textures in the lower of two values: this value, or the Max Size value specified in [Texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html). The time it takes to import a texture is proportional to the number of pixels it contains, so a texture size with a lower maximum can speed up import times. It’s recommended to use this setting only during development as the resulting textures are lower in resolution.  
**Texture Compression** | Override the texture compression options set in [Texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).  
  
**Note** : The following texture compression options only apply to textures referenced in [GPU texture formats reference](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-formats-reference.html).  
  

  * **Force Fast Compressor** :Use a faster but lower quality texture compression mode for formats that support it (BC7, BC6H, ASTC, ETC, ETC2). Usually this results in more compression artifacts, but for many formats the compression itself is 2 to 20 times faster. This setting also disables **Crunch** texture compression format on any textures that have it. The effect of this setting is the same as if all textures had their **Compressor Quality** set to a low number in the platforms section of their [Texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
  * **Force Uncompressed** : Use uncompressed formats. This is faster to import (because it skips the texture compression process), but the resulting textures take up more memory and game data size, and can impact rendering performance. The effect of this setting is the same as if all textures had their **Compression** set to **None** in their platforms’ [Texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
  * **Force No Crunch** : Disable Crunch compression for all textures. Crunch compression can take a long time, so disabling it can speed up the import process significantly. However, the resulting textures take up more disk space. Selecting this option is the same as disabling **Use Crunch Compression** in the [Texture import settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) for all textures.

  
## Build options
To build your application, select one of the following options:
**Property** | **Description**  
---|---  
**Build** | Build the Player without launching it. The default build is incremental, except for the first build, which is always a full non-incremental clean build. This option runs a build without the [StrictMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.StrictMode.html) option enabled.  
**Clean build** | Create a clean, [non-incremental](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html#creating-non-incremental-builds) build.  
**Force skip data build** | Skip the content step of the build process. This requires that you have already performed a successful build and that it is compatible with the current **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) in your project. Refer to[Forcing a Scripts-only Build](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html#force-scripts-only-build) for more information.  
**Build and Run** | Build the Player and open it on your target platform. This option runs a build with the [StrictMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.StrictMode.html) option enabled. Unity will do an incremental build when possible, otherwise it will perform a clean build.  
**Note** : The **Build** and **Build and Run** settings are visible only for the active profile. 
## Build Data
**Note** : The **Build Data** section is visible only when using a **build profile** A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile).
**Setting** | **Description**  
---|---  
**Override Global Scene List** | Select **Override Global Scene List** to create a custom scene list for your build profile. When selecting **Override Global Scene List** , scenes are automatically inherited from the global [scene list](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profile-scene-list.html).  
**Scripting Defines** | Add custom scripting defines for your build profile. These custom scripting defines are additive and don’t override other scripting defines in your project. For more information, refer to [Custom scripting symbols](https://docs.unity3d.com/6000.0/Documentation/Manual/custom-scripting-symbols.html).  
## Platform settings
Each platform has specific build settings. For more information, refer to the following platform-specific documentation:
**Platform** | **Documentation**  
---|---  
**Android** | [Android build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html)  
**iOS** and **tvOS** | [iOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettingsiOS.html)  
**Embedded Linux** | [Embedded Linux build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-linux-build-settings.html)  
**Linux** | [Linux build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)  
**macOS** | [macOS build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/macosbuildsettings.html)  
**QNX** | [QNX build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-settings.html)  
**Universal Windows Platform** | [UWP build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/windowsstore-buildsettings.html)  
**Web** | [Web build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html)  
**Windows** | [Windows build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStandaloneBinaries.html)  
**Note** : For information on build settings for closed platforms, refer to the included documentation in the Unity installer of each **closed platform** Includes platforms that require confidentiality and legal agreements with the platform provider for using their developer tools and hardware. These platforms aren’t open to development unless you have an established relationship with the provider. For example PlayStation®, Game Core for Xbox®, and Nintendo®.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Closedplatform).
### Shared build settings
The following build settings are available for all profile types. The values of these settings are shared across platform profiles but not across build profiles.
**Note** : Updating shared settings of an active platform profile using [`EditorUserBuildSettings`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html) applies changes across all platform profiles. However, updating shared settings of an active build profile with [`EditorUserBuildSettings`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUserBuildSettings.html) only updates that specific build profile.
**Property** | **Description**  
---|---  
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

  
## Player Settings Overrides
**Note** : The **Player Settings Overrides** section is visible only when using a build profile.
**Property** | **Description**  
---|---  
**Customize player settings** | Create custom [Player](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html) settings for your build profile. For more information, refer to [Override settings with build profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-override-settings#override-player).   
  
**Note** : A link to the global **Player** settings is available in the **Build Profiles** toolbar.  
## Additional resources
  * [Create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html)
  * [Build Profiles scripting API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.Profile.BuildProfile.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/build-types.html)
Introduction to build types
[](https://docs.unity3d.com/6000.0/Documentation/Manual/incremental-build-pipeline.html)
Incremental build pipeline
