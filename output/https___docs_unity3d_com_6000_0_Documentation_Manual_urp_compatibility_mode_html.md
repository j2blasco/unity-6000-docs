* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/compatibility-mode.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Compatibility Mode in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html)
Modify URP source code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
Write a Scriptable Render Pass in Compatibility Mode in URP
# Compatibility Mode in URP
If you enable **Compatibility Mode (Render Graph Disabled)** in URP graphics settings, you can write a Scriptable Render Pass without using the [render graph API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html). The setting is in **Project Settings** > **Graphics** > **Pipeline Specific Settings** > **URP** > **Render Graph**.
**Note:** Unity no longer develops or improves the **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) that doesn’t use the [render graph API](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html). Use the render graph API instead when developing new graphics features.
Page | Description  
---|---  
[Write a Scriptable Render Pass in Compatibility Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html) | An example of creating a Scriptable Render Pass in Compatibility Mode.  
[Example of a Scriptable Renderer Feature in Compatibility mode](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/how-to-fullscreen-blit.html) | An example that describes how to create a custom Renderer Feature that performs a full screen **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit).  
[Scriptable Render Pass Compatibility Mode API reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/scriptable-render-pass-reference.html) | Reference for the Scriptable Render Pass API.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/modify-urp-source-code.html)
Modify URP source code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/write-a-scriptable-render-pass.html)
Write a Scriptable Render Pass in Compatibility Mode in URP
