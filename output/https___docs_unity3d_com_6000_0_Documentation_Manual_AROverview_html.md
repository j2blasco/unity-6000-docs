* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [Overview](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-landing.html)
  * AR development in Unity


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html)
XR packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)
VR and MR development in Unity
# AR development in Unity
Get started with **augmented reality** development in Unity.
Augmented Reality (AR) involves a different set of design challenges compared to **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) or traditional real-time 3D applications. An augmented reality app overlays its content on the real world around the user. AR devices, such as glasses, visors, or mobile devices, use transparent displays to allow the user to see the real-world with virtual content overlaid on top.
To place an object in the real world, you must first determine where to place it. For example, you might want to place a virtual painting on a physical wall. If you place a virtual potted plant, you might want it on a physical table or the floor. An AR app receives information about the world from the user’s device, and decides how to use this information to create a good experience for the user. Depending on target device capabilities, this information includes location of planar surfaces (planes), and the detection of objects, people, and faces.
The following sections provide an overview of an [AR scene](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#ar-scene), the [AR packages](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#ar-packages), and [AR Template](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#ar-template) you can use to develop AR applications in Unity.
## Introduction to an AR scene
When you open a typical AR **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in Unity, you will not find many **3D objects** A 3D GameObject such as a cube, terrain or ragdoll. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GameObjects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#3DObject) in the **Scene** or the **Hierarchy** view. Instead, most **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the scene define the settings and logic of the app. 3D content is typically created as **prefabs** An asset type that allows you to store a GameObject complete with components and properties. The prefab acts as a template from which you can create new object instances in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Prefabs.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Prefab) that are added to the scene at runtime in response to AR-related events.
![A typical AR scene in Unity](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/xr-ar-scene.png)  
  
_A typical AR scene in the Unity Editor._
## AR scene elements
The following sections outline the [Required scene elements](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#basic-ar-scene) to make AR work, and the [Optional scene elements](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#optional-scene-elements) you can add to enable specific AR features. To learn more about how to configure an **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) scene [Set up an XR scene](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-scene-setup.html).
**Note:** AR GameObjects appear in the create menu when you enable an [AR provider plug-in](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#ar-provider-plug-ins) in **XR**Plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) Management**.
### Required scene elements
An AR scene must contain the `AR Session` and `XR Origin` GameObjects. The available options for the [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) depends on the packages you’ve installed in your project. AR Foundation uses the [Mobile AR](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#mobile-ar) and XR Interaction Toolkit uses the [AR](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#origin-ar) variant.
If you start your project from an [AR template](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#ar-template), these components will come configured in the scene.
To manually add the relevant `XR Origin` and `AR Session` GameObjects:
  1. Right-click in the **Hierarchy** window.
  2. Go to **GameObject** > **XR**.
  3. Select the relevant component.


**Note:** You must only have one active XR Origin in a scene.
#### AR Session
The **AR Session** GameObject contains the components you need to control the lifecycle and input of AR experience:
  * [AR Session component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/session.html)
  * [AR Input Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARInputManager.html)


#### XR Origin (Mobile AR)
The **XR Origin (Mobile AR)** GameObject is a variant of the [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) for hand-held AR applications. This variant isn’t configured for controller input by default. This version of the `XR Origin` is used by AR Foundation.
The **XR Origin (Mobile AR)** GameObject consists of the following components:
  * [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARSessionOrigin.html)
  * ****Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) Offset** GameObject: 
    * [AR Camera Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-manager-component)
    * [AR Camera Background component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-background-component)


For more information, refer to AR Foundation [Set up your scene](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/project-setup/scene-setup.html) and [Device tracking](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/device-tracking).
#### XR Origin (AR)
The **XR Origin (AR)** GameObject is a variant of the [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) for hand-held AR applications and comes configured for controller input. The [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0) package provides this variant.
The **XR Origin (AR)** GameObject consists of the following:
  * [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/api/UnityEngine.XR.ARFoundation.ARSessionOrigin.html)
  * **Camera Offset** GameObject: 
    * [AR Camera Manager component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-manager-component)
    * [AR Camera Background component](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/features/Camera/camera-components.html#ar-camera-background-component)
  * **LeftHand/RightHand Controller** GameObjects: 
    * [XR Controller (Action-based) component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-controller-action-based.html)
    * [XR Ray Interactor component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-ray-interactor.html)
    * [Line Renderer component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
    * [XR Interactor Line Visual component](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/xr-interactor-line-visual.html)
    * [Sorting Group component](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/sorting-group/sorting-group-landing.html)


Refer to [Create a basic scene](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/create-basic-scene.html) to learn more about scene configuration with XR Interaction Toolkit.
### Optional scene elements
To enable an AR feature, you must add the corresponding components to your project. Typically, this includes an [AR Manager](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/architecture/managers.html#trackables-and-trackable-managers), but other features might also require additional components.
To learn more about the required components for AR Foundation features, refer to the documentation for the relevant AR Foundation [Feature](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/features/features.html). For more in-depth information about setting up your AR Foundation app, visit [Scene set up](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/project-setup/scene-setup.html).
## AR packages
To build AR apps in Unity, you can install the [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/) package along with the XR provider plug-ins for the devices you want to support.
To develop AR/**MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR) apps for the Apple Vision Pro device, you also need the [PolySpatial visionOS packages](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest). Unity provides additional packages, including the [XR Interaction Toolkit](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html#xr-interaction-toolkit) to make it easier and faster to develop AR experiences.
### AR provider plug-ins
AR platforms are available as provider plug-ins by the XR Plug-in Management system. To understand how to use the XR Plug-in Management system to add and enable provider plug-ins for your target platforms, refer to [XR Project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html).
The AR provider plug-ins supported by Unity include:
**Plug-in** | **Supported devices**  
---|---  
[Apple ARKit XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.arkit@6.1) | iOS  
[Apple visionOS XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.visionos@latest) | visionOS  
[Google ARCore XR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.arcore@6.1) | Android  
[OpenXR Plug-in](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.10/manual/index.html) | [Devices with an OpenXR runtime](https://docs.unity3d.com/Packages/com.unity.xr.openxr@1.14/manual/index.html#runtimes)  
**Note:** Depending on the platform or device, you might need to install additional packages along with OpenXR. For example, to build an AR app for HoloLens 2, you must install the Microsoft’s [Mixed Reality OpenXR Plugin](https://learn.microsoft.com/en-us/windows/mixed-reality/develop/unity/mixed-reality-openxr-plugin).
### AR Foundation
The [AR Foundation](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/) package supports AR development in Unity.
AR Foundation enables you to create multiplatform AR apps with Unity. In an AR Foundation project, you choose which AR features to enable by adding the corresponding manager components to your scene. When you build and run your app on an AR device, AR Foundation enables these features using the platform’s native AR SDK, so you can create once and deploy to the world’s leading AR platforms.
A device can be AR-capable without supporting all possible AR features. Available functionality depends on both the device platform and the capabilities of the specific device. Even on the same platform, capabilities can vary from device to device. For example, a specific device model might support AR through its world-facing camera, but not its user-facing camera. To learn which platforms support each AR Foundation feature, refer to the [Platform support](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.1/manual/index.html#platform-support) table in the AR Foundation documentation.
You can access samples scenes that demonstrate AR Foundation features from the [AR Foundation Samples](https://github.com/Unity-Technologies/arfoundation-samples) app (GitHub). To learn more, refer to [AR Foundation samples](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.2/manual/samples.html) in the AR Foundation package documentation.
### PolySpatial visionOS packages
Augmented and mixed reality development for the Apple Vision Pro device relies on a set of packages that implement the Unity PolySpatial architecture on the visionOS platform.
The PolySpatial architecture splits a Unity game or app into two logical pieces: a simulation controller and a presentation view. The simulation controller drives all app-specific logic, such as MonoBehaviours and other scripting, user interface behavior, asset management, physics, etc. Almost all of your game’s behavior is part of the simulation. The presentation view handles both input and output, which includes rendering to the display and other forms of output, such as audio. The view sends input received from the operating system – including pinch gestures and head position – to the simulation for processing each frame. After each simulation step, the view updates the display by rendering **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) to the screen, submitting audio buffers to the system, etc.
On the visionOS platform, the simulation part runs in a Unity Player, while the presentation view is rendered by Apple’s RealityKit. For every visible object in the simulation, a corresponding object exists in the RealityKit scene graph.
**Note:** PolySpatial is only used for augmented and **mixed reality** Mixed Reality (MR) combines its own virtual environment with the user’s real-world environment and allows them to interact with each other.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedReality) on the Apple Vision Pro. **Virtual reality** Virtual Reality (VR) immerses users in an artificial 3D world of realistic images and sounds, using a headset and motion tracking. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VirtualReality) and windowed apps run in a Unity Player that also controls rendering (using the Apple Metal graphics API).
### XR Interaction Toolkit
The [Unity XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.1/) provides tools for building both AR and VR interactions. The AR functionality provided by the XR Interaction Toolkit includes:
  * AR gesture system to map screen touches to gesture events
  * AR placement Interactable component to help place virtual objects in the real world
  * AR gesture Interactor and Interactable components to support object manipulations such as place, select, translate, rotate, and scale
  * AR annotations to inform users about AR objects placed in the real world


## AR template
Unity’s AR Mobile template provides a starting point for augmented reality development in Unity. This template configures **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings), pre-installs necessary packages, and includes sample scenes with various pre-configured example assets to demonstrate an AR-ready project. You can access the template through the Unity Hub when you create a new project. Refer to [Create a new project](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-create-projects.html#create-a-new-xr-project) for information about creating a project with the template.
For more information about the template assets and sample scene, refer to the [AR Mobile template](https://docs.unity3d.com/Packages/com.unity.template.ar-mobile@2.0) documentation.
## Additional resources
  * [Set up an XR scene](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-scene-setup.html)
  * [Create virtual and mixed reality experiences in Unity](https://unity.com/resources/create-virtual-mixed-reality-experiences-unity) (E-book)
  * [XR packages](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-support-packages.html)
XR packages
[](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)
VR and MR development in Unity
