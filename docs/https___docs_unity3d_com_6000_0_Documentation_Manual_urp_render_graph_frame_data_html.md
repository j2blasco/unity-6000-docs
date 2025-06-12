* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * Frame data in the render graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)
Transfer a texture between render passes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
Get data from the current frame in URP
# Frame data in the render graph system in URP
Fetch the textures that the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) creates for the current frame or previous frames, for example a color texture or a depth texture.
**Page** | **Description**  
---|---  
[Get data from the current frame](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html) | Fetch the textures URP creates for the current frame.  
[Get data from previous frames](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-get-previous-frames.html) | To fetch the previous frames the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) rendered, use the `UniversalCameraData.historyManager` API.  
[Add textures to the camera history](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-add-textures-to-camera-history.html) | To add your own texture to the camera history, create a camera history type to store the texture between frames.  
[Get the current framebuffer from GPU memory](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-framebuffer-fetch.html) | To speed up rendering, use the `SetInputAttachment` API to read the frame that Unity has rendered so far.  
[Frame data textures reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data-reference.html) | Explore the textures you can fetch from the current frame or previous frames.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)
Transfer a texture between render passes in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
Get data from the current frame in URP
