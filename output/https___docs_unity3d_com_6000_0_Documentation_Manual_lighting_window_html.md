* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting reference](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-reference.html)
  * Lighting window reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-reference.html)
Lighting reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html)
Lighting Settings Asset Inspector window reference
# Lighting window reference
The Lighting window (menu: **Window** > **Rendering** > **Lighting**) is the main control point for Unity’s lighting features. You can use the Lighting window to adjust settings related to the lighting in your Scene, and to optimise your precomputed lighting data for quality, bake time, and storage space.
## Related APIs
You can perform many of the functions available in the Lighting window in **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), using the [LightingSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightingSettings.html) and [Lightmapping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Lightmapping.html) APIs.
## Lighting window layout
The Lighting window contains the following elements:
  * The [Scene tab](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#Scene)
  * The [Adaptive Probe Volumes tab](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#ProbeVolumes) - Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) and High-Definition Render Pipeline (HDRP) only
  * The [Environment tab](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#Environment)
  * The [Realtime Lightmaps tab](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#RealtimeLightmaps)
  * The [Baked Lightmaps tab](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#BakedLightmaps)
  * The [control area](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#ControlArea), at the bottom of the window


## The Scene tab
The **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) tab displays information about the [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html) that is assigned to the active Scene. If no Lighting Settings Asset is assigned to the active Scene, it displays information about the [default LightingSettings object](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
The Scene tab is divided into the following sections:
  * [Lighting Settings Asset controls](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#AssetControls)
  * [Lighting settings](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#LightingSettingsProperties) - Realtime Lighting, Mixed Lighting and Lightmapping settings


### Lighting Settings Asset controls
Use the controls in this section to assign a Lighting Settings Asset to the active Scene, or to create a new Lighting Settings Asset.
**Property:** | **Function:**  
---|---  
**Lighting Settings** | The Lighting Settings Asset assigned to the active Scene.  
**New Lighting Settings** | Click this button to generate a new Lighting Settings Asset in your Project, and automatically assign the new Lighting Settings Asset to the active Scene.  
### Lighting Settings
Use this section to view and edit the properties of the Lighting Settings Asset or `LightingSettings` object assigned to the current Scene. See [Lighting Settings Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html).
## The Adaptive Probe Volumes tab - URP and HDRP only
The Adaptive Probe Volumes tab contains settings related to Adaptive Probe Volumes (APV). This tab only appears if you use URP or HDRP in your project. Refer to the following for more information:
  * [Adaptive Probe Volumes in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * [Adaptive Probe Volumes in HDRP](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/probevolumes.html)


## The Environment tab
The Environment tab contains settings related to environmental lighting effects for the current Scene. The contents depend on the render pipeline that your Project uses.
The Environment tab is divided into two sections:
  * [Environment](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#EnvironmentSection)
  * [Other settings](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#OtherSection)


### Environment
The Environment section contains lighting-related settings and controls that apply to the environmental lighting in the current scene, such as the Skybox, diffuse lighting and reflections.
**Property** | **Description**  
---|---  
**Skybox Material** | A [Skybox](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html) is a Material that appears behind everything else in the Scene to simulate the sky or other distant background. Use this property to choose the Skybox you want to use for the Scene. The default value is the built-in Default Skybox.  
**Sun Source** | Select a Light to use as the sun in your Scene. Unity uses this Light to simulate the effect of sun position and intensity on the Skybox and your Scene. If you set this to **None** , Unity considers the brightest directional light in the Scene the sun. Lights whose **Render Mode** property is set to **Not Important** do not affect the Skybox.   
  
For more information about the **Render Mode** setting, see the Additional settings section of [Lights](https://docs.unity3d.com/Manual/class-Light.html).  
**Realtime Shadow Color** | Define the color that Unity uses to render real-time shadows in Subtractive Lighting Mode.  
**Environment Lighting** | This section contains settings that affect [ambient light](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-ambient-light.html) in the current Scene.  
**Source** | Use this to define a source color for ambient light in the Scene. The default value is **Skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox). The options are: 
  * **Skybox** : Use the colors of the Skybox set in **Skybox Material** to determine the ambient light coming from different angles. This allows for more precise effects than **Gradient**.
  * **Gradient** : Choose separate colors for ambient light from the sky, horizon and ground, and blend smoothly between them.
  * **Color** : Use a flat color for all ambient light.

  
**Intensity Multiplier** | Use this to set the brightness of the ambient light in the Scene, defined as a value between 0 and 8. The default value is 1.  
**Environment Reflections** | This section contains global settings for [Reflection Probe](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) baking, and settings that affect global reflections.  
**Source** | Use this setting to specify whether you want to use the Skybox for reflection effects, or a Cubemap of your choice. The default value is **Skybox**. The options are: 
  * **Skybox** : Select this to use the Skybox as the reflection source.
  * **Custom** : Select this to use either a Cubemap asset or a [RenderTexture of type cube](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html) for reflections.

  
**Resolution** | Use this to set the resolution of the Skybox for reflection purposes. This property is visible only when **Source** is set to **Skybox**.  
**Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) | Use this to specify the Cubemap to use for reflection purposes. This property is visible only when **Source** is set to **Cubemap**.  
**Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) | Use this to define whether or not reflection textures are compressed. The default setting is **Auto**. The options are: 
  * **Auto** : The reflection texture is compressed if the compression format is suitable.
  * **Uncompressed** : The reflection texture is stored in memory uncompressed.
  * **Compressed** : The texture is compressed.

  
**Intensity Multiplier** | The degree to which the reflection source is visible in reflective objects.  
**Bounces** | A reflection bounce occurs when a reflection from one object is then reflected by another object. Use this property to set how many times the Reflection Probes evaluate bounces back and forth between objects. If this is set to 1, then Unity only takes the initial reflection (from the skybox or cube map specified in the **Reflection Source** property) into account.  
### Other Settings
The Other Settings section contains settings for fog, [Halos](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)The glowing light areas around light sources, used to give the impression of small dust particles in the air. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Halo), [Flares](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html) and [Cookies](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html).
**Property** | **Description**  
---|---  
**Fog** A post-processing effect that overlays a color onto objects depending on the distance from the camera. Use this to simulate fog or mist in outdoor environments, or to hide clipping of objects near the camera’s far clip plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Fog) | Enables or disables fog in the Scene. Note that fog is not available with the [Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html). For more information, refer to [Fog settings](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#fogsettings).  
**Halo Texture** | Set the Texture you want to use for drawing a [Halo](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html) around lights.  
**Halo Strength** | Define the visibility of Halos around Lights, from a value between 0 and 1.  
**Flare Fade Speed** | Define the time (in seconds) over which [lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) fade from view after initially appearing. This is set to 3 by default.  
**Flare Strength** | Define the visibility of lens flares from lights, from a value between 0 and 1.  
**Spot Cookie** | Set the [Cookie](https://docs.unity3d.com/6000.0/Documentation/Manual/Cookies.html) texture you want to use for [Spot Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/Lighting.html). The default is ‘Soft’. To revert to ‘Soft’, select **None**.  
#### Fog settings
**Property** | **Description**  
---|---  
**Color** | Use the color picker to set the color Unity uses to draw fog in the Scene.  
**Fog Mode** | Define the way in which the fogging accumulates with distance from the camera. For more information, refer to [Fog Mode dropdown](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html#fogmodedropdown). The options are: 
  * **Linear** : Fog density increases linearly with distance. **Start** sets the distance from the Camera at which the fog starts. **End** sets the distance from the Camera at which the fog completely obscures Scene GameObjects.
  * **Exponential** : Fog density increases exponentially with distance. **Density** controls the density of the fog. The fog appears more dense as the **Density** increases.
  * **Exponential Squared** : Fog density increases faster with distance (exponentially and squared). **Density** controls the density of the fog. The fog appears more dense as the **Density** increases.

  
## The Realtime Lightmaps tab
The Realtime **Lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) tab shows a list of all lightmaps generated by the **Enlighten** A lighting system by Geomerics used in Unity for Enlighten Realtime Global Illumination. [More info](https://www.siliconstudio.co.jp/en/products-service/enlighten/)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Enlighten) Realtime **Global Illumination** A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination) system in the current Scene. If Enlighten Realtime Global Illumination is not enabled in your Project, this tab will be empty.
## The Baked Lightmaps tab
This tab displays a list of all the lightmaps generated by the [lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmappers.html)A tool in Unity that bakes lightmaps according to the arrangement of lights and geometry in your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmapper) for the current scene, and the [Lighting Data Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/LightmapSnapshot.html).
If you [use Scene view Draw Modes to preview lightmapping](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping-preview.html), the tab also contains the temporary lightmaps Unity generates for the preview.
If Baked Global Illumination is not enabled in your Project, the tab is empty.
## Control area
Controls for precomputing lighting data are at the bottom of the Lighting window.
**Property** | **Description**  
---|---  
**GPU Baking Device** | Use this to change the GPU that Unity uses for precomputing lighting data. This property is visible only when you use the [GPU Progressive Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html) backend.  
**GPU Baking Profile** | The profile you select in this property defines how the GPU Lightmapper breaks lightmaps into smaller tiles to reduce GPU memory usage. The options are: 
  * **Automatic** : Unity chooses the tile size based on the size of the largest lightmap while still aiming for good GPU utilization.
  * **Highest Performance** and **High Performance** : Force a higher fixed tile size for all lightmaps.
  * **Low Memory Usage** and **Lowest Memory Usage** : Force a lower fixed tile size for all lightmaps. Small tiles take up less GPU memory at the expense of lower GPU utilization, leading to longer bake times.

This property is visible only when you use the [GPU Progressive Lightmapper](https://docs.unity3d.com/6000.0/Documentation/Manual/progressive-lightmapper.html).  
**Bake on Scene Load** | Set whether Unity automatically generates precomputed lighting data. The options are: 
  * **Never** : Prevent Unity from automatically generating precomputed lighting data when you open a scene. To generate lighting data manually, select **Generate Lighting**. This is the default mode in a new Unity 6 project.
  * **If Missing Lighting Data** : Enable Unity automatically generating precomputed lighting data when you open a scene, if the data doesn’t exist or is invalid. This is the default mode for a project that was created in Unity 2023.2 or earlier. Refer to [Upgrade to Unity 6.0](https://docs.unity3d.com/6000.0/Documentation/Manual/UpgradeGuideUnity6.html) for more information.

  
**Generate Lighting** | Select the **Generate Lighting** button to precompute lighting data. This data includes lightmaps for the Baked Global Illumination system, lightmaps for the Enlighten Realtime Global Illumination system, Light Probes, Adaptive Probe Volumes, and Reflection Probes. Edits you make after starting the bake process using the **Generate Lighting** button do not affect baked lighting.  
  
The dropdown options are: 
  * **Bake Probe Volumes** : Bake only the Adaptive Probe Volumes in the scene or Baking Set.
  * **Bake Reflection Probes** : Bake only the Reflection Probes for all open Scenes. **Note:** If you select **Bake Reflection Probes** but you haven’t baked the scene before, Unity also bakes lightmaps, Light Probes, and Adaptive Probe Volumes.
  * **Clear Baked Data** : Clear all precomputed lighting data from all open scenes without clearing the [GI Cache](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)The cached intermediate files used when Unity precomputes lighting data. Unity keeps this cache to speed up computation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GICache).

  
* * *
  * [Lighting Settings Asset] added in [2020.1](https://docs.unity3d.com/2020.1/Documentation/Manual/30_search.html?q=newin20201) NewIn20201


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-reference.html)
Lighting reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightingSettings.html)
Lighting Settings Asset Inspector window reference
