* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
  * XR packages


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
Overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)
AR development in Unity
# XR packages
The Unity packages that support **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) development fall into two broad categories:
  * [XR provider plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html#plug-ins): Provider plug-ins enable support for XR devices and platforms. For example, the Apple ARKit **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) allows **AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) applications to run on the iOS platform and the OpenXR plug-in allows applications to run on several **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) and **MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR) systems.
  * [Feature and tool support packages](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html#support-packages): These packages provide features and tools for developing XR applications.


## XR provider plug-ins
The Unity XR plug-in framework provides the basis for XR development in Unity. You can add support for an XR device to a project by installing and enabling the relevant XR plug-in. You can add or remove plug-ins to the project at any time.
For instructions on how to add XR plug-ins to your project using the **XR Plug-in Management** system, refer to [XR Project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html).
Unity supports the following XR plug-ins:
Plug-in | Supported devices  
---|---  
[Apple ARKit](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.0/) | [iOS devices](https://developer.apple.com/documentation/arkit/verifying_device_support_and_user_permission)  
[Google ARCore](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.0/) | Handheld [Android devices](https://developers.google.com/ar/devices)  
[Microsoft HoloLens](https://docs.microsoft.com/en-us/windows/mixed-reality/develop/unity/unity-development-overview) | HoloLens, HoloLens 2  
[Microsoft Windows Mixed Reality](https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/mixed-reality-openxr-plugin) | Microsoft supported package for HoloLens and Windows Mixed Reality headsets (various manufacturers).   
  
**Note:** In Unity 2021+. use the OpenXR provider plug-in for Windows Mixed Reality. The previous WMR provider package is not supported beyond Unity 2020.3. Refer to [Windows Mixed Reality support](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html#wmr-support) for more information.  
[Oculus](https://docs.unity3d.com/Packages/com.unity.xr.oculus@4.3/) | Oculus Rift, Meta Quest 2, Quest 3, Quest Pro.  
[OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.12/) | Any device with an OpenXR runtime, including Meta headsets, Vive headsets, Valve SteamVR, HoloLens, Windows **Mixed Reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedReality), and others.  
[Unity OpenXR: Meta](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@latest) | Meta Quest devices.  
[Unity OpenXR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@0.4/manual/index.html) | Android XR devices.  
PlayStation VR (available to registered PlayStation developers) | Sony PS VR and PS VR2 devices. Refer to [PlayStation Partners](https://partners.playstation.net/) for more information.  
[Apple visionOS XR](https://docs.unity3d.com/Packages/com.unity.xr.visionos@1.0/) | Apple Vision Pro  
Refer to [XR Platform System Requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#xr) for system requirements for developing XR projects in Unity.
**Notes:**
  * One plug-in can support more than one type of XR device and more than one operating system.
  * Plug-ins for additional XR devices might be available from their platform creators or other third parties.
  * The [OpenXR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.12) integrates core OpenXR features for all XR platforms. [Unity OpenXR: Meta](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@latest) integrates Meta-specific vendor extensions to provide additional features for Meta Quest devices.
  * Unity does not directly support XR on the Web platform. Projects that add support for WebXR, such as [Needle Engine](https://engine.needle.tools/docs/xr.html), [SimpleWebXR](https://github.com/Rufus31415/Simple-WebXR-Unity), and [WebXR Export](https://github.com/De-Panther/unity-webxr-export), are available. (Unity does not test or guarantee compatibility with third party tools.)


## XR support packages
Unity’s XR packages build on the XR plug-in framework to add additional application-level features and developer tools.
The XR packages include:
Package | Description  
---|---  
[XR Plug-in Management](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html) | Adds **Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings) for managing the platforms and plug-ins used by a Unity XR project. Refer to [Project setup](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html) for information about managing XR plug-ins.  
[AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/) | Provides cross-platform AR features, such as plane detection, meshing, and object tracking. Required for developing AR applications with the Unity XR packages.  
[XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/) | Provides interaction components for adding controller-based interaction and manipulation, UI interaction, and movement. Supports VR, MR, and AR.  
[XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/) | Provides an interface for accessing hand tracking data in an XR application. You must also use a provider plug-in that supports hand tracking, such as [OpenXR version 1.12](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.12).  
[PolySpatial visionOS packages](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest) | A set of packages that provides support for VR and AR/MR apps on the Apple Vision Pro. Requires a [Unity Pro, Enterprise, or Industry subscription](https://unity.com/pricing).  
[Unity Mars](https://docs.unity3d.com/Packages/com.unity.mars@latest/) | Provides components and tools for adapting AR content to the user’s surroundings. For example, it supplies a standard way of querying the environment to find suitable locations for adding your digital content to the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Requires a license that includes Unity Mars. Refer to [Unity Mars](https://unity.com/products/unity-mars) for information about license requirements.  
[XR Core Utilities](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.3/) | Contains software utilities used by other XR plug-ins and packages. Typically installed in your project as a dependency of other XR packages.  
[XR Legacy Input Helpers](https://docs.unity3d.com/Packages/com.unity.xr.legacyinputhelpers@2.1/) | Contains software utilities related to XR input. This package is being phased out, but is still installed as a dependency by some XR packages.  
**Note:** If you use the AR Foundation package in a project, the version numbers of AR Foundation, ARCore, and ARKit must all match. That is, if you are using version 6.0 of the AR Foundation package, you must also use version 6.0 of the ARCore and ARKit packages.
## XR platform support notes
The following information provides details about support for specific XR devices.
### Apple visionOS support
You can develop windowed apps with only the visionOS platform support module installed. A windowed app operates in a single, flat window, much like a window on a desktop platform. A user’s gaze and hand gestures are translated into touch input by the visionOS operating system (direct access to the gaze and hand tracking data is not supported in this mode.) You can create or port non-XR Unity applications and games to the Apple Vision Pro device as windowed apps. Refer to [visionOS platform](https://docs.unity3d.com/6000.0/Documentation/Manual/visionOS.html) for more information.
To develop XR apps (VR, AR, or MR), you must install the visionOS and PolySpatial packages. You must have a [Unity Pro, Enterprise, or Industry subscription](https://unity.com/pricing) to use these packages. Refer to the [PolySpatial visionOS documentation](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest) for more information.
### Magic Leap support
Developing for the Magic Leap 1 is not supported after Unity 2020.3. Developing for the Magic Leap 2 is not supported after Unity 6.0.
Unity version | Package version | Device model  
---|---|---  
Unity 2019.4–2020.3 | [com.unity.xr.magicleap@6.4](https://docs.unity3d.com/Packages/com.unity.xr.magicleap@6.4) | Magic Leap 1  
Unity 2021.1–2022.1 | No version supported. | None  
Unity 2022.2–6000.0 | [com.unity.xr.magicleap@7.0](https://docs.unity3d.com/Packages/com.unity.xr.magicleap@7.0) | Magic Leap 2  
Unity 6001.0+ | No version supported (end of life). | None  
### Windows Mixed Reality support
Use the OpenXR provider plug-in to develop for Windows Mixed Reality devices.
To configure the OpenXR provider plug-in for Windows MR:
  1. In the Unity Editor, open **Edit > Project Settings**
  2. Select the **XR Plug-in Management** category.
  3. Choose the **Windows, Mac, Linux** tab.
  4. In the **Plug-in Providers** list, enable **OpenXR**.
The OpenXR package installs, if necessary.
  5. Click the Help icon next to the **Windows Mixed Reality feature group** option to open the [Microsoft Mixed Reality OpenXR Plugin setup instructions](https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/mixed-reality-openxr-plugin).
  6. Follow the instructions to install the Microsoft Mixed Reality OpenXR plug-in. (The **Microsoft Mixed Reality Feature Tool** program lists the plug-in under its **Platform Support** category.)
  7. Enable the **Windows Mixed Reality feature group**.


After you have installed the plug-in, review the **OpenXR** settings under **XR Plug-in Management**.
### Meta Quest support
Unity supports development for Meta Quest 2, 3, 3S, and Quest Pro. Refer to [Develop for Meta Quest workflow](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-meta-quest-develop.html) to get started with development for Quest devices.
#### Quest 1 support
Meta has dropped support for the Quest 1 device as of version 51.0 of their Platform SDK. The Platform SDK is included in version 51.0 of the Oculus Integration package on the Unity **Asset Store** A growing library of free and commercial assets created by Unity and members of the community. Offers a wide variety of assets, from textures, models and animations to whole project examples, tutorials and Editor extensions. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetStore.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AssetStore). To continue developing for the Quest 1, you must use version 50 or earlier of the Oculus Integration package. If needed, you can download this version from the Meta Quest downloads page: <https://developer.oculus.com/downloads/package/unity-integration/50.0>.
In addition, version 4+ of the Oculus provider plug-in package no longer supports Quest 1 development. You must use an earlier version of the Oculus provider plug-in to continue developing for the Quest 1. Because Oculus 4.0 is the **verified package** When a package passes release cycle testing for a specific version of Unity, it receives the _Verified For_ designation. This means that these packages are guaranteed to work with the designated version of Unity.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Verifiedpackage) version on Unity 2022.3, you must downgrade to the lower package version.
To install version 3.3.0 of the Oculus package:
  1. Open your project in the Unity Editor.
  2. Click [Oculus XR plug-in version 3.3.0](com.unity3d.kharma:upmpackage/com.unity.xr.oculus@3.3.0).
_The Package Manager window opens, showing the**Add package by name** dialog_
  3. Click **Add** to install the last compatible version of the plug-in.


Alternately, you can open the **Add package by name** dialog manually and enter the package id and version. You can also edit the project’s **package manifest** Each package has a _manifest_ , which provides information about the package to the Package Manager. The manifest contains information such as the name of the package, its version, a description for users, dependencies on other packages (if any), and other details. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Packagemanifest) file directly to reference the required package version:
```
"com.unity.xr.oculus": "3.3.0"

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
Overview
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)
AR development in Unity
