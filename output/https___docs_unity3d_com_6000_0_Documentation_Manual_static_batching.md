* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * [Batching static GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
  * Introduction to static batching


[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
Batching static GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html)
Enable static batching
# Introduction to static batching
Static batching is a [draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) method that combines meshes that don’t move to reduce [draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html). It transforms the combined meshes into world space and builds one shared vertex and index buffer for them. Then Unity performs a single draw call that uses this combined **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) to draw all objects in the batch at once. **Static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) can significantly reduce the number of draw calls.
Static batching is more efficient than [dynamic batching](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) because static batching doesn’t transform vertices on the CPU. For more information about the performance implications for static batching, see [Performance implications](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html#performance-implications).
## Requirements and compatibility
This section includes information about the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) compatibility of static batching.
### Render pipeline compatibility
**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
## Performance implications
Using static batching requires additional CPU memory to store the combined geometry. If multiple GameObjects use the same mesh, Unity creates a copy of the mesh for each **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), and inserts each copy into the combined mesh. This means that the same geometry appears in the combined mesh multiple times. Unity does this regardless of whether you use the [editor](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html#editor) or [runtime API](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html#runtime) to prepare the GameObjects for static batching. If you want to keep a smaller memory footprint, you might have to sacrifice rendering performance and avoid static batching for some GameObjects. For example, marking trees as static in a dense forest environment can have a serious memory impact.
**Note** : There are limits to the number of vertices a static batch can include. Each static batch can include up to 64000 vertices. If there are more, Unity creates another batch.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html)
Batching static GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html)
Enable static batching
