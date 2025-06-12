* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * Render graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/blit-overview.html)
Blit in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html)
Introduction to the render graph system in URP
# Render graph system in URP
The render graph system is a set of APIs you use to create a [Scriptable Render Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html).
Page | Description  
---|---  
[Introduction to the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html) | What the render graph system is, and how it optimizes rendering.  
[Write a render pass using the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html) | Write a Scriptable Render Pass using the render graph APIs.  
[Textures in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/working-with-textures.html) | Access and use textures in your render passes, and how to **blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit).  
[Frame data in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-frame-data.html) | Get the textures URP creates for the current frame and use them in your render passes.  
[Draw objects in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-draw-objects-in-a-pass.html) | Draw objects in the render graph system using the `RendererList` API.  
[Compute shaders in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-compute-shader.html) | Create a render pass that runs a compute **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).  
[Analyze a render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-view.html) | Check a render graph using the Render Graph Viewer, Rendering Debugger, or Frame Debugger.  
[Optimize a render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-optimize.html) | To optimize a render graph, merge or reduce the number of render passes.  
[Use Compatibility Mode APIs in the render graph system](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-unsafe-pass.html) | To use Compatibility Mode APIs in the render graph system, such as `SetRenderTarget`, use the render graph `UnSafePass` API.  
[Render Graph Viewer window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-viewer-reference.html) | Reference for the **Render Graph Viewer** window.  
## Additional resources
  * [Frame Debugger](https://docs.unity3d.com/2023.3/Documentation/Manual/frame-debugger-window.html)
  * [Example of a complete Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/create-custom-renderer-feature.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/blit-overview.html)
Blit in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html)
Introduction to the render graph system in URP
