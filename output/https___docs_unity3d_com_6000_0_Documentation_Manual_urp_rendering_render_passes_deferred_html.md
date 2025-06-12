* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * Render passes in the Deferred rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html)
Introduction to the deferred rendering path
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html)
G-buffer layout in the Deferred rendering path in URP
# Render passes in the Deferred rendering path in URP
The following table lists the render passes the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) uses.
**Render event** | **Render pass that occurs after the render event** | **Description**  
---|---|---  
**BeforeRendering** | - | -  
**BeforeRenderingShadows** | - | -  
**AfterRenderingShadows** | - | -  
**BeforeRenderingPrePasses** |  **DepthPrepass** , or **DepthPrepass** and **DepthNormalPrepass**. | Render depth and normal textures in a prepass, for materials that Unity renders in a Forward pass.  
**AfterRenderingPrePasses** | - | -  
**BeforeRenderingGbuffer** | **GBufferPass** | Render the G-Buffer, then copy the G-Buffer depth texture.  
**AfterRenderingGbuffer** | **SSAO** | Calculate the screen space **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (SSAO) texture. Unity calculates this here only if you [enable SSAO](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html), and disable **After Opaque**.  
**BeforeRenderingDeferredLights** | **Deferred Pass** | Deferred rendering. Unity uses the SSAO texture during this render pass, if it was created.  
**AfterRenderingDeferredLights** | - | -  
**BeforeRenderingOpaques** | - | Render opaque forward-only materials.  
**AfterRenderingOpaques** | - | Calculate and blend the screen space ambient occlusion (SSAO) texture. Unity calculates this here only if you [enable SSAO](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html), and enable **After Opaque**.  
**BeforeRenderingSkybox** | - | -  
**AfterRenderingSkybox** | - | -  
**BeforeRenderingTransparents** | - | -  
**AfterRenderingTransparents** | - | -  
**BeforeRenderingPostProcessing** | - | -  
**AfterRenderingPostProcessing** | - | -  
**AfterRendering** | - | -  
For the full list of render events, and injection points for custom render passes, refer to [Injection points reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html).
## Source code reference
The following table lists the files that contain code related to the Deferred rendering path, located in the `com.unity.render-pipelines.universal` folder.
**File path** | **Description**  
---|---  
`Runtime/DeferredLights.cs` | Defines the main class that handles the Deferred rendering path.  
`Runtime/Passes/GBufferPass.cs` | Implements a `ScriptableRenderPass` for the G-buffer rendering pass.  
`Runtime/Passes/DeferredPass.cs` | Implements a `ScriptableRenderPass` for the **Deferred shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) pass.  
`Shaders/Utils/StencilDeferred.shader` | Defines the rendering behavior for stencil-based deferred lighting when using the Deferred rendering path.  
`Shaders/Utils/ClusterDeferred.shader` | Defines the rendering behavior for cluster-based deferred lighting when using the Deferred+ rendering path.  
`ShaderLibrary/GBufferInput.hlsl` | Contains utility functions for reading material properties from the G-buffers in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).  
`ShaderLibrary/GBufferOutput.hlsl` | Contains utility functions for writing material properties to the G-buffers in URP.  
## Additional resources
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html)
Introduction to the deferred rendering path
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html)
G-buffer layout in the Deferred rendering path in URP
