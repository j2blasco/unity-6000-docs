* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-optimize.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
  * Optimize Enlighten Realtime Global Illumination


[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-use.html)
Enable Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LODRealtimeGI.html)
LOD and Enlighten Realtime Global Illumination
# Optimize Enlighten Realtime Global Illumination
Enlighten Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) uses a set of **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) to store real-time indirect bounces. For this reason, enabling it increases memory requirements, even if you are using it along with Baked Global Illumination.
The number of **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) calculations needed to generate lighting also increases when you use **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination because it samples an additional set of lightmaps and **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).
If Enlighten Realtime Global Illumination doesn’t respond quickly enough to changes in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) lighting, there are several ways to address this problem:
  * Reduce the real-time lightmap resolution to speed up calculation at runtime.
  * Increase the CPU Usage setting for **Realtime GI** in the Quality Settings window. The tradeoff is that other systems receive less CPU time to do their work. Whether this is acceptable depends on your Project. This is a per-Scene setting, so you can dedicate more or less CPU time based on the complexity of each individual Scene in your Project.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-use.html)
Enable Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LODRealtimeGI.html)
LOD and Enlighten Realtime Global Illumination
