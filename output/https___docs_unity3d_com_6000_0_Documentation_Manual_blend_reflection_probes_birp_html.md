* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/blend-reflection-probes-birp.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * Blend Reflection Probes in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-Shader.html)
Add Light Probe Proxy Volume support to a custom shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html)
Light component Inspector window reference for the Built-In-Render-Pipeline
# Blend Reflection Probes in the Built-In Render Pipeline
To enable Reflection Probe blending navigate to **Graphic Settings** > **Tier settings**. Tier settings are only available in Unity’s [Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html). When blending is enabled, Unity gradually fades out one probe’s cubemap while fading in the other’s as the reflective object passes from one zone to the other. This gradual transition avoids the situation where a distinctive object suddenly “pops” into the reflection as an object crosses the zone boundary.
Blending is controlled using the **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) property of the [Mesh Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)A mesh component that takes the geometry from the Mesh Filter and renders it at the position defined by the object’s Transform component. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-MeshRenderer.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MeshRenderer) component. Four blending options are available:
  * **Off** - Reflection probe blending is disabled. Only the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) will be used for reflection
  * **Blend Probes** - Blends only adjacent probes and ignores the skybox. You should use this for objects that are “indoors” or in covered parts of the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) (eg, caves and tunnels) since the sky is not visible from these place and so should never appear in the reflections.
  * **Blend Probes and Skybox** - Works like _Blend Probes_ but also allows the skybox to be used in the blending. You should use this option for objects in the open air, where the sky would always be visible.
  * **Simple** - Disables blending between probes when there are two overlapping reflection probe volumes.


When probes have equal **Importance** values, the blending weight for a given probe zone is calculated by dividing its intersection (volume) with the object’s bounding box by the sum of all probes’ intersections with the box. For example, if the box intersects probe A’s zone by 1.0 cubic units and intersects probe B’s zone by 2.0 cubic units then the blending values will be:
  * Probe A: 1.0 / (1.0 + 2.0) = 0.33
  * Probe B: 2.0 / (1.0 + 2.0) = 0.67


In other words, the blend will incorporate 33% of probe A’s reflection and 67% of probe B’s reflection.
The calculation must be handled slightly differently in the case where one probe is entirely contained within the other, since the inner zone overlaps entirely with the outer. If the object’s bounding box is entirely within the inner zone then that zone’s blending weight is 1.0 (ie, the outer zone is not used at all). When the object is partially outside the inner zone, the intersection volume of its bounding box with the inner zone is divided by the total volume of the box. For example, if the intersection volume is 1.0 cubic units and the bounding box’s volume is 4.0 cubic units, then the blending weight of the inner probe will be 1.0 / 4.0 = 0.25. This value is then subtracted from 1.0 to get the weight for the outer probe which in this case will be 0.75.
When one probe involved in the blend has a higher **Importance** value than another, the more important probe overrides the other in the usual way.   
  

## Additional resources
  * [Reflections](https://docs.unity3d.com/6000.0/Documentation/Manual/reflections-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume-Shader.html)
Add Light Probe Proxy Volume support to a custom shader in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html)
Light component Inspector window reference for the Built-In-Render-Pipeline
