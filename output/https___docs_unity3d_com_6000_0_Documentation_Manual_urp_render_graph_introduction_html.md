* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-introduction.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Custom rendering and post-processing in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customizing-urp.html)
  * [Render graph system in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
  * Introduction to the render graph system in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
Render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
Write a render pass using the render graph system in URP
# Introduction to the render graph system in URP
The render graph system is a set of APIs you use to write a [Scriptable Render Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/intro-to-scriptable-render-passes.html) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP).
When you use the render graph API to create a Scriptable Render Pass, you tell URP the following:
  1. The textures or **render textures** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) to use. This stage is the recording stage.
  2. The graphics commands to execute, using the textures or render textures from the recording stage. This stage is the execution stage.


You can then [add your Scriptable Render Pass to the URP renderer](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/custom-rendering-pass-workflow-in-urp.html). Your Scriptable Render Pass becomes part of URP’s internal render graph, which is the sequence of render passes URP steps through each frame. URP automatically optimizes your render pass and the render graph to minimize the number of render passes, and the memory and bandwidth the render passes use.
## How URP optimizes rendering
URP does the following to optimize rendering in the render graph:
  * Merges multiple render passes into a single render pass.
  * Avoids allocating resources the frame doesn’t use.
  * Avoids executing render passes if the final frame doesn’t use their output.
  * Avoids duplicating resources, for example by replacing two texture that have the same properties with a single texture.
  * Automatically synchronizes the compute and graphics GPU command queues.


On mobile platforms that use tile-based deferred rendering (TBDR), URP can also merge multiple render passes into a single native render pass. A native render pass keeps textures in tile memory, rather than copying textures from the GPU to the CPU. As a result, URP uses less memory bandwidth and rendering time.
To check how URP optimizes rendering in your custom render passes, refer to [Analyze a render graph](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-view.html).
## Additional resources
  * [Use frame data](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/accessing-frame-data.html)
  * [Transfer a texture between render passes](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-pass-textures-between-passes.html)
  * [Inject a render pass via scripting](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/customize/inject-render-pass-via-script.html)
  * [Inject a render pass using a Scriptable Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-features/scriptable-renderer-features/inject-a-pass-using-a-scriptable-renderer-feature.html)
  * [The render graph system](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/render-graph-system.html) in the Scriptable Render Pipeline (SRP) Core manual.
  * [CommandBuffer.BeginRenderPass](https://docs.unity3d.com/2023.3/Documentation/ScriptReference/Rendering.CommandBuffer.BeginRenderPass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph.html)
Render graph system in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/render-graph-write-render-pass.html)
Write a render pass using the render graph system in URP
