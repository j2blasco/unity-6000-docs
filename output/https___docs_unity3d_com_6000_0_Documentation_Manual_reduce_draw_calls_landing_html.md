* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * Optimizing draw calls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance.html)
Reduce rendering work on the CPU or GPU
[](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html)
Introduction to optimizing draw calls
# Optimizing draw calls
There are several methods you can use in Unity to optimize and reduce draw calls and render-state changes. Some methods are more suited for certain **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) than others.
**Page** | **Description**  
---|---  
[Introduction to optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html) | Learn about why reducing draw calls improves rendering time, and how Unity prioritizes optimization methods.  
[GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html) | Resources and techniques for rendering multiple copies of the same **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) at the same time.  
[Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html) | Combine meshes to reduce draw calls, for either static or moving **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).  
[Combine meshes manually](https://docs.unity3d.com/6000.0/Documentation/Manual/combining-meshes.html) | Merge multiple meshes into a single mesh that Unity can render in a single draw call.  
## Additional resources
Refer to the following if your project uses the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) or the High Definition Render Pipeline (HDRP):
  * [Scriptable Render Pipeline (SRP) Batcher in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-landing.html)
  * [BatchRendererGroup in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/batch-renderer-group.html)
  * [Optimizing draw calls in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance.html)
Reduce rendering work on the CPU or GPU
[](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html)
Introduction to optimizing draw calls
