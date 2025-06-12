* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Get started with QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-get-started.html)
  * QNX Player settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html)
Set up your environment for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-develop.html)
Develop for QNX
# QNX Player settings reference
QNX Player settings lets you customize how Unity builds and displays your final application. To access the Player settings window for QNX, go to **Edit** > **Project Settings** > **Player** and select the **QNX** tab. You can use the [PlayerSettings API](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html) to control most of the settings available in this window. For a description of the general Player settings, refer to [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
## General settings
The Player settings differ between the platform modules that you have installed. Each platform has its own Player settings which you must set for each version of your application you want to build. To navigate between them, click the tabs with the appropriate platform operating system icon.
![The main Player settings window](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/qnx-player-settings.png) The main Player settings window
You can find documentation for the properties in the following sections:
  * [Icon](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#Icon)
  * [Resolution and Presentation](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#resolution)
  * [Splash Image](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#Splash)
  * [Other Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#Other)


## Icon
Enable the **Override for QNX** setting to assign a custom icon for your QNX game.
##  Resolution and presentation
Use the Resolution and Presentation section to customize aspects of the screen’s appearance in the Resolution and Standalone Player Options sections.
### Resolution section
This section lets you customize the screen mode and default size.
Property | Description  
---|---  
**Use 32-bit Display Buffer** | QNX only supports 32-bit color buffers.  
**Disable Depth and Stencil** | This isn’t supported on the QNX platform.  
**Render Over Native UI** | This isn’t supported on the QNX platform.  
##  Splash Image
The [Virtual Reality Splash Image](https://docs.unity3d.com/Documentation/Manual/class-PlayerSettingsSplashScreen.html) setting is used for selecting a custom splash image for **Virtual Reality** Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VirtualReality) (VR) displays. However, it doesn’t apply to QNX platform.
##  Other Settings
This section allows you to customize a range of options organized into the following groups:
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#Renderin)
  * [Configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#Configur)


###  Rendering
Use these settings to customize how Unity renders your game for the QNX platform.
![Rendering settings for QNX](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/qnx-other-rendering.png) Rendering settings for QNX **Property** | **Description**  
---|---  
**Color Space** | Choose which color space to use for rendering. For more information, refer to [Linear rendering overview](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting).  
  

  * **Gamma** : Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.
  * **Linear** : Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using [sRGB](https://en.wikipedia.org/wiki/SRGB) sampling. If your [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html) are in linear color space, you need to work in linear color space and deactivate sRGB sampling for each Texture.

  
**Force SRGB blit** | Enable this to use Force SRGB blit for Linear color space. If your graphics drivers don’t support the linear color space, selecting this option will convert Linear color space to Gamma (SRGB) color space.  
**Multithreaded Rendering** | Enable this option to use multithreaded rendering. This is only supported on Metal.  
**Static Batching** | Enable this option to use Static batching.  
**Dynamic Batching** | Enable this option to use [Dynamic Batching](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) on your build (enabled by default). **Note:** Dynamic batching has no effect when a [Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html) is active, so this setting is only visible when nothing is set in the Scriptable Render Pipeline Asset Graphics setting.  
**Static Batching Threshold** | Controls the maximum vertex threshold used when batching. For more information, refer to [Sprite Batch Vertex Threshold.](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-spriteBatchVertexThreshold.html).  
**GPU Compute Skinning** | Enable this option to enable GPU compute skinning, freeing up CPU resources.  
**Graphics Jobs** | Enable this option to instruct Unity to offload graphics tasks (render loops) to worker threads running on other CPU cores. This is intended to reduce the time spent in `Camera.Render` on the main thread, which is often a bottleneck.  
**Texture compression format** | Choose the texture compression format to use for textures in your Project. The options are ETC, ETC2, ASTC, DXT, and PVRTC. For more information on each of these compression formats, refer to [TextureImporterOverride](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html).  
**Normal Map Encoding** | Choose Normal Quality or High Quality to set the lightmap encoding. This setting affects the encoding scheme and compression format of the lightmaps.  
**Lightmap Streaming** | Enable this option to load only the lightmap mipmaps as needed to render the current game Cameras. This value applies to the lightmap textures as they are generated. Note: To use this setting, you must enable the Texture Streaming Quality setting. 
  * **Streaming Priority** : Set the lightmap mip map streaming priority to resolve resource conflicts. These values are applied to the light map textures as they’re generated. Positive numbers give higher priority. Valid values range from –128 to 127.

  
**Frame Timing Stats** | Enable this option to gather CPU/GPU frame timing statistics.  
**OpenGL: Profiler GPU Recorders** | Enable profiler recorders when rendering with OpenGL.  
**Virtual Texturing (Experimental)** | Indicates whether to enable [Virtual Texturing](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html).  
**Note:** The Unity Editor requires a restart for this setting to take effect.  
**Load/Store Action Debug Mode** | Highlights undefined pixels that might cause rendering problems on mobile platforms. This affects the Unity Editor Game view, and your built application if you select **Development Build** in the **Platform Settings** section of the **Build Profiles** window. Refer to [LoadStoreActionDebugModeSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html) for more information.  
**360 Stereo Capture** | Indicates whether Unity can capture stereoscopic 360 images and videos. When enabled, Unity compiles additional shader variants to support 360 capture (currently only on Windows/macOS). When enabled, enable_360_capture keyword is added during the Stereo RenderCubemap call. Note that this keyword isn’t triggered outside the Stereo RenderCubemap function. For more information, refer to [Stereo 360 Image and Video Capture](https://blog.unity.com/technology/stereo-360-image-and-video-capture?_ga=2.228952412.1984266774.1645442174-1855761588.1624871061).  
###  Configuration
**Property** | **Description**  
---|---  
**Scripting Backend** | You cannot change the scripting backend for QNX.  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with third-party libraries. However, it has no effect on Editor-specific code (code in an Editor directory, or within an Editor-specific Assembly Definition).  
  
**Tip:** If you’re having problems with a third-party assembly, you can try the suggestion in the [API Compatibility Level](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-player-settings.html#apiComp) section.  
  

  * **.Net Framework** : Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnetProfileAssemblies).
  * **.Net Standard 2.1** : Produces smaller builds and has full cross-platform support.

  
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation.   
**Note** : To use this, set Scripting Backend to IL2CPP.  
**C++ Compiler Configuraion** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.   
**Note** : This property is disabled unless Scripting Backend is set to IL2CPP.  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to [Automatic Memory Management](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html).  
**Allow downloads over HTTP** | Indicate whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
  

  * **Not Allowed** : Never allow downloads over HTTP.
  * **Allowed in Development Builds** : Only allow downloads over HTTP in development builds.
  * **Always Allowed** : Allow downloads over HTTP in development and release builds.

  
**Player Data path** | Enter the directory path on the system where you want to save the .`config` and log files. You can also change this from the command line of the player by adding the following arguments:`-platform-hmi-player-data-path <pathname>`.  
**Log startup Timings** | Enable this option to log the startup of the Player.  
**CPU Configuration** | Set the target CPU configuration for the player runtime. The default number of cores is 0, but you can increase it by entering a number. The options for each CPU are: **Disabled** , **High Performance** , and **Low Performance**.  
**Loading image** | Use this setting to select a custom splash image for the loading screen.   
**Screen graphics config path** | Enter the directory path on the system where you want to save the .`config` and log files.   
**Active Input Handling** | Choose how to handle input from users. 
  * **Input Manager (Old)** : Use the original [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) settings.
  * **Input System Package (New)** : Uses the new [input system package](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest).
  * **Both** : Use both systems.

  
###  Shader Settings and Shader Variant Loading Settings
Use these settings to control how much memory **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) use at runtime.
![Shader settings for QNX](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/qnx-shader-settings.png)
**Property** | **Description**  
---|---  
**Shader precision model** | Select the default precision of samplers used in shaders. For more information, refer to [HLSL data types](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-DataTypesAndPrecision.html).  
**Strict shader variant matching** | Use the error shader if a shader variant is missing and display an error in the console.  
**Keep Loaded Shaders Alive** | When enabled, you can’t unload a shader. For more information, refer to [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is 16. For more information, refer to [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html).  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is 0, which means there’s no limit.  
**Override** | Enable this to override Default chunk size and Default chunk count for this build target.  
###  Script Compilation
![Script Compilation settings for QNX](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/qnx-script-compilation.png) Script Compilation settings for QNX **Property** | **Description**  
---|---  
**Scripting Define Symbols** | Sets custom compilation flags.   
  
For more details, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).  
**Additional Compiler Arguments** | Adds entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, click **Add** (**+**). To remove an entry, click **Remove** (**-**).  
  
When you have added all desired arguments, click **Apply** to include your additional arguments in future compilations. Click **Revert** to reset this list to the most recent applied state.  
**Suppress Common Warnings** | Indicates whether to display the C# warnings [CS0169](https://docs.microsoft.com/en-us/dotnet/csharp/misc/cs0169) and [CS0649](https://docs.microsoft.com/en-us/dotnet/csharp/misc/CS0649).  
**Allow ‘unsafe’ Code** | Enables support for compiling [‘unsafe’ C# code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef` files and enable the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Indicates whether to prevent compilation with the -deterministic C# flag. With this setting enabled, compiled assemblies are byte-for-byte the same each time they’re compiled.  
  
For more information, refer to [C# Compiler Options that control code generation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/deterministic-compiler-option).  
### Optimization
  
**Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) at build time.  
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**Managed Stripping Level** | Choose how aggressively Unity strips unused managed (C#) code. When Unity builds your app, the Unity Linker process can strip unused code from the managed DLLs your Project uses. Stripping code can make the resulting executable smaller, but can sometimes remove code that’s in use.   
  
For more information about these options and bytecode stripping with IL2CPP, refer to [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html). 
  * **Minimal** : Use this to strip class libraries, UnityEngine, Windows Runtime assemblies, and copy all other assemblies.
  * **Low** : Remove unreachable managed code to reduce build size and Mono/IL2CPP build times.
  * **Medium** : Run UnityLinker to reduce code size beyond what **Low** can achieve. You might need to support a custom link.xml file, and some reflection code paths might not behave the same. 
  * **High** : UnityLinker will strip as much code as possible. This will further reduce code size beyond what Medium can achieve but managed code debugging of some methods might no longer work. You might need to support a custom link.xml file, and some reflection code paths might not behave the same. 

  
**Vertex Compression** | Sets vertex compression per channel. This affects all the meshes in your project.   
Typically, Vertex Compression is used to reduce the size of mesh data in memory, reduce file size, and improve GPU performance.   
  
For more information on how to configure vertex compression and limitations of this setting, refer to [Compressing mesh data](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh-compression).  
**Optimize Mesh Data** | Enable this option to strip unused vertex attributes from the mesh used in a build. This option reduces the amount of data in the mesh, which can help reduce build size, loading times, and runtime memory usage.   
  
**Warning:** If you have this setting enabled, don’t change material or shader settings at runtime.   
  
For more information, refer to [PlayerSettings.stripUnusedMeshComponents](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-stripUnusedMeshComponents.html).  
**Texture Mipmap Stripping** | Enables mipmap stripping for all platforms. It strips unused mipmap levels from Textures at build time.   
Unity determines unused mipmap levels by comparing the mipmap level against the quality settings for the current platform. If a mipmap level is excluded from every quality setting for the current platform, then Unity strips those mipmap levels from the build at build time. If `QualitySettings.globalTextureMipmapLimit` is set to a mipmap level that has been stripped, Unity will set the value to the closest mipmap level that hasn’t been stripped.  
### Logging
Select what type of logging you want to allow in specific contexts within the QNX builds.
  * Select your preferred logging method from the available options.
  * Check a box that corresponds to each Log Type (Error, Assert, Warning, Log, and Exception) based on the type of logging you require. For example:
    * **ScriptOnly** : Logs only when running **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).
    * **Full** : Logs all the time.
    * **None** : No logs are ever recorded.


### Legacy
This section covers the legacy player settings.
Property | Description  
---|---  
**Clamp BlendShapes (Deprecated)** | Enable the option to clamp the range of blend shape weights in [SkinnedMeshRenderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html).  
**Upload Cleared Texture Data** | This is a legacy feature and currently not needed because it uses up the bandwidth. By default, this is enabled for debugging purposes. Enabling this setting clears the initial data and automatically uploads the texture from script to the video memory.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-environment-setup.html)
Set up your environment for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-develop.html)
Develop for QNX
