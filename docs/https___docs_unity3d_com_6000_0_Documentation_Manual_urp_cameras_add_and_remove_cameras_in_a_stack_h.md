* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
  * Add and remove cameras in a camera stack in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html)
Set up a camera stack in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-the-same-render-target.html)
Set up split-screen rendering in URP
# Add and remove cameras in a camera stack in URP
Camera stacks contain a single Base **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) with one or more Overlay Cameras stacked on top. In the Editor, you can add, remove, and reorder these cameras as much as you like to achieve the desired effects.
This page is split into the following sections:
  * [Add a camera to a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html#add-a-camera-to-a-camera-stack)
  * [Remove a camera from a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html#remove-a-camera-from-a-camera-stack)
  * [Reorder cameras in a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html#reorder-cameras-in-a-camera-stack)


## Add a camera to a camera stack
To add a camera to a camera stack, use the following steps:
  1. Select a Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with the **Render Type** set to **Base** , making it a Base Camera. If you do not have a Base Camera in your scene, create one.
  2. Create another camera in your scene, and select it.
  3. In the camera **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, set the **Render Type** to **Overlay**.
  4. Select the Base Camera again. In the camera Inspector window, go to the **Stack** section, select **Add** (**+**), then select the name of the Overlay Camera.


The Overlay Camera is now part of the Base Camera’s camera stack. Unity renders the Overlay Camera’s output on top of the Base Camera’s output.
**Note:** When you create multiple cameras for a camera stack, consider whether the cameras are all necessary. Each camera you add makes rendering slower, because an active camera runs through the entire rendering loop even if it renders nothing.
### Add a camera to a camera stack with a C# script
You can also add a camera to a camera stack with a C# script. Use the `cameraStack` property of the Base Camera’s [Universal Additional Camera Data](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html) component, as shown below:
```
var cameraData = camera.GetUniversalAdditionalCameraData();
cameraData.cameraStack.Add(myOverlayCamera);

```

## Remove a camera from a camera stack
To remove a camera from a camera stack, use the following steps:
  1. Create a camera stack that contains at least one Overlay Camera. For instructions, refer to [Add a camera to a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html#add-a-camera-to-a-camera-stack).
  2. Select the camera stack’s Base Camera.
  3. In the camera Inspector window, go to the **Stack** section, select the name of the Overlay Camera you want to remove, then then select **Remove** (**-**).


The Overlay Camera remains in the scene, but is no longer part of the camera stack.
### Remove a camera from a camera stack with a C# script
You can also remove a Camera from a camera stack with a C# script. Use the `cameraStack` property of the Base Camera’s [Universal Additional Camera Data](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html) component, as shown below:
```
var cameraData = camera.GetUniversalAdditionalCameraData();
cameraData.cameraStack.Remove(myOverlayCamera);

```

## Reorder cameras in a camera stack
To reorder the cameras in a camera stack, use the following steps:
  1. Create a camera stack that contains more than one Overlay Camera. For instructions, refer to [Add a camera to a camera stack](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html#add-a-camera-to-a-camera-stack).
  2. Select the Base Camera in the camera stack.
  3. In the Camera Inspector, go to the **Stack** section.
  4. Use the handles next to the names of the Overlay Cameras to reorder the list of Overlay Cameras.


The Base Camera renders the base layer of the camera stack, and the Overlay Cameras in the stack render on top of this in the order that they are listed, from top to bottom.
### Reorder a camera from a camera stack with a C# script
You can also reorder a camera stack with a C# script. Use the `cameraStack` property of the Base Camera’s [Universal Additional Camera Data](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html) component. The `cameraStack` is a `List` and can be reordered in the same way as any other `List`.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html)
Set up a camera stack in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-the-same-render-target.html)
Set up split-screen rendering in URP
