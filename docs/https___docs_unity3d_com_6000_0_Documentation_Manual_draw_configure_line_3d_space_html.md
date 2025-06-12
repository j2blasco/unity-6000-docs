* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-line-3d-space.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Lines and trails](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lines-trails-billboards.html)
  * [Rendering lines](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-lines.html)
  * Draw and configure a line in 3D space


[](https://docs.unity3d.com/6000.0/Documentation/Manual/line-rendering-introduction.html)
Rendering lines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
Line Renderer component reference
# Draw and configure a line in 3D space
To create a **Line Renderer** A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer):
  1. In the Unity menu bar, go to **GameObject** > **Effects** > **Line**.
  2. Select the Line Renderer **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
  3. Add points to the Line Renderer’s Positions array, either by directly setting array values in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window or by using the **Create Points** **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) Editing Mode. Refer to [Access scene editing tools](https://docs.unity3d.com/6000.0/Documentation/Manual/draw-configure-line-3d-space.html#SceneEditingMode).
  4. Use the Inspector window to configure the color, width, and other display settings of the line.

![Example Line Renderer configuration](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LineRenderer-example.jpg) Example Line Renderer configuration
## Set the Line Renderer Material
By default, a Line Renderer uses the built-in Material, **Default-Line**. You can make many changes to the appearance of the line without changing this Material, such as editing the color gradient or width of the line.
For other effects, such as applying a texture to the line, you will need to use a different Material. If you do not want to write your own **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for the new Material, Unity’s built-in [Standard Particle Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShaders.html) work well with Line Renderers.
See [Creating and using Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html) for more information.
## Access scene editing tools
You can use the Line Renderer’s Inspector to change the Scene Editing Mode. Different Scene Editing Modes enable you to use the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) and the Inspector to edit the Line Renderer in different ways.
There are three Scene Editing Modes: **None** , **Edit Points** , and **Create Points**.
### Scene Editing Mode: None
When no Scene Editing Mode is selected, you can configure and perform a simplification operation that removes unnecessary points from the Positions array.
### Scene Editing Mode: Edit Points
When the Scene Editing Mode is set to **Edit Points** , Unity represents each point in the Line Renderer’s Positions array as a yellow sphere in the Scene view. You can move the individual points using the Move tool.
### Scene Editing Mode: Create Points
When the Scene Editing Mode is set to **Create Points** , you can click inside the Scene view to add new points to the end of the Line Renderer’s Positions array.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/line-rendering-introduction.html)
Rendering lines
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)
Line Renderer component reference
