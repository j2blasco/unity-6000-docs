* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-enable.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [Batching draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
  * [Batching moving GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-landing.html)
  * Enable dynamic batching


[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html)
How Unity batches moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/combining-meshes.html)
Combine meshes manually
# Enable dynamic batching
Unity always uses **dynamic batching** An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) for dynamic geometry such as Particle Systems
To use dynamic batching for meshes:
  1. Go to **Edit** > **Project Settings** > **Player**.
  2. In **Other Settings** , enable **Dynamic Batching**.
  3. In **Other Settings** , enable **Dynamic Batching**.


If your project uses the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP), the [Scriptable Render Pipeline (SRP) Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html) is enabled by default. To enable dynamic batching instead, go to the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#rendering) and enable **Dynamic Batching**.
Unity automatically batches moving meshes into the same draw call if they fulfill the criteria described in the [common usage information](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-Enable.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/dynamic-batching-meshes.html)
How Unity batches moving GameObjects
[](https://docs.unity3d.com/6000.0/Documentation/Manual/combining-meshes.html)
Combine meshes manually
