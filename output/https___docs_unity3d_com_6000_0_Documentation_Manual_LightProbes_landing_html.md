* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-landing.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * Precalculating indirect light with Light Probes


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-Reference.html)
Lightmap UVs Settings in the Model Import Settings Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)
Light Probes
# Precalculating indirect light with Light Probes
Resources and techniques for using **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) to store the light at specific points in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), so that Unity can calculate indirect lighting for **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) more quickly. 
**Page** | **Description**  
---|---  
[Introduction to Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) | Learn about using Light Probes to store the light passing through specific points in a scene.  
[Light Probes and moving GameObjects](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-MovingObjects.html) | Understand how dynamic GameObjects sample the light from Light Probes.  
[Place Light Probes with the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html) | Choose where to place Light Probes, and choose the right amount of probes if you use **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination).  
[Place Light Probes with a script](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Placing-Scripting.html) | An example of forming a ring of Light Probes with a script.  
[Set a GameObject to use light from Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-MeshRenderer.html) | Use a **Mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) Renderer component to set a GameObject correctly to receive light from Light Probes.  
[Load Light Probes in multiple scenes](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-and-scene-loading.html) | Use a script to control when Unity updates Light Probes if you load multiple scenes.  
[Move Light Probes at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Moving.html) | Use the `LightProbes` API to move Light Probes, for example if you create a world by loading multiple scenes additively and moving each scene to a different position.  
[Troubleshooting Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/light-probes-troubleshooting.html) | Solve common issues with Light Probes, such as light bleeding and ringing.  
[Light Probes reference](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-Reference.html) | Explore the properties and settings in the Light Probe component **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window reference and the Edit **Light Probe Group** A component that enables you to add Light Probes to GameObjects in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeGroup) tool.  
# Additional resources
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * [Configure an object to sample more light probes in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingGiUvs-Reference.html)
Lightmap UVs Settings in the Model Import Settings Inspector window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)
Light Probes
