* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * [Batching moving GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
  * How Unity batches moving GameObjects


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html)
Introduction to dynamic batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-enable.html)
Enable dynamic batching
# How Unity batches moving GameObjects
Dynamic batching for meshes works by transforming all vertices into world space on the CPU, rather than on the GPU. This means **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) is only an optimization if the transformation work is less resource intensive than doing a draw call. 
The resource requirements of a draw call depend on many factors, primarily the graphics API. For example, on consoles or modern APIs like Apple Metal, the draw call overhead is generally much lower, and often dynamic batching doesn’t produce a gain in performance. To determine whether it’s beneficial to use dynamic batching in your application, [profile](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html) your application with and without dynamic batching.
Unity can use dynamic batching for shadows casters, even if their materials are different, as long as the material values Unity needs for the shadow pass are the same. For example, multiple crates can use materials that have different textures. Although the material assets are different, the difference is irrelevant for the shadow caster pass and Unity can batch shadows for the crate **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in the shadow render step.
## Dynamic batching for dynamically generated geometries
The following renderers dynamically generate geometries, such as particles and lines, that you can optimize using dynamic batching:
  * [Built-in Particle Systems](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysUsage.html)
  * [Line Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)A component that takes an array of two or more points in 3D space and draws a straight line between each one. You can use a single Line Renderer component to draw anything from a simple straight line to a complex spiral. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LineRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LineRenderer)
  * [Trail Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)A visual effect that lets you to make trails behind GameObjects in the Scene as they move. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TrailRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TrailRenderer)


Dynamic batching for dynamically generated geometries works differently than it does for meshes:
  1. For each renderer, Unity builds all dynamically batchable content into one large vertex buffer.
  2. The renderer sets up the material state for the batch.
  3. Unity then binds the vertex buffer to the GPU.
  4. For each Renderer in the batch, Unity updates the offset in the vertex buffer and submits a new draw call.


This approach is similar to how Unity submits draw calls for [static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html)A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html)
Introduction to dynamic batching
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-enable.html)
Enable dynamic batching
