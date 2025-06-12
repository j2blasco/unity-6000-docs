* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/create-configure-halo.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Light halos](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-haloes.html)
  * Create and configure a halo light effect


[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-haloes.html)
Light halos
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)
Halo component reference
# Create and configure a halo light effect
**Note:** This workflow is compatible only with the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline). For similar functionality in other render pipelines, see [Lens flares and halos](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-lens-flares.html).
Add a Halo component to a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with a [Light component](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html). Then set its size and color properties to give the desired glowing effect.
**Note:** A Light can also display a halo without a separate Halo component by enabling its _Draw Halo_ property, but you cannot configure its size and color.
To see Halos in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) view, check **Fx** button in the **Scene View** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView) **Toolbar** A row of buttons and basic controls at the top of the Unity Editor that allows you to interact with the Editor in various ways (e.g. scaling, translation). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Toolbar.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Toolbar).
To override the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) used for Halos, open the [Graphics](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html) window and set **Light Halo** to the shader that you would like to use as the override.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-haloes.html)
Light halos
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)
Halo component reference
