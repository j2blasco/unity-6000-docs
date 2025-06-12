* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/build-for-linux.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [Linux](https://docs.unity3d.com/6000.0/Documentation/Manual/linux.html)
  * Build a Linux application


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)
Linux build settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linux-editor-troubleshooting.html)
Troubleshooting the Linux Editor issues
# Build a Linux application
To build your Unity application on the Linux platform, use the following steps:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Linux** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Linux** platform.
  3. Select **Switch Profile** to set the new build profile as the active profile.
  4. Select **Build** or **Build And Run**. For more information on these options, refer to [Build your application](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles-reference.html#build-options).
  5. In the Linux file chooser window, select the destination for Unity to place the build.
  6. In the **Name** field, enter an appropriate name for the build.
  7. Select **Save**. This starts the build process.


## Linux Player build binaries
When you build a Unity application on the Linux platform, Unity produces the following files, where `ProjectName` is the name of your application:
  * `ProjectName.x86_64`: This is the project executable file for your application. It contains the program entry point that initiates the Unity engine when launched.
  * `UnityPlayer.so`: This `.so` file contains all the native Unity engine code. It’s signed with the Unity Technologies certificate allowing you to verify that no malicious entities have tampered with your engine code.
  * `*.pdb` files: These are symbol files you can use to debug managed (C#) code. Unity copies these files to the build directory if you enable ****Development Build** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild)** in the **Platform Settings** section of the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)A set of customizable configuration settings to use when creating a build for your target platform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/build-profiles.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Buildprofile) window.
  * `*_s.debug` files: These are symbol files you can use to debug native (C/C++) code. Unity copies these files to the build directory if you enable **Development Build** in the **Platform Settings** section of the [Build Profiles](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html) window.
  * `ProjectName_Data` folder: This folder contains all the data needed to run your application.
  * `libdecor-0.so.0`: This `.so` file is a Linux shared library used by Wayland clients to manage client-side window decorations. It ensures consistent window behavior and appearance across various compositors.
  * `libdecor-cairo.so`: This `.so` file is a Linux shared library that integrates Cairo graphics with `libdecor`. It renders client-side decorations in Wayland to enhance visual consistency and performance.


If you’re using the **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) **scripting backend** A framework that powers scripting in Unity. Unity supports three different scripting backends depending on target platform: Mono, .NET and IL2CPP. Universal Windows Platform, however, supports only two: .NET and IL2CPP. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ScriptingBackend), your application Player build also includes the following file and folder:
  * `GameAssembly.so`: This `.so` file contains all managed (C#) game logic and **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) converted into native code (C/C++) for enhanced performance.
  * `ProjectName_BackUpThisFolder_ButDontShipItWithYourGame` folder: This folder contains intermediate files generated during IL2CPP builds that are useful for debugging rather than distribution.


## Additional resources
  * [Linux build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html)
Linux build settings reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/linux-editor-troubleshooting.html)
Troubleshooting the Linux Editor issues
