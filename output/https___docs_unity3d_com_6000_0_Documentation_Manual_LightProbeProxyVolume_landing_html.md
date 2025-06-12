* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html)
Add ambient occlusion in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)
Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline
# Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline
To make lighting more realistic, use a **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) Proxy Volume to configure a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) to sample multiple Light Probes.
**Page** | **Description**  
---|---  
[Light Probe Proxy Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeProxyVolume) | Understand how a Light Probe Proxy Volume component generates a 3D grid and texture that Unity uses to create gradients on GameObjects.  
[Set a GameObject to use a Light Probe Proxy Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-add.html) | Use the settings in a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component to set a GameObject to sample multiple probes.  
[Configure a Light Probe Proxy Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-configure.html) | Change the size and data format of a Light Probe Proxy Volume.  
[Light Probe Proxy Volume component reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-reference.html) | Explore the properties and settings in the Light Probe Proxy Volume component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window to customize how Unity generates the 3D grid and texture.  
[Add Light Probe Proxy Volume support to a custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-Shader.html) | An example of a particle **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that uses the `ShadeSHPerPixel` function to add support for a Light Probe Proxy Volume.  
## Additional resources
  * [Precalculating indirect light with Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html)
Add ambient occlusion in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)
Introduction to Light Probe Proxy Volumes in the Built-In Render Pipeline
