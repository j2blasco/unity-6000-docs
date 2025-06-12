* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/xr-untethered-device-optimization.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Graphics performance and profiling](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-profiling.html)
  * [Graphics performance and profiling in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-performance-and-profiling-in-urp.html)
  * [Reducing rendering work on the CPU or GPU in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/OptimizingGraphicsPerformance-urp.html)
  * Optimize for untethered XR devices in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)
Adjust settings to improve performance in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
Optimizing draw calls in URP
# Optimize for untethered XR devices in URP
This page describes the optimization techniques for URP projects that target untethered **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) devices.
Most untethered XR devices use tile-based GPUs. The guidelines on this page help you use this hardware architecture more efficiently and avoid using rendering techniques that are less efficient on those devices.
To learn more about how tiled-based GPUs work, refer to the additional resources section. 
## Use Vulkan API
Vulkan API is more stable and provides better performance compared to OpenGL ES API in URP projects targeting XR platforms.
Refer to [Graphics API support](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsAPIs.html) for information on how to change the graphics API to Vulkan.
## Use OpenXR Plugin
Use the [OpenXR Plugin](https://docs.unity3d.com/Packages/com.unity.xr.openxr@latest?subfolder=/manual/index.html) in projects that target XR platforms.
Enable the following settings in your project:
  * **Multi-view \ Single pass rendering**
  * **Foveated rendering**


To configure the **Render Mode** to **Single Pass Instanced \ Multi-view** :
  1. Open the ****Project Settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings)** window.
  2. Under **XR**Plug-in** A set of code created outside of Unity that creates functionality in Unity. There are two kinds of plug-ins you can use in Unity: Managed plug-ins (managed .NET assemblies created with tools like Visual Studio) and Native plug-ins (platform-specific native code libraries). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/plug-ins.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Plug-in) Management**, open the **OpenXR** settings.
  3. Under the **Android** tab, change the **Render Mode** to **Single Pass Instanced \ Multi-view**.


## Use render graph system
Starting with Unity 6.0 Preview, new URP projects use the render graph system. Refer to [Benefits of the render graph system](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/render-graph-benefits.html) to understand the benefits of RenderGraph.
## Use Forward rendering
In URP, Deferred rendering generates several render targets for the G-buffer. Unity performs multiple [graphics memory loads](https://developer.qualcomm.com/software/snapdragon-profiler/app-notes/avoid-gmem-loads) to access those render targets, which is slow on tile-based GPUs.
Refer to [Deferred rendering implementation details](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html) for more information on the implementation of the G-buffer in URP.
The ****Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath)** settings is in the [**Rendering**](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html#rendering) section of the [Universal Renderer Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html).
## Avoid post-processing
Avoid **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) on untethered XR devices because of its performance impact.
URP renders post-processing in multiple render passes where the output of one pass is the input of the next one. On tile-based GPUs one of the most resource intensive tasks is performing a GMEM load. Post-processing passes often cause GMEM loads because they might load additional textures or copy the current screen color information to perform certain effects. In certain post-processing effects, for example in [bloom](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-bloom.html)A post-processing effect used to reproduce an imaging artifact of real-world cameras. The effect produces fringes of light extending from the borders of bright areas in an image, contributing to the illusion of an extremely bright light overwhelming the camera or eye capturing the scene.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Bloom), rendering a **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) requires sampling adjacent pixels. This can cause extra GMEM loads for accessing pixels outside a certain tile.
In URP, the post-processing pass executes a final **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) even if there are no effects to execute. This requires another GMEM load because the blit operation copies the current texture in which Unity executes the post-processing pass to the final **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) texture.
On XR platforms Unity performs such operations once per view which increases the performance impact. 
**Note:** Some effects can cause motion sickness. Refer to section [Post-processing in URP for VR](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html#post-processing-in-urp-for-vr) for a list of effects that can cause motion sickness.
To disable post-processing for a specific **Universal Renderer** :
  1. Select a **Universal Renderer** asset.
  2. Under **Post-processing** , ensure that the **Enabled** checkbox is cleared.


To disable post-processing for a camera:
  1. Select a camera in the **Hierarchy** window.
  2. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, expand the **Rendering** section.
  3. Ensure that **Post Processing** is cleared.


## Avoid geometry shaders
Avoid using geometry **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) on platforms with tile-based GPUs. Some devices don’t support geometry shaders. 
The generation of additional primitives and vertices breaks the tiled GPU flow because the division of primitives after the binning pass becomes invalid.
## Use MSAA for anti-aliasing
Tile-based GPUs can store more samples in the same tile. This makes Multi-sample Anti-aliasing (MSAA) efficient on mobile and untethered XR platforms. 2X MSAA value provides a good balance between visual quality and performance.
You can change the MSAA settings in the **Quality** section of the URP Asset.
For more information on MSAA, refer to [Anti-aliasing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/anti-aliasing.html).
## Disable depth priming
Disable depth priming on XR platforms. XR devices have two views, which increases the performance impact from performing the depth pre-pass. 
For untethered XR devices there are no benefits of performing the depth priming. You can obtain similar results using hardware optimization features, such as Low-Resolution-Z (LRZ) or Hidden Surface Removal (HSR).
For information on how to configure or disable depth priming, refer to the [Depth Priming Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html#rendering) property description.
## Disable Opaque texture and Depth texture properties
Disable the **Opaque Texture** and **Depth Texture** properties to improve performance. Enabling those options causes extra texture copy operations, which requires extra GMEM loads.
Refer to the [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html#rendering) section of the URP Asset description for more information on these options.
To identify if your current configuration is using intermediate textures, use the [Render Graph Viewer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-view.html) window.
## Disable SSAO
Screen-Space **Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (SSAO) might have poor performance on mobile and untethered XR devices. 
SSAO in URP requires the depth priming pass, two blur passes to reduce the noise, and an additional blit pass to clean the image. Such passes require several GMEM loads which have a high performance impact on tile-based GPUs.
To disable SSAO:
  1. Select a Universal Renderer asset.
  2. In the **Inspector** window, under the **Renderer Features** section, ensure that **Screen Space Ambient Occlusion** is disabled or absent.


## Disable HDR
HDR rendering has higher precision and improves graphics fidelity, but requires more bits per pixel to process. Disable **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) to reduce memory bandwidth and improve performance.
Most untethered XR devices don’t support HDR rendering.
To disable HDR:
  1. Select a URP Asset.
  2. In the **Inspector** window, in the **Quality** section, clear the **HDR** property.


## Additional resources
  * [Tile-Based Rendering](https://developer.arm.com/documentation/102662/0100/Overview) (Arm)
  * [GPU Tile-Based Rendering](https://developer.qualcomm.com/sites/default/files/docs/adreno-gpu/snapdragon-game-toolkit/gdg/gpu/overview.html#tile-based-rendering) (Qualcomm Adreno)
  * [Post-processing Effects on Mobile: Optimization and Alternatives](https://community.arm.com/arm-community-blogs/b/graphics-gaming-and-vr-blog/posts/post-processing-effects-on-mobile-optimization-and-alternatives) (Arm community)
  * [Tiled Rendering](https://en.wikipedia.org/wiki/Tiled_rendering) (Wikipedia)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)
Adjust settings to improve performance in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/reduce-draw-calls-landing-urp.html)
Optimizing draw calls in URP
