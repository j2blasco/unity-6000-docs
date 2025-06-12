* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LODRealtimeGI.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
  * LOD and Enlighten Realtime Global Illumination


[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-optimize.html)
Optimize Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGI.html)
Global Illumination Profiler module
# LOD and Enlighten Realtime Global Illumination
Objects with **Receive**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** set to ****Lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap)** have a lighting solution with lightmaps for baked direct and [indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmappingDirectional.html), and lightmaps for **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination. For more information about **Receive Global Illumination** , see the [Mesh Renderer settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html) and the script reference for [ReceiveGI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ReceiveGI.html).
When you use Unity’s **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) system in a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) where you have enabled Baked Global Illumination and Enlighten Realtime Global Illumination, the system lights the most detailed model out of the **LOD Group** A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) as if it has the **Contribute Global Illumination** setting enabled and isn’t part of the LOD group."
Enlighten can only compute direct lighting for lower LODs and the LOD system must rely on [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) to sample indirect lighting.
To enable the Editor to produce lightmaps with Enlighten Realtime Global Illumination, select the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) you want to affect, view its Renderer component in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window, and ensure that **Contribute Global Illumination** is enabled.
For lower LODs in a LOD Group, you can only combine baked lightmaps with Enlighten Realtime Global Illumination from [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html) or [Light Probe Proxy Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)A component that allows you to use more lighting information for large dynamic GameObjects that cannot use baked lightmaps (for example, large Particle Systems or skinned Meshes). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbeProxyVolume), which you must place around the LOD Group.
![An animation showing how real-time ambient color affects the Enlighten Realtime Global Illumination used by lower LODs](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/LODRealtimeGI.gif) An animation showing how real-time ambient color affects the Enlighten Realtime Global Illumination used by lower LODs
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-optimize.html)
Optimize Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/ProfilerGI.html)
Global Illumination Profiler module
