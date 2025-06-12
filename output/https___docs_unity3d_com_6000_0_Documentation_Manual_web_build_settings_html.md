* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/web-build-settings.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * Web build settings


[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
Build and distribute a Web application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
Web Build folder
# Web build settings
Use the Web **Build Settings** to configure how Unity builds your application for the Web platform.
## Access the build settings for Web
You can update your Web platform build settings from the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.
To access the build settings for Web: 
  1. Go to **File** > **Build Profiles**. 
  2. Select **Web**. 


## Web build settings reference
The following table gives an overview of the Web build settings. 
**Property** | **Description**  
---|---  
**Client Browser Type** | Select the browser client that you want your application to launch at runtime. For example, if you choose System Default, then your application launches the default browser, and removes the **Path to Client Browser** setting. 
  * **System Default** : This is the default setting. Select this option to launch the application in the default browser.
  * **Microsoft Edge** : Select this option to launch the application in Edge browser.
  * **Apple Safari** : Select this option to launch the application in Safari.
  * **Mozilla Firefox** : Select this option to launch the application in Firefox.
  * **Google Chrome** : Select this option to launch the application in Chrome.
  * **Chromium** : Select this option to launch the application in a Chromium browser.

  
**Path to Client Browser** | Specify the path to the browser client that you want your application to launch at runtime.  
  
**Note:** This option is only visible if the Client Browser Type isn’t set to the default browser  
**Texture Compression** | The texture compression format to use for the build. For more information, refer to [Web texture compression](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-texture-compression.html). 
  * **Use Player Settings** : This is the default selection. It uses the texture compression format you set in the [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsWebGL.html)Settings that let you set various player-specific options for the final game built by Unity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#PlayerSettings) window.
  * **ETC2** : Uses ETC2 format, which is widely supported on mobile devices.
  * **ASTC** : Uses ASTC format, which is widely supported on mobile devices.
  * **DXT** : Uses DXT format, which is widely supported on desktop devices.

  
**Development Build** | Include scripting debug symbols and the [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) in your build. Use this setting when you want to test your application. When you select this option, Unity sets the `DEVELOPMENT_BUILD` scripting define symbol. Your build then includes preprocessor directives that set `DEVELOPMENT_BUILD` as a condition.  
  
For more information, refer to [Platform dependent compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).  
**Code Optimization** | Select the optimization mode to use for compiling the Web code. 
  * **Shorter Build Time** : This is the default setting. Select this option to generate Web code that takes the least amount of time to build.
  * **Runtime Speed** : Select this option to generate Web code that’s optimized for runtime performance, at the expense of taking a longer time to build.
  * **Runtime Speed with LTO** : This is the same as Runtime Speed, but with an additional Link Time Optimizations (LTO) stage (sometimes called Whole Program Optimization). Enable LTO when compiling shipping builds for deployment to end users.
  * **Disk Size** : Select this option to favor optimizations that minimize build size, at the expense of taking a longer time to build. It’s recommended to select this option when targeting mobile web browsers that might have limits on the size of WebAssembly files that can be loaded. Smaller disk sizes generally result in shorter page startup times.
  * **Disk Size with LTO** : This is the same as Disk Size but enables an additional Link Time Optimizations (LTO) stage. This is also known as Whole Program Optimization. Select this option when compiling shipping builds for deployment to end users.

  
**Autoconnect Profiler** | Automatically connect the Unity Profiler to your build. For more information, refer to [Profiler](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html).  
  
**Note** : This option is available only if you select **Development Build**.  
**Deep Profiling** | Allow the Profiler to process all your script code and record every function call, returning detailed profiling data. For more information, refer to [Deep Profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerWindow.html#deep-profiling).   
  
This property is available only if you enable **Development Build**.   
  
**Note** : Enabling **Deep Profiling** might slow down script execution.  
## Additional Resources
  * [Build and distribute a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
  * [Build your Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
  * [Deploy a Web application](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-deploying.html)
  * [BuildOptions API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building-distribution.html)
Build and distribute a Web application
[](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-building.html)
Web Build folder
