* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightingBakedAmbientOcclusion.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-birp.html)
  * [Shadows in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shadows-in-birp.html)
  * Add ambient occlusion in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-resolution-birp.html)
Configure shadow resolution in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html)
Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline
# Add ambient occlusion in the Built-In Render Pipeline
**Ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (AO) is a feature that simulates the soft shadows that occur in creases, holes, and surfaces that are close to each another. These areas occlude (block out) **ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientlight), so they appear darker.
It works by approximating how much ambient light can hit a point on a surface. It then darkens creases, holes and surfaces that are close to each other.
You can use ambient occlusion to add realism to your lighting.
## Baked Ambient Occlusion
If **Baked**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** is enabled in your **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), Unity can bake ambient occlusion into the **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap). This is known as **Baked Ambient Occlusion**.
To enable baked ambient occlusion in your Scene:
  1. Open the **Lighting** window (menu: **Window** > **Rendering** > **Lighting**)
  2. Navigate to the **Mixed Lighting** section
  3. Enable **Baked Global Illumination**
  4. Navigate to the **Lightmapping Settings** section
  5. Enable **Ambient Occlusion**


## Realtime ambient occlusion
If Global Illumination is not enabled in your Scene but you still want the effect of ambient occlusion, you can use a **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effect to apply real-time ambient occlusion to your Scene.
If ****Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination** is enabled in your scene, the resolution for indirect lighting does not capture fine details or dynamic objects. We recommend using a real-time ambient occlusion post-processing effect, which has much more detail and results in higher quality lighting.
For information on real-time ambient occlusion post-processing effects, see [post-processing effects](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html).
## Additional resources
  * [Screen space ambient occlusion in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-resolution-birp.html)
Configure shadow resolution in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbeProxyVolume-landing.html)
Configure a GameObject to sample more Light Probes in the Built-In Render Pipeline
