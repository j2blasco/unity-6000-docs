* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-settings.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Embedded systems](https://docs.unity3d.com/6000.0/Documentation/Manual/embedded-systems.html)
  * [QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx.html)
  * [Build and deliver for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
  * QNX build settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
Build and deliver for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-command-line.html)
Build for QNX from the command line
# QNX build settings reference
Use the QNX build settings to configure and build your application for the QNX platform. The QNX build settings are included in the **Platform Settings** section of the [Build Profiles window](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html).
**Property** | **Description**  
---|---  
**QNX Version** | The target OS version for QNX is automatically detected depending on the QNX environment. For example, Neutrino RTOS 7.0 or Neutrino RTOS 7.1.  
**Architecture** | Choose the CPU architecture to build for the QNX platform:  

  * **x64** : 64-bit CPU
  * **arm64** : 64-bit ARM CPU

  
**Remote Device** | Deploy and launch the app to a connected device on a remote device based on the connection and authentication information you provide. 
  * **Address (required)** : The address of the remote device. You can also specify a port by adding a colon after the address (for example, 10.110.91.3:2121).
  * **Username (optional)** : The user name on the remote device.
  * **Exports** : Specify the additional exports, if they’re required to launch the device remotely. Multiple environment variables are separated by a space. For example, `ENV_VAR1=1 ENV_VAR2=2`.
  * **Install Path** : The installation path for the application. If not set, the default value `~tmp/unity/test` will be used.

  
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

  
## Additional resources
  * [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile)
  * [Build and deliver for QNX](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-and-deliver.html)
Build and deliver for QNX
[](https://docs.unity3d.com/6000.0/Documentation/Manual/qnx-build-command-line.html)
Build for QNX from the command line
