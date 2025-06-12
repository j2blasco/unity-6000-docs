* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * Introduction to batching draw calls


[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
Batching draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html)
Enable draw call batching
# Introduction to batching draw calls
Draw call batching is a [draw call optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html) method that combines meshes so that Unity can render them in fewer draw calls. Unity provides two built-in draw call batching methods:
  * [Static batching](https://docs.unity3d.com/6000.0/Documentation/Manual/static-batching.html): For [static](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html) **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), Unity combines them and renders them together.
  * [Dynamic batching](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching.html): For small enough meshes, this transforms their vertices on the CPU, groups similar vertices together, and renders them in one draw call.


Unity’s built-in draw call batching has several advantages over manually merging meshes; most notably, Unity can still cull meshes individually. However, it also has some downsides; static batching incurs memory and storage overhead, and dynamic batching incurs some CPU overhead.
## Render pipeline compatibility
**Feature** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Static Batching** | Yes | Yes | Yes | Yes  
**Dynamic Batching** | Yes | No | Yes | Yes   
## Limitations
Transparent **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) often require Unity to render meshes in back-to-front order. To batch transparent meshes, Unity first orders them from back to front and then tries to batch them. Since Unity must render the meshes back-to-front, it often can’t batch as many transparent meshes as opaque meshes.
Unity can’t apply dynamic batching to GameObjects that contain mirroring in their **Transform component** A Transform component determines the Position, Rotation, and Scale of each object in the scene. Every GameObject has a Transform. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Transform.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TransformComponent). For example, if one GameObject has a scale of **1** and another GameObject has a scale of **–1** , Unity can’t batch them together.
If you are not able to use draw call batching, manually combining meshes that are close to each other can be a good alternative. For more information on combining meshes, see [Combining meshes](https://docs.unity3d.com/6000.0/Documentation/Manual/combining-meshes.html).
**Warning** : When you access shared material properties from a C# script, make sure to use [Renderer.sharedMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-sharedMaterial.html) and not [Renderer.material](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer-material.html). `Renderer.material` creates a copy of the material and assigns the copy back to the Renderer. This stops Unity from batching the draw calls for that Renderer.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
Batching draw calls
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html)
Enable draw call batching
