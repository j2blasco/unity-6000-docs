* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Color](https://docs.unity3d.com/6000.0/Documentation/Manual/graphics-color.html)
  * [High dynamic range (HDR)](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-landing.html)
  * [Color space and HDR in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp-landing.html)
  * HDR in the Built-in Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp-landing.html)
Color space and HDR in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-in-urp.html)
HDR
# HDR in the Built-in Render Pipeline
Support for **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) in the Built-In **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) depends on the **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in use.
## Forward Rendering
In the **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path, a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) only supports HDR if you have a **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effect on the Camera. This is due to performance considerations. If you have no post-processing effect on the Camera, the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) will be rendered directly to the back buffer where HDR is not supported.
## Deferred Shading
In the **Deferred Shading** A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) rendering path, when HDR is enabled for a Camera the lighting buffer is also allocated as a floating point buffer. This reduces banding in the lighting buffer.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/hdr-birp-landing.html)
Color space and HDR in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/hdr-in-urp.html)
HDR
