* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/CameraTroubleshooting.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * Troubleshooting cameras


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)
Camera Inspector window reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
2D in Unity
# Troubleshooting cameras
Solve common issues with **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera), such as flickering lights and shadows.
## Reduce flickering
### Symptoms
Objects, lights, and shadows flicker if they’re far away. 
### Cause
The flickering occurs because distances are too large to calculate positions precisely with floating point math. In each frame, the object, light, or shadow is at a slightly different position, so it moves in and out of the view frustum.
### Resolution
To minimize flickering, use one of the following approaches:
  * Reduce the far **clipping plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane) distance in the Camera **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to avoid the distance of objects becoming too large for precise calculations.
  * Make everything in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) smaller, to reduce distances across your whole scene.
  * Enable camera-relative culling, so Unity uses the camera position as the relative position for shadow calculations. For more information, refer to [Culling settings in Graphics settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#culling-settings).


## Reduce tearing
### Symptoms
A ‘tear’ across the screen, where the top and bottom halves don’t match up.
![Simulated example of tearing. The shift in the picture is visible in the magnified portion.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Tearing.jpg) Simulated example of tearing. The shift in the picture is visible in the magnified portion.
### Cause
Updates in Unity aren’t synchronized with updates of the display device, so Unity might send a new frame while the display device is still rendering the previous frame. This results in a visible ‘tear’ at the position the frame changes.
### Resolution
To reduce tearing, go to **Edit** > **Project Settings** > **Quality** , then set **VSync Count** to one of the following:
  * **Every V Blank** to send frames only during the periods when the display device isn’t updating, which is called its vertical blank.
  * **Every Second V Blanks** to send frames during every other vertical blank. Use this value if your project takes longer than one update of the display device to render a frame.


## Additional resources
  * [Quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html)
  * [Camera Inspector windows reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
  * [Camera Inspector window reference for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)
Camera Inspector window reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
2D in Unity
