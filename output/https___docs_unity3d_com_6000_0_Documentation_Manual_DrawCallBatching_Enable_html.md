* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * Enable draw call batching


[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)
Introduction to batching draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
Batching static GameObjects
# Enable draw call batching
[Mesh Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer), [Trail Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TrailRenderer), [Line Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer), [Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem), and [Sprite Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)A component that lets you display images as Sprites for use in both 2D and 3D scenes. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sprite/renderer/renderer-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SpriteRenderer) are supported for draw call batching. Other types of rendering components, including Skinned **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderers Cloth, are not supported. Unity only batches Renderers with other Renderers of the same type; for example, Mesh Renderers with Mesh Renderers.
Unity batches draw calls of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that use the same material. This means to get the best results from draw call batching, share materials among as many GameObjects as possible. If you have two material assets that are identical apart from their textures, you can combine the textures into a single, larger texture. This process is called texture atlasing. For more information, see the [Wikipedia article](http://en.wikipedia.org/wiki/Texture_atlas) on texture atlasing. When textures are in the same atlas, you can use a single material asset instead.
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can use a [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) to change material properties without breaking draw call batching. The CPU still needs to make some render-state changes, but using a `MaterialPropertyBlock` is faster than using multiple materials. If your project uses a Scriptable Render Pipeline, don’t use a `MaterialPropertyBlock` because they remove SRP Batcher compatibility for the material.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)
Introduction to batching draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
Batching static GameObjects
