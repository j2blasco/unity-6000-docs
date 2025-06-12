* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * Baking lightmaps before runtime


[](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-lighting-setup.html)
Global illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)
Introduction to lightmaps and baking
# Baking lightmaps before runtime
Resources for precalculating the lit colors of **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and storing them in textures called **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap).
**Page** | **Description**  
---|---  
[Lightmaps and baking](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html) | Learn about precalculating the color and brightness of surfaces in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), then storing the result in a texture called a lightmap for later use.  
[Set up your scene and lights for baking](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html) | Set up meshes and GameObjects so that they store precalculated color in lightmaps.  
[Preview baked lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html) | Edit a scene and preview changes to lightmaps and lighting without affecting the baked lightmaps.  
[Bake lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-bake.html) | Generate lightmaps for your scene.  
[Configuring baking lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html) | Resources for selecting CPU or GPU lightmapping, and changing how GameObjects store lighting in lightmaps.  
[Troubleshooting baked lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-troubleshooting.html) | Solve common issues with baked lightmaps, such as hard edges or light bleeding.  
[Optimize baked lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/GPUProgressiveLightmapper.html) | Speed up baking time by configuring baking settings or selecting different GPUs for rendering and baking.  
[Lightmapping settings in the Lighting Settings Asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-reference.html) | Explore the properties and settings in the Lighting Settings Asset window to customize baking lightmaps.  
## Additional resources
  * [Configure lightmapping with a Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/global-illumination-configure.html)
  * [Lighting Settings Asset Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/choose-a-lighting-setup.html)
Global illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)
Introduction to lightmaps and baking
