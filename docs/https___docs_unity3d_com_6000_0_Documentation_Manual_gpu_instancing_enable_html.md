* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-enable.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Optimizing draw calls](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing.html)
  * [GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing-landing.html)
  * Enable GPU instancing


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html)
Introduction to GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-troubleshoot.html)
Troubleshooting GPU instancing
# Enable GPU instancing
Unity uses GPU instancing for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that share the same **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) and material. To instance a mesh and material:
  * The material’s [shader](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) must support GPU instancing. Unity’s [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) supports GPU instancing, as do all [surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader). To add GPU instancing support to any other shader, see [Creating shaders that support GPU instancing](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-shader.html).
  * The mesh must come from one of the following sources, grouped by behavior: 
    * A [MeshRenderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) component or a [Graphics.RenderMesh](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMesh.html) call.   
Behavior: Unity adds these meshes to a list and then checks to see which meshes it can instance.   
Unity does not support GPU instancing for [SkinnedMeshRenderers](https://docs.unity3d.com/6000.0/Documentation/Manual/class-SkinnedMeshRenderer.html) or MeshRenderer components attached to GameObjects that are SRP Batcher compatible. For more information, see [SRP Batcher compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher.html).
    * A [Graphics.RenderMeshInstanced](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshInstanced.html) or [Graphics.RenderMeshIndirect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.RenderMeshIndirect.html) call. These methods render the same mesh multiple times using the same shader. Each call to these methods issues a separate draw call. Unity does not merge these draw calls.


To use GPU instancing for a material, select the **Enable GPU Instancing** option in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector).
To enable **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) rendering for `Graphics.RenderMeshInstanced`, provide a [MaterialPropertyBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MaterialPropertyBlock.html) that includes the Probe data. For more information and code examples, see [LightProbes.CalculateInterpolatedLightAndOcclusionProbes](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightProbes.CalculateInterpolatedLightAndOcclusionProbes.html).
Alternatively, if your project uses the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can pass an LPPV component reference and [LightProbeUsage.UseProxyVolume](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.LightProbeUsage.UseProxyVolume.html) to `Graphics.RenderMeshInstanced`. When you do this, all instances sample the volume for the [L0 and L1 bands](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html) of the Light Probe data. If you want to supplement L2 data and occlusion data, use a `MaterialPropertyBlock`. For more information, see [Light Probes: Technical Information](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html).
## Additional resources
  * [Make materials incompatible with the SRP Batcher in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/SRPBatcher-Incompatible.html)
  * [Creating custom shaders that support GPU instancing in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-shader.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUInstancing.html)
Introduction to GPU instancing
[](https://docs.unity3d.com/6000.0/Documentation/Manual/gpu-instancing-troubleshoot.html)
Troubleshooting GPU instancing
