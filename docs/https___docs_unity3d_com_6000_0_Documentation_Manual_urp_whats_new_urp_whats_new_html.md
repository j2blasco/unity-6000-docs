* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/whats-new/urp-whats-new.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * What's new in URP 17 (Unity 6)


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/requirements.html)
Requirements and compatibility for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
Get started with URP
# What’s new in URP 17 (Unity 6)
This section contains information about new features, improvements, and issues fixed in URP 17.
For a complete list of changes made in URP 17, refer to the [Changelog](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/changelog/CHANGELOG.html).
## Features
This section contains the overview of the new features in this release.
### Render graph system
In this release, Unity introduces the [render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html) system. The render graph system is a framework built on top of the Scriptable **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (SRP) API. This system improves the way you customize and maintain the render pipeline.
The render graph system reduces the amount of memory URP uses and makes memory management more efficient. The render graph system only allocates resources the frame actually uses, and you no longer need to write complicated logic to handle resource allocation and account for rare worst-case scenarios. The render graph system also generates correct synchronization points between the compute and graphics queues, which reduces frame time.
The [Render Graph Viewer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-viewer-reference.html) lets you visualize how render passes use frame resources, and debug the rendering process.
For more information about the render graph system, refer to the [render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html) documentation.
### Alpha Processing setting in post-processing
URP 17 adds an **Alpha Processing** setting (**URP Asset** > **Post-processing** > **Alpha Processing**). If you enable this setting, URP renders the post-processing output into a render texture with an alpha channel. In previous versions, URP discarded the alpha channel by replacing alpha values with 1.
The render target requires a format with the alpha channel. The camera color buffer format must be RGBA8 for SDR (HDR off) and RGBA16F for HDR (64-bits). You can configure the format using the settings in **URP Asset** > **Quality**.
Example use cases for this feature:
  * Render in-game UI, such as a head-up display. You can render multiple **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) with different **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) configurations and compose the final output using the alpha channel.
  * Render a character customization screen, where Unity renders a background interface and a 3D character with different post-processing effects and blends them using the alpha channel.
  * **XR** An umbrella term encompassing Virtual Reality (VR), Augmented Reality (AR) and Mixed Reality (MR) applications. Devices supporting these forms of interactive applications can be referred to as XR devices. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/XR.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#XR) applications that need to support video pass-through.


### Reduce rendering work on the CPU
URP 17 contains new features that let you speed up the rendering process by moving certain tasks to the GPU and reducing the workload on the CPU.
#### GPU Resident Drawer
URP 17 includes a new rendering system called the **GPU Resident Drawer**.
This system automatically uses the [BatchRendererGroup API](https://docs.unity3d.com/Manual/batch-renderer-group.html) to draw **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) with GPU instancing, which reduces the number of draw calls and frees CPU processing time.
For more information on the GPU Resident Drawer, refer to the section [Reduce rendering work on the CPU](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/reduce-rendering-work-on-cpu.html).
#### GPU occlusion culling
When using GPU **occlusion culling** A process that disables rendering GameObjects that are hidden (occluded) from the view of the camera. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/OcclusionCulling.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Occlusionculling), Unity uses the GPU instead of the CPU to exclude objects from rendering when they’re occluded behind other objects. Unity uses this information to speed up rendering in **scenes** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) that have a lot of occlusion.
For more information on GPU occlusion culling, refer to the section [Reduce rendering work on the CPU](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/gpu-culling.html).
### Foveated rendering in the Forward+ Rendering Path
The Forward+ **Rendering Path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) now supports foveated rendering.
### Camera history API
This release contains the [camera history API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.UniversalCameraHistory.html) which lets you access per-camera history textures and use them in custom render passes. History textures are the color and depth textures that Unity rendered for each **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in previous frames.
You can use history textures for rendering algorithms that use frame data from one or multiple previous frames.
URP implements per-camera color and depth texture history and history access for custom render passes.
### Mipmap Streaming section in the Rendering Debugger
The [Rendering Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/rendering-debugger.html) now contains a **Mipmap Streaming** section. This section lets you inspect the texture streaming activity.
### Spatial Temporal Post-Processing (STP)
Spatial Temporal Post-Processing (STP) optimizes GPU performance and enhances visual quality by upscaling frames Unity renders at a lower resolution. STP works on desktop platforms, consoles, and mobile devices that support compute **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
To enable STP, in the active **URP Asset** , select **Quality** > **Upscaling Filter** > **Spatial Temporal Post-Processing (STP)**. 
## Improvements
This section contains the overview of the major improvements in this release.
### Adaptive Probe Volumes (APV)
This release contains the following improvements to [Adaptive Probe Volumes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes.html):
  * [APV Lighting Scenario Blending](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-bakedifferentlightingsetups.html).
  * [APV sky occlusion support](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-skyocclusion.html).
  * [APV disk streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/probevolumes-streaming.html).


### Volume framework enhancements
This release comes with CPU performance optimizations of the volume framework on all platforms, especially mobile platforms. You can now set global volume default values and override them in quality settings.
### 8192 shadow texture resolution
The **Shadow Resolution** property now contains the `8192` option for the Main Light and Additional Lights.
### Use the URP Config package to change render pipeline settings
The [URP Config package](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/URP-Config-Package.html) lets you change certain render pipeline settings that are not available in the Editor interface.
For example, you can [change the maximum number of visible lights](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-plus-rendering-path-limitations.html).
### The URP documentation has moved to the Unity Manual
The documentation for the Universal Render Pipeline in Unity 6 has moved from the separate URP documentation site to the main Unity Manual. We’ve restructured URP-specific and general graphics pages so they focus more on user outcomes. The purpose of this change is to improve the discoverability of the URP documentation and reader experience.
Links to pages on the separate URP site now redirect to the relocated pages in the main manual (or an equivalent).
The [URP scripting API](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@17.0/api/index.html) documentation remains on the separate website.
## Issues resolved
For a complete list of issues resolved in URP 17, refer to the [Changelog](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/changelog/CHANGELOG.html).
## Known issues
For information on the known issues in URP 17, refer to the section [Known issues](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/requirements.html)
Requirements and compatibility for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
Get started with URP
