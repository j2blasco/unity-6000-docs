* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * Lighting data


[](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
Direct and indirect lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-precomputed-data.html)
Introduction to lighting data
# Lighting data
Resources for how Unity stores lighting data and visibility data for lightmapping, **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe), and **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).
**Page** | **Description**  
---|---  
[Introduction to lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-precomputed-data.html) | Understand how Unity stores lighting data and visibility data for lightmapping, Light Probes, and Reflection Probes.  
[Lighting Data Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmapSnapshot.html) | Learn about the asset Unity creates to store precomputed lighting data for a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
[GI cache](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)The cached intermediate files used when Unity precomputes lighting data. Unity keeps this cache to speed up computation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GICache) | Learn about the internal data cache Unity uses to store intermediate files when it precomputes lighting data for lightmapping.  
[Lightmap data format](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-TechnicalInformation.html) | Understand how Unity stores light intensity as textures during lightmapping, and learn about support for high dynamic range (HDR) **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap).  
[Light Probe data format](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html) | Understand how Unity stores light as spherical harmonics data in Light Probes.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
Direct and indirect lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-precomputed-data.html)
Introduction to lighting data
