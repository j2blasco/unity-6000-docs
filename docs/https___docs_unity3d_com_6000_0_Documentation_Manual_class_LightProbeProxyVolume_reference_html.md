* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-reference.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * [Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html)
  * Light Probe Proxy Volume component reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-configure.html)
Configure a Light Probe Proxy Volume in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-Shader.html)
Add Light Probe Proxy Volume support to a custom shader in the Built-In Render Pipeline
# Light Probe Proxy Volume component reference for the Built-In Render Pipeline
There are three options available:
**Bounding Box Mode:** | **Function:**  
---|---  
**Automatic Local** (default value) | A local-space bounding box is computed. The interpolated Light Probe positions are generated inside this bounding box. If a Renderer component isn’t attached to the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), then a default bounding box is generated. The bounding box computation encloses the current Renderer, and sets all the Renderers down the hierarchy that have the **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) property to **Use Proxy Volume**.  
**Automatic World** | A bounding box is computed which encloses the current Renderer and all the Renderers down the hierarchy that have the **Light Probes** property set to **Use Proxy Volume**. The bounding box is world-aligned.  
**Custom** | A custom bounding box is used. The bounding box is specified in the local-space of the GameObject. The bounding box editing tools are available. You can edit the **bounding volume** A closed shape representing the edges and faces of a collider or trigger.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Boundingvolume) manually by modifying the **Size** and **Origin** values in the UI (see below).  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-configure.html)
Configure a Light Probe Proxy Volume in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-Shader.html)
Add Light Probe Proxy Volume support to a custom shader in the Built-In Render Pipeline
