* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baked-tags.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * [Configuring lightmaps and baking](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
  * Group GameObjects together in a lightmap with Baked Tags


[](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html)
Select the CPU or GPU for baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-troubleshooting.html)
Troubleshooting baked lightmaps
# Group GameObjects together in a lightmap with Baked Tags
The two images below shows two views of the same **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene):
![In this example, all the GameObjects have the same Baked tag, and Unity stores all lighting data in one atlas.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BakedLightmaps-Merged.png) ![In this example, one GameObject is assigned a different Baked tag, and Unity creates a separate lightmap for it.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/BakedLightmaps-Merged2.png)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html)
Select the CPU or GPU for baking
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-troubleshooting.html)
Troubleshooting baked lightmaps
