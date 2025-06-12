* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInstancing.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Particle shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShadersLanding.html)
  * [Particle System optimization in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html)
  * Apply GPU instancing for a Particle System in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html)
Particle System optimization in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-surface-shader.html)
Example of Particle System GPU instancing in a Surface Shader
# Apply GPU instancing for a Particle System in the Built-In Render Pipeline
GPU instancing offers a large performance boost compared with CPU rendering. You can use it if you want your **particle system** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem) to render **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) particles (as opposed to the default [rendering mode](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html) of rendering **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) particles).
To be able to use GPU instancing with your particle systems:
  * Set your Particle System’s [renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html) mode to **Mesh**
  * Use a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for the [renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html) material that supports GPU Instancing
  * Run your project on a platform that supports GPU instancing


To enable GPU instancing for a particle system, you must enable the **Enable GPU Instancing** checkbox in the **Renderer** module of your particle system.
![The option to enable Particle System GPU instancing in the Renderer module](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysInstancingEnable.png) The option to enable Particle System GPU instancing in the Renderer module
Unity comes with a built-in particle shader that supports GPU instancing, but the default particle material does not use it, so you must change this to use GPU instancing. The particle shader that supports GPU instancing is called **Particles/Standard Surface**. To use it, you must create your own new **material** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material), and set the material’s shader to **Particles/Standard Surface**. You must then assign this new material to the material field in the Particle System [renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysRendererModule.html) module.
![The built-in shader that is compatible with Particle System GPU Instancing](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/PartSysInstancingShader.png) The built-in shader that is compatible with Particle System GPU Instancing
If you are using a different shader for your particles, it must use ‘#pragma target 4.5’ or higher. See [Shader Compile Targets](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompileTargets.html) for more details. This requirement is higher than regular GPU Instancing in Unity because the Particle System writes all its instance data to a single large buffer, rather than breaking up the instancing into multiple draw calls.
## Custom shader examples
You can also write custom shaders that make use of GPU Instancing. See the following sections for more information:
  * [Particle system GPU Instancing in a Surface Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-surface-shader.html)
  * [Particle system GPU Instancing in a Custom Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-custom-shader.html)
  * [Customising instance data used by the Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-custom-vertex-streams.html) (to work alongside Custom Vertex Streams)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html)
Particle System optimization in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-surface-shader.html)
Example of Particle System GPU instancing in a Surface Shader
