* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * Batching static GameObjects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html)
Enable draw call batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)
Introduction to static batching
# Batching static GameObjects
Resources for combining static **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) into fewer draw calls.
**Page** | **Description**  
---|---  
[Introduction to static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html) | Understand how Unity builds a combined **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), and a shared vertex and index buffer.  
[Enable static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-enable.html) | Enable Unity performing **static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) at build time or at runtime.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html)
Enable draw call batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)
Introduction to static batching
