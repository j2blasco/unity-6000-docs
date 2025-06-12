* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html

  * [The Unity Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/unity-editor.html)
  * [Editor Features](https://docs.unity3d.com/6000.0/Documentation/Manual/EditorFeatures.html)
  * [Project Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)
  * Graphics


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html)
Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html)
Package Manager
# Graphics
Use the **Graphics** settings (main menu: **Edit** > **Project Settings** , then select the **Graphics** category) to apply global settings for Graphics.
When you build your project, the values of these settings become static. You can’t change the settings at runtime.
This section provides documentation on the following groups of properties:
  * [Set Default Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#SRLoop)
  * [Shader stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#stripping)
  * [Shader loading](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#shader-loading)
  * [Culling settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#culling-settings)
  * [Pipeline Specific Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#pipeline-specific-settings)
    * [Camera Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Camera)
    * [Tier Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Tier)
    * [Built-in shader settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Built-in)
    * [Always-included Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#Always)


##  Set Default Render Pipeline Asset
Use the **Default**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline)** field to set the default render pipeline Unity uses to render your project. For example, set **Default Render Pipeline** to a Universal Render Pipeline (URP) Asset to use URP to render your project.
If **Default Render Pipeline** is set to **None** , Unity uses the Built-In Render Pipeline.
For more information, refer to the following:
  * [Pipeline Specific Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GraphicsSettings.html#pipeline-specific-settings)
  * [How to get, set, and configure the active render pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/srp-setting-render-pipeline-asset.html)


## Shader stripping
These properties allow you to configure [shader variant stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-stripping.html) in your build.
By default, Unity examines the **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) in the build and automatically strips [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant) that are not used in those scenes. However, this can cause problems if you want to use shaders or variants at runtime that would not otherwise be included in the build. For example, if you use AssetBundles or Addressables that rely on those shaders or variants, or if you use [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html) to change variants at runtime.
**Property** | **Function**  
---|---  
**Lightmap Modes** | Determine the shader variant stripping behavior for lightmap-related shaders. The options are:
  * **Automatic** : Unity examines the scenes in the build and automatically strips variants that are not used in those scenes. This is the default setting.
  * **Custom** : Select this option to manually include or exclude variants for the following lightmap modes:
    * **Baked Non-Directional**
    * **Baked Directional**.
    * **Realtime Non-Directional**
    * **Realtime Directional**
    * **Baked Shadowmask**
    * **Baked Subtractive**

  
**Fog Modes** | Determine the shader variant stripping behavior for shaders that relate to Unity’s built-in fog effect. The options are:
  * **Automatic** : Unity examines the scenes in the build and automatically strips variants that are not used in those scenes. This is the default setting.
  * **Custom** : Select this option to manually include or exclude variants for the following fog modes:
    * **Linear**
    * **Exponential**
    * **Exponential Squared**

  
**Instancing Variants** | Determine the shader variant stripping behavior for shaders that relate to GPU instancing. The options are:
  * **Strip Unused** : Unity only includes variants for GPU instancing for a given shader if at least one material that uses that shader has **Enable instancing** enabled. This is the default setting.
  * **Strip All** : Strip all variants for GPU instancing, even if they are being used.
  * **Keep All** : Include all variants for GPU instancing, even if they are not being used.

  
##  Shader loading
These properties allow you to configure how Unity prewarms [shader variant collections](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html) in your application.
For information on prewarming, including important information about graphics API support, refer to [Shader loading: Prewarming shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-prewarm.html).
**Property** | **Function**  
---|---  
**Renderer Light Probe Selection** | Choose the type of probe Unity uses when a Renderer receives global illumination from Light Probes but is not within the volume of influence (the tetrahedron) of any group of Light Probes.  
Options:
  * **Find closest Light Probe** : the default option. With this option selected, Unity searches for the nearest Light Probe, which consumes significant system resources.
  * **Use Ambient Probe** : Select this option to make Unity fall back to the [Ambient Probe](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderSettings-ambientProbe.html) in situations described above. This option uses less system resources.

  
**Preloaded shaders** | The shader variant collections to prewarm on application start.  
**Preload shaders after showing first scene** | This property determines when Unity prewarms the shader variants specified in **Preloaded shaders**.  
  
If enabled, Unity loads and prewarms the variants after the first scene has fully loaded. Otherwise, Unity loads and prewarms them before showing the first scene.  
**Preloaded time limit per frame (ms)** | Determines how Unity prewarms the shader variants specified in **Preloaded shaders** if **Preload shaders after showing first scene** is enabled.  
  
If the value is 0, Unity preloads all shader variants on the next frame after it displays the first scene.  
  
Otherwise, Unity preloads new shader variants over multiple frames after it displays the first scene. In a given frame, Unity prewarms shader variants until it reaches the time limit set in this property, then doesn’t begin prewarming new shader variants until the next frame.  
### Tracked shader variants
The Unity Editor can track which [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html) your application uses when it runs. You can use this information to build [shader variant collections](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html).
**Control** | **Function**  
---|---  
**Create asset** | Creates a new shader variant collection asset using the currently tracked shader variants.  
**Clear** | Clear tracked shader variants.  
##  Culling settings
**Camera-Relative Culling** determines whether Unity uses the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) position as the reference point for culling.
**Property** | **Function**  
---|---  
**Lights** | Use the camera position as the reference point to cull lights instead of the world space origin. Enable **Lights** to reduce flickering if lights are far away from the camera. Refer to [Understanding the View Frustum](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html) for more information.  
**Shadows** | Use the camera position as the reference point to cull shadows instead of the world space origin. Enable **Shadows** to reduce flickering if shadows are far away from the camera. Refer to [Understanding the View Frustum](https://docs.unity3d.com/6000.0/Documentation/Manual/UnderstandingFrustum.html) for more information.  
##  Pipeline-specific settings
The **Graphics** settings window always contains the Built-in Render Pipeline settings below.
However if your project uses a Scriptable Render Pipeline (SRP), for example the Universal Render Pipeline (URP) or the High Definition Render Pipeline (HDRP), the window contains a tab for each SRP in your project. Refer to the following pages for more information:
  * [URP Graphics Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-global-settings.html)
  * [HDRP Graphics Settings window reference](https://docs.unity3d.com/Packages/com.unity.render-pipelines.high-definition@17.0/manual/Default-Settings-Window.html)


### Camera Settings
These properties control various rendering settings.
**Property** | **Function**  
---|---  
**Transparency Sort Mode** | Define the order for rendering objects by their distance along a specific axis. Renderers in Unity are sorted by several criteria, such as their layer number or their distance from the camera. This is generally only useful in 2D development: for example, sorting Sprites by height or along the Y-axis. The options are:
  * **Default** : Sort objects based on the Camera mode.
  * **Perspective** : Sort objects based on perspective view.
  * **Orthographic** : Sort objects based on orthographic view.
  * **Custom Axis** : Sort objects based on the sort mode defined with the **Transparency Sort Axis**.

  
**Transparency Sort Axis** | Define a custom **Transparency Sort Mode**.  
### Tier Settings
In the Built-in Render Pipeline, you can use **Tier settings** to change rendering and shader compilation settings for different types of hardware. For more information, see [Graphics tiers](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-tiers.html).
**Property** | **Function**  
---|---  
**Standard Shader Quality** | Set the quality of the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) to _High_ , _Medium_ , or _Low_.  
**Reflection Probes Box Projection** | Enable projection for reflection UV mappings on [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe).  
**Reflection Probes Blending** | Enable [blending on Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingReflectionProbes.html).  
**Detail Normal Map** | Enable [Detail Normal Map](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterDetail.html) sampling, if assigned.  
**Enable Semitransparent Shadows** | Enable Semitransparent Shadows. This adds or removes the UNITY_USE_DITHER_MASK_FOR_ALPHABLENDED_SHADOWS shader compiler define.  
**Enable Light Probe Proxy Volume** | Enable rendering a 3D grid of interpolated [Light Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LightProbeProxyVolume.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe).  
**Cascaded Shadows** | Enable using cascaded shadow maps. This adds or removes the UNITY_NO_SCREENSPACE_SHADOWS shader compiler define.  
**Prefer 32 bit shadow maps** | Enable 32-bit float shadow map when you are targeting platforms that use DX11 or DX12. Most platforms have a fixed shadow map format that you can’t adjust. These vary in format, and can be 16-bit, 24-bit, or 32-bit, and can also be either float- or integer-based. 32-bit shadow maps give higher quality shadows than 16-bit, but use increased memory and bandwidth on the GPU. **Note:** To use 32-bit shadow maps, make sure the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) is also set to 32-bit.  
**Use HDR** | Enable [High Dynamic Range rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html) for this tier.  
**HDR Mode** | Select the format to use for the HDR buffer when **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) is enabled for the current Graphics Tier. By default, this is set to _FP16_. The options are:
  * **FP16** : Color render texture format, 16-bit floating point per channel.
  * **R11G11B10** : Color render texture format. R and G channels are 11-bit floating point, B channel is 10-bit floating point.

  
**Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) | Choose how Unity should render graphics. Different rendering paths affect the performance of your game, and how lighting and shading are calculated. Some paths are more suited to different platforms and hardware than others. _Deferred_ rendering is not supported when using Orthographic projection. If the camera’s projection mode is set to Orthographic, these values are overridden, and the camera always uses _Forward_ rendering. The options are:
  * **Forward**
  * **Deferred**
  * **Legacy Vertex Lit**

For more information, refer to [Rendering paths](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html).  
**Realtime Global Illumination CPU Usage** | The CPU budget you allow Enlighten Realtime Global Illumination to use for lighting calculations at runtime. Increasing this makes the system react faster to changes in lighting at a cost of using more CPU time. **Note:** Some platforms allow all CPUs to be occupied by worker threads whereas some enforce maximums. For example, some gaming consoles allow a maximum of 4 CPU cores. For Android devices, if it is a bigLittle architecture, only the little CPUs are used; otherwise the maximum is one less than the total number of CPUs. If you use the URP or HDRP render pipelines, you can configure this property in the [quality settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html). The options are:
  * **Low** : 25% of the allowed CPU threads are used as worker threads.
  * **Medium** : 50% of the allowed CPU threads are used as worker threads.
  * **High** : 75% of the allowed CPU threads are used as worker threads.
  * **Unlimited** : 100% of the allowed CPU threads are used as worker threads.

  
### Built-in shader settings
Use these settings to specify which shader to use for each of the listed features in the Built-in Render Pipeline.
**Rendering path** | **Shader to use**  
---|---  
**Deferred** | Use with [Deferred shading](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading).  
**Deferred Reflection** | Use with [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html) in deferred shading.  
**Screen Space shadows** | Use with cascaded shadow maps for directional lights on PC/console platforms.  
**Motion vectors** | Use for object-based motion vector calculations.  
**Lens Flare** A component that simulates the effect of lights refracting inside a camera lens. Use a Lens Flare to represent very bright lights or add atmosphere to your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-LensFlare.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LensFlare) | Use with [Lens Flares](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Flare.html).  
**Light Halo** | Use with [Light Halos](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Halo.html).  
For each of these features, you can choose which type of Shader to use:
  * **No Support** disables this calculation. Use this setting if you are not using deferred shading. This will save some space in the built game data files.
  * **Built-in Shader** uses Unity’s built-in Shaders to do the calculation. This is the default.
  * **Custom Shader** uses your own compatible Shader to do the calculation. This enables you to do deep customization of deferred rendering.


When you choose **Custom shader** , a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) reference property appears below the feature property where you can set a reference to the Shader you want to use.
### Always Included Shaders
This is a list of shaders for which Unity includes all possible [variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html) in every build. This can be useful if you want to use shaders or variants at runtime that would not otherwise be included in the build; for example, if you use AssetBundles or Addressables that rely on those shaders or variants, or if you use [shader keywords](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html) to change variants at runtime.
**Warning:** This feature is not recommended for shaders that have a large number of variants, such as the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html); it can lead to significant runtime and build time performance problems. You should instead create [shader variant collections](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variant-collections.html) that contain only the variants you need, and include those in your build.
**Note:** This setting overrides [shader keyword declaration settings](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-keywords.html#declaring-keywords-definition-type). For each shader in the list, Unity includes all sets of all keywords, even if you use the “shader feature” declaration type.
To add a shader to the list, increase the value in the **Size** property. To remove the last shader in the list, decrease the **Size** property. To remove a shader which is not the last one in the list, you can set the value to **None**.
GraphicsSettings
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-EditorManager.html)
Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html)
Package Manager
