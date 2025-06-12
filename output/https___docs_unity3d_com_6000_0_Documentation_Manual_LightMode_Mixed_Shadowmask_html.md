* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Mixed-Shadowmask.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Light sources](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-sources.html)
  * [Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components.html)
  * [Configuring Light components](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-light-components-configuring.html)
  * [Configuring Mixed lights with Lighting Modes](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)
  * Lighting Mode


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)
Configuring Mixed lights with Lighting Modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Scene.html)
Set the Lighting Mode of a scene
# Lighting Mode
To control the behaviour of all the lights in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that have a **Light Mode** A Light property that defines the use of the Light. Can be set to Realtime, Baked and Mixed. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightMode) of Mixed, set the Lighting Mode in the [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
There are four options for Lighting Mode, in order of visual fidelity:
  * Distance **Shadowmask** A Texture that shares the same UV layout and resolution with its corresponding lightmap. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadowmask) mode renders realistic lighting at a long distance, but has the most performance impact. You can use this mode for open worlds on high-end or mid-range platforms.
  * Shadowmask mode is similar to **Distance Shadowmask** A version of the Shadowmask lighting mode that includes high quality shadows cast from static GameObjects onto dynamic GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DistanceShadowmask) but has fewer real-time shadows and less performance impact.
  * Baked Indirect mode renders realistic lighting and [realtime shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-realtime.html).
  * Subtractive mode renders simple lighting and low-fidelity shadows, but has a low performance impact. You can use this mode for low-end hardware, simple scenes with few lights, or stylized art such as cel shading.


For information about which **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) supports which Lighting Mode, refer to [Render pipeline feature comparison reference](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines-feature-comparison.html#lighting).
## How Unity calculates lighting
The following table shows how Unity calculates lighting from Mixed lights for each Lighting Mode.
**Lighting from Mixed lights** | **Baked Indirect Lighting Mode** | **Shadowmask Lighting Mode** | **Distance Shadowmask Lighting Mode** | **Subtractive Lighting Mode**  
---|---|---|---|---  
Direct lighting | Real-time | Real-time | Real-time | Real-time for dynamic **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject), baked for static GameObjects.  
Indirect lighting | Baked | Baked | Baked | Baked  
Specular highlights | Yes | Yes | Yes | Dynamic GameObjects only  
Shadows from dynamic GameObjects, up to [**Shadow Distance**](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-distance.html) | Real-time | Real-time | Real-time | Real-time, from the single highest-intensity Directional Light only  
Shadows from static GameObjects, up to [**Shadow Distance**](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-distance.html) | Real-time | Baked, from a maximum of 4 lights per GameObject | Real-time | Baked, from a maximum of 4 lights per GameObject  
Shadows from static GameObjects, beyond [**Shadow Distance**](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-distance.html) | No shadows | Baked, from a maximum of 4 lights per GameObject | Baked, from a maximum of 4 lights per GameObject | No shadows  
## Where Unity stores lighting data
Unity stores baked indirect lighting in the following places:
  * **Light Probes** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) store indirect lighting of dynamic GameObjects.
  * **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) textures store indirect lighting of static GameObjects. In Subtractive mode, lightmap textures also store direct lighting.


Unity stores shadows in the following places:
  * Shadowmap textures store real-time shadows, if the Lighting Mode supports them.
  * Light Probes and shadow mask textures store baked shadows from static GameObjects, if the Lighting Mode supports them. In Subtractive mode, lightmaps store them instead.


In Subtractive mode, real-time and baked shadows might not blend correctly, because lightmaps don’t contain enough data to calculate blending accurately. To improve blending, adjust the **Realtime Shadow Color** setting in the [Lighting window](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html).
### Shadow mask textures
If you select Shadowmask mode or Distance Shadowmask mode, Unity creates shadow mask textures to store baked shadows for static GameObjects. Each shadow mask texture stores occlusion information about **baked lights** Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#baked)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BakedLights), and has the following characteristics:
  * Uses the same UV layout and resolution as a corresponding lightmap.
  * Stores up to four lights per texel, with each light stored in an RGBA channel.


If more than four lights overlap a texel, Unity bakes the remaining lights for that texel. If you bake again, the same lights stay baked unless you change the overlapping lights. 
## Additional resources
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Setting a light as realtime or baked](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-landing.html)
  * [Shadows](https://docs.unity3d.com/6000.0/Documentation/Manual/shadows.html)A UI component that adds a simple outline effect to graphic components such as Text or Image. It must be on the same GameObject as the graphic component. [More info](https://docs.unity3d.com/Packages/com.unity.ugui@latest/index.html?subfolder=/manual/script-Shadow.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadow)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode-landing.html)
Configuring Mixed lights with Lighting Modes
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightMode-Scene.html)
Set the Lighting Mode of a scene
