* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/XRPluginArchitecture.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
  * XR architecture


[](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)
VR and MR development in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VRReference.html)
XR API reference
# XR architecture
Unity supports **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) development through its **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) framework and a set of feature and tool packages. Go to the [XR Plug-in Management](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-plugin-management.html) category in ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)** to enable XR support in a Unity project and to choose the plug-ins for the XR platforms that your project supports. Use the Unity Package Manager to install the additional feature packages.
The following diagram illustrates the current Unity XR plug-in framework structure and how it works with platform provider implementations:
![The Unity XR plug-in framework structure](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/unity-xr-tech-stack.png)
XR subsystems define a common interface for XR features. XR plug-ins implement these subsystem interfaces to provide data to the subsystem at runtime. Your XR application can access data for an XR feature through Unity Engine and package APIs.
## XR provider plug-in framework
An XR provider plug-in is a Unity plug-in that supports one or more XR device platforms. For example, the ARCore plugin supports the Android **AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) platform on hand-held Android devices, while the OpenXR plug-in supports several XR devices on multiple operating systems. 
An XR provider plug-in implements interfaces called _subsystems_. A plug-in that implements one or more subsystems is called a _provider_ plug-in. Typically, a provider plug-in uses the device platform’s native libraries to implement the Unity interfaces for their devices.
Unity uses subsystem interfaces to communicate with providers for various platforms, powering the XR features of your application. Because of these interfaces, you can reuse the same feature code in your application across all XR devices that have a provider for that feature.
### Subsystems
XR subsystems give you access to XR features in your Unity app. Unity defines a common interface for subsystems so that all provider plug-ins implementing a feature generally work the same way in your app. Often you can change the active provider and rebuild your app to run on a different XR platform, as long as the platforms are largely similar.
The Unity Engine defines a set of fundamental XR subsystems. Unity packages can provide additional subsystems. For example, the AR Subsystems package contains many of the AR-specific subsystem interfaces.
The subsystems defined in the Unity Engine include:
Subsystem | Description  
---|---  
[Display](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRDisplaySubsystem.html) | Stereo XR display.  
[Input](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRInputSubsystem.html) | Spatial tracking and controller input.  
[Meshing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRMeshSubsystem.html) | Generate 3D meshes from environment scans.  
**Note:** Unity applications typically do not interact with subsystems directly. Instead, the features provided by a subsystem are exposed to the application through an XR plug-in or package. For example, the [ARMeshManager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARMeshManager.html) component in the AR Foundation package lets you add the meshes created by the Meshing subsystem to a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)
VR and MR development in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VRReference.html)
XR API reference
