* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/linux-il2cpp-crosscompiler.html

  * [Scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting.html)
  * [Compilation and code reload ](https://docs.unity3d.com/6000.0/Documentation/Manual/compilation-and-code-reload.html)
  * [Scripting backends](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends.html)
  * [IL2CPP Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)
  * Linux IL2CPP cross-compiler


[](https://docs.unity3d.com/6000.0/Documentation/Manual/handling-il2cpp-additional-args.html)
Handling platform specific settings for IL2CPP additional arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/il2cpp-managed-stack-traces.html)
Managed stack traces with IL2CPP
# Linux IL2CPP cross-compiler
The Linux **IL2CPP** A Unity-developed scripting back-end which you can use as an alternative to Mono when building projects for some platforms. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-backends-il2cpp.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#IL2CPP) cross-compiler is a set of sysroot and toolchain packages that allow you to build Linux IL2CPP Players on any Standalone platform without needing to use the Linux Unity Editor or rely on Mono. 
If you meet the prerequisites, Unity automatically installs these packages for you when you choose the Linux build target. If you want to opt out of this process and use your own sysroot and toolchain packages, go to **Edit** > **Project Settings** > **Toolchain Management** and disable the **Install Toolchain package automatically** checkbox. If you already have these installed, you also need to remove them from the Package Manager. 
**Warning:** Setting additional IL2CPP arguments might affect your project compilation. For more information, refer to [Handling platform specific settings for IL2CPP additional arguments](https://docs.unity3d.com/6000.0/Documentation/Manual/handling-il2cpp-additional-args.html).
## Prerequisites
Unity needs the following to install the IL2CPP cross-compiler packages:
  * Unity 2019.4 or above.
  * Enough available disk space for your chosen Linux toolchain package. For further information, refer to the [Required disk space for Linux toolchain packages](https://docs.unity3d.com/6000.0/Documentation/Manual/linux-il2cpp-crosscompiler.html#requiredDiskSpace).
  * Scripting backend set to IL2CPP. To set the scripting backend to IL2CPP: Go to **Edit** > **Project Setting** > **Player Settings for Linux** > **Other Settings** > **Configuration**. Set the **Scripting Backend** to **IL2CPP**.
  * IL2CPP module. For information on how to install the IL2CPP module, follow the steps documented on [Adding modules](https://docs.unity3d.com/hub/manual/AddModules.html).


## Linux sysroot package
A Linux sysroot package is a directory which includes all the headers and libraries you need to build for Linux.
Every operating system (OS) has its own build systems which vary from one to another. If you build using the headers and libraries of a particular OS, the built Player might not run on other operating systems. To address this, Unity provides a sysroot to build with which works on all supported Linux platforms.
## Linux toolchain packages
Unity provides toolchain packages for macOS, Windows, and Linux. Each of these platforms builds for Linux in a unique way.
A Linux toolchain package is a set of tools (including the compiler and linker) that Unity needs to build for Linux from each of these operating systems.
## Required disk space for Linux toolchain packages 
Make sure you have enough disk space to account for the package download, decompression, and use.
In the rare instances where you are unsure whether you have enough space, define a UNITY_SYSROOT_CACHE environment variable and use it to store the uncompressed sysroots and toolchain packages. An environment variable is a variable that you set outside of Unity which is available for Unity to reference. In this case, you set a cache that Unity can reference when decompressing the sysroot and toolchain packages. Environment variables are specific to your operating system, so you need to follow your system’s guidelines to set them. 
The table below shows the total disk space requirements for each toolchain package.
Toolchain package | Required disk space  
---|---  
com.unity.toolchain.linux-x86_64 | 462 MB  
com.unity.toolchain.macos-x86_64-linux-x86_64 | 2 GB  
com.unity.toolchain.win-x86_64-linux-x86_64 | 2 GB  
## Using the Linux IL2CPP cross-compiler
If you meet all the prerequisites on this page, you can build your project as a Linux Player. Unity automatically uses the Linux IL2CPP cross-compiler at build time.
To build a Linux Player, follow these steps:
  1. Open the **Build Profiles** window (menu: **File** > **Build Profiles**).
  2. From the list of platforms in the **Platforms** panel, select **Linux** or [create a build profile](https://docs.unity3d.com/6000.0/Documentation/Manual/create-build-profile.html) for the **Linux** platform.
  3. Select **Switch Platform**.
  4. Select **Build** or **Build And Run**.


## Additional resources
  * [How to add modules in the Unity Editor](https://docs.unity3d.com/hub/manual/AddModules.html)
  * [Linux build settings reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Buildsettings-linux.html) platform docs.
  * [Linux Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/PlayerSettings-linux.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/handling-il2cpp-additional-args.html)
Handling platform specific settings for IL2CPP additional arguments
[](https://docs.unity3d.com/6000.0/Documentation/Manual/il2cpp-managed-stack-traces.html)
Managed stack traces with IL2CPP
