* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsStandaloneBinaries.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/Windows.html)
  * Windows build settings reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
Windows Player: IL2CPP Scripting Backend
[](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
XR
# Windows build settings reference
Use these settings to configure how Unity builds your application for Windows platform. You can update your Windows build settings from the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/BuildSettings.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.
**Property** | **Description**  
---|---  
**Architecture** | Select the CPU to build for (only applies to Build And Run). 
  * **Intel 64-bit** : Use Intel/AMD 64-bit CPU architecture.
  * **Intel 32-bit** : Use 32-bit Intel CPU architecture.
  * **ARM 64-bit** : Use 64-bit ARM CPU architecture.

  
**Build and Run on** | Select the target device or transport to deploy and launch the app during **Build And Run**. 
  * **Local Machine** : Deploys and launches the app on the local PC.
  * **Remote Device (via Device Portal)** : Deploys and launches the app to a connected device over the Device Portal transport.

  
**Copy PDB files** | Enable this setting to include Microsoft program database (PDB) files in the built Player. PDB files contain debugging information for your application, but might increase the size of your Player.  
**Create Visual Studio Solution** | Enable this setting to generate Visual Studio Solution files for your Project, so you can build your final executable in Visual Studio.  
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

  
## Windows Player build binaries
When you build a Unity title on the Windows platform, Unity produces the following files, where `ProjectName` is the name of your application:
  * `ProjectName.exe` - The project executable file, that’s your project application. This contains the program entry point which calls into the Unity engine when launched. The path to the source code for `ProjectName.exe` is in the `WindowsPlayer` folder: `Editor\Data\PlaybackEngines\WindowsStandaloneSupport\Source\WindowsPlayer`.
  * `UnityPlayer.dll` - The DLL file that contains all the native Unity engine code. It’s signed with the Unity Technologies certificate, which lets you verify that no malicious entities have tampered with your engine.
  * `*.pdb files` - Symbol files for debugging. Unity copies these to the build directory if you enable **Copy PDB files** in the **Build Profiles** window.
  * `WinPixEventRuntime.dll` - This DLL enables [Introducing PIX on Windows (beta)](https://blogs.msdn.microsoft.com/pix/2017/01/17/introducing-pix-on-windows-beta/) support. Unity only creates this file if you enable the ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** option in the **Build Profiles** window.
  * `ProjectName_Data folder` - This folder contains all the data needed to run your application.


## Modify and rebuild your application
To modify your application or distribute the built code (for example, if you want to sign it or modify the built executable metadata), you must rebuild your project and place the output in your built game directory.
Modifying the built executable metadata, such as the publisher or company name is necessary to ensure that your application is correctly identified by the system. For example, various operating system tools and dialogs, such as Windows firewall use the executable metadata to display your application’s information, such as the publisher or company name. The Unity Player executable included with the Unity installation is pre-built and might not reflect details specific your application. In this case, you can modify the executable metadata to include your application’s information.
To modify the metadata, follow these steps:
  1. Enable the **Create Visual Studio Solution** setting to generate Visual Studio Solution files for your project and build your project in the Unity Editor.
  2. Open the build folder and locate a subfolder with the same name as your project. In the subfolder, find the `WindowsPlayerVersion.rc` file and open it with a text editor.
  3. Remove the lines of code that include conditional compilation directive `#if defined(BUILDING_UNITY_PLAYER_DLL)` and the corresponding `#endif`.
  4. Modify any metadata, such as `CompanyName`, `FileVersion`, `FileDescription`, or `ProductName` as required. For more information on these fields, refer to the documentation on [StringFileInfo BLOCK Statement](https://learn.microsoft.com/en-us/windows/win32/menurc/stringfileinfo-block).
  5. Open the Visual Studio Solution from the build folder using Visual Studio and rebuild your project.


**Note** : To build your application outside of Unity, you need [Visual Studio](https://www.visualstudio.com/) 2019 or 2022 with Desktop development with C++ workload installed.
## Additional resources
  * [Visual Studio project generation for Windows](https://docs.unity3d.com/6000.0/Documentation/Manual/VisualStudioprojectgenerationWindows.html)
  * [BuildOptions API reference](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/WindowsPlayerIL2CPPScriptingBackend.html)
Windows Player: IL2CPP Scripting Backend
[](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
XR
