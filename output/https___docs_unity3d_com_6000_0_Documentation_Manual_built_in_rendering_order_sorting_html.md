* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-sorting.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering order in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
  * Set how a camera sorts materials in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-set-queue.html)
Set the render queue for a material in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
Custom rendering in the Built-In Render Pipeline
# Set how a camera sorts materials in the Built-In Render Pipeline
How you change the sorting behavior within a render queue depends on the index of the render queue:
  * For queues with an index up to and including 2500 (Geometry + 500), you can change the opaque sort mode for a **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) by using the [Camera.opaqueSortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-opaqueSortMode.html) API.
  * For queues with an index of 2501 or above, you can change the default transparent sort mode by using the [Rendering.GraphicsSettings-transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsSettings-transparencySortMode.html) API. You can change the transparent sort mode for a Camera by using the [Camera.transparencySortMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-transparencySortMode.html) API.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-set-queue.html)
Set the render queue for a material in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GraphicsCommandBuffers-landing.html)
Custom rendering in the Built-In Render Pipeline
