* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
  * VR and MR development in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)
AR development in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/XRPluginArchitecture.html)
XR architecture
# VR and MR development in Unity
Get started with **virtual reality** and **mixed reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedReality) development in Unity.
Virtual Reality (VR) and Mixed Reality (MR) both refer to extended reality experiences where specialized devices provide a way for the user to interact with a virtual environment.
In **VR** experiences, the environment is closed. This means that the user can’t see their surrounding environment, and can only see virtual content displayed on the screen. The user can only interact with virtual content, rather than their physical environment. VR experiences are often achieved with a headset (a Head-Mounted Display [HMD]), where a screen within the headset displays the virtual environment. VR experiences are fully immersive, and so are a good choice for creating immersive, story-driven experiences and gameplay.
MR combines elements of the real and virtual environments, enabling users to see and interact with both simultaneously. MR relies on devices that are able to display a real-time view of the user’s surroundings, and blend the real-world view with virtual content. Some headsets, such as the Meta Quest 3, achieve MR through passthrough cameras, which capture the surrounding environment and display it on the screen. Other devices achieve MR without passthrough cameras, for example the Microsoft HoloLens devices are transparent glasses which project virtual content directly onto the lenses. MR is useful in situations where real-world integration is beneficial, such as training or educational experiences. You can also use MR to create social gaming experiences, or to enhance gameplay with locational information.
**Note:** On some modern devices, you can develop an app that has both **MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR) and VR modes to allow the user to toggle between these modes within your app.
## Considerations for VR and MR development
VR and MR development shares common workflows and design considerations with any real-time 3D development in Unity. However, distinguishing factors include:
  * **Richer user input** : in addition to traditional button and joystick controllers, VR devices provide spatial head, controller, and hand and finger tracking (on supported platforms).
  * **More intimate interaction with the environment** : in conjunction with the possibilities of richer input, VR raises the expectations of much closer and physical interaction with the environment than typical 3D games and applications. Users expect to be able to pick things up and interact with objects in the environment. With head tracking, the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) can get much closer to the walls and other boundaries of the environment and can even pass through them.
  * **User comfort concerns** : many people experience motion sickness in VR when camera movement doesn’t match the movement of their head. You can mitigate the causes of motion sickness by maintaining a high frame rate, offering a range of locomotion options so that users can choose a mode they are comfortable with, and avoiding moving the camera independently of the user’s head tracking.


