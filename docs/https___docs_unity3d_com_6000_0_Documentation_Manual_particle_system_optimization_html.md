* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/particle-system-optimization.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Prebuilt shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp.html)
  * [Particle shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardParticleShadersLanding.html)
  * Particle System optimization in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/define-custom-data-formats-particles.html)
Define custom data formats for particles in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInstancing.html)
Apply GPU instancing for a Particle System in the Built-In Render Pipeline
# Particle System optimization in the Built-In Render Pipeline
Resources for using GPU instancing to improve the performance of your **particle systems** A component that simulates fluid entities such as liquids, clouds and flames by generating and animating large numbers of small 2D images in the scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ParticleSystem.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#particlesystem).
**Property** | **Function**  
---|---  
[Apply GPU instancing for a Particle System](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInstancing.html) | Activate and apply GPU instancing, which renders **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) particles instead of **billboard** A textured 2D object that rotates so that it always faces the Camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-BillboardRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Billboard) particles to improve performance.  
[Example of Particle System GPU Instancing in a Surface Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-surface-shader.html) | View an example script for applying GPU instancing to a Surface **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).  
[Example of Particle System GPU Instancing in a Custom Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-custom-shader.html) | View an example script for applying GPU instancing to a Custom Shader.  
[Example of Particle system GPU Instancing with custom vertex streams](https://docs.unity3d.com/6000.0/Documentation/Manual/example-particle-system-gpu-instancing-custom-vertex-streams.html) | View an example script for applying GPU instancing with custom vertex streams.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/define-custom-data-formats-particles.html)
Define custom data formats for particles in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/PartSysInstancing.html)
Apply GPU instancing for a Particle System in the Built-In Render Pipeline
