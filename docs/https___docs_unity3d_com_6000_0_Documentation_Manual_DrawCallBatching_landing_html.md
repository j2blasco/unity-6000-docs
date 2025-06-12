* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * Batching draw calls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-troubleshoot.html)
Troubleshooting GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)
Introduction to batching draw calls
# Batching draw calls
Resources and approaches for improving performance by combining static **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) or moving GameObjects into fewer draw calls.
**Page** | **Description**  
---|---  
[Introduction to batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) | Understand how Unity creates batches of static and dynamic GameObjects to reduce draw calls.  
[Enable draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html) | Make sure GameObjects are compatible with **static batching** A technique Unity uses to draw GameObjects on the screen that combines static (non-moving) GameObjects into big Meshes, and renders them in a faster way. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#StaticBatching) and **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching).  
[Batching static GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching-landing.html) | Resources for combining static GameObjects into fewer draw calls.  
[Batching moving GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html) | Resources for combining moving GameObjects into fewer draw calls.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-troubleshoot.html)
Troubleshooting GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)
Introduction to batching draw calls
