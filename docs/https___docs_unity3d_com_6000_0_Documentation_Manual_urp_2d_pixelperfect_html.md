* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [2D in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/Unity2D.html)
  * [2D game development in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/2d-urp-landing.html)
  * [Precise pixel scaling and rotation via the Pixel Perfect Camera in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
  * Introduction to the Pixel Perfect Camera in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
Precise pixel scaling and rotation via the Pixel Perfect Camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-prep-sprites.html)
Prepare your sprites for the 2D Pixel Perfect Camera in URP
# Introduction to the Pixel Perfect Camera in URP
Understand how to use the **Pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) Perfect **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) to keep your pixel art crisp and clear at different resolutions, and stable in motion.
The **2D Pixel Perfect** package contains the **Pixel Perfect Camera** component. The component calculates what Unity needs to scale the **viewport** The user’s visible area of an app on their screen.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Viewport) with resolution changes to maintain the pixel perfect visual style, so that you don’t need to calculate manually. You can use the component settings to adjust the definition of the rendered pixel art within the camera viewport, and preview any changes made in the Game view.
![Pixel Perfect Camera Gizmo](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/2D/2D_Pix_image_0.png) Pixel Perfect Camera Gizmo
To begin using the component, attach the **Pixel Perfect Camera** component to the main Camera **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The component is represented by two green bounding boxes centered on the **Camera** **Gizmo** A graphic overlay associated with a GameObject in a Scene, and displayed in the Scene View. Built-in scene tools such as the move tool are Gizmos, and you can create custom Gizmos using textures or scripting. Some Gizmos are only drawn when the GameObject is selected, while other Gizmos are drawn by the Editor regardless of which GameObjects are selected. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GizmosMenu.html#GizmosIcons)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Gizmo) in the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView). The solid green bounding box shows the visible area in Game view, while the dotted bounding box shows the [Reference Resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-ref.html#reference-resolution).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect.html)
Precise pixel scaling and rotation via the Pixel Perfect Camera in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/2d-pixelperfect-prep-sprites.html)
Prepare your sprites for the 2D Pixel Perfect Camera in URP
