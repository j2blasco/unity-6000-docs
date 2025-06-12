* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/configure-for-better-performance.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * Configure for better performance in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html)
Known issues in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
Graphics quality settings in URP
# Configure for better performance in URP
You can disable or change Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) settings and features that have a large performance impact. This helps you get better performance for your project, especially on lower-end platforms.
Depending on your project or the platforms you target, one or all of the following might have the biggest effect:
  * Which **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) you choose
  * How much memory URP uses
  * Processing time on the CPU
  * Processing time on the GPU


You can use the [Unity Profiler](https://docs.unity3d.com/Manual/Profiler.html) or a GPU **profiler** A window that helps you to optimize your game. It shows how much time is spent in the various areas of your game. For example, it can report the percentage of time spent rendering, animating, or in your game logic. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Profiler.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Profiler) such as [RenderDoc](https://docs.unity3d.com/Manual/RenderDocIntegration.html) or [Xcode](https://docs.unity3d.com/Manual/XcodeFrameDebuggerIntegration.html) to measure the effect of each setting on the performance of your project.
You might not be able to disable some features if your project needs them.
## Choose a rendering path
Refer to [Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html) for more information about the three rendering paths in URP, and the performance effects and limitations of each one.
## Reduce how much memory URP uses
You can do the following in the [URP Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html):
  * Disable **Depth Texture** unless you need it (for example, if you use a shader that samples scene depth), so that URP doesn’t store a depth texture unless it’s needed.
  * Disable **Opaque Texture** , so that URP doesn’t store a snapshot of the opaques in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) unless it needs to.
  * If you use the Deferred rendering path, disable **Use Rendering Layers** so that URP doesn’t create an extra render target. 
  * Disable **High Dynamic Range (HDR)** if you don’t need it, so that URP doesn’t do **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) calculations. If you need HDR, set **HDR Precision** to **32 Bit**.
  * Reduce **Main Light > Shadow Resolution**, to lower the resolution of the shadow map for the main light.
  * If you use additional lights, reduce **Additional Lights > Shadow Atlas Resolution**, to lower the resolution of the shadow map for additional lights.
  * Disable **Light Cookies** if you don’t need them, or reduce **Cookie Atlas Resolution** and **Cookie Atlas Format**.
  * On lower-end mobile platforms, set **Store Actions** to **Auto** or **Discard** , so that URP doesn’t use memory bandwidth to copy the render targets from each pass into and out of memory.


In the [Universal Renderer asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html), you can set **Intermediate Texture** to **Auto** , so that Unity only renders using an intermediate texture when necessary. This might also reduce how much GPU memory bandwidth URP uses. Use the [Frame Debugger](https://docs.unity3d.com/Manual/frame-debugger-window.html) to check if URP removes the intermediate texture when you change this setting.
You can also do the following:
  * Minimize the use of the Decal Renderer Feature, because URP creates an additional render pass to render decals. This also reduces processing time on the CPU and GPU. Refer to [Decal Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html) for more information.
  * [Strip shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-stripping.html) for features you don’t use.


## Reduce processing time on the CPU
You can do the following in the URP Asset:
  * Set **Volume Update Mode** to **Via Scripting** , so that URP doesn’t update volumes every frame. You need to update volumes manually using an API such as [UpdateVolumeStack](https://docs.unity3d.com/Packages/com.unity.render-pipelines.universal@latest/index.html?subfolder=/api/UnityEngine.Rendering.Universal.CameraExtensions.html#UnityEngine_Rendering_Universal_CameraExtensions_UpdateVolumeStack_UnityEngine_Camera_).
  * On lower-end mobile platforms, if you use [Reflection Probes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/reflection-probes.html)A rendering component that captures a spherical view of its surroundings in all directions, rather like a camera. The captured image is then stored as a Cubemap that can be used by objects with reflective materials. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ReflectionProbe.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ReflectionProbe), disable **Probe Blending** and **Box Projection**.
  * In the **Shadows** section, reduce **Max Distance** so that URP processes fewer objects in the shadow pass. This also reduces processing time on the GPU.
  * In the **Shadows** section, reduce **Cascade Count** to reduce the number of render passes. This also reduces processing time on the GPU.
  * In the **Additional Lights** section, disable **Cast Shadows**. This also reduces processing time on the GPU and how much memory URP uses.


Each **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) in the Scene requires resources for URP culling and rendering. To optimize URP for better performance, minimize the number of cameras you use. This also reduces processing time on the GPU.
## Reduce processing time on the GPU
You can do the following in the URP Asset:
  * Reduce or disable **Anti-aliasing (MSAA)** , so that URP doesn’t use memory bandwidth to copy frame buffer attachments into and out of memory. This also reduces how much memory URP uses.
  * Disable ****Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) Holes**.
  * Enable **SRP Batcher** , so that URP reduces the GPU setup between draw calls and makes material data persistent in GPU memory. Check your **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) are compatible with the [SRP Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html) first. This also reduces processing time on the CPU.
  * On lower-end mobile platforms, disable ****LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) Cross Fade**, so that URP doesn’t use alpha testing to fade level of detail (LOD) meshes in and out.
  * Set **Additional Lights** to **Disabled** , or **Per Vertex** if you use the **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path. This reduces the work URP does to calculate lighting. This also reduces processing time on the CPU if you set to **Disabled**.
  * Disable **Soft Shadows** , or enable **Soft Shadows** but reduce **Quality**.


You can do the following in the Universal Renderer asset:
  * Enable **Native RenderPass** if you use Vulkan, Metal or DirectX 12 graphics APIs, so that URP automatically reduces how often it copies **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) into and out of memory. This also reduces how much memory URP uses.
  * If you use the Forward or Forward+ rendering path, set **Depth Priming Mode** to **Auto** or **Forced** for PC and console platforms, or **Disabled** for mobile platforms. On PC and console platforms, this makes URP create and use depth textures to avoid running **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) shaders on obscured pixels.
  * Set **Depth Texture Mode** to **After Transparents** , so that URP avoids switching render targets between the opaque pass and the transparent pass.


You can also do the following:
  * Avoid use of the [Complex Lit shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shader-complex-lit.html), which has complex lighting calculations. If you use the Complex Lit shader, disable **Clear Coat**.
  * On lower-end mobile platforms, use the [Baked Lit shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/baked-lit-shader.html) for static objects and the [Simple Lit shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/simple-lit-shader.html) for dynamic objects.
  * If you use Screen Space Ambient Occlusion (SSAO), refer to [Ambient Occlusion](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html)A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) for more information about settings that have a large performance impact.


## Additional resources
  * [Understand performance in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/understand-performance.html)
  * [Optimize for better performance](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/optimize-for-better-performance.html)
  * [Introduction to the Universal Render Pipeline for advanced Unity creators](https://resources.unity.com/games/introduction-universal-render-pipeline-for-advanced-unity-creators)
  * [Performance optimization for high-end graphics on PC and console](https://unity.com/how-to/performance-optimization-high-end-graphics)
  * [Making Alba: How to build a performant open-world game](https://www.youtube.com/watch?v=YOtDVv5-0A4)
  * [Post-processing in URP for mobile devices](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/integration-with-post-processing.html).
  * [Optimizing lighting for a healthy frame rate](https://unity.com/how-to/advanced/optimize-lighting-mobile-games)


Refer to the following for more information on the settings:
  * [Deferred Rendering Path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * [Forward rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html)
  * [Universal Render Pipeline Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/universalrp-asset.html)
  * [Universal Renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/known-issues.html)
Known issues in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-quality-settings-landing.html)
Graphics quality settings in URP
