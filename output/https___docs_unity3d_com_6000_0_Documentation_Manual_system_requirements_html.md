* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html

  * [Install and upgrade](https://docs.unity3d.com/6000.0/Documentation/Manual/install-and-upgrade.html)
  * [Install Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
  * System requirements for Unity 6.0 


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
Install Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-installers.html)
Install Unity using installer files
# System requirements for Unity 6.0
This page outlines the system requirements you need to run Unity 6.0 on all supported platforms.
  * [Unity Editor system requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#editor)
  * [Unity Editor platform limitations](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#limitations)
  * [Unity Player system requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#player): 
    * [Mobile](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#mobile)
    * [Console](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#console)Abbreviation of **game console**  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#console)
    * [Desktop](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#desktop)
    * [Server platform](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#server)
    * [Web platform](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#web)
    * [XR platform](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#xr)
      * [Standalone XR devices](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#standalone-xr)
      * [Meta](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#oculus)
      * [OpenXR](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#openxr)
      * [Windows Mixed Reality](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#wmr)
      * [Magic Leap](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#magic)
      * [Google ARCore](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#arcore)
      * [Apple visionOS](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#visionos)
    * [Embedded Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#embedded)


## Unity Editor system requirements
This section lists the hardware and software requirements to run the Unity Editor. Actual performance and rendering quality might vary depending on the complexity of your project.
For all operating systems, the Unity Editor is supported on workstations or laptop form factors running without emulation, container or compatibility layer.
**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 10 version 21H1 (build 19043) or newer (X64), Windows 11 21H2 (build 22000) or newer (Arm64) | X64 architecture with SSE2 instruction set support, Arm64 | DX10, DX11, DX12 or Vulkan capable GPUs | Hardware vendor officially supported drivers  
**macOS** | Big Sur 11 or newer | X64 architecture with SSE2 instruction set support (Intel processors)   
Apple M1 or above (Apple silicon-based processors) | Metal-capable Intel and AMD GPUs | Apple officially supported drivers (Intel processor)   
Rosetta 2 is required for Apple silicon devices running on either Apple silicon or Intel versions of the Unity Editor  
**Linux** | Ubuntu 22.04, Ubuntu 24.04 | X64 architecture with SSE2 instruction set support | OpenGL 3.2+ or Vulkan-capable, Nvidia and AMD GPUs | Gnome desktop environment running on top of X11 or Wayland windowing system, Nvidia official proprietary graphics driver, or AMD Mesa graphics driver. Other configuration and user environment as provided stock with the supported distribution (Kernel, Compositor, etc.)   
**Notes:**   
• **Ubuntu 22.04:** Wayland is supported with AMD graphics cards.   
• **Ubuntu 24.04:** Wayland is supported with AMD graphics cards and Nvidia graphics cards utilizing Nvidia proprietary graphics drivers 550 and above.   
### RAM recommendations for the Unity Editor
To run the Unity Editor on Windows, macOS, or Linux, a minimum of 8 GB RAM is recommended.
However, the amount of RAM required to load and run your project depends on your project’s size and complexity. Larger and more complex projects require additional RAM.
## Unity Editor platform limitations
### Windows on Arm
  * Download and install of Windows on Arm Editor via the Unity Hub is only possible through Hub version v3.7.0 Beta 1 or later. For more information, see the [Unity Hub release notes](https://unity.com/unity-hub/release-notes). 
To switch to the latest beta version of the Hub, change **Preferences** > **Advanced** > **Channel** to **Beta**. Alternatively, re-download Unity: <https://unity.com/download>
  * Unity doesn’t support platforms that don’t provide native Windows Arm64 SDKs. Build for these platforms might still work with x86 emulation for Windows on Arm.
  * Unity doesn’t support packages with third-party binary dependencies that don’t provide native Windows on Arm support. These packages might work with x86 emulation for Windows on Arm.
  * Unity doesn’t support Vulkan for Windows on Arm. 
  * Unity doesn’t support CPU lightmapping for Windows on Arm, only GPU lightmapping.


### Apple
On macOS, secondary Editor windows only maximize, and don’t enter full screen mode.
### Apple silicon devices
Unity doesn’t support CPU lightmapping for Apple silicon devices, only GPU lightmapping.
### Linux
The Linux Editor has the following limitations:
  * Video importing is limited to the VP8 video format.
  * File systems are case sensitive.
  * If the Editor generates a `Pipe error !` message, you must increase the maximum open file limit in your current Editor session. For example, run `ulimit -n 4096` in the terminal before launching the Editor. For more information, refer to the [Troubleshooting Linux Editor issues](https://docs.unity3d.com/6000.0/Documentation/Manual/linux-editor-troubleshooting.html) page.
  * Wayland support for Desktop Linux is currently in experimental stage. To run the Linux player in Native Wayland mode when using a Wayland session, use `-force-wayland` command line argument.


## Unity Player system requirements
This section lists the minimum requirements to build and run the Unity Player. Actual performance and rendering quality might vary depending on the complexity of your project.
### Mobile
**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Android** | 6.0 (API 23)+   
Customized versions of Android must include all supported Google standard APIs. | ARMv7 with Neon Support (32-bit) or ARM64 | OpenGL ES 3.0+, Vulkan | • 1GB+ RAM   
• Supported hardware devices must meet or exceed Google’s Android Compatibility Definition ([Version 9.0](https://source.android.com/compatibility/9/android-9-cdd.html)) limited to the following Device Types:   
1. Handheld (Section 2.2)   
2. Television (Section 2.3)  
3. Tablets (Section 2.6)  
• Hardware must be running Android OS natively. Android within a container or emulator isn’t supported.  
• For development: Android SDK (15/API 35), Android NDK (r27c) and OpenJDK (17), which are installed by default with [Unity Hub](https://docs.unity3d.com/6000.0/Documentation/Manual/android-sdksetup.html).  
**iOS/iPadOS** | 13+ | A8 SoC+ | Metal | • Xcode version 15+   
• For development and debugging: refer to Apple documentation on [XCode support](https://developer.apple.com/support/xcode/).  
• For App Store submission: refer to Apple’s [submission guidelines](https://developer.apple.com/app-store/submitting/) for the required Xcode version.  
**tvOS** | 13+ | A8 SoC+ | Metal | • Xcode version 15+   
• Apple TV HD or newer.  
### Console
For information on PlayStation®4 (including PS VR), PlayStation®5 (including PS VR2), Xbox One, Xbox Series X|S, and Nintendo Switch™, refer to the [Game Development For Console Platforms](https://unity.com/solutions/console) page. To build on console platforms, only Windows versions of Unity are supported. For specific requirements on any additional platform specific software needed, please refer to the developer documentation on the platform holders website, or contact your platform representative directly for further information.
For specific system requirements of the Unity Editor, refer to the version of Unity you are using on the [Unity downloads page](https://unity3d.com/get-unity/download).
**Platform** | **Operating system**  
---|---  
**Nintendo Switch™** | Microsoft Windows 10 Pro (64-bit) English or Japanese version  
**Xbox Series X|S** | Windows 10 64-bit (Version 1709 or higher): Home, Professional, and Enterprise  
**Xbox One** | Windows 10 64-bit (Version 1709 or higher): Home, Professional, and Enterprise  
**PlayStation®4 (including PS VR)** | Windows 10 Pro 64-bit (x64) Version 22H2  
**PlayStation®5 (including PS VR2)** | Windows 10 Pro 64-bit (x64) Version 22H2  
### Desktop
For all operating systems, the Unity Player is supported on workstations, laptop or tablet form factors, running without emulation, container or compatibility layer.
**Operating system** | **Operating system version** | **CPU** | **Graphics API** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 10 version 21H1 (build 19043) or newer | x86, x64 architecture with SSE2 instruction set support, Arm64 | DX10, DX11, DX12 or Vulkan capable GPUs | Hardware vendor officially supported drivers  
For development: IL2CPP scripting backend requires Visual Studio 2019 with C++ Tools component or later and Windows SDK version 10.0.19041.0 or newer  
**Universal Windows Platform** | Windows 10 version 21H1 (build 19043) or newer, Xbox One, Xbox Series X and Series S, HoloLens | x86, x64 architecture with SSE2 instruction set support, Arm, Arm64 | DX10, DX11, DX12 capable GPUs | Hardware vendor officially supported drivers.  
For development: Visual Studio 2019 with C++ Tools component or later and Windows SDK version 10.0.19041.0 or newer.  
**macOS** | Big Sur 11 or newer | Apple Silicon, x64 architecture with SSE2 | Metal capable Intel and AMD GPUs | Apple officially supported drivers.  
For development: IL2CPP scripting backend requires Xcode.  
**Linux** | Ubuntu 22.04, Ubuntu 24.04 | x64 architecture with SSE2 instruction set support   
**Note:** Desktop Linux supports only 64-bit architecture. | OpenGL 3.2+, Vulkan capable GPUs | Gnome desktop environment running on top of X11 or Wayland windowing system.  
Other configuration and user environment as provided stock with the supported distribution (such as Kernel or Compositor)  
Nvidia and AMD GPUs using Nvidia official proprietary graphics driver, or AMD Mesa graphics driver.   
**Notes:**   
• **Ubuntu 22.04:** Wayland is supported with AMD graphics cards.   
• **Ubuntu 24.04:** Wayland is supported with AMD graphics cards and Nvidia graphics cards utilizing Nvidia proprietary graphics drivers 550 and above.  
### Server platform
**Operating system** | **Operating system version** | **CPU** | **GPU** | **Additional requirements**  
---|---|---|---|---  
**Windows** | Windows 10 version 21H1 (build 19043) or newer, running on workstation and rack form factors, without emulation or compatibility layer | x86, x64 architecture with SSE2 instruction set support, Arm64 | No explicit GPU support | Hardware vendor officially supported drivers  
**macOS** | Big Sur 11 or newer running on workstation and rack form factors, without emulation or compatibility layer | Apple Silicon, x64 architecture with SSE2 instruction set support, Apple silicon | No explicit GPU support | Hardware vendor officially supported drivers  
**Linux** | Ubuntu 22.04 (AMD64), Ubuntu 24.04 (AMD64), running on workstation and rack form factors, without emulation or compatibility layer | x64 architecture with SSE2 instruction set support | No explicit GPU support | Hardware vendor officially supported drivers  
### Web platform
**Operating system running browsers** | **Hardware** | **Additional requirements**  
---|---|---  
**Windows, macOS, and Linux** | Workstation and laptop form factors | Versions of Chrome, Firefox, Safari or Edge (Chromium-based) that are:  
• WebGL 2.0 capable  
• HTML 5 standards compliant  
• 64-bit  
• WebAssembly capable  
**Android and iOS** | Android or iOS device | Browser requirements:   
• iOS Safari 15 and newer  
• Chrome 58 and newer  
### XR platform system requirements
To enable **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) and properly configure your Unity project, follow the steps outlined in the [XR plug-in architecture](https://docs.unity3d.com/6000.0/Documentation/Manual/XRPluginArchitecture.html) page.
### Standalone XR devices
**Device** | **Device software**  
---|---  
Magic Leap 2 | Magic Leap 2 Core OS version 1.0+  
Meta Quest 1 | Quest software version 50 or earlier (Refer to [Quest 1 support](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html#xr-quest1-support) for more information.)  
Meta Quest 2 | Quest software version 39+  
Meta Quest Pro | Quest software version 46+  
Meta Quest 3 | Quest software version 59+  
Microsoft HoloLens 1 | Windows 10 Holographic version 1809+  
Microsoft HoloLens 2 | Windows Holographic version 1903+  
### Meta desktop XR: Rift, Rift S
**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | Windows 10+  
**CPU** | [See Oculus recommended specifications.](https://support.oculus.com/248749509016567/?locale=en_US)  
**GPU** | [See Oculus recommended specifications.](https://support.oculus.com/248749509016567/?locale=en_US)  
**Graphics API** | DX11  
### OpenXR
Refer to the [OpenXR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest/index.html) documentation for a list of compatible runtimes.
### Windows Mixed Reality
**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | Windows 10 RS4+  
**CPU** | Intel 64-bit  
**Graphics API** | DX11  
### Google ARCore
**Specification** | **Minimum requirement**  
---|---  
**Operating system version** | See list of [ARCore-supported devices](https://developers.google.com/ar/devices).  
**CPU** | ARM 32-bit and 64-bit  
**Graphics API** | OpenGL ES 3.0+  
**Latest supported SDK version** | ARCore 1.24  
### Apple visionOS
**Specification** | **visionOS 1** | **visionOS 2**  
---|---|---  
**Operating system version** | visionOS 1 | visionOS 2.0  
**Graphics API** | Metal or RealityKit | Metal or RealityKit  
**Xcode version** | 15.2+ | Xcode 16 Beta 6  
**Additional requirements** | • Apple silicon macOS build of the Unity Editor. The Intel version of the Unity Editor on macOS does not support visionOS development.  
• Virtual reality, mixed reality, and hybrid app development requires [Unity PolySpatial](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest).  
**Note:** You can create or update Xcode projects using the visionOS platform module in the Unity Editor on Windows. You must use an Apple silicon computer to run Xcode itself, including to make development and release builds of your app.
### Embedded systems
Support for embedded platforms such as Embedded Linux and QNX is available for a wide variety of chipsets as part of the [Premium Runtimes](https://docs.unity.com/#Premium%20Runtimes). This includes support for Linux on ARM based chipsets and additional APIs for Android Automotive.
The following table lists the recommended system requirements for Unity on embedded systems.
**Operating system** | **RAM** | **CPU** | **GPU**  
---|---|---|---  
Embedded Linux | 1GB+ | Dualcore x64, ARM64 | OpenGL ES 3 or Vulkan 1.1 Capable  
QNX | 1GB+ | Dualcore x64, ARM64 | OpenGL ES 3  
Android (Automotive) system requirements are the same as Android under [Mobile](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#mobile).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GettingStartedInstallingUnity.html)
Install Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/install-unity-with-installers.html)
Install Unity using installer files
