* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/xr-scene-setup.html

  * [Platform development ](https://docs.unity3d.com/6000.0/Documentation/Manual/PlatformSpecific.html)
  * [XR](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)
  * [XR project set up](https://docs.unity3d.com/6000.0/Documentation/Manual/configuring-project-for-xr.html)
  * Set up an XR scene


[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-create-projects.html)
Create an XR project
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-input-overview.html)
XR input options
# Set up an XR scene
To set up an **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), add an **XR Origin**. 
These objects are collections of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and components that provide a frame of reference for transforming spatial tracking data into the scene, including controlling the scene **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). When you add an **XR Origin** to a scene, it controls the attached camera to track the user’s head-mounted (VR) or hand-held (AR) device. In addition, the versions of the XR Origin that contain GameObjects for controllers will move them to track the user’s controllers. 
**Notes** : 
  * The older **XR Rig** name has been changed from “rig” to “origin” to better reflect the object’s role in a Unity scene. In addition, the **XR Origin** component has replaced the **Camera Offset** component and provides a few additional settings. Refer to [XR Origin component](https://docs.unity3d.com/Packages/com.unity.xr.core-utils@2.3/manual/xr-origin-reference.html) for more information.
  * The option to **Convert Camera to XR Rig** still appears in the **GameObject** > **XR** menu if you do not have the XR Interaction Toolkit package installed in the project. Although this option still works, Unity recommends using the appropriate **XR Origin** option from the XR Interaction Toolkit or AR Foundation packages for best compatibility with other XR features.
  * The _**AR** Augmented Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AR) Session Origin_ has been replaced by the _XR Origin (AR)_ and _XR Origin (Mobile AR)_ options in version 5 of the AR Foundation package.
  * The controller GameObjects included with some **XR Origin** objects do not have **visual components** A component that enables you to easily create GUI-specific functionality. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/UIVisualComponents.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VisualComponent), such as a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), and are not configured to receive user input other than tracking data. You must add 3D models and the components or **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts) necessary to act upon user input, if desired. The [XR Interaction Toolkit](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/general-setup.html#configure-xr-controller-and-interactor) package provides components for handling user input.


Refer to [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) for a description of the XR Origin options available to use in a scene.
## Prerequisites
Before you can set up a scene for XR, you must first:
  * [Set up the project for XR](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-configure-providers.html).
  * Add the AR Foundation to the project, if you are developing an AR app.
  * Add the XR Interaction Toolkit package, if you plan to use it (recommended).
  * If you use the XR Interaction Toolkit, import the [**Starter Assets**](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/samples.html). These assets contain Input System actions and presets that you can use to configure XR controller input.


## Set up a scene for XR
The basic steps to set up a scene for XR include:
  1. Create or open the scene in the Unity Editor.
  2. Add one of the **XR Origin** options to the scene with the **GameObject > XR** menu. You will see different options in the menu depending on which XR packages you have added to your project. Refer to [XR Origin](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-origin.html) for a description of the available XR Origin options.
  3. Configure XR input. Refer to [XR input options](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-input-overview.html) for more information.


Your projects might have additional setup considerations depending on the project type, platform, and Unity packages that you plan to use:
  * For AR projects, refer to [Scene setup](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@6.0/manual/project-setup/scene-setup.html) in the AR Foundation manual for additional set up steps and more detailed instructions. 
  * For **VR** Virtual Reality [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/VROverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VR) projects using the XR Interaction Toolkit, refer to [General Setup](https://docs.unity3d.com/Packages/com.unity.xr.interaction.toolkit@3.0/manual/general-setup.html) in the Interaction Toolkit manual for additional information.
  * For AR/**MR** Mixed Reality  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MR) projects on the Apple Vision Pro, use a [Volume Camera](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest?subfolder=/manual/VolumeCamera.html) instead of an XR Origin. Refer to [PolySpatial visionOS: Starting a new visionOS project](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest?subfolder=/manual/TutorialCreateFromScratch.html#mixed-reality-and-shared-space).
  * For VR projects on the Apple Vision Pro, you must add an [AR Session](https://docs.unity3d.com/Packages/com.unity.xr.arfoundation@latest?subfolder=/manual/features/session.html) object from the **AR Foundation** package to a scene to access head and hand tracking data. VR apps on this device also have access to additional ARKit data, such as plane detection, scene reconstruction meshes, and image tracking. Refer to [Fully Immersive VR on visionOS](https://docs.unity3d.com/Packages/com.unity.polyspatial.visionos@latest?subfolder=/manual/VRApps.html).


## Detect whether XR is enabled
If you have a scene that can be used in both XR and non-XR contexts, you can use the [XRSettings.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-enabled.html) property to detect whether the XR subsystems are currently loaded and active. With that information you can activate or deactivate the appropriate sets of GameObjects and components.
```
public void CheckXRStatus()
{
    if (UnityEngine.XR.XRSettings.enabled)
    {
        Debug.Log("XR is active.");
    }
    else
    {
        Debug.Log("XR is not available.");
    }
}


```

**Note:** you can read the value of the [XRSettings.enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/XR.XRSettings-enabled.html) property to determine the XR status. However, setting the value is no longer supported and does nothing. For information about how to dynamically turn XR on and off at runtime, refer to [Manage XR loader lifecycles](https://docs.unity3d.com/Packages/com.unity.xr.management@4.4/manual/EndUser.html#managing-xr-loader-lifecycles-manually). 
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-create-projects.html)
Create an XR project
[](https://docs.unity3d.com/6000.0/Documentation/Manual/xr-input-overview.html)
XR input options
