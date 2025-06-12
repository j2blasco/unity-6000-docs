* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
  * [Reducing rendering work on the CPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/reduce-rendering-work-on-cpu.html)
  * Enable GPU occlusion culling in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/make-object-compatible-gpu-rendering.html)
Make a GameObject compatible with the GPU Resident Drawer in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)
Adjust settings to improve performance in URP
# Enable GPU occlusion culling in URP
GPU occlusion culling means Unity uses the GPU instead of the CPU to exclude objects from rendering when they’re occluded behind other objects. Unity uses this information to speed up rendering in **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that have a lot of occlusion.
The GPU Resident Drawer works only with the following:
  * The [Forward+](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html) **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath).
  * [Graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html) and platforms that support compute **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).


## How GPU occlusion culling works
Unity generates depth textures from the perspective of **cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) and lights in the scene.
The GPU then uses the depth textures from the current frame and the previous frame to cull objects. Unity renders only objects that are unoccluded in either frame. Unity culls the remaining objects, which are occluded in both frames.
Whether GPU occlusion culling speeds up rendering depends on your scene. GPU occlusion culling is most effective in the following setups:
  * Multiple objects use the same **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh), so Unity can group them into a single draw call.
  * The scene has a lot of occlusion, especially if the occluded objects have a high number of vertices.


If occlusion culling doesn’t have a big effect on your scene, rendering time might increase because of the extra work the GPU does to set up GPU occlusion culling. 
## Enable GPU occlusion culling
  1. Go to **Graphics** , select the **URP** tab, then in the **Render Graph** section make sure **Compatibility Mode (Render Graph Disabled)** is disabled.
  2. [Enable the GPU Resident Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html#enable-the-gpu-resident-drawer).
  3. In the active [Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html), enable **GPU Occlusion**.


## Analyze GPU occlusion culling
You can use the following to analyze GPU occlusion culling:
  * [Rendering Statistics](https://docs.unity3d.com/Manual/RenderingStatistics.html) overlay to check rendering speed increases.
  * [Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html) to troubleshoot issues.


## Additional resources
  * [Reduce rendering work on the CPU](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/reduce-rendering-work-on-cpu.html)
  * [Occlusion culling](https://docs.unity3d.com/Manual/OcclusionCulling.html)A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/make-object-compatible-gpu-rendering.html)
Make a GameObject compatible with the GPU Resident Drawer in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)
Adjust settings to improve performance in URP
