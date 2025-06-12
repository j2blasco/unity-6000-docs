* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * [Changing lighting at runtime](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probe-volumes-change-lighting-at-runtime.html)
  * Update light from the sky at runtime with sky occlusion


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
Bake different lighting setups with Lighting Scenarios
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html)
Optimize loading Adaptive Probe Volume data
# Update light from the sky at runtime with sky occlusion
You can enable sky occlusion when you use Adaptive Probe Volumes. Sky occlusion means that when a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) samples a color from the sky, Unity dims the color if the light can’t reach the GameObject.
Sky occlusion in Unity uses the sky color from the [ambient probe](https://docs.unity3d.com/2023.3/Documentation/ScriptReference/RenderSettings-ambientProbe.html), which updates at runtime. This means you can dynamically light GameObjects as the sky color changes. For example, you can change the sky color from light to dark, to simulate the effect of a day-night cycle.
If you enable sky occlusion, Adaptive Probe Volumes might take longer to bake, and Unity might use more memory at runtime.
## How sky occlusion works
When you enable sky occlusion, Unity bakes an additional static sky occlusion value into each probe in an Adaptive Probe Volume. The sky occlusion value is the amount of indirect light the probe receives from the sky, including light that bounced off static GamesObjects.
At runtime, when a static or dynamic GameObject samples an Adaptive Probe Volume probe, Unity approximates the light from the sky using two values:
  * A sky color from the ambient probe, which updates when the sky color changes.
  * The sky occlusion value, which is static.


## Limitations
When Unity calculates sky occlusion values, Unity treats the surfaces of GameObjects as opaque and a gray color. As a result, transparent or translucent GameObjects like windows or leaves bounce light away instead of transmitting it through. Also, dark-colored walls reflect the same amount of light as light-colored walls. To minimize lighting issues, disable **Contribute GI** in the [**Static Editor Flags** property](https://docs.unity3d.com/6000.0/Documentation/Manual/StaticObjects.html) for transparent or translucent GameObjects.
To override the gray color Unity uses, go to **Sky Occlusion Settings** in the [Adaptive Probe Volumes panel](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html#sky-occlusion-settings) and adjust **Albedo Override**.
## Enable sky occlusion
First, enable the GPU **lightmapper** A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper). Unity doesn’t support sky occlusion if you use **Progressive CPU** instead.
  1. Go to **Window** > **Rendering** > **Lighting**.
  2. Go to the ****Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene)** panel.
  3. Set **Lightmapper** to **Progressive GPU**.


To enable sky occlusion, follow these steps: 
  1. Go to the **Adaptive Probe Volumes** panel.
  2. Enable **Sky Occlusion**.


To update the lighting data, you must also [bake the Adaptive Probe Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-use.html#add-and-bake-an-adaptive-probe-volume) after you enable or disable sky occlusion.
## Update light at runtime
To update light from the sky at runtime, you must use colors for the **ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientlight) in your scene, not a **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox). To use colors, do the following:
  1. Go to **Window** > **Rendering** > **Lighting**.
  2. Go to the **Environment** panel.
  3. Set **Source** to either **Gradient** or **Color**.
You can also set **Source** to **Skybox** , but you must update the ambient probe yourself each time you update the skybox. To update the ambient probe, use the [`DynamicGI.UpdateEnvironment`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DynamicGI.UpdateEnvironment.html) API. This has a very large impact on performance.


To update the light from the sky at runtime, do either of the following:
  * Use the properties in the [`RenderSettings`](https://docs.unity3d.com/ScriptReference/RenderSettings.html) API to change the sky colors, for example [ambientSkyColor](https://docs.unity3d.com/ScriptReference/RenderSettings-ambientSkyColor.html).
  * Use the [**Animation** window](https://docs.unity3d.com/Manual/AnimationEditorGuide.html).


## Enable more accurate sky direction data
When an object samples the ambient probe, by default Unity uses the surface normal of the object as the direction to the sky. This direction might not match the direction the light comes from, for example if the object is inside and the sky light bounces off other objects to reach it.
Unity can instead calculate, store, and use an accurate direction from each Adaptive Probe Volume probe, and take bounce lighting into account. This makes sky occlusion more accurate, especially in areas like caves where probes don’t have a direct line of sight to the sky, or when the sky has contrasting colors and the light comes from a specific direction such as through a window.
To enable this feature, in the **Adaptive Probe Volumes** of the Lighting window, enable **Sky Direction**.
If you enable **Sky Direction** , the following applies:
  * Baking takes longer and Unity uses more memory at runtime.
  * There might be visible seams, because Unity doesn’t interpolate sky direction data between probes.


To override the directions Unity uses, use a [Probe Adjustment Volume component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-adjustment-volume-component-reference.html).
## Additional resources
  * [Adaptive Probe Volumes panel properties](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html#sky-occlusion-settings) for more information about sky occlusion settings
  * [Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#probe-volume-panel) for information about displaying baked sky occlusion data


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html)
Bake different lighting setups with Lighting Scenarios
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html)
Optimize loading Adaptive Probe Volume data
