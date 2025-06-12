* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-change.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Camera render types in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type.html)
  * Change the render type of a camera in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html)
Introduction to camera render types in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
Multiple cameras in URP
# Change the render type of a camera in URP
Use a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s **Render Type** property to make it a Base Camera or an Overlay Camera.
To change the type of a Camera in the Unity Editor:
  1. Create or select a Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
  2. In the Camera **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), use the **Render Type** drop-down menu to select a different type of Camera. Select either:
     * **Base** to change the Camera to a Base Camera
     * **Overlay** to change the Camera to an Overlay Camera


You can change a Camera’s type in a script, by setting the `renderType` property of the Camera’s [Universal Additional Camera Data](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalAdditionalCameraData.html) component, like this:
```
var cameraData = camera.GetUniversalAdditionalCameraData();
cameraData.renderType = CameraRenderType.Base;

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html)
Introduction to camera render types in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
Multiple cameras in URP
