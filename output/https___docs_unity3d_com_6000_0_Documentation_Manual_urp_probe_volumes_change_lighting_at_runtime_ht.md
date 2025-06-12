* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * Changing lighting at runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-usebakingsets.html)
Bake multiple scenes together with Baking Sets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
Choose how to change lighting at runtime
# Changing lighting at runtime
You can change how objects use the baked data in Adaptive Probe Volumes, to create lighting that changes at runtime. For example, you can turn the lights on and off in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), or change the time of day.
Page | Description  
---|---  
[Choose how to change lighting at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html) | Choose whether to use Lighting Scenarios or sky occlusion.  
[Bake different lighting setups with Lighting Scenarios](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html) | Use multiple Lighting Scenarios to store baking results for different scene setups, and switch or blend between them at runtime.  
[Update light from the sky at runtime with sky occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html) | Sky occlusion means that when a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) samples a color from the sky, Unity dims the color if the light can’t reach the GameObject.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-usebakingsets.html)
Bake multiple scenes together with Baking Sets
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-understand-changing-lighting-at-runtime.html)
Choose how to change lighting at runtime
