* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Adaptive Probe Volumes (APV) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html)
  * Adaptive Probe Volumes panel reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-inspector-reference.html)
Adaptive Probe Volume Inspector reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-options-override-reference.html)
Probe Volumes Options Override reference
# Adaptive Probe Volumes panel reference
This page explains the properties in the **Adaptive Probe Volumes** panel in Lighting settings. To open the panel, from the main menu select **Window** > **Rendering** > **Lighting** > **Adaptive Probe Volumes**.
## Baking
To open Baking Set properties, either select the Baking Set asset in the Project window, or from the main menu select **Window** > **Rendering** > **Lighting** > **Adaptive Probe Volumes** tab.
### Baking
**Property** | **Description**  
---|---  
**Baking Mode** | Selects which scenes to bake. The options are:
  * **Single Scene:** Uses only the active scene to calculate the lighting data in Adaptive Probe Volumes.
  * **Baking Set:** Uses the scenes in this Baking Set to calculate the lighting data in Adaptive Probe Volumes.

  
**Current Baking Set** | The current Baking Set asset.  
****Scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in Baking Set** | Lists the scenes in the current Baking Set.  
**Status** | Indicates whether the scene is loaded.  
**Bake** | When enabled, URP generates lighting for this scene.  
**Add/Remove Scene** | Use **+** and **-** to add or remove a scene from the active Baking Set.  
**Reorder Scenes** | Use the two-line icon to the left of each scene to drag the scene up or down in the list.  
### Probe Placement
**Property** | **Description**  
---|---  
**Probe Positions** | Sets when Unity recalculates probe positions. The options are: 
  * **Recalculate:** Recalculate probe positions during baking, to accommodate changes in scene geometry. Refer to [Bake different lighting setups with Lighting Scenarios](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups) for more information.
  * **Don’t Recalculate:** Don’t recalculate probe positions during baking. This keeps the probe positions the same as the last successful bake, which means URP can blend probes in different Lighting Scenarios. Refer to [Bake different lighting setups with Lighting Scenarios](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups) for more information.

  
**Min Probe Spacing** | The minimum distance between probes, in meters. Refer to [Configure the size and density of Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-changedensity) for more information.  
**Max Probe Spacing** | The maximum distance between probes, in meters. Refer to [Configure the size and density of Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-changedensity) for more information.  
**Renderer Filter Settings** | Sets which layers and renderers Unity uses to generate and place probes. The options are: 
  * **Layer Mask:** Specify the [Layers](https://docs.unity3d.com/Manual/Layers.html) URP considers when it generates probe positions. Select a Layer to enable or disable it.
  * **Min Renderer Size:** The smallest [Renderer](https://docs.unity3d.com/ScriptReference/Renderer.html) size URP considers when it places probes.

  
### Lighting Scenarios
This section appears only if you enable **Lighting Scenarios** under ****Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) Lighting** in the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).
To rename a Lighting Scenario, double-click its name.
**Status** | **Description**  
---|---  
**Active** | Set the currently loaded Lighting Scenario, which URP writes to when you select **Generate Lighting**.  
**Status** | Indicates the status of the active Lighting Scenario. The statuses are:
  * **Invalid Scenario:** A warning icon appears if the active Lighting Scenario is baked but URP can’t load it anymore, for example if another Lighting Scenario has been baked that caused changes in the probe subdivision.
  * **Not Baked:** An information icon appears if you haven’t baked any lighting data for the active Lighting Scenario.
  * **Not Loaded:** An information icon appears if scenes in the Baking Set aren’t currently loaded in the Hierarchy window, so URP can’t determine the Lighting Scenario status.

  
## Sky Occlusion Settings
**Property** | **Description**  
---|---  
**Sky Occlusion** | Enable [sky occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html).  
**Samples** | Set the number of samples Unity uses to calculate the light each probe receives from the sky. Higher values increase the accuracy of the sky occlusion data, but increasing baking time. The default value is 2048.  
**Bounces** | Set the number of times Unity bounces light from the sky off objects when calculating the sky occlusion data. Higher values increase the accuracy of the sky occlusion data, but increase baking time. Use higher values if objects block the direct view from probes to the sky. The default value is 2.  
**Albedo Override** | Set the brightness of the single color Unity uses to represent objects the sky light bounces off, instead of the actual color of the objects. Higher values brighten the baked sky occlusion lighting. The default value is 0.6.  
**Sky Direction** | Enable Unity storing and using more accurate data about the directions from probes towards the sky. Refer to [Add dynamic color and shadows from the sky](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html#enable-more-accurate-sky-direction-data) for more information.  
## Probe Invalidity Settings
#### Probe Dilation Settings
**Property** | **Description**  
---|---  
**Enable Dilation** | When enabled, URP replaces data in invalid probes with data from nearby valid probes. Enabled by default. Refer to [Fix issues with Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues).  
**Search Radius** | Determine how far from an invalid probe URP searches for valid neighbors. Higher values include more distant probes that might be in different lighting conditions than the invalid probe, resulting in unwanted behaviors such as light leaks.  
**Validity Threshold** | Set the ratio of backfaces a probe samples before URP considers it invalid. Higher values mean URP is more likely to mark a probe invalid.  
**Dilation Iterations** | Set the number of times Unity repeats the dilation calculation. This increases the spread of dilation effect, but increases the time URP needs to calculate probe lighting.  
**Squared Distance Weighting** | Enable weighing the contribution of neighbouring probes by squared distance, rather than linear distance. Probes that are closer to invalid probes will contribute more to the lighting data.  
#### Virtual Offset Settings
**Property** | **Description**  
---|---  
**Enable Virtual Offset** | Enable URP moving the capture point of invalid probes into a valid area. Refer to [Fix issues with Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues).  
**Search Distance Multiplier** | Set the length of the sampling ray URP uses to search for valid probe positions. High values might cause unwanted results, such as probe capture points pushing through neighboring geometry.  
**Geometry Bias** | Set how far URP pushes a probe’s capture point out of geometry after one of its sampling rays hits geometry.  
**Ray Origin Bias** | Set the distance between a probe’s center and the point URP uses as the origin of each sampling ray. High values might cause unwanted results, such as rays missing nearby occluding geometry.  
****Layer Mask** A value defining which layers to include or exclude from an operation, such as rendering, collision or your own code. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Layers.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LayerMask)** | Specify which layers URP includes in **collision** A collision occurs when the physics engine detects that the colliders of two GameObjects make contact or overlap, when at least one has a Rigidbody component and is in motion. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CollidersOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Collision) calculations for [Virtual Offset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues.html).  
**Refresh Virtual Offset Debug** | Re-run the virtual offset simulation to preview updated results, without affecting baked data.  
### Adaptive Probe Volume Disk Usage
**Property** | **Description**  
---|---  
**Scenario Size** | Indicates how much space on disk is used by the baked Light Probe data.  
**Baking Set Size** | Indicates how much space on disk is used by all the baked Light Probe data for the currently selected Baking Set. This includes the data for all Lighting Scenarios, and the data shared by all Lighting Scenarios.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-inspector-reference.html)
Adaptive Probe Volume Inspector reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-options-override-reference.html)
Probe Volumes Options Override reference
