* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
  * Introduction to GPU instancing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-enable.html)
Enable GPU instancing
# Introduction to GPU instancing
GPU instancing is a [draw call optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/optimizing-draw-calls.html) method that renders multiple copies of a **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) with the same material in a single draw call. Each copy of the mesh is called an instance. This is useful for drawing things that appear multiple times in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), for example, trees or bushes.
GPU instancing renders identical meshes in the same draw call. To add variation and reduce the appearance of repetition, each instance can have different properties, such as **Color** or **Scale**. Draw calls that render multiple instances appear in the [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html) as **Render Mesh (instanced)**.
## Requirements and compatibility
This section includes information about the platform, **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), and SRP Batcher compatibility of GPU instancing.
### Platform compatibility
GPU instancing is available on every platform. However, the performance benefits of GPU instancing depend on the platform and the GPU you’ve chosen. For example, the performance benefits are more prominent on mobile platforms than on desktop platforms.
### Render pipeline compatibility
**Feature** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom Scriptable Render Pipeline (SRP)** | **Built-in Render Pipeline**  
---|---|---|---|---  
**GPU instancing** | Yes (1) | Yes (1) | Yes (1) | Yes  
**Notes** :
  1. Only if the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) isn’t compatible with the [SRP Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html). Refer to [Make materials incompatible with the SRP Batcher](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-Incompatible.html) for more information.


### Lighting
GPU instancing supports Unity’s [Baked Global Illumination system](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html). Unity Standard Shaders and **surface shaders** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) in the Built-In Render Pipeline support GPU instancing and Unity’s Baked **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) system by default.
Each GPU instance supports global illumination from one of the following sources:
  * Any number of [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).
  * One [lightmap](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap).   
**Note** : An instance can use multiple atlas regions in the lightmap.
  * One [Light Probe Proxy Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeProxyVolume)(LPPV) component.   
**Note** : You must bake the LPPV for the space volume that contains all the instances.


GPU instancing automatically works with:
  * Dynamic [Mesh Renderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) affected by Light Probes.
  * Static Mesh Renderers you bake to the same lightmap texture. A Mesh Renderer is static in this context if it includes **Contribute GI** in its [Static Editor Flags](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-enable.html)
Enable GPU instancing