To get started with VR development, use the XR Plug-in Management system to install and enable XR provider plug-ins for the devices you want to support. Refer to [XR Project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html) for more information.
## Basic VR and MR scene elements
A basic VR or MR **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) should contain an [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html), which defines the 3D origin for tracking data. This collection of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and components also contains the main scene Camera and the GameObjects representing the user’s controllers. Refer to [Set up an XR scene](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-scene-setup.html) for instructions on setting up a basic VR scene.
You typically need a way for the user to move around and to interact with the 3D world you have created. The [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/) provides components for creating interactions like selecting and grabbing objects. It also provides a customizable locomotion system. You can use the [Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.5/) in addition to or instead of the **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) Interaction Toolkit.
## VR packages
Most of the features and APIs used for VR development in Unity are provided through packages. These packages include:
  * [Provider plug-ins](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#vr-plugin)
  * [XR Interaction Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#xr-interaction-toolkit)
  * [XR Core Utilities](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#xr-core-utilities)
  * [Input System](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#input-system)
  * [VR project template](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#vr-template)
  * [Hand tracking](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#hand-tracking)


### VR and MR provider plug-ins
VR and MR platforms are available as provider plug-ins by the XR **Plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) Management system. To understand how to use the XR Plug-in Management system to add and enable provider plug-ins for your target platforms, refer to [XR Project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html).
The following table describes the plug-ins available for VR and MR development, and the devices that they support:
**Plug-in** | **MR/VR** | **Supported devices**  
---|---|---  
[Apple visionOS XR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.visionos@latest) | MR and VR | Apple Vision Pro  
[Oculus Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.oculus@latest) | VR | Oculus Rift, Meta Quest 2, Meta Quest 3, Meta Quest 3s, Meta Quest Pro  
[OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest) | MR and VR |  [Devices with an OpenXR runtime](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.14/manual/index.html#runtimes) including Meta Quest devices, Valve SteamVR, HoloLens  
[Unity OpenXR: Meta OpenXR](https://docs.unity3d.com/Packages/com.unity.xr.meta-openxr@latest) | MR and VR | Meta Quest devices  
[Unity OpenXR: Android XR](https://docs.unity3d.com/Packages/com.unity.xr.androidxr-openxr@latest) | MR and VR | Android XR devices  
PlayStation VR | VR | PlayStation VR and VR2. (Requires Sony Developer registration.)  
[Mock HMD](https://docs.unity3d.com/Packages/com.unity.xr.mock-hmd@latest) | VR | Simulates a VR headset in the Unity Editor Play mode  
**Note:** Many headset makers are working toward using the OpenXR runtime as a standard. However, this process isn’t complete and there can be feature discrepancies between OpenXR and a headset maker’s own provider plug-in or SDK.
### XR Interaction Toolkit
The [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/) can make it easier and faster to develop VR applications. The XR Interaction Toolkit provides:
  * An [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) set up with controllers.
  * [XR controller](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/general-setup.html#configure-xr-controller-and-interactor) setups with Input System presets for basic interactions like select and grab.
  * [Interactor and Interactable components](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/architecture.html#interactors) for creating object manipulation.
  * A configurable [locomotion system](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/locomotion.html).
  * [XR UI input](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/ui-setup.html).


### XR Core Utilities
The [XR Core Utilities](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.3/manual/index.html) package contains software utilities used by other Unity XR plug-ins and packages. Typically, this package gets installed in your project as a dependency of other XR packages.
### Input System
The Unity [Input System](https://docs.unity3d.com/Packages/com.unity.inputsystem@1.8/manual/index.html) package not only supports accessing user input from VR controller buttons and joysticks, but also provides access to XR tracking data and haptics. The Input System package is required if you use the [XR Interaction Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#xr-interaction-toolkit) or the [OpenXR provider plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html#vr-plugin).
## VR and MR templates
Unity provides templates for VR and MR development. These templates are accessible from the Unity Hub, and provide a sample scene pre-configured with the relevant packages and components to get started with VR and MR development.
The available VR and MR templates are:
  * [VR Template](https://docs.unity3d.com/Packages/com.unity.template.vr@latest)
  * [VR Multiplayer Template](https://docs.unity3d.com/Packages/com.unity.template.vr-multiplayer@latest)
  * [MR Template](https://docs.unity3d.com/Packages/com.unity.template.mixed-reality@latest)
  * [MR Tabletop Multiplayer Template](https://docs.unity3d.com/Packages/com.unity.template.mr-multiplayer@latest)


To learn more about creating an XR project from a template, refer to [Create an XR project](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-create-projects.html#create-a-new-xr-project).
## Hand tracking
Hand tracking is a feature that allows users to interact with a VR application using their hands. Hand tracking is supported by the [XR Hands](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.2/manual/index.html) package.
The Hands package provides:
  * A standard [hand data model](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-data-model.html).
  * An [API](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/api/UnityEngine.XR.Hands.XRHandSubsystem.html) for accessing hand tracking data.
  * The [XR Hand Skeleton Driver](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-visuals.html) component, which maps a set of Transforms to their corresponding hand **joints** A physics component allowing a dynamic connection between Rigidbody components, usually allowing some degree of movement such as a hinge. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Joints.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#joint) and updates those Transforms as tracking data is received.
  * The [XR Hand Mesh Controller](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/hand-data/xr-hand-visuals.html#xr-hand-mesh-controller), which enables and disables a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) as hand tracking is acquired or lost.
  * A [HandVisualizer](https://docs.unity3d.com/Packages/com.unity.xr.hands@1.4/manual/project-setup/scene-setup.html) sample that demonstrates how to use the hand tracking API.


## Additional resources
  * [Create virtual and mixed reality experiences in Unity](https://unity.com/resources/create-virtual-mixed-reality-experiences-unity) (E-book)
  * [Make a VR multiplayer game, Part 1 | Unity](https://www.youtube.com/watch?v=i9GVZp9GZUE) (YouTube)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)
AR development in Unity
[](https://docs.unity3d.com/6000.0/Documentation/Manual/XRPluginArchitecture.html)
XR architecture
