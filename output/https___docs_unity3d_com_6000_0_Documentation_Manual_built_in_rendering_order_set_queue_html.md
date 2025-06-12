* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-set-queue.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering order in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
  * Set the render queue for a material in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order.html)
Render queues and sorting behaviours in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-sorting.html)
Set how a camera sorts materials in the Built-In Render Pipeline
# Set the render queue for a material in the Built-In Render Pipeline
By default, Unity places objects in the render queue specified in their Unity **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). You define this value using the `[Queue]` [SubShader tag](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
You can override this value on a per-material basis.
In the Unity Editor, you can do this in the [material Inspector](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html) by setting the **Render Queue** property. In a C# script, you can do this by setting the value of [Material.renderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material-renderQueue.html) using the [Rendering.RenderQueue](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderQueue.html) enum.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order.html)
Render queues and sorting behaviours in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-sorting.html)
Set how a camera sorts materials in the Built-In Render Pipeline
