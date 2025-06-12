* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-bake.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Baking lightmaps before runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-baking-before-runtime.html)
  * Bake lighting


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html)
Preview baked lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
Configuring lightmaps and baking
# Bake lighting
To generate **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) for your Scene:
  1. Open the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) (menu: **Window** > **Rendering** > **Lighting**)
  2. At the bottom of the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) tab on the Lighting window, select **Generate Lighting**.
  3. A progress bar appears in Unity Editor’s status bar, in the bottom-right corner.


When lightmapping is complete, Unity’s Scene and Game views update automatically and you can view the resulting lightmaps by going to the **Baked Lightmaps** tab in the Lighting Window.
When you generate lighting, Unity adds [Lighting Data Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmapSnapshot.html), [baked lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) and [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/ReflectionProbes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) to the [Assets](https://docs.unity3d.com/6000.0/Documentation/Manual/SpecialFolders.html)Any media or data that can be used in your game or project. An asset may come from a file created outside of Unity, such as a 3D Model, an audio file or an image. You can also create some asset types in Unity, such as an Animator Controller, an Audio Mixer or a Render Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/AssetWorkflow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Asset) folder.
## Bake lightmaps automatically
To set Unity to bake lightmaps automatically when you open a scene that has no lighting data, follow these steps:
  1. Go to **Window** > **Rendering** > **Lighting**.
  2. Set **Bake on Scene Load** to **If Missing Lighting Data**.


If you share your project with someone else, you can use this option to reduce the size of your project by not including lighting data. When a scene is opened by someone else, Unity calculates the missing lighting data.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html)
Preview baked lighting
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-configure.html)
Configuring lightmaps and baking
