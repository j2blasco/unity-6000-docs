* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * Textures in the Render Graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
Write a render pass using the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html)
Create a texture in the render graph system in URP
# Textures in the Render Graph system in URP
How to access and use textures in a custom render pass in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).
Page | Description  
---|---  
[Create a texture in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html) | Create a texture in a render graph system render pass.  
[Import a texture into the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-import-a-texture.html) | To create or use a **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) in a render graph system render pass, use the `RTHandle` API.  
[Use a texture in a render pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-read-write-texture.html) | To allow a render pass to read from or write to a texture, use the render graph system API to set the texture as an input or output.  
[Transfer a texture between passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html) | Set a texture as a global texture, or add the texture to the frame data.  
## Additional resources
  * [Use frame data](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
  * The **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) examples in the [URP RenderGraph Samples](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/package-sample-urp-package-samples.html)
  * [Example of a complete Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
Write a render pass using the render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-create-a-texture.html)
Create a texture in the render graph system in URP
