* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/make-object-compatible-gpu-rendering.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
  * [Reducing rendering work on the CPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/reduce-rendering-work-on-cpu.html)
  * Make a GameObject compatible with the GPU Resident Drawer in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html)
Enable the GPU Resident Drawer in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html)
Enable GPU occlusion culling in URP
# Make a GameObject compatible with the GPU Resident Drawer in URP
To make a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) compatible with the [GPU Resident Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html), check it has the following properties:
  * Has a [Mesh Renderer component](https://docs.unity3d.com/Manual/class-MeshRenderer.html).
  * In the **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component, ****Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe)** isn’t set to **Use Proxy Volume**.
  * Uses only static **global illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination), not real time global illumination.
  * Uses a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that supports DOTS instancing. Refer to [Supporting DOTS Instancing](https://docs.unity3d.com/Manual/dots-instancing-shaders.html) for more information.
  * Doesn’t move position after one **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) finishes rendering and before another camera starts rendering.
  * Doesn’t use the `MaterialPropertyBlock` API.
  * Doesn’t have a script that uses a per-instance callback, for example `OnRenderObject`.


## Exclude a GameObject from the GPU Resident Drawer
To exclude a GameObject from the GPU Resident Drawer, add a **Disallow GPU Driven Rendering** component to the GameObject.
  1. Select the GameObject.
  2. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, select **Add Component**.
  3. Select **Disallow GPU Driven Rendering**.


Select **Apply to Children Recursively** to exclude both the GameObject and its children.
## Additional resources
  * [Mesh Renderer component](https://docs.unity3d.com/Manual/class-MeshRenderer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html)
Enable the GPU Resident Drawer in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html)
Enable GPU occlusion culling in URP
