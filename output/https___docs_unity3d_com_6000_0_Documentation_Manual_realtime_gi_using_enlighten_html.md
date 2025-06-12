* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
  * Introduction to Realtime Global Illumination using Enlighten


[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
Creating lightmaps at runtime with Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-use.html)
Enable Enlighten Realtime Global Illumination
# Introduction to Realtime Global Illumination using Enlighten
Unity uses a middleware solution called **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) for Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination).
By default, [Realtime Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#realtime)Light components whose Mode property is set to Realtime. Unity calculates and updates the lighting of Realtime Lights every frame at runtime. No Realtime Lights are precomputed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#realtime)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RealtimeLights) contribute only direct lighting to a **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). If you enable **Realtime Global Illumination** (Enlighten Realtime Global Illumination) in your Scene, Realtime Lights also contribute indirect lighting to a Scene.
## Render pipeline support
See [render pipeline feature comparison](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html) for more information about support for Realtime Global Illumination using Enlighten across **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
## When to use Enlighten Realtime Global Illumination
Enlighten Realtime Global Illumination (Realtime GI) is useful for Lights that change slowly and have a significant visual impact on your Scene, such as the sun moving across the sky, or a slowly pulsating light in a closed corridor. This feature is not intended for special effects or Lights that change quickly, because latency and the number of CPU cycles needed make that sort of application impractical. Enlighten Realtime Global Illumination is suitable for games targeting mid-level to high-end PC systems and consoles. Some high-end mobile devices may also be powerful enough to make use of this feature, but you should keep Scenes small and the resolution for real-time **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) low to ensure acceptable performance.
## How Enlighten Realtime Global Illumination works
Enlighten Realtime Global Illumination does the following:
  1. Splits the scene into small surface patches (clusters).
  2. Determines the degree to which the patches are visible to each other.
  3. Groups patches visible to each other into systems.


At runtime, Enlighten Realtime Global Illumination uses this precomputed visibility information to approximate how Realtime Lights bounce in the Scene, saves the results in a set of lightmaps, and then uses these lightmaps to apply indirect lighting to the Scene. It is computationally intensive to update the lightmaps, and so the process is split across several frames. It takes Enlighten Realtime Global Illumination several frames to propagate changes to indirect lighting throughout the Scene.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
Creating lightmaps at runtime with Enlighten Realtime Global Illumination
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-use.html)
Enable Enlighten Realtime Global Illumination
