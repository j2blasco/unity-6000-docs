* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/reduce-rendering-work-on-cpu.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
  * Reducing rendering work on the CPU in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
Reducing rendering work on the CPU or GPU in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html)
Enable the GPU Resident Drawer in URP
# Reducing rendering work on the CPU in URP
You can use the GPU Resident Drawer or GPU **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling) to speed up rendering. When you enable these features, Unity optimizes the rendering pipeline so the CPU has less work to do each frame, and the GPU draws **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) more efficiently.
**Page** | **Description**  
---|---  
[Enable the GPU Resident Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html) | Automatically use the `BatchRendererGroup` API to use instancing and reduce the number of draw calls.  
[Make a GameObject compatible with the GPU Resident Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/make-object-compatible-gpu-rendering.html) | Include or exclude a GameObject from the GPU Resident Drawer.  
[Enable GPU occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html) | Use the GPU instead of the CPU to exclude GameObjects from rendering when they’re occluded behind other GameObjects.  
## Additional resources
  * [Graphics performance fundamentals](https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
Reducing rendering work on the CPU or GPU in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html)
Enable the GPU Resident Drawer in URP
