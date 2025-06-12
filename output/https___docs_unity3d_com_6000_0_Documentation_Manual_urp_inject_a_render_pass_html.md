* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/inject-a-render-pass.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Adding a Scriptable Render Pass to the frame rendering loop in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-viewer-reference.html)
Render Graph Viewer window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
Injecting a render pass via a Scriptable Renderer Feature in URP
# Adding a Scriptable Render Pass to the frame rendering loop in URP
Add a custom render pass to the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) frame rendering loop by creating a Scriptable Renderer Feature, or using the `RenderPipelineManager` API.
Page | Description  
---|---  
[Injecting a render pass via a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html) | Write a class that inherits `ScriptableRendererFeature`, and use it to creates an instance of the custom render pass you created, and insert the custom render pass into the rendering pipeline.  
[Inject a render pass via scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html) | Use the `RenderPipelineManager` API to insert a custom render pass into the rendering pipeline.  
[Restrict a render pass to a scene area](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/restrict-render-pass-scene-area.html) | Enable a custom rendering effect only if the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is inside a volume in a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene).  
[Injection points reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/custom-pass-injection-points.html) | URP contains multiple injection points that let you inject render passes at different points in the frame rendering loop.  
## Additional resources
  * [Custom post-processing](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing/custom-post-processing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-viewer-reference.html)
Render Graph Viewer window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-renderer-features-landing.html)
Injecting a render pass via a Scriptable Renderer Feature in URP
