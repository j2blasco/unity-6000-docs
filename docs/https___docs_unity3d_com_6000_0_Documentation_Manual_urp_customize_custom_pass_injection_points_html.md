* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Adding a Scriptable Render Pass to the frame rendering loop in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html)
  * Injection points reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html)
Restrict a render pass to a scene area in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html)
Modify URP source code
# Injection points reference for URP
URP contains multiple injection points that let you inject render passes into the frame rendering loop and execute them upon different events.
Injection points give a custom render pass access to URP buffers. A render pass has read and write access to all buffers at each injection point.
Unity provides the following events in the rendering loop. You can use these events to inject your custom passes.
**Injection point** | **Description**  
---|---  
BeforeRendering | Executes a `ScriptableRenderPass` instance before rendering any other passes in the pipeline for the current **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). Camera matrices and stereo rendering are not setup at this point. You can use this injection point to draw to custom input textures used later in the pipeline, for example, LUT textures.  
BeforeRenderingShadows | Executes a `ScriptableRenderPass` instance before rendering shadow maps (**MainLightShadow** , **AdditionalLightsShadow** passes).  
Camera matrices and stereo rendering are not set up at this point.  
AfterRenderingShadows | Executes a `ScriptableRenderPass` instance after rendering shadow maps (**MainLightShadow** , **AdditionalLightsShadow** passes).  
Camera matrices and stereo rendering are not set up this point.  
BeforeRenderingPrePasses | Executes a `ScriptableRenderPass` instance before rendering prepasses (**DepthPrepass** , **DepthNormalPrepass** passes).  
Camera matrices and stereo rendering are already set up at this point.  
AfterRenderingPrePasses | Executes a `ScriptableRenderPass` instance after rendering prepasses (**DepthPrepass** , **DepthNormalPrepass** passes).  
Camera matrices and stereo rendering are set up at this point.  
BeforeRenderingGbuffer | Executes a `ScriptableRenderPass` instance before rendering the **GBuffer** pass.  
AfterRenderingGbuffer | Executes a `ScriptableRenderPass` instance after rendering the **GBuffer** pass.  
BeforeRenderingDeferredLights | Executes a `ScriptableRenderPass` instance before rendering the **Deferred** pass.  
AfterRenderingDeferredLights | Executes a `ScriptableRenderPass` instance after rendering the **Deferred** pass.  
BeforeRenderingOpaques | Executes a `ScriptableRenderPass` instance before rendering opaque objects (**DrawOpaqueObjects** pass).  
AfterRenderingOpaques | Executes a `ScriptableRenderPass` instance after rendering opaque objects (**DrawOpaqueObjects** pass).  
BeforeRenderingSkybox | Executes a `ScriptableRenderPass` instance before rendering the **skybox** A special type of Material used to represent skies. Usually six-sided. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/sky-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Skybox) (**Camera.RenderSkybox** pass).  
AfterRenderingSkybox | Executes a `ScriptableRenderPass` instance after rendering the skybox (**Camera.RenderSkybox** pass).  
BeforeRenderingTransparents | Executes a `ScriptableRenderPass` instance before rendering transparent objects (**DrawTransparentObjects** pass).  
AfterRenderingTransparents | Executes a `ScriptableRenderPass` instance after rendering transparent objects (**DrawTransparentObjects** pass).  
BeforeRenderingPostProcessing | Executes a `ScriptableRenderPass` instance before rendering **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects (**Render PostProcessing Effects** pass).  
AfterRenderingPostProcessing | Executes a `ScriptableRenderPass` instance after rendering post-processing effects but before the final **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit), post-processing anti-aliasing effects, and color grading.  
AfterRendering | Executes `ScriptableRenderPass` instance after rendering all other passes.  
The following diagram shows the passes and the flow of frame resources in a URP frame:
![URP frame rendering graph and pases](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/customizing-urp/urp-frame-graph-passes.png) URP frame rendering graph and pases
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html)
Restrict a render pass to a scene area in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html)
Modify URP source code
