* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-runtime.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components.html)
  * [Configuring Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components-configuring.html)
  * [Configuring Mixed lights with Lighting Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)
  * Adjust Mixed lights at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Scene.html)
Set the Lighting Mode of a scene
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer-landing.html)
Configuring lights with the Light Explorer
# Adjust Mixed lights at runtime
In the Baked Indirect Lighting Mode, you can subtly change the properties of a Mixed Light at runtime. Changes affect the real-time direct lighting that the Mixed Light contributes to the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), without affecting the baked indirect lighting that the Mixed Light contributes to the Scene. This allows you to combine the benefits of baked indirect lighting with some of the dynamic capabilities of a Realtime Light. This works especially well in Baked Indirect Lighting Mode, due to the lack of precomputed shadows.
You must be careful with runtime changes to Light properties, and only make small changes that don’t cause unrealistic combinations of real-time direct and baked indirect lighting. For example, if you bake a red Mixed Light into a **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) and then change its color to green at runtime, the direct lighting is green but the indirect lighting baked into the lightmap remains red. The same applies to moving a Mixed Light at runtime: direct lighting follows the Light’s new position, but indirect lighting remains at the position at which the Light was baked.
This video shows an example of how to slightly modify a Mixed Light without causing noticeable inconsistencies in the indirect lighting: <https://youtu.be/XN6ya31gm1I>
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Scene.html)
Set the Lighting Mode of a scene
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingExplorer-landing.html)
Configuring lights with the Light Explorer
