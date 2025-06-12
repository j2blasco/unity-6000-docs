* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * [Batching moving GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
  * Introduction to dynamic batching


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
Batching moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html)
How Unity batches moving GameObjects
# Introduction to dynamic batching
Dynamic batching is a [draw call batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html) method that batches moving **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to reduce [draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html). **Dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) works differently between meshes and geometries that Unity generates dynamically at runtime, such as [particle systems](https://docs.unity3d.com/6000.0/Documentation/Manual/ParticleSystems.html)A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem). For information about the internal differences between meshes and dynamic geometries, see [Dynamic batching for meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html) and [Dynamic batching for dynamically generated geometries](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html#dynamic-batching-dynamic-geometry).
**Note** : Dynamic batching for meshes was designed to optimize performance on old low-end devices. On modern consumer hardware, the work dynamic batching does on the CPU can be greater than the overhead of a draw call. This negatively affects performance. For more information, see [Dynamic batching for meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html).
## Requirements and compatibility
This section includes information about the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) compatibility of dynamic batching.
### Render pipeline compatibility
**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Dynamic Batching** | Yes | No | Yes | Yes  
### Limitations
In the following scenarios, Unity either can’t use dynamic batching at all or can only apply dynamic batching to a limited extent:
  * Unity can’t apply dynamic batching to meshes that contain more than 900 vertex attributes and 300 vertices. This is because dynamic batching for meshes has an overhead per vertex. For example, if your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) uses vertex position, vertex normal, and a single UV, then Unity can batch up to 300 vertices. However, if your shader uses vertex position, vertex normal, UV0, UV1, and vertex tangent, then Unity can only batch 180 vertices.
  * If GameObjects use different material instances, Unity can’t batch them together, even if they are essentially the same. The only exception to this is shadow caster rendering.
  * GameObjects with lightmaps have additional renderer parameters. This means that, if you want to batch lightmapped GameObjects, they must point to the same **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) location.
  * Unity can’t fully apply dynamic batching to GameObjects that use multi-pass shaders. 
    * Almost all Unity shaders support several lights in **forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering). To achieve this, they process an additional render pass for each light. Unity only batches the first render pass. It can’t batch the draw calls for the additional per-pixel lights.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
Batching moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html)
How Unity batches moving GameObjects
