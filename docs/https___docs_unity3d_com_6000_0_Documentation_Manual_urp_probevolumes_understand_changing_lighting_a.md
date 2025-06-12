* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * [Changing lighting at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html)
  * Choose how to change lighting at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html)
Changing lighting at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
Bake different lighting setups with Lighting Scenarios
# Choose how to change lighting at runtime
You can change how objects use the baked data in Adaptive Probe Volumes, to create lighting that changes at runtime. For example, you can turn the lights on and off in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or change the time of day.
You can use one of the following processes:
  * [Bake different lighting setups with Lighting Scenarios](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html), for example you can bake a Lighting Scenario for each stage in a day-night cycle.
  * [Update light from the sky at runtime with sky occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html).


Lighting Scenarios have the following advantages:
  * Lighting Scenarios are more accurate. Lighting Scenarios don’t approximate the light from the sky, or the color of objects that light bounces off.
  * Lighting Scenarios store all the lighting in a scene, so you can update light from both the sky and scene lights.


Sky occlusion has the following advantages:
  * Easier to set up. For example, you only need to bake once to set up the data you need for a day-night cycle.
  * Better performance.
  * Faster and smoother transitions, because sky occlusion doesn’t have to blend between different sets of data.


You can use sky occlusion and Lighting Scenarios together. For example, you can use sky occlusion to update the light from the sky, and Lighting Scenarios to update the position of the sun or the state of an interior lamp.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html)
Changing lighting at runtime
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
Bake different lighting setups with Lighting Scenarios
