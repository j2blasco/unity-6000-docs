* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Universal Render Pipeline reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-reference-landing.html)
  * Universal Render Pipeline asset reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-reference-landing.html)
Universal Render Pipeline reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)
Universal Renderer asset reference for URP
# Universal Render Pipeline asset reference for URP
In the URP Asset, you can configure settings for:
  * [**Rendering**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#rendering)
  * [**Quality**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#quality)
  * [**Lighting**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#lighting)
  * [**Shadows**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#shadows)
  * [**Post-processing**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#post-processing)
  * [**Volumes**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#volumes)
  * [**Adaptive Performance**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#adaptive-performance)


**Note:** If you have the experimental 2D Renderer enabled (menu: **Graphics Settings** > add the 2D Renderer Asset under **Scriptable Render Pipeline Settings**), some of the options related to 3D rendering in the URP Asset don’t have any impact on your final app or game.
### Rendering
The **Rendering** settings control the core part of the pipeline rendered frame.
Property | Description  
---|---  
**Depth Texture** | Enables URP to create a `_CameraDepthTexture`. URP then uses this [depth texture](https://docs.unity3d.com/Manual/SL-DepthTextures.html) by default for all **Cameras** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in your **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). You can override this for individual cameras in the [Camera Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html).  
**Opaque Texture** | Enable this to create a `_CameraOpaqueTexture` as default for all cameras in your scene. This works like the [GrabPass](https://docs.unity3d.com/Manual/SL-GrabPass.html) in the built-in render pipeline.  
  
The **Opaque Texture** provides a snapshot of the scene right before URP renders any transparent meshes. You can use this in transparent Shaders to create effects like frosted glass, water refraction, or heat waves. You can override this for individual cameras in the [Camera Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html).  
**Opaque Downsampling** | Set the sampling mode on the opaque texture to one of the following:
  * **None** : Produces a copy of the opaque pass in the same resolution as the camera.
  * **2x Bilinear** : Produces a half-resolution image with bilinear filtering.
  * **4x Box** : Produces a quarter-resolution image with box filtering. This produces a softly blurred copy.
  * **4x Bilinear** : Produces a quarter-resolution image with bi-linear filtering.

  
****Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) Holes** | If you disable this option, the URP removes all Terrain hole **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variants when you build for the Unity Player, which decreases build time.  
**GPU Resident Drawer** | The GPU Resident Drawer automatically uses the [`BatchRendererGroup`](https://docs.unity3d.com/Manual/batch-renderer-group.html) API to draw GameObjects with GPU instancing. For more information, refer to [Use the GPU Resident Drawer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-resident-drawer.html).  
  
Available options:
  * **Disabled** : Unity doesn’t automatically draw GameObjects with GPU instancing.
  * **Instanced Drawing** : Unity automatically draws GameObjects with GPU instancing.

  
**Small-Mesh Screen-Percentage** | Set the screen percentage Unity uses to cull small GameObjects, to speed up rendering. Unity culls GameObjects that fill less of the screen than this value.  
  
This setting might not work if you use your own [Level of Detail (LOD) meshes](https://docs.unity3d.com/Manual/LevelOfDetail.html).  
  
Set the value to 0 to stop Unity culling small GameObjects.  
  
To prevent Unity culling an individual GameObject that covers less screen space than this value, go to the **Inspector** window for the GameObject and add a **Disallow Small Mesh Culling** component.  
**GPU**Occlusion Culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling)** | Enable Unity to use the GPU instead of the CPU to exclude **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) from rendering when they’re hidden behind other GameObjects. Refer to [Use GPU occlusion culling](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html) for more information.  
**SRP Batcher** | Enable the SRP Batcher. This is useful if you have many different Materials that use the same Shader. The SRP Batcher is an inner loop that speeds up CPU rendering without affecting GPU performance. When you use the SRP Batcher, it replaces the SRP rendering code inner loop.  
  
If both **SRP Batcher** and **Dynamic Batching** are enabled, SRP Batcher will take precedence over dynamic batching as long as the shader is SRP Batcher compatible.  
  
**Note** : If assets or shaders in a project are not optimized for use with the SRP Batcher, low performance devices might be more performant when you disable the SRP Batcher.  
**Dynamic Batching** | Enable [Dynamic Batching](https://docs.unity3d.com/Manual/DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching), to make the render pipeline automatically batch small dynamic objects that share the same Material. This is useful for platforms and graphics APIs that do not support GPU instancing.  
  
If your targeted hardware does support GPU instancing, disable **Dynamic Batching**. You can change this at run time.  
**Debug Level** | Set the level of debug information that the render pipeline generates.  
  
Available options:
  * **Disabled** : Debugging is disabled. This is the default.
  * **Profiling** : Makes the render pipeline provide detailed information tags, which you can find in the FrameDebugger.

  
**Shader Variant Log Level** | Set the level of information about Shader Stripping and Shader Variants you want to display when Unity finishes a build.  
  
Available options:
  * **Disabled** : Unity doesn’t log anything.
  * **Only Universal** : Unity logs information for all of the [URP Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html).
  * **All** : Unity logs information for all Shaders in your build.

  
You can check the information in Console panel when your build has finished.  
**Store Actions** | Defines if Unity discards or stores the render targets of the DrawObjects Passes.  
  
Available options:
  * **Auto** : Unity uses the **Discard** option by default, and falls back to the **Store** option if it detects any injected Passes.
  * **Discard** : Unity discards the render targets of render Passes that are not reused later (lower memory bandwidth).
  * **Store** : Unity stores all render targets of each Pass. **Store** significantly increases the memory bandwidth on mobile and tile-based GPUs.

  
### Quality
These settings control the quality level of the URP. This is where you can make performance better on lower-end hardware or make graphics look better on higher-end hardware.
**Tip:** If you want to have different settings for different hardware, you can configure these settings across multiple Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) assets, and switch them out as needed.
Property | Description  
---|---  
**HDR** | Enable this to allow rendering in High Dynamic Range (HDR) by default for every camera in your scene. With HDR, the brightest part of the image can be greater than 1.  
  
This gives you a wider range of light intensities, so your lighting looks more realistic, such as being able to pick out details and experience less saturation even with bright light. This is useful if you want a wide range of lighting or to use [bloom](https://docs.unity3d.com/Manual/PostProcessing-Bloom.html)A post-processing effect used to reproduce an imaging artifact of real-world cameras. The effect produces fringes of light extending from the borders of bright areas in an image, contributing to the illusion of an extremely bright light overwhelming the camera or eye capturing the scene.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Bloom) effects.  
  
If you’re targeting lower-end hardware, you can disable this to skip HDR calculations and get better performance. You can override this for individual cameras in the Camera Inspector.  
****HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) Precision** | The precision of the Camera color buffer in HDR rendering. The 64 bit precision lets you avoid banding artifacts, but requires higher bandwidth and might make sampling slower. Default value: 32 bit.  
**Anti Aliasing (MSAA)** | Use [Multisample Anti-aliasing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html#msaa) by default for every Camera in your scene while rendering. This softens edges of your geometry, so they’re not jagged or flickering. In the drop-down menu, select how many samples to use per pixel: **2x** , **4x** , or **8x**. The more samples you choose, the smoother your object edges are.  
  
If you want to skip MSAA calculations, or you don’t need them in a 2D game, select **Disabled**. You can override this for individual cameras in the Camera Inspector.  
  
**Note** : On mobile platforms that do not support the [StoreAndResolve](https://docs.unity3d.com/ScriptReference/Rendering.RenderBufferStoreAction.StoreAndResolve.html) store action, if **Opaque Texture** is selected in the URP asset, Unity ignores the **Anti Aliasing (MSAA)** property at runtime (as if Anti Aliasing (MSAA) is set to Disabled).  
**Render Scale** | This slider scales the render target resolution (not the resolution of your current device). Use this when you want to render at a smaller resolution for performance reasons or to upscale rendering to improve quality.  
  
**Note** : This only scales the game rendering. UI rendering is left at the native resolution for the device.  
**Upscaling Filter** | Select which image filter Unity uses when performing the upscaling. Unity performs upscaling when the Render Scale value is less than 1.0.  
**Automatic** | Unity selects one of the filtering options based on the Render Scale value and the current screen resolution. If integer scaling is possible, Unity selects the Nearest-Neighbor option, otherwise Unity selects the Bilinear option.  
**Bilinear** | Unity uses the bilinear or linear filtering provided by the graphics API.  
**Nearest-Neighbor** | Unity uses the nearest-neighbor or point sampling filtering provided by the graphics API.  
  
**Note** : The **Nearest-Neighbour** filter doesn’t work if **Post-processing** is enabled.  
**FidelityFX Super Resolution 1.0** | Unity uses the AMD FidelityFX Super Resolution 1.0 (FSR) technique to perform upscaling.  
  
Unlike most other Upscaling Filter options, this filter remains active even at a Render Scale value of 1.0. This filter can still improve image quality even when no scaling is occurring. This also makes the transition between scale values 0.99 and 1.0 less noticeable in cases where dynamic resolution scaling is active.  
  
**Note** : This filter is only supported on devices that support Unity shader model 4.5 or higher. On devices that do not support Unity shader model 4.5, Unity uses the **Automatic** option instead.  
**Override FSR Sharpness** | Unity shows this check box when you select the FSR filter. Selecting this check box lets you specify the intensity of the FSR sharpening pass.  
**FSR Sharpness** | Specify the intensity of the FSR sharpening pass. A value of 0.0 provides no sharpening, a value of 1.0 provides maximum sharpness.  
  
**Note** : This option has no effect when FSR is not the active upscaling filter.  
**Spatial-Temporal Post-Processing (STP) 1.0** | Uses the Spatial Temporal Post-Processing (STP) technique to perform upscaling. Selecting this option forces the **Anti-Aliasing** setting in the [Camera Inspector window](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.md) to **Temporal Anti-aliasing (TAA)**.  
  
This setting improves image quality even without scaling, so it remains active when **Render Scale** is set to 1.0.  
  
For more information on STP, refer to [Spatial-Temporal Post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/stp/stp-upscaler.html).  
  
**Note** : This setting is supported only on non-GLES devices that support compute shaders. On unsupported devices, Unity uses **Automatic** instead.  
****LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) Cross Fade** | Use this property to enable or disable the LOD cross-fade. If you disable this option, URP removes all LOD cross-fade shader variants when you build the Unity Player, which decreases the build time.  
**LOD Cross Fade Dithering Type** | When an [LOD group](https://docs.unity3d.com/Manual/class-LODGroup.html)A component to manage level of detail (LOD) for GameObjects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LODGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LODGroup) has **Fade Mode** set to **Cross Fade** , Unity renders the Renderer’s LOD meshes with cross-fade blending between them using alpha testing. This property defines the type of LOD cross-fade.  
  
Available options:
  * **Bayer Matrix** : better performance than the Blue Noise option, but has a repetitive pattern.
  * **Blue Noise** : uses a precomputed blue noise texture and provides a better look than the Bayer Matrix option, but has a slightly higher performance cost.

  
### Lighting
These settings affect the lights in your scene.
If you disable some of these settings, the relevant [keywords](https://docs.unity3d.com/Manual/shader-keywords) are [stripped from the Shader variables](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html). If there are settings that you know for certain you won’t use in your game or app, you can disable them to improve performance and reduce build time.
Property | Description  
---|---  
**Main Light** | These settings affect the main [Directional Light](https://docs.unity3d.com/Manual/Lighting.html) in your scene. You can select this by assigning it as a [Sun Source](https://docs.unity3d.com/Manual/GlobalIllumination.html) in the Lighting Inspector. If you don’t assign a sun source, the URP treats the brightest directional light in the scene as the main light.  
  
You can choose between [Pixel Lighting](https://docs.unity3d.com/Manual/LightPerformance.html) and **None**. If you choose None, URP doesn’t render a main light, even if you’ve set a sun source.  
**Cast Shadows** | Check this box to make the main light cast shadows in your scene.  
**Shadow Resolution** | This controls how large the shadow map texture for the main light is. High resolutions give sharper, more detailed shadows. If memory or rendering time is an issue, try a lower resolution.  
**Light Probe System** | Select the light probe system this URP Asset uses.  
  
Available options:
  * **Light Probe Groups (Legacy)** : Use the same [Light Probe Group system](https://docs.unity3d.com/Manual/class-LightProbeGroup.html) as the Built-In Render Pipeline.
  * **Adaptive Probe Volumes** : Use [Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html).

  
**Memory Budget** | Limits the width and height of the textures that store baked Global Illumination data, which determines the amount of memory Unity sets aside to store baked Adaptive Probe Volume data. These textures have a fixed depth.  
  
Available options:
  * **Memory Budget Low**
  * **Memory Budget Medium**
  * **Memory Budget High**

  
**SH Bands** | Determines the [spherical harmonics (SH) bands](https://docs.unity3d.com/Manual/LightProbes-TechnicalInformation.html) Unity uses to store probe data. L2 provides more precise results, but uses more system resources.  
  
Available options: 
  * **Spherical Harmonics L1**
  * **Spherical Harmonics L2**

  
**Enable Streaming** | Enable to stream Adaptive Probe Volume data from CPU memory to GPU memory at runtime. Refer to [Optimize loading Adaptive Probe Volume data](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html) for more information.  
**Estimated GPU Memory Cost** | Indicates the amount of texture data used by Adaptive Probe Volumes in your project.  
**Additional Lights** | Here, you can choose to have additional lights to supplement your main light. Choose between [Per Vertex](https://docs.unity3d.com/Manual/LightPerformance.html), [Per Pixel](https://docs.unity3d.com/Manual/LightPerformance.html), or **Disabled**.  
**Per Object Limit** | This slider sets the limit for how many additional lights can affect each GameObject. Unity ignores this setting if you select the Forward+ **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath).  
**Cast Shadows** | Check this box to make the additional lights cast shadows in your scene.  
**Shadow Atlas Resolution** | This controls the size of the textures that cast directional shadows for the additional lights.  
  
This is a sprite atlas that packs up to 16 shadow maps. High resolutions give sharper, more detailed shadows. If memory or rendering time is an issue, try a lower resolution.  
**Shadow Resolution Tiers** | Set the resolution of the shadows cast by additional lights at various tiers.  
  
Resolutions must have a value of 128 or greater, and are rounded to the next power of two.  
  
**Note** : This property is only visible when the **Cast Shadows** property is enabled for Additional Lights.  
**Cookie Atlas Resolution** | The size of the cookie atlas the additional lights use. All additional lights are packed into a single cookie atlas.  
  
This property is only visible when the **Light Cookies** property is enabled.  
**Cookie Atlas Format** | The format of the cookie atlas for additional lights. All additional lights are packed into a single cookie atlas.  
  
Available options:
  * **Grayscale Low**
  * **Grayscale High**
  * **Color Low**
  * **Color High**
  * **Color HDR**

This property is only visible when the **Light Cookies** property is enabled.  
**Reflection Probes** | Use these properties to control **reflection probe** A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe) settings.  
**Probe Blending** | Smooth the transitions between Reflection Probes. For more information, refer to [Reflection Probe Blending](https://docs.unity3d.com/6000.0/Documentation/Manual/blend-reflection-probes-birp.html). This setting is always enabled if you select the Forward+ rendering path.  
**Box Projection** | Create reflections on objects based on their position within the probe’s box, while still using a single probe as the reflection source. For more information, refer to [Advanced Reflection Probe features](https://docs.unity3d.com/6000.0/Documentation/Manual/AdvancedRefProbe.html).  
**Mixed Lighting** | Enable [Mixed Lighting](https://docs.unity3d.com/Manual/LightMode-Mixed.html) to configure the pipeline to include mixed lighting shader variants in the build.  
**Use Rendering Layers** | With this option selected, you can configure certain Lights to affect only specific GameObjects. For more information on Rendering Layers and how to use them, refer to the documentation on [Rendering Layers](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-layers.html).  
**Light Cookies** | Enables [light cookies](https://docs.unity3d.com/Manual/Cookies.html). This property enables **Cookie Atlas Resolution** and **Cookie Atlas Format** for additional lights.  
**SH Evaluation Mode** | Defines the spherical harmonic (SH) lighting evaluation type.  
  
Available options:
  * **Auto** : Unity selects a mode automatically.
  * **Per Vertex** : Evaluate lighting per vertex.
  * **Mixed** : Evaluate lighting partially per vertex, partially per pixel.
  * **Per Pixel** : Evaluate lighting per pixel.

  
### Shadows
These settings let you configure how shadows look and behave, and find a good balance between the visual quality and performance.
![Shadows](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/lighting/urp-asset-shadows.png) Shadows
The **Shadows** section has the following properties.
Property | Description  
---|---  
**Max Distance** | The maximum distance from the Camera at which Unity renders the shadows. Unity does not render shadows farther than this distance.  
  
**Note** : This property is in metric units regardless of the value in the **Working Unit** property.  
**Working Unit** | The unit in which Unity measures the shadow cascade distances.  
**Cascade Count** | The number of [shadow cascades](https://docs.unity3d.com/Manual/shadow-cascades.html). With shadow cascades, you can avoid crude shadows close to the Camera and keep the Shadow Resolution reasonably low.  
  
For more information, refer to the documentation on [shadow cascades](https://docs.unity3d.com/6000.0/Documentation/Manual/shadow-cascades.html). Increasing the number of cascades reduces the performance. Cascade settings only affects the main light.  
**Split** **1** | The distance where cascade 1 ends and cascade 2 starts.  
**Split** **2** | The distance where cascade 2 ends and cascade 3 starts.  
**Split** **3** | The distance where cascade 3 ends and cascade 4 starts.  
**Last** **Border** | The size of the area where Unity fades out the shadows. Unity starts fading out shadows at the distance **Max Distance** - **Last Border** , at **Max Distance** the shadows fade to zero.  
**Depth Bias** | Use this setting to reduce [shadow acne](https://docs.unity3d.com/Manual/ShadowPerformance.html).  
**Normal Bias** | Use this setting to reduce [shadow acne](https://docs.unity3d.com/Manual/ShadowPerformance.html).  
**Soft Shadows** | Select this check box to enable extra processing of the shadow maps to give them a smoother look.  
**Performance impact** : High impact on platforms that use tile-based rendering, such as mobile platforms and untethered XR platforms.  
When this option is disabled, Unity samples the shadow map once with the default hardware filtering.  
**Quality** | Select the quality level of soft shadow processing.  
  
Available options:
  * **Low** : good balance of quality and performance for mobile platforms. Filtering method: 4 PCF taps.
  * **Medium** : good balance of quality and performance for desktop platforms. Filtering method: 5x5 tent filter. This is the default value.
  * **High** : best quality, higher performance impact. Filtering method: 7x7 tent filter.

  
**Conservative Enclosing Sphere** | Enable this option to improve shadow frustum culling and prevent Unity from excessively culling shadows in the corners of the shadow cascades.  
  
Disable this option only for compatibility purposes of existing projects created in previous Unity versions.  
  
If you enable this option in an existing project, you might need to adjust the shadows cascade distances because the shadow culling enclosing spheres change their size and position.  
  
**Performance impact** : Enabling this option is likely to improve performance, because the option minimizes the overlap of shadow cascades, which reduces the number of redundant static shadow casters.  
### Post-processing
This section allows you to fine-tune global **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) settings.
Property | Description  
---|---  
**Grading Mode** | Select the [color grading](https://docs.unity3d.com/Manual/PostProcessing-ColorGrading.html) mode to use for the Project.
  * **High Dynamic Range** : This mode works best for high precision grading similar to movie production workflows. Unity applies color grading before tonemapping.
  * **Low Dynamic Range** : This mode follows a more classic workflow. Unity applies a limited range of color grading after tonemapping.

  
**LUT Size** | Set the size of the internal and external [look-up textures (LUTs)](https://docs.unity3d.com/Manual/PostProcessing-ColorGrading.html) that the Universal Render Pipeline uses for color grading. Higher sizes provide more precision, but have a potential cost of performance and memory use. You cannot mix and match LUT sizes, so decide on a size before you start the color grading process.  
  
The default value, **32** , provides a good balance of speed and quality.  
**Alpha Processing** | With this setting enabled, URP post-processing effects output properly processed alpha values. With this setting disabled, URP discards the alpha channel by replacing alpha values with 1. The render target requires a format with the alpha channel.  
If you use HDR rendering, set the **HDR Precision** property to 64 bit, because the 32 bit format does not have the alpha channel.  
  
**Rendering into a render texture**  
If you are rendering the output with the alpha channel into a render texture, ensure that the **Color Format** property of the render texture has the alpha channel.  
On the camera that renders output with the alpha values, set the **Background Type** property in the **Environment** section to **Solid Color**. This lets you identify and process the alpha values in a shader.  
  
**Limitations**
  * In a setup with camera stacking, post-processing effects on an overlay camera still affect all cameras below it. This setting lets you configure different post-processing effects for separate cameras (not in the same camera stack) and use render textures and a compositing pass to combine them.
  * When applying post-processing effects, this feature preserves the alpha values as they were before applying an effect. As a consequence, pre-built post-processing effects that draw pixels beyond the original borders of objects (for example, bloom or depth of field effects) might render with sharp edges around objects they are affecting. This does not apply to effects that distort geometry, like the panini projection or the lens distortion effect. Those effects also distort the alpha channel.

  
**Fast sRGB/Linear Conversions** | Select this option to use faster, but less accurate approximation functions when converting between the sRGB and Linear color spaces.  
**Data Driven Lens Flare** | Allocate the shader variants and memory URP needs for [lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/lens-flare-srp-reference.html)A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) effect.  
**Screen Space Lens Flare** | Allocate the shader variants and memory URP needs for [screen space lens flares](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shared/lens-flare/reference-screen-space-lens-flare.html).  
### Volumes
Property | Description  
---|---  
**Volume Update Mode** | Select how Unity updates Volumes at run time. 
  * **Every Frame** : Unity updates volumes every frame.
  * **Via Scripting** : Unity updates volumes when triggered via scripting.

In the Editor, Unity updates Volumes every frame when not in Play mode.  
**Volume Profile** | Set the [Volume Profile](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volume-Profile.html) that a scene uses by default.  
  
Refer to [Understand volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Volumes.html) for more information.  
The list of Volume Overrides that the Volume Profile contains appears below **Volume Profile**. You can add, remove, disable, and enable Volume Overrides, and edit their properties. Refer to [Volume Overrides](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/VolumeOverrides.html) for more information.
### Adaptive Performance
This section is available if the Adaptive Performance package is installed in the project. The **Use Adaptive Performance** property lets you enable the Adaptive Performance functionality.
Property | Description  
---|---  
**Use Adaptive Performance** | Select this check box to enable the Adaptive Performance functionality, which adjusts the rendering quality at runtime.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-reference-landing.html)
Universal Render Pipeline reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)
Universal Renderer asset reference for URP
