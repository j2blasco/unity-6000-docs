* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/camera-background-birp.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-birp.html)
  * Set the camera background with Clear Flags in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-birp.html)
Cameras in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)
Camera Inspector window reference for the Built-In Render Pipeline
# Set the camera background with Clear Flags in the Built-In Render Pipeline
Each **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) stores color and depth information when it renders its view. The portions of the screen that are not drawn in are empty, and will display the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) by default. When you are using multiple Cameras, each one stores its own color and depth information in buffers, accumulating more data as each Camera renders. As any particular Camera in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) renders its view, you can set the **Clear Flags** to clear different collections of the buffer information. To do this, choose one of the following four options:
## Skybox
This is the default setting. Any empty portions of the screen will display the current Camera’s skybox. If the current Camera has no skybox set, it will default to the skybox chosen in the [Lighting Window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) (menu: **Window** > **Rendering** > **Lighting**). It will then fall back to the **Background Color**. Alternatively a [Skybox component](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html) can be added to the camera. 
## Solid color
Any empty portions of the screen will display the current Camera’s **Background Color**.
## Depth only
If you want to draw a player’s gun without letting it get clipped inside the environment, set one Camera at **Depth** 0 to draw the environment, and another Camera at **Depth** 1 to draw the weapon alone. Set the weapon Camera’s **Clear Flags** to **depth only**. This will keep the graphical display of the environment on the screen, but discard all information about where each object exists in 3-D space. When the gun is drawn, the opaque parts will completely cover anything drawn, regardless of how close the gun is to the wall.
![The gun is drawn last, after clearing the depth buffer of the cameras before it](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/Camera-ClearFlags.jpg) The gun is drawn last, after clearing the depth buffer of the cameras before it
## Don’t clear
This mode does not clear either the color or the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer). The result is that each frame is drawn over the next, resulting in a smear-looking effect. This isn’t typically used in games, and would more likely be used with a custom **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
Note that on some GPUs (mostly mobile GPUs), not clearing the screen might result in the contents of it being undefined in the next frame. On some systems, the screen may contain the previous frame image, a solid black screen, or random colored **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-birp.html)
Cameras in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)
Camera Inspector window reference for the Built-In Render Pipeline
