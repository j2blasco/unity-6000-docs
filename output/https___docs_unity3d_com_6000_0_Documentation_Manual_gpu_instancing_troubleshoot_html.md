* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-troubleshoot.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
  * Troubleshooting GPU instancing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-enable.html)
Enable GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
Batching draw calls
# Troubleshooting GPU instancing
Meshes that have a low number of vertices can’t be processed efficiently using GPU instancing because the GPU can’t distribute the work in a way that fully uses the GPU’s resources. This processing inefficiency can have a detrimental effect on performance. The threshold at which inefficiencies begin depends on the GPU, but as a general rule, don’t use GPU instancing for meshes that have fewer than 256 vertices.
If you want to render a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) with a low number of vertices many times, best practice is to create a single buffer that contains all the mesh information and use that to draw the meshes.
## Additional resources
  * [Make materials incompatible with the SRP Batcher in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-Incompatible.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-enable.html)
Enable GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching-landing.html)
Batching draw calls
