* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/Windows.html)
  * Windows Player settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Windows.html)
Integrating Unity into Windows applications
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windows-develop.html)
Develop for Windows
# Windows Player settings
This page details the **Player** settings specific to Windows. For a description of the general **Player** settings, refer to [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings).
![Windows Player settings](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/WindowsPlayerSettings.png) Windows Player settings
You can find documentation for the properties in the following sections:
  * [Icon](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Icon)
  * [Resolution and Presentation](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Resolution)
  * [Splash Image](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Splash)
  * [Other Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Other)


## Icon
Enable the **Override for Windows, Mac, Linux** setting to assign a custom icon for your desktop game. You can upload different sizes of the icon to fit each of the squares provided.
![Icon settings for the desktop platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCIcon.png) Icon settings for the desktop platforms
## Resolution and Presentation
Use the **Resolution and Presentation** section to customize aspects of the screen’s appearance in the [Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Resolution1) and [Standalone Player Options](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Resolution2) sections.
### Resolution
This section allows you to customize the screen mode and default size.
![Resolution section for the Desktop Player platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCRes.png) Resolution section for the Desktop Player platforms **Property** | **Description**  
---|---  
**Run In Background** | Enable this option to allow the application to run in the background when it loses focus. When disabled, the application pauses when it loses focus.  
**Fullscreen Mode** | Choose the full-screen mode. This defines the default window mode at startup.  
  

  * **Fullscreen Window** : Set your app window to the full-screen native display resolution, covering the whole screen. This mode is also known as borderless full-screen. Unity renders the app content at the resolution set by a script, or the native display resolution if none is set and scales it to fill the window. When scaling, Unity adds black bars to the rendered output to match the display aspect ratio to prevent content stretching. This process is called [letterboxing](https://en.wikipedia.org/wiki/Letterboxing_\(filming\)). The OS overlay UI displays on top of the full-screen window (such as IME input windows). All platforms support this mode.
  * **Exclusive Fullscreen (Windows only)** : Set your app to maintain sole full-screen use of a display. Unlike **Fullscreen Window** , this mode changes the OS resolution of the display to match the app’s chosen resolution. This option is only supported on Windows.
  * **Maximized Window (Windows and Mac only)** : Set the app window to the operating system’s definition of **maximized**. On Windows, it is a full-screen window with a title bar. On macOS, it is a full-screen window with a hidden menu bar and dock. **Fullscreen Window** is the default setting for other platforms.
  * **Windowed** : Set your app to a standard, non-full-screen movable window, the size of which is dependent on the app resolution. In this mode, the window is resizable by default. Use the [Resizable Window](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#resizable) setting to disable this. All desktop platforms support this full-screen mode.

  
**Default Is Native Resolution** | Enable this option to make the game use the default resolution used on the target machine.   
**Note** : This property isn’t visible if you set **Fullscreen Mode** to **Windowed**.  
**Default Screen Width** | Set the default width of the game screen in pixels.   
  
**Note** : This property is visible only if you set **Fullscreen Mode** to **Windowed**.  
**Default Screen Height** | Set the default height of the game screen in pixels.   
  
**Note** : This property is visible only if you set **Fullscreen Mode** to **Windowed**.  
**Mac Retina Support** | Enable this option to enable support for high DPI (Retina) screens on a Mac. Unity enables this by default. This enhances Projects on a Retina display, but it’s somewhat resource-intensive when active.  
### Standalone Player Options
Use the **Standalone Player Options** to specify how the user can customize the screen. For example, you can determine whether the user can resize the screen and how many instances can run concurrently.
![Standalone Player Options settings for the Standalone Player platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCStand.png) Standalone Player Options settings for the Standalone Player platforms **Property** | **Description**  
---|---  
**Use Player Log** | Enable this option to write a log file with debugging information. This option is enabled by default.  
**Resizable Window** | Enable this option to allow resizing of the desktop player window.  
**Visible in Background** | Enable this option to display the application in the background if **Windowed** [Fullscreen Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#fullscreen) is used.  
  
**Note:** This prevents keyboard shortcuts that minimize the app window, for example, `Alt+Tab` and `Windows+M`, from functioning. For more information, refer to [PlayerSettings.visibleInBackground](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-visibleInBackground.html).  
**Allow Fullscreen Switch** | Enable this option to allow default OS full-screen key presses to toggle between full-screen and windowed modes.  
**Force Single Instance** | Enable this option to restrict desktop players to a single concurrent running instance.  
**Use DXGI flip model swap chain for D3D11** | Using the flip model ensures the best performance. This setting affects the D3D11 graphics API. Disable this option to fall back to the Windows 7-style BitBlt model. For more information, refer to [PlayerSettings.useFlipModelSwapchain](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-useFlipModelSwapchain.html).  
## Splash Image
Use the **Virtual Reality Splash Image** setting to select a custom splash image for [Virtual Reality](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VirtualReality) displays. For information on common Splash Screen settings, see [Splash Screen](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsSplashScreen.html).
![Splash Image Player settings for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCSplash.png) Splash Image Player settings for desktop platforms
## Other Settings
This section allows you to customize a range of options organized into the following groups:
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Rendering)
  * [Vulkan Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Vulkan)
  * [Configuration](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Configuration)
  * [Shader Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#ShaderSettings)
  * [Shader Variant Loading Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#ShaderVariantLoading)
  * [Optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Optimization)
  * [Stack Trace](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Logging)
  * [Legacy](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#Legacy)
  * [Capture Logs](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#CaptureLogs)


### Rendering
Use these settings to customize how Unity renders your game for desktop platforms.
**Property** | **Description**  
---|---  
**Color Space** | Choose which color space to use for rendering. For more information, refer to [Linear rendering overview](https://docs.unity3d.com/6000.0/Documentation/Manual/LinearLighting).  
  

  * **Gamma** : Gamma color space is typically used for calculating lighting on older hardware restricted to 8 bits per channel for the framebuffer format. Even though monitors today are digital, they might still take a gamma-encoded signal as input.
  * **Linear** : Linear color space rendering gives more precise results. When you select to work in linear color space, the Editor defaults to using [sRGB](https://en.wikipedia.org/wiki/SRGB) sampling. If your [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures.html) are in linear color space, you need to work in linear color space and deactivate sRGB sampling for each Texture.

  
**MSAA Fallback** | Select the multi sample antialiasing fallback strategy to upgrade or downgrade the sample count if the sample count requested by the user is not supported by the device.  
  

  * **Upgrade** : The sample count reduces to the nearest supported lower sample count.
  * **Downgrade** : The sample count increases to the next higher sample count. If that sample count is not supported, then it reduces to the nearest supported lower sample count.

  
**Auto Graphics API for Windows** | Enable this option to use the recommended Graphics API on the Windows machine the game is running on. Disable it to add and remove supported Graphics APIs.   
**Auto Graphics API for Mac** | Enable this option to use the recommended Graphics API on the Mac the game is running on. Disable it to add and remove supported Graphics APIs. Windows doesn’t support this property.   
**Auto Graphics API for Linux** | Enable this option to use the recommended Graphics API on the Linux machine it runs on. Disable it to add and remove supported Graphics APIs.   
**Color Gamut** | You can add or remove [color gamuts](https://en.wikipedia.org/wiki/Gamut) to use for rendering. Click the plus (+) icon to view a list of available gamuts. A color gamut defines a possible range of colors available for a given device (such as a monitor or screen). The sRGB gamut is the default (and required) gamut.  
**Static Batching** | Enable this option to use [static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching).  
**Dynamic Batching** | Use [Dynamic Batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) on your build (enabled by default).  
  
**Note:** Dynamic batching has no effect when a [Scriptable Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/scriptable-render-pipeline-introduction.html) is active, so this setting is only visible if the **Scriptable Render Pipeline Asset** [Graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#SRLoop) setting is blank.  
**Sprite Batching Threshold** | Controls the maximum vertex threshold used when batching.  
**GPU Skinning** | Calculate mesh skinning and blend shapes on the GPU via shaders to free up CPU resources and improve performance.  
  

  * **CPU** : Select this option to perform mesh skinning and blend shapes calculation on the CPU.
  * **GPU** : Select this option to perform mesh skinning and blend shapes calculation on the GPU.
  * **GPU (Batched)** : Select this option to use batching and reordering to perform mesh skinning and blend shapes calculation on the GPU. Batching reduces the number of dispatch calls to the GPU and can improve performance.

  
**Graphics Jobs** | Offload graphics tasks (render loops) to worker threads running on other CPU cores. This option reduces the time spent in `Camera.Render` on the main thread, which can be a bottleneck.  
**Graphics Jobs Mode** | Specify the graphics jobs mode to use in your application. For information about jobs in Unity, refer to [Job system](https://docs.unity3d.com/6000.0/Documentation/Manual/job-system-overview.html).  
  
**Note** : This option is available only when **Graphics Jobs** is enabled and **Graphics APIs** is set to DX12 or Vulkan.  
  

  * **Native** : The main thread writes Unity graphics commands for worker threads. The worker threads write the commands to a task executor which the render thread consumes.
  * **Legacy** : The main thread writes Unity graphics commands for worker threads. The worker threads write commands directly to the render thread. The render thread reads the Unity graphics commands and converts them to native graphics commands.
  * **Split** : The main thread writes Unity graphics commands for worker threads. The render thread reads the Unity graphics commands and converts them to native graphics commands. The render thread then starts worker threads to write native graphics commands.

  
**Lightmap Encoding** | Defines the encoding scheme and compression format of the lightmaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**  
**HDR Cubemap Encoding** | Defines the encoding scheme and compression format of the HDR Cubemaps.   
You can choose from **Low Quality** , **Normal Quality** , or **High Quality**. For more information, refer to [Lightmaps: Technical information](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-TechnicalInformation.html).  
**Lightmap Streaming** | Enable this option to use [Mipmap Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html) for lightmaps. Unity applies this setting to all lightmaps when it generates them.  
  
**Note:** To use this setting, you must enable the [Texture Mipmap Streaming Quality](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html#texStream) setting.  
**Streaming Priority** | Set the priority for all lightmaps in the [Mipmap Streaming system](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html). Unity applies this setting to all lightmaps when it generates them.  
Positive numbers give higher priority. Valid values range from `-128` to `127`.  
**Frame Timing Stats** | Enable this property to gather CPU and GPU frame timing data using [FrameTimingManager](https://docs.unity3d.com/6000.0/Documentation/Manual/frame-timing-manager.html) API. If you disable this property, [Dynamic Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution)A Camera setting that allows you to dynamically scale individual render targets to reduce workload on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DynamicResolution-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#dynamicresolution) camera setting can’t use this data to dynamically adjust the resolution to reduce GPU workload.  
**OpenGL: Profiler GPU Recorders** | Enable GPU recorder support and disable the GPU profiler. OpenGL API doesn’t allow both recorder and profiler to work simultaneously. Disable this property to use GPU profiler.  
**Allow HDR Display Output** | Enable HDR mode output when the application runs. This only works on displays that support this feature. If the display doesn’t support HDR mode, the game runs in standard mode.  
**Use HDR Display Output** | Checks if the main display supports HDR, and if it does, swaps to HDR output when the application launches.  
  
**Note** : This option is available only when **Allow HDR Display Output** is active.  
**Swap Chain Bit Depth** | Select the number of bits in each color channel for swap chain buffers. For more information on bit depth, refer to [D3DHDRDisplayBitDepth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/D3DHDRDisplayBitDepth.html).  
  
**Note** : This setting is visible only when **Use HDR Display Output** is enabled.  
  

  * **Bit Depth 10** : Unity uses the R10G10B10A2 buffer format and Rec2020 primaries with ST2084 PQ encoding.
  * **Bit Depth 16** : Unity uses the R16G16B16A16 buffer format and Rec709 primaries with linear color (no encoding).

  
**Virtual Texturing (Experimental)** | Reduce GPU memory usage and texture loading times if your Scene has many high resolution textures. For more information, refer to [Virtual Texturing](https://docs.unity3d.com/6000.0/Documentation/Manual/svt-streaming-virtual-texturing.html).  
**Note** : The Unity Editor requires a restart for this property to take effect.  
**360 Stereo Capture** | Indicate whether Unity can capture stereoscopic 360 images and videos. When enabled, Unity compiles additional shader variants to support 360 capture (currently only on Windows/OSX). The `enable_360_capture` keyword is added during the [`RenderToCubemap`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.RenderToCubemap.html) call, but isn’t triggered outside of this function.  
**Load/Store Action Debug Mode** | Highlights undefined pixels that might cause rendering problems on mobile platforms. This affects the Unity Editor Game view, and your built application if you select **Development Build** in the **Platform Settings** section of the **Build Profiles** window. For more information, refer to [LoadStoreActionDebugModeSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LoadStoreActionDebugModeSettings.html).  
**Editor Only** | Indicates whether the Load/Store Action Debug Mode only runs in the Unity Editor.  
  
**Note** :This property is visible only when Load/Store Action Debug Mode is set to true.  
### Vulkan Settings
![Vulkan Player settings for macOS.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCOther-Vulkan.png)
**Property** | **Description**  
---|---  
**SRGB Write Mode** |  Enable this option to allow `Graphics.SetSRGBWrite()` renderer to toggle the sRGB write mode during runtime. That is, if you want to temporarily turn off Linear-to-sRGB write color conversion, you can use this property to achieve that. Enabling this has a negative impact on performance on mobile tile-based GPUs; therefore, do NOT enable this for mobile.  
**Number of swapchain buffers** |  Set this option to 2 for double-buffering, or 3 for triple-buffering to use with Vulkan renderer. This setting may help with latency on some platforms, but in most cases you should not change this from the default value of 3. Double-buffering might have a negative impact on performance. Do not use this setting on Android.  
**Acquire swapchain image late as possible** |  If enabled, Vulkan delays acquiring the backbuffer until after it renders the frame to an offscreen image. Vulkan uses a staging image to achieve this. Enabling this setting causes an extra blit when presenting the backbuffer. This setting, in combination with double-buffering, can improve performance. However, it also can cause performance issues because the additional blit takes up bandwidth.  
**Recycle command buffers** | Indicates whether to recycle or free [CommandBuffers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html) after Unity executes them.  
### Configuration
![Configuration settings for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCOther-Config.png) Configuration settings for desktop platforms **Property** | **Description**  
---|---  
**Scripting Backend** | Choose the scripting backend you want to use. The scripting backend determines how Unity compiles and executes C# code in your Project.  
  

  * **Mono** : Compiles C# code into .NET Common Intermediate Language (CIL) and executes that CIL using a Common Language Runtime. For more information, refer to [Mono](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-mono.html)A scripting backend used in Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mono).
  * **IL2CPP** : Compiles C# code into CIL, converts the CIL to C++ and then compiles that C++ into native machine code, which executes directly at runtime. For more information, refer to [IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP).

  
**API Compatibility Level** | Choose which .NET APIs you can use in your project. This setting can affect compatibility with third-party libraries. However, it has no effect on Editor-specific code (code in an Editor directory, or within an Editor-specific Assembly Definition).  
  
**Tip:** If you’re having problems with a third-party assembly, you can try the suggestion in the [API Compatibility Level](https://docs.unity3d.com/6000.0/Documentation/Manual/playersettings-windows.html#apiComp) section.  
  

  * **.Net Framework** : Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.0 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.0. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnetProfileAssemblies).
  * **.Net Standard 2.1** : Produces smaller builds and has full cross-platform support.

  
**Editor Assemblies Compatibility Level** | Select which .NET APIs to use in your Editor assemblies.  
  

  * **.NET Framework** : Compatible with the .NET Framework 4 (which includes everything in the .NET Standard 2.1 profile plus additional APIs). Choose this option when using libraries that access APIs not included in .NET Standard 2.1. Produces larger builds and any additional APIs available aren’t necessarily supported on all platforms. For more information, refer to [Referencing additional class library assemblies](https://docs.unity3d.com/6000.0/Documentation/Manual/dotnet-profile-assemblies.html).
  * **.NET Standard** : Compatible with [.NET Standard 2.1](https://docs.microsoft.com/en-us/dotnet/standard/net-standard). Produces smaller builds and has full cross-platform support.

  
**IL2CPP Code Generation** | Defines how Unity manages IL2CPP code generation. This option is only available if you use the IL2CPP scripting backend.  
  

  * **Optimize for runtime speed** : Generates code optimized for runtime performance. This setting is activated by default.
  * **Optimize for code size and build time** : Generates code optimized for build size and iteration. This setting generates less code and produces a smaller build, but can reduce runtime performance for generic code. Use this option when faster build times are important, such as when iterating on changes.

  
**C++ Compiler Configuration** | Choose the C++ compiler configuration used when compiling IL2CPP generated code.  
  

  * **Debug** : The debug configuration turns off all optimizations, which makes the code quicker to build but slower to run.
  * **Release** : The release configuration enables optimizations so that the compiled code runs faster, the binary size is reduced, but compilation takes longer.
  * **Master** : Master configuration enables all possible optimizations, squeezing every bit of performance possible. For instance, on platforms that use the MSVC++ compiler, this option enables link-time code generation. Compiling code using this configuration can take significantly longer than it does using the Release configuration. The recommended best practice is to build the shipping version of your game using the Master configuration if the increase in build time is acceptable.

  
**IL2CPP Stacktrace Information** | Choose the information to include in a stack trace. For further details on the information types, refer to [Managed stack traces with IL2CPP](https://docs.unity3d.com/6000.0/Documentation/Manual/IL2CPP-managed-stack-traces.html).  
  

  * **Method Name** : Include each managed method in the stack trace.
  * **Method Name, File Name, and Line Number** : Include each managed method with file and line number information in the stack trace.   
  
**Note** : Using this option can increase both the build time and final size of the built program.

  
**Use incremental GC** | Uses the incremental garbage collector, which spreads garbage collection over several frames to reduce garbage collection-related spikes in frame duration. For more information, refer to [Automatic Memory Management](https://docs.unity3d.com/6000.0/Documentation/Manual/performance-managed-memory.html).  
**Allow downloads over HTTP** | Indicate whether to allow downloading content over HTTP. The default option is **Not allowed** due to the recommended protocol being HTTPS, which is more secure.  
  

  * **Not Allowed** : Never allow downloads over HTTP.
  * **Allowed in Development Builds** : Only allow downloads over HTTP in development builds.
  * **Always Allowed** : Allow downloads over HTTP in development and release builds.

  
**Active Input Handling** | Choose how to handle input from users.  
  

  * **Input Manager (Old)** : Use the original [Input](https://docs.unity3d.com/6000.0/Documentation/Manual/class-InputManager.html) settings.
  * **Input System Package (New)** : Uses the new [input system package](https://docs.unity3d.com/Packages/com.unity.inputsystem@latest).
  * **Both** : Use both systems.

  
#### API Compatibility Level
You can choose your mono API compatibility level for all targets. Sometimes a third-party .NET library uses functionality that is outside of your .NET compatibility level. In order to understand what is going on in such cases, and how to best fix it, try following these suggestions: 
  1. Install [ILSpy](https://www.microsoft.com/en-us/p/ilspy/9mxfbkfvsq13?cid=msft_web_chart&activetab=pivot:overviewtab) for Windows.
  2. Drag the .NET assemblies for the API compatibility level that you are having issues with into ILSpy. You can find these under `Frameworks/Mono/lib/mono/YOURSUBSET/`.
  3. Drag in your third-party assembly.
  4. Right-click your third-party assembly and select **Analyze**.
  5. In the analysis report, inspect the **Depends on** section. The report highlights anything that the third-party assembly depends on, but that is not available in the .NET compatibility level of your choice in red.


### Shader Settings
**Property** | **Description**  
---|---  
**Shader Precision Model** | Select the default precision shaders use. For more information, refer to [Use 16-bit precision in shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Use16BitPrecisionInShaders.html).  
  

  * **Platform default** : Use lower precision on mobile platforms, and full precision on other platforms.
  * **Unified** : Use lower precision if the platform supports it.

  
**Strict shader variant matching** | Enable this option to use the error shader for rendering if a shader variant is missing in the Player build and display an error in the console. The error specifies the shader, subshader index, pass, and keywords used for shader variant search  
**Keep Loaded Shaders Alive** | Keep all loaded shaders alive and prevent unloading.  
### Shader Variant Loading Settings
Use these settings to control how much memory **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) use at runtime.
**Property** | **Description**  
---|---  
**Default chunk size (MB)** | Sets the maximum size of compressed shader variant data chunks Unity stores in your built application for all platforms. The default is `16`. For more information, refer to [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-loading.html#dynamicloading).  
**Default chunk count** | Sets the default limit on how many decompressed chunks Unity keeps in memory on all platforms. The default is `0`, which means there’s no limit.  
**Override** | Enables overriding **Default chunk size** and **Default chunk count** for this build target.  
**Chunk size (MB)** | Overrides the value of **Default chunk size (MB)** on this build target.  
**Chunk count** | Overrides the value of **Default chunk count** on this build target.  
### Script Compilation
![Script compilation settings for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/ProjectSettingsScriptCompilation.png) Script compilation settings for desktop platforms **Property** | **Description**  
---|---  
**Scripting Define Symbols** | Set custom compilation flags. For more details, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).  
**Additional Compiler Arguments** | Add entries to this list to pass additional arguments to the Roslyn compiler. Use one new entry for each additional argument.  
To create a new entry, press the ‘+’ button. To remove an entry, press the ‘-’ button.  
When you have added all desired arguments, click the **Apply** button to include your additional arguments in future compilations. The **Revert** button resets this list to the most recent applied state.  
**Suppress Common Warnings** | Disable this setting to display the C# warnings [CS0169](https://docs.microsoft.com/en-us/dotnet/csharp/misc/cs0169) and [CS0649](https://docs.microsoft.com/en-us/dotnet/csharp/misc/CS0649).  
**Allow ‘unsafe’ Code** | Enable support for compiling [‘unsafe’ C# code](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/keywords/unsafe) in a pre-defined assembly (for example, `Assembly-CSharp.dll`).   
For Assembly Definition Files (`.asmdef`), click on one of your `.asmdef` files and enable the option in the Inspector window that appears.  
**Use Deterministic Compilation** | Disable this setting to prevent compilation with the -deterministic C# flag. With this setting enabled, compiled assemblies are byte-for-byte identical each time they’re compiled.  
For more information, refer to Microsoft’s [deterministic compiler option documentation](https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/compiler-options/deterministic-compiler-option).  
### Optimization
![Optimization settings for desktop platforms](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PlayerSetPCOther-Optimize.png) Optimization settings for desktop platforms **Property** | **Description**  
---|---  
**Prebake Collision Meshes** | Adds collision data to [Meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Mesh.html) at build time.  
**Preloaded Assets** | Sets an array of Assets for the player to load on startup.   
To add new Assets, increase the value of the **Size** property and then set a reference to the Asset to load in the new **Element** box that appears.  
**Strip Engine Code** | Enable this option if you want the Unity Linker tool to remove code for Unity Engine features that your Project doesn’t use. This setting is only available with the [IL2CPP scripting backend](https://docs.unity3d.com/6000.0/Documentation/Manual/IL2CPP). Most apps do not use every available DLL. This option strips out DLLs that your app doesn’t use to reduce the size of the built Player. If your app is using one or more classes that would normally be stripped out under your current settings, Unity displays a debug message when you try to build the app.  
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
### Stack Trace
Select your preferred stack trace method by enabling the option that corresponds to each Log Type (**Error** , **Assert** , **Warning** , **Log** , and **Exception**) based on the type of logging you require. For more information, refer to [stack trace logging](https://docs.unity3d.com/6000.0/Documentation/Manual/StackTrace.html). 
**Property** | **Description**  
---|---  
**None** | No logs are ever recorded.  
**ScriptOnly** | Logs only when running **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts).  
**Full** | Logs all the time.  
### Legacy
Enable **Clamp BlendShapes (Deprecated)** option to clamp the range of blend shape weights in [SkinnedMeshRenderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html).
### Capture Logs
Enable **Capture Startup Logs** option to capture logs emitted at startup by the engine. These logs can then be retrieved later on, which can be useful when using third-party logging libraries for example.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/UnityasaLibrary-Windows.html)
Integrating Unity into Windows applications
[](https://docs.unity3d.com/6000.0/Documentation/Manual/windows-develop.html)
Develop for Windows
