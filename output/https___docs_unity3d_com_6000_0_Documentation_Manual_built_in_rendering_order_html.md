* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering order in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
  * Render queues and sorting behaviours in the Built-in Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
Rendering order in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-set-queue.html)
Set the render queue for a material in the Built-In Render Pipeline
# Render queues and sorting behaviours in the Built-in Render Pipeline
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), the order in which Unity renders objects is based on two things: which render queue the object is in, and how Unity sorts objects within that render queue.
## Render queues
Unity sorts objects into groups called render queues. Unity renders the contents of one render queue, and then renders the contents of another render queue, and so on.
Unity has the following named render queues, which it renders in the following order:
**Name** | **Index** | **Description**  
---|---|---  
**Background** | 1000 | Use this queue for anything that should be drawn in the background of your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
**Geometry** | 2000 | Use this queue for opaque geometry. This is the default queue.  
**AlphaTest** | 2450 | Use this queue for alpha tested geometry. This is after the **Geometry** queue because it’s more efficient to render alpha-tested objects after all solid ones are drawn.  
**Transparent** | 3000 | Use this queue for anything alpha-blended (shaders that don’t write to the depth buffer). Examples include glass, or particle effects.  
**Overlay** | 4000 | Use this queue for effects that are rendered on top of everything else, such as **lens flares** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare).  
Note that **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) materials are a special case. Unity draws Skybox materials after all opaque geometry (after queue index 2500), but before all transparent geometry (before queue index 2501).
## Sorting behaviors within render queues
Within each render queue, Unity sorts and draws objects based on their distance from the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). The sorting behavior depends on the index of the render queue:
  * For queues with an index up to and including 2500 (Geometry + 500), Unity sorts Renderers in these queues using the behavior defined in [OpaqueSortMode.FrontToBack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/OpaqueSortMode.FrontToBack.html) by default.
  * For queues with an index of 2501 or above, Unity sorts Renderers in these queues using the behavior defined in [TransparencySortMode.Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TransparencySortMode.Default.html) by default.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
Rendering order in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-set-queue.html)
Set the render queue for a material in the Built-In Render Pipeline
