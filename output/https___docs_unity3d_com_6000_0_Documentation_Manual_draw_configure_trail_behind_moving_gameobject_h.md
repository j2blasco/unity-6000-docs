* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-trail-behind-moving-gameobject.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering trails](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-trails.html)
  * Draw and configure a trail behind a moving GameObject


[](https://docs.unity3d.com/6000.0/Documentation/Manual/trail-rendering-introduction.html)
Rendering trails for moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)
Trail Renderer component reference
# Draw and configure a trail behind a moving GameObject
To create a **Trail Renderer** A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TrailRenderer):
  1. In the Unity menu bar, go to **GameObject** > **Effects** > **Trail**.
  2. Select the Trail Renderer **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), and parent it to the GameObject that you want it to generate a trail for.
  3. Use the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to configure the color, width, and other display settings of the trail.
  4. Preview the trail in Edit Mode by moving the GameObject and observing the effect in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view.

![An example Trail Renderer configuration, and the resulting trail.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/TrailRenderer-example2.jpg) An example Trail Renderer configuration, and the resulting trail.
## Set the Trail Renderer Material
By default, a Trail Renderer uses the built-in Material, **Default-Line**. You can make many changes to the appearance of the trail without changing this Material, such as editing the color gradient or width of the trail.
For other effects, such as applying a texture to the trail, you will need to use a different Material. If you do not want to write your own **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for the new Material, Unity’s built-in [Standard Particle Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShaders.html) work well with Trail Renderers. If you apply a Texture to a Trail Renderer, the Texture should be of square dimensions (for example 256x256, or 512x512).
If you apply more than one Material to a Trail Renderer, the trail is rendered once for each Material.
See [Creating and using Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html) for more information.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/trail-rendering-introduction.html)
Rendering trails for moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)
Trail Renderer component reference
