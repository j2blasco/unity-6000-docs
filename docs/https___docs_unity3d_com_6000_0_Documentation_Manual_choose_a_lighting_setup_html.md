* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-lighting-setup.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * Global illumination


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
Precalculating surface lighting with lightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
Baking lightmaps before runtime
# Global illumination
Global illumination is a group of techniques that model both direct and indirect lighting to provide realistic lighting results.
Unity has the following **global illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) systems:
  * Baked Global Illumination
  * **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination


With both systems, you need to make sure you set up texture UVs correctly, and control **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) placement to avoid increasing baking time.
If you’re experimenting with lighting, you can disable both global illumination systems so lighting updates more quickly. To compensate for the lack of indirect lighting, enable [screen space ambient occlusion (SSAO)](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html).
For more information about support for global illumination across **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), refer to [render pipeline feature comparison reference](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html).
## Baked Global Illumination
Unity uses a CPU or GPU **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) to store lighting data in your build, in Light Probes, **Reflection Probes** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), and textures called **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap). 
Lighting quality is usually better than Enlighten Realtime Global Illumination.
For more information, refer to [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html).
## Enlighten Realtime Global Illumination
Unity stores some lighting data in your build, but uses the data to create lightmaps at runtime. As a result, you can adjust lights and see the effects on indirect lighting in real-time, in the Editor or at runtime.
Enlighten Realtime Global Illumination doesn’t support global illumination from realtime shadows.
For more information, refer to [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html). 
## Using both systems together
The Unity Editor and Player allow you to use both Enlighten Realtime Global Illumination and baked lighting at the same time.
However, simultaneously enabling these features greatly increases baking time and memory usage at runtime, because they do not use the same data sets. You can expect visual differences between indirect light you have baked and indirect light provided by Enlighten Realtime Global Illumination, regardless of the lightmapper you use for baking. This is because Enlighten Realtime Global Illumination often operates at a significantly different resolution than Unity’s baking backends, and relies on different techniques to simulate indirect lighting.
If you wish to use both Enlighten Realtime Global Illumination and baked lighting at the same time, limit your simultaneous use of both global illumination systems to high-end platforms and/or to projects that have tightly controlled **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with predictable costs. Only expert users who have a very good understanding of all lighting settings can effectively use this approach. Consequently, picking one of the two global illumination systems is usually a safer strategy for most projects. Using both systems is rarely recommended.
## Additional resources
  * [Choose a render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-render-pipeline.html)
  * [Choose a Light Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-choose.html)
  * [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * [Manage your templates](https://docs.unity3d.com/hub/manual/Templates.html)
  * [Creating Believable Visuals tutorial (Built-In Render Pipeline)](https://unity3d.com/learn/tutorials/s/creating-believable-visuals)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
Precalculating surface lighting with lightmaps
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
Baking lightmaps before runtime
