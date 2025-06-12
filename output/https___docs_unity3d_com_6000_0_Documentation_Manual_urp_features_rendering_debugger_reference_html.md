* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Rendering Debugger in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html)
  * Rendering Debugger window reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-add-controls.html)
Add controls to the Rendering Debugger in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-birp.html)
Graphics performance and profiling in the Built-In Render Pipeline
# Rendering Debugger window reference for URP
The Rendering Debugger contains the following sections:
  * [Display Stats](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#display-stats)
  * [Frequently Used](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#frequently-used)
  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#rendering)
  * [Material](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#material)An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material)
  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#lighting)
  * [Render Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#render-graph)
  * [Probe Volume](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#probe-volume-panel)


## Display Stats
The **Display Stats** panel shows statistics relevant to debugging performance issues in your project. You can only view this section of the Rendering Debugger in Play Mode. Refer to [Open the Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-use.html#navigation-at-runtime) for more information. 
###  Frame Stats
The Frame Stats section displays the average, minimum, and maximum value of each property. URP calculates each Frame Stat value over the 30 most recent frames.
**Property** | **Description**  
---|---  
**Frame Rate** | The frame rate (in frames per second) for the current **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) view.  
**Frame Time** | The total frame time for the current camera view.  
**CPU Main Thread Frame** | The total time (in milliseconds) between the start of the frame and the time when the Main Thread finished the job.  
**CPU Render Thread Frame** | The time (in milliseconds) between the start of the work on the Render Thread and the time Unity waits to render the present frame ([Gfx.PresentFrame](https://docs.unity3d.com/2022.1/Documentation/Manual/profiler-markers.html)).  
**CPU Present Wait** | The time (in milliseconds) that the CPU spent waiting for Unity to render the present frame ([Gfx.PresentFrame](https://docs.unity3d.com/2022.1/Documentation/Manual/profiler-markers.html)) during the last frame.  
**GPU Frame** | The amount of time (in milliseconds) the GPU takes to render a given frame.  
**Debug XR Layout** | Display debug information for XR passes.   
This mode is only available in editor and development builds.  
### Bottlenecks
A bottleneck is a condition that occurs when one process performs significantly slower than other components, and other components depend on it. 
The **Bottlenecks** section describes the distribution of the last 60 frames across the CPU and GPU. You can only check the Bottleneck information when you build your player on a device. 
**Note** : Vsync limits the **Frame Rate** based on the refresh rate of your device’s screen. This means when you enable Vsync, the **Present Limited** category is 100% in most cases. To turn Vsync off, go to **Edit** > **Project settings** > **Quality** > **Current Active Quality Level** and set the **Vsync Count** set to **Don’t Sync**.
#### Bottleneck categories
**Category** | **Description**  
---|---  
**CPU** | The percentage of the last 60 frames in which the CPU limited the frame time.  
**GPU** | The percentage of the last 60 frames in which the GPU limited the frame time.  
**Present limited** | The percentage of the last 60 frames in which the frame time was limited by the following presentation constraints:
  * Vertical Sync (Vsync): Vsync synchronizes rendering to the refresh rate of your display.
  * [Target framerate](https://docs.unity3d.com/ScriptReference/Application-targetFrameRate.html): A function that you can use to manually limit the frame rate of an application. If a frame is ready before the time you specify in targetFrameRate, Unity waits before presenting the frame.

  
**Balanced** | This percentage of the last 60 frames in which the frame time was not limited by any of the above categories. A frame that is 100% balanced indicates the processing time for both CPU and GPU is approximately equal.  
#### Bottleneck example
If **Vsync** Vertical synchronization (VSync) is a display setting that caps a game’s frame rate to match the refresh rate of a monitor, to prevent image tearing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#VSync) limited 20 of the 60 most recent frames, the Bottleneck section might appear as follows: 
  * **CPU** 0.0%: This indicates that URP did not render any of the last 60 frames on the CPU.
  * **GPU** 66.6%: This indicates that the GPU limited 66.6% of the 60 most recent frames rendered by URP.
  * **Present Limited** 33.3%: This indicates that presentation constraints (Vsync or the [target framerate](https://docs.unity3d.com/ScriptReference/Application-targetFrameRate.html)) limited 33.3% of the last 60 frames.
  * **Balanced** 0.0%: This indicates that in the last 60 frames, there were 0 frames where the CPU processing time and GPU processing time were the same.


In this example, the bottleneck is the GPU.
### Detailed Stats
The Detailed Stats section displays the amount of time in milliseconds that each rendering step takes on the CPU and GPU. URP updates these values once every frame based on the previous frame. 
**Property** | **Description**  
---|---  
Update every second with average | Calculate average values over one second and update every second.  
Hide empty scopes | Hide profiling scopes that use 0.00ms of processing time on the CPU and GPU.  
Debug XR Layout | Enable to display debug information for [XR](https://docs.unity3d.com/Manual/XR.html)An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) passes. This mode only appears in the editor and **development builds** A development build includes debug symbols and enables the Profiler. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/https:/docs.unity.com/devops/en/manual/build-target-configurations#Build_target_advanced_settings_overview)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DevelopmentBuild).  
## Frequently Used
This section contains a selection of properties that users use often. The properties are from the other sections in the Rendering Debugger window. For information about the properties, refer to the sections [Material](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#material), [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#lighting), and [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-reference.html#rendering).
## Rendering
The properties in this section let you visualize different rendering features.
### Rendering Debug
**Property** | **Description**  
---|---  
**Map Overlays** | Specifies which render pipeline texture to overlay on the screen. The options are:
  * **None** : Renders the scene normally without a texture overlay.
  * **Depth** : Overlays the camera’s depth texture on the screen.
  * **Additional Lights Shadow Map** : Overlays the [shadow map](https://docs.unity3d.com/Manual/shadow-mapping.html) that contains shadows cast by lights other than the main directional light.
  * **Main Light Shadow Map** : Overlays the shadow map that contains shadows cast by the main directional light.

  
**Map Size** | The width and height of the overlay texture as a percentage of the view window URP displays it in. For example, a value of **50** fills up a quarter of the screen (50% of the width and 50% of the height).  
****HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR)** | Indicates whether to use [high dynamic range](https://docs.unity3d.com/Manual/HDR.html) to render the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). Enabling this property only has an effect if you enable **HDR** in your URP Asset.  
**MSAA** | Indicates whether to use [Multisample Anti-aliasing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#msaa) to render the scene. Enabling this property only has an effect if:
  * You set **Anti Aliasing (MSAA)** to a value other than **Disabled** in your URP Asset.
  * You use the Game View. MSAA has no effect in the Scene View.

  
**Post-processing** | Specifies how URP applies post-processing. The options are:
  * **Disabled** : Disables post-processing.
  * **Auto** : Unity enables or disables post-processing depending on the currently active debug modes. If color changes from post-processing would change the meaning of a debug mode’s pixel, Unity disables post-processing. If no debug modes are active, or if color changes from post-processing don’t change the meaning of the active debug modes’ pixels, Unity enables post-processing.
  * **Enabled** : Applies post-processing to the image that the camera captures.

  
**Additional Wireframe Modes** | Specifies whether and how to render wireframes for meshes in your scene. The options are:
  * **None** : Doesn’t render wireframes.
  * **Wireframe** : Exclusively renders edges for meshes in your scene. In this mode, you can see the wireframe for meshes through the wireframe for closer meshes.
  * **Solid Wireframe** : Exclusively renders edges and faces for meshes in your scene. In this mode, the faces of each wireframe mesh hide edges behind them.
  * **Shaded Wireframe** : Renders edges for meshes as an overlay. In this mode, Unity renders the scene in color and overlays the wireframe over the top.

  
**Overdraw** | Indicates whether to render the overdraw debug view. This is useful to check where Unity draws **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) over one other.  
#### Mipmap Streaming
**Property** | **Description**  
---|---  
**Disable Mip Caching** | If you enable **Disable Mip Caching** , Unity doesn’t cache mipmap levels in GPU memory, and constantly discards mipmap levels from GPU memory when they’re no longer needed. This means the mipmap streaming debug views more accurately display which mipmap levels Unity uses at the current time. Enabling this setting increases the amount of data Unity transfers from disk to the CPU and the GPU.  
**Debug View** | Set a mipmap streaming debug view. Options:
  * **None** : Display the normal view.
  * **Mip Streaming Performance** : Use color to indicate which textures use mipmap streaming, and whether mipmap streaming limits the number of mipmap levels Unity loads.
  * **Mip Streaming Status** : Use color on materials to indicate whether their textures use mipmap streaming. Diagonal stripes mean some of the textures use a [`requestedMipmapLevel`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html) that overrides mipmap streaming. Yellow means Unity can’t stream the texture, or the texture is assigned to terrain.
  * **Mip Streaming Activity** : Use color to indicate whether Unity recently streamed the textures.
  * **Mip Streaming Priority** : Use color to indicate the streaming priority of the textures. Set streaming priority for a texture in the [**Texture Import Settings** window](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html).
  * **Mip Count** : Display the number of mipmap levels Unity loads for the textures.
  * **Mip Ratio** : Use color to indicate the pixel density of the highest-resolution mipmap levels Unity uploads for the textures.

  
**Debug Opacity** | Set the opacity of the **Debug View** you select. 0 means not visible and 1 means fully visible. This property is visible only if **Debug View** is not set to **None**.  
**Combined Per Material** | Set the **Debug View** to display debug information of all the textures on a material, not individual texture slots. This property is only visible if **Debug View** is set to **Mip Streaming Status** or **Mip Streaming Activity**.  
**Material Texture Slot** | Set which texture Unity uses from each material to display debug information. For example, set **Material Texture Slot** to **Slot 3** to display debug information for the fourth texture. If a material has fewer textures than the **Material Texture Slot** value, Unity uses no texture. This property is visible only if **Combined Per Material** is disabled, and **Debug View** is not set to **None**.  
**Display Status Codes** | Display more detailed statuses for textures that display as **Not streaming** or **Warning** in the **Mip Streaming Status** debug view. This property is visible only if **Debug View** is set to **Mip Streaming Status**.  
**Activity Timespan** | Set how long a texture displays as **Just streamed** , in seconds. This property is visible only if **Debug View** is set to **Mip Streaming Activity**.  
****Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) Texture** | Set which terrain texture Unity displays. You can select either **Control** for the control texture, or one of the diffuse textures. This property is visible only if **Debug View** is not set to **None**.  
### Pixel Validation
**Property** | **Description**  
---|---  
**Pixel Validation Mode** | Specifies which mode Unity uses to validate pixel color values. The options are:
  * **None** : Renders the scene normally and doesn’t validate any pixels.
  * **Highlight NaN, Inf and Negative Values** : Highlights pixels that have color values that are NaN, Inf, or negative.
  * **Highlight Values Outside Range** : Highlights pixels that have color values outside a particular range. Use **Value Range Min** and **Value Range Max**.

  
**Channels** | Specifies which value to use for the pixel value range validation. The options are:
  * **RGB** : Validates the pixel using the luminance value calculated from the red, green, and blue color channels.
  * **R** : Validates the pixel using the value from the red color channel.
  * **G** : Validates the pixel using the value from the green color channel.
  * **B** : Validates the pixel using the value from the blue color channel.
  * **A** : Validates the pixel using the value from the alpha channel.

This property only appears if you set **Pixel Validation Mode** to **Highlight Values Outside Range**.  
**Value Range Min** | The minimum valid color value. Unity highlights color values that are less than this value.  
  
This property only appears if you set **Pixel Validation Mode** to **Highlight Values Outside Range**.  
**Value Range Max** | The maximum valid color value. Unity highlights color values that are greater than this value.  
  
This property only appears if you set **Pixel Validation Mode** to **Highlight Values Outside Range**.  
### Material
The properties in this section let you visualize different Material properties.
#### Material Filters
**Property** | **Description**  
---|---  
**Material Override** | Select a Material property to visualize on every GameObject on screen.  
The available options are:
  * Albedo
  * Specular
  * Alpha
  * Smoothness
  * AmbientOcclusion
  * Emission
  * NormalWorldSpace
  * NormalTangentSpace
  * LightingComplexity
  * Metallic
  * SpriteMask
  * RenderingLayerMasks

With the **LightingComplexity** value selected, Unity shows how many Lights affect areas of the screen space.   
With the **RenderingLayerMasks** value selected, you can filter the layers you want to debug either manually using the **Filter Layers** option or by selecting a light with the **Filter Rendering Layers by Light** option. Additionally, you can override the debug colors using **Layers Color**.  
**Vertex Attribute** | Select a vertex attribute of GameObjects to visualize on screen.  
The available options are:
  * Texcoord0
  * Texcoord1
  * Texcoord2
  * Texcoord3
  * Color
  * Tangent
  * Normal

  
#### Material Validation
**Property** | **Description**  
---|---  
**Material Validation Mode** | Select which Material properties to visualize: Albedo, or Metallic. Selecting one of the properties shows the new context menu.  
**Validation Mode: Albedo** | Selecting **Albedo** in the Material Validation Mode property shows the **Albedo Settings** section with the following properties:  
**Validation Preset** : Select a pre-configured material, or Default Luminance to visualize luminance ranges.  
**Min Luminance** : Unity draws pixels where the luminance is lower than this value with red color.  
**Max Luminance** : Unity draws pixels where the luminance is higher than this value with blue color.  
**Hue Tolerance** : available only when you select a pre-set material. Unity adds the hue tolerance to the minimum and maximum luminance values.  
**Saturation Tolerance** : available only when you select a pre-set material. Unity adds the saturation tolerance to the minimum and maximum luminance values.  
**Validation Mode: Metallic** | Selecting **Metallic** in the Material Validation Mode property shows the **Metallic Settings** section with the following properties:  
**Min Value** : Unity draws pixels where the metallic value is lower than this value with red color.  
**Max Value** : Unity draws pixels where the metallic value is higher than this value with blue color.  
## Lighting
The properties in this section let you visualize different settings and elements related to the lighting system, such as shadow cascades, reflections, contributions of the Main and the Additional Lights, and so on.
### Lighting Debug Modes
**Property** | **Description**  
---|---  
**Lighting Debug Mode** | Specifies which lighting and shadow information to overlay on-screen to debug. The options are:
  * **None** : Renders the scene normally without a debug overlay.
  * **Shadow Cascades** : Overlays shadow cascade information so you can determine which shadow cascade each pixel uses. Use this to debug shadow cascade distances. For information on which color represents which shadow cascade, refer to the [Shadows section of the URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#shadows).
  * **Lighting Without Normal Maps** : Renders the scene to visualize lighting. This mode uses neutral materials and disables normal maps. This and the **Lighting With Normal Maps** mode are useful for debugging lighting issues caused by normal maps.
  * **Lighting With Normal Maps** : Renders the scene to visualize lighting. This mode uses neutral materials and allows normal maps.
  * **Reflections** : Renders the scene to visualize reflections. This mode applies perfectly smooth, reflective materials to every Mesh Renderer.
  * **Reflections With Smoothness** : Renders the scene to visualize reflections. This mode applies reflective materials without an overridden smoothness to every GameObject.

  
**Lighting Features** | Specifies flags for which lighting features contribute to the final lighting result. Use this to view and debug specific lighting features in your scene. The options are:
  * **Nothing** : Shortcut to disable all flags.
  * **Everything** : Shortcut to enable all flags.
  * **Global Illumination** : Indicates whether to render [global illumination](https://docs.unity3d.com/Manual/realtime-gi-using-enlighten.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination).
  * **Main Light** : Indicates whether the main directional [Light](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/light-component.html) contributes to lighting.
  * **Additional Lights** : Indicates whether lights other than the main directional light contribute to lighting.
  * **Vertex Lighting** : Indicates whether additional lights that use per-vertex lighting contribute to lighting.
  * **Emission** : Indicates whether [emissive](https://docs.unity3d.com/Manual/StandardShaderMaterialParameterEmission.html) materials contribute to lighting.
  * **Ambient Occlusion** : Indicates whether [ambient occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html)A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) contributes to lighting.

  
## Render Graph
The properties in this section let you change how the [render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html) works.
**Property** | **Description**  
---|---  
**Clear Render Targets At Creation** | Clears **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) the first time the render graph system uses them.  
**Clear Render Targets When Freed** | Clears render textures when they’re no longer used by render graph.  
**Disable Pass Culling** | Disables URP culling render passes that have no impact on the final render.  
**Disable Pass Merging** | Disables URP merging render passes. For more information about URP merging passes, refer to [Optimize a render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-optimize.html).  
**Enable Logging** | Enables logging to the **Console** window.  
**Log Frame Information** | Logs how URP uses the resources during the frame, in the **Console** window.  
**Log Resources** | Logs the resources URP uses during the frame, in the **Console** window.  
# Probe Volumes
These settings make it possible for you to visualize [Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html) in your Scene, and configure the visualization.
### Subdivision Visualization
**Property** | **Sub-property** | **Description**  
---|---|---  
**Display Cells** | Display cells. Refer to [Understanding Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html) for more information.  
**Display Bricks** | Display bricks. Refer to [Understanding Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html) for more information.  
**Live Subdivision Preview** | Enable a preview of Adaptive Probe Volume data in the scene without baking. This might make the Editor slower. This setting appears only if you select **Display Cells** or **Display Bricks**.  
| **Cell Updates Per Frame** | Set the number of cells, bricks, and probe positions to update per frame. Higher values might make the Editor slower. The default value is 4. This property appears only if you enable **Live Subdivision Preview**.  
| **Update Frequency** | Set how frequently Unity updates cell, bricks, and probe positions, in seconds. The default value is 1. This property appears only if you enable **Live Subdivision Preview**.  
**Debug Draw Distance** | Set how far from the scene camera Unity draws debug visuals for cells and bricks, in meters. The default value is 500.  
### Probe Visualization
**Property** | **Sub-property** | **Description**  
---|---|---  
**Display Probes** | Display probes.  
| **Probe Shading Mode** | Set what the Rendering Debugger displays. The options are:
  * **SH** : Display the [spherical harmonics (SH) lighting data](https://docs.unity3d.com/Manual/LightProbes-TechnicalInformation.html) for the final color calculation. The number of bands depends on the **SH Bands** setting in the active [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html).
  * **SHL0** : Display the spherical harmonics (SH) lighting data with only the first band.
  * **SHL0L1** : Display the spherical Harmonics (SH) lighting data with the first two bands.
  * **Validity** : Display whether probes are valid, based on the number of backfaces the probe samples. Refer to [Fix issues with Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-fixissues.html) for more information about probe validity.
  * **Probe Validity Over Dilation Threshold** : Display red if a probe samples too many backfaces, based on the **Validity Threshold** set in the [Adaptive Probe Volumes panel](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html). This means the probe can’t be baked or sampled.
  * **Invalidated By Touchup Volumes** : Display probes that a [Probe Adjustment Volume component](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-adjustment-volume-component-reference.html) has made invalid.
  * **Size** : Display a different color for each size of [brick](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-concept.html).
  * **Sky Occlusion SH** : If you enable [sky occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html), this setting displays the amount of indirect light the probe receives from the sky that bounced off static GameObjects. The value is a scalar, so it displays as a shade of gray.
  * **Sky Direction** : Display a green circle that represents the direction from the probe to the sky. This setting displays a red circle if Unity can’t calculate the direction, or **Sky Direction** in the [Adaptive Probe Volumes panel](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-lighting-panel-reference.html) is disabled.

  
| **Debug Size** | Set the size of the displayed probes. The default is 0.3.  
| **Exposure Compensation** | Set the brightness of the displayed probes. Decrease the value to increase brightness. The default is 0. This property appears only if you set **Probe Shading Mode** to **SH** , **SHL0** , or **SHL0L1**.  
| **Max Subdivisions Displayed** | Set the lowest probe density to display. For example, set this to 0 to display only the highest probe density.  
| **Min Subdivisions Displayed** | Set the highest probe density to display.  
**Debug Probe Sampling** | Display how probes are sampled for a pixel. In the **Scene view** An interactive view into the world you are creating. You use the Scene View to select and position scenery, characters, cameras, lights, and all other types of Game Object. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheSceneView.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SceneView), in the **Adaptive Probe Volumes** overlay, select **Select Pixel** to change the pixel.  
| **Debug Size** | Set the size of the **Debug Probe Sampling** display.  
| **Debug With Sampling Noise** | Enable sampling noise for this debug view. Enabling this gives more accurate information, but makes the information more difficult to read.  
**Virtual Offset Debug** | Display the offsets Unity applies to **Light Probe** Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) capture positions.  
| **Debug Size** | Set the size of the arrows that represent Virtual Offset values.  
**Debug Draw Distance** | Set how far from the scene camera Unity draws debug visuals for cells and bricks, in meters. The default is 200.  
### Streaming
Use the following properties to control how URP streams Adaptive Probe Volumes. Refer to [Optimize loading Adaptive Probe Volume data](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html) for more information.
**Property** | **Description**  
---|---  
**Freeze Streaming** | Stop Unity from streaming probe data.  
**Display Streaming Score** | If you enable **Display Cells** , this setting darkens cells that have a lower priority for streaming. Cells closer to the camera usually have the highest priority.  
**Maximum cell streaming** | Stream as many cells as possible every frame.  
**Display Index Fragmentation** | Open an overlay that displays how fragmented the streaming memory is. A green square is an area of used memory. The more spaces between the green squares, the more fragmented the memory.  
**Index Fragmentation Rate** | Displays the amount of fragmentation as a numerical value, where 0 is no fragmentation.  
**Verbose Log** | Log information about streaming.  
### Scenario Blending
Use the following properties to control how URP blends Lighting Scenarios. Refer to [Bake different lighting setups with Lighting Scenarios](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html) for more information.
**Property** | **Description**  
---|---  
**Number of Cells Blended Per Frame** | Determines the maximum number of cells Unity blends per frame. The default is 10,000.  
**Turnover Rate** | Set the blending priority of cells close to the camera. The range is 0 to 1, where 0 sets the cells close to the camera with high priority, and 1 sets all cells with equal priority. Increase **Turnover Rate** to avoid cells close to the camera blending too frequently.  
**Scenario To Blend With** | Select a Lighting Scenario to blend with the active Lighting Scenario.  
**Scenario Blending Factor** | Set how far to blend from the active Lighting Scenario to the **Scenario To Blend With**. The range is 0 to 1, where 0 is fully the active Lighting Scenario, and 1 is fully the **Scenario To Blend With**.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger-add-controls.html)
Add controls to the Rendering Debugger in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-birp.html)
Graphics performance and profiling in the Built-In Render Pipeline
