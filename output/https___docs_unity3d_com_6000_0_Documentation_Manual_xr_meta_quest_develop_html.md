* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-meta-quest-develop.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [XR project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html)
  * Develop for Meta Quest workflow


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-plugin-management.html)
XR Plug-in Management settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-run.html)
Run an XR application
# Develop for Meta Quest workflow
Unity supports development for Meta Quest 2, 3, and 3S, and Quest Pro.
The following sections outline Unity’s resources and packages to develop for Meta Quest devices.
## Packages
Unity provides multiple packages that you can use to develop for Meta Quest devices. The route you choose to develop for Meta Quest depends on whether you’re also targeting other **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) platforms.
Refer to the following table to understand when to use each of Unity’s Meta Quest-compatible packages:
**Package** | **Description** | ****VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR)/**MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR)** | **Target platform**  
---|---|---|---  
[Unity OpenXR plug-in](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.14/manual/index.html) | Integrates core OpenXR features. | VR and MR | All [OpenXR runtimes.](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.13/manual/index.html#runtimes)  
[Unity Meta OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@2.1/manual/index.html) | Integrates Meta-specific vendor extensions of OpenXR to provide additional features for Meta Quest devices. Provides Meta Quest integration for [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/index.html) to enable **mixed reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedReality) features. | VR and MR | Provides additional OpenXR features for Meta Quest devices, such as Passthrough.  
[Oculus XR plug-in](https://docs.unity3d.com/Packages/com.unity.xr.oculus@4.4/manual/index.html) | Tools, SDKs and resources for VR development on Quest. | VR | Meta Quest devices only.  
**Tip:** You can use the Unity OpenXR **plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) and the Unity Meta OpenXR package together to develop a cross-platform application that has additional features tailored for Meta Quest devices.
**Note:** From OpenXR 1.14, the [Unity OpenXR: Meta 2.1](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@2.1/manual/index.html) package is at feature parity with the [Oculus plugin](https://docs.unity3d.com/Packages/com.unity.xr.oculus@4.4/manual/index.html). Unity will focus feature development on OpenXR, and recommends that users of the Oculus XR plugin migrate to OpenXR for long-term support and cross-platform compatibility.
To learn more about the packages Unity provides for XR development, refer to [XR packages](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html).
### Meta packages
Meta also provides packages to develop for Meta Quest in Unity. Refer to Meta’s [Import XR packages](https://developers.meta.com/horizon/documentation/unity/unity-package-manager/#meta-xr-packages-overview) documentation to learn about the packages Meta provides.
**Note:** These packages and related documentation are maintained by Meta.
## Templates
You can use the following templates as a starting point for your Meta Quest project:
  * [Mixed Reality template](https://docs.unity3d.com/Packages/com.unity.template.mixed-reality@2.0)
  * [VR Template](https://docs.unity3d.com/Packages/com.unity.template.vr@9.0)
  * [VR Multiplayer template](https://docs.unity3d.com/Packages/com.unity.template.vr-multiplayer@2.0)
  * [Mixed Reality multiplayer tabletop template](https://docs.unity3d.com/Packages/com.unity.template.mr-multiplayer@1.0/manual/index.html)


Refer to [Create an XR project](https://docs.unity3d.com/Manual/xr-create-projects.html) to understand how to use templates as a starting point for your project.
## Additional resources
  * [Get started developing for Meta Quest 3 with Unity](https://unity.com/blog/engine-platform/get-started-developing-for-quest-3-with-unity) (Unity blog post)
  * [Standalone XR device system requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/system-requirements.html#xr)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-plugin-management.html)
XR Plug-in Management settings
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-run.html)
Run an XR application
