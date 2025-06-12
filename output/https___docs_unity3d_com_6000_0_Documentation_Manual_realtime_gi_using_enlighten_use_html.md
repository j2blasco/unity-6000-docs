* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-use.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Precalculating surface lighting with lightmaps](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-landing.html)
  * [Creating lightmaps at runtime with Enlighten Realtime Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-landing.html)
  * Enable Enlighten Realtime Global Illumination


[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html)
Introduction to Realtime Global Illumination using Enlighten
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-optimize.html)
Optimize Enlighten Realtime Global Illumination
# Enable Enlighten Realtime Global Illumination
To enable Enlighten Realtime Global Illumination in your Scene, open the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html) (menu: **Window** > **Rendering** > **Lighting**) and enable **Realtime Global Illumination**.
To disable the effect of **Realtime GI** on a specific Light, select the Light **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) and, in the Light component, set the **Indirect Multiplier** to 0. This means that the Light doesn’t contribute any indirect light to the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).
To disable **Realtime GI** altogether, open the Lighting window (menu: **Window** > **Rendering** > **Lighting**) and uncheck **Realtime Global Illumination**.
For detailed step-by-step advice on using **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination), see the Unity tutorial on [Precomputed Realtime GI](https://learn.unity.com/project/lighting-optimization-with-precomputed-realtime-gi).
## Light Probes and Enlighten Realtime Global Illumination
Note that [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) behave differently when you enable Enlighten Realtime Global Illumination.
In order to react to runtime changes in Scene lighting, they sample lighting iteratively at runtime.
When you disable Enlighten Realtime Global Illumination in a Scene, Light Probes only use baked lighting data. This means that they don’t react to runtime changes in Scene lighting.
## Shadows and Enlighten Realtime Global Illumination
If a Light also casts shadows, Unity renders both dynamic and static GameObjects in the Scene into the Light’s [shadow map](https://docs.unity3d.com/6000.0/Documentation/Manual/Shadows.html). The [Material Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html) of both static and dynamic GameObjects sample this shadow map so that these GameObjects cast real-time shadows onto each other. The **Shadow Distance** setting determines the maximum distance at which shadows begin to fade out and disappear entirely, which in turn affects performance and image quality.
Enlighten Realtime Global Illumination results also include soft shadows, unless the Scene is very small. These shadows are typically more coarse-grained than what lightmapping can achieve.
To modify **Shadow Distance** settings, navigate to **Edit** > **Project Settings** > **Quality** > **Shadows**.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html)
Introduction to Realtime Global Illumination using Enlighten
[](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten-optimize.html)
Optimize Enlighten Realtime Global Illumination
