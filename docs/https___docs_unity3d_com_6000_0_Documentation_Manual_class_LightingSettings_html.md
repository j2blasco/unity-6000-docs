* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting reference](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-reference.html)
  * Lighting Settings Asset Inspector window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)
Lighting window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html)
Lightmap Parameters Asset Inspector window reference
# Lighting Settings Asset Inspector window reference
[Switch to Scripting](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html "Go to LightingSettings page in the Scripting Reference")
When you view the Lighting Settings Asset in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) or the Lighting window, the properties that you can view or edit are divided into the following sections:
  * [Realtime Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#RealtimeLighting)
  * [Mixed Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html#MixedLighting)


For information about **Lightmapping Settings** section of the Lighting Settings Asset, refer to [Lightmapping settings in the Lighting Settings Asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-reference.html).
## Realtime Lighting
This section contains [settings](https://docs.unity3d.com/Manual/lighting-window.html) related to the [Enlighten Realtime Global Illumination system](https://docs.unity3d.com/6000.0/Documentation/Manual/realtime-gi-using-enlighten.html).
**Property** | **Description**  
---|---  
**Realtime**Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)** | Enable this property to use the **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime Global Illumination system in **Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that use this Lighting Settings Asset.  
**Realtime Environment Lighting** | Enable this property to use the Enlighten Realtime Global Illumination system to calculate and update ambient light in real-time.   
  
This property is only available when both Enlighten **Realtime Global Illumination** and **Baked Global Illumination** are enabled in the Scene.  
**Indirect Resolution** | Specifies the number of texels per unit to use for realtime lightmaps. Increasing this value improves lightmap quality, but also increases render time.  
  
This property is only available if you enable **Realtime Global Illumination**.  
## Mixed Lighting
This section contains settings that affect the behavior of [Baked Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#baked)Light components whose Mode property is set to Baked. Unity pre-calculates the illumination from Baked Lights before runtime, and does not include them in any runtime lighting calculations. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#baked)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#BakedLights) and [Mixed Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-introduction.html#mixed)Light components whose Mode property is set to Mixed. Some calculations for Mixed Lights are performed in advance, and some calculations for Mixed Lights are performed at runtime. The behavior of all Mixed Lights in a Scene is determined by the Scene’s Lighting Mode. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightModes-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#MixedLights) in Scenes that use this Lighting Settings Asset.
**Property** | **Description**  
---|---  
**Baked Global Illumination** | When this setting is enabled, Unity enables the Baked Global Illumination system for the Scenes that use this Lighting Settings Asset. When this setting is disabled, Unity disables the Baked Global Illumination system for the Scenes that use this Lighting Settings Asset.  
  
When the Baked Global Illumination system is enabled, Unity uses Baked lights in the Scene for lightmapping only, and Mixed lights behave according to the **Lighting Mode** setting. When the Baked Global Illumination system is disabled, Unity forces all Baked and Mixed lights in the Scene to act as though they were Realtime Lights.  
**Lighting Mode** | Specifies which [Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html) Unity uses for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  
### Lighting Mode dropdown
**Value** | **Description**  
---|---  
**Baked Indirect** | Use [Baked Indirect Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#baked-indirect) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  
  
In Baked Indirect Lighting Mode, Mixed Lights provide real-time direct lighting and Unity bakes indirect light into lightmaps and Light Probes. Real-time shadow maps provide shadows.  
**Shadowmask** | Use [Shadowmask Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#shadowmask) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  
  
In Shadowmask Lighting Mode Mixed Lights provide real-time direct lighting while indirect light is baked into lightmaps and probes. This mode combines real-time and baked shadows.  
**Subtractive** | Use [Subtractive Lighting Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-mode.html#subtractive) for all Mixed Lights in the Scenes that use this Lighting Settings Asset.  
  
In Subtractive Lighting Mode Mixed Lights provide baked direct and indirect lighting for static objects. Dynamic objects receive real-time direct lighting and cast shadows using the Directional Light.  
## Additional resources
  * [Create lighting presets with a Lightmap Parameters Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/configure-with-lightmap-parameters-asset.html)
  * [Configure lightmapping with a Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/global-illumination-configure.html)
  * [Lightmapping settings in the Lighting Settings Asset reference](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-reference.html)


LightingSettings
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)
Lighting window reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightmapParameters.html)
Lightmap Parameters Asset Inspector window reference
