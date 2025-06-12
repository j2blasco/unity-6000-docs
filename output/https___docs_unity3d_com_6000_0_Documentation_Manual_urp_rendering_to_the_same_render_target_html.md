* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-to-the-same-render-target.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Multiple cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-multiple.html)
  * Set up split-screen rendering in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html)
Add and remove cameras in a camera stack in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
Apply different post processing effects to separate cameras in URP
# Set up split-screen rendering in URP
In the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), multiple [Base Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-types-and-render-type-introduction.html#base-camera) or [Camera Stacks](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-stacking.html) can render to the same render target. This allows you to create effects such as split screen rendering.
If more than one Base **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) or Camera Stack renders to the same area of a render target, Unity draws each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) in the overlapping area multiple times. Unity draws the Base Camera or Camera Stack with the highest priority last, on top of the previously drawn pixels. For more information on the camera render order optimization, refer to [Understand camera render order](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras-advanced.html).
You use the Base Camera’s ****Viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport) Rect** property to define the area of the render target to render to. For more information on viewport coordinates, refer to the [Unity Manual](https://docs.unity3d.com/Manual/class-Camera.html) and [API documentation](https://docs.unity3d.com/ScriptReference/Camera-rect.html).
## Setting up split screen rendering
![Setting up split screen rendering in URP](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/camera-split-screen-viewport.png) Setting up split screen rendering in URP
  1. Create a Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Its **Render Mode** defaults to **Base** , making it a Base Camera.
  2. Select the Camera. In the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector), scroll to the Output section. Change the values for **Viewport rect** to the following: 
     * X: 0
     * Y: 0
     * W: 0.5
     * H: 1
  3. Create another Camera in your scene. Its **Render Mode** defaults to **Base** , making it a Base Camera.
  4. Select the Camera. In the Inspector, scroll to the Output section. Change the values for **Viewport rect** to the following: 
     * X: 0.5
     * Y: 0
     * W: 0.5
     * H: 1


Unity renders the first Camera to the left-hand side of the screen, and the second Camera to the right-hand side of the screen.
You can change the Viewport rect for a Camera in a script by setting its `rect` property, like this:
```
myUniversalAdditionalCameraData.rect = new Rect(0.5f, 0f, 0.5f, 0f);

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/add-and-remove-cameras-in-a-stack.html)
Add and remove cameras in a camera stack in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/apply-different-post-proc-to-cameras.html)
Apply different post processing effects to separate cameras in URP
