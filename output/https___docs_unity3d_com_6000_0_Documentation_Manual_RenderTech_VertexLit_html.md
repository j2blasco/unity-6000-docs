* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-VertexLit.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-paths.html)
  * Legacy Vertex Lit rendering path in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)
Deferred rendering path in the Built-In Render Pipeline 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
Rendering order in the Built-In Render Pipeline
# Legacy Vertex Lit rendering path in the Built-In Render Pipeline
This page describes details of the Vertex Lit [rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in Unity’s Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
The Vertex Lit path generally renders each object in one pass, with lighting from all lights calculated for each vertex.
It’s the fastest rendering path and has the widest hardware support.
Since all lighting is calculated at the vertex level, this rendering path does not support most per-pixel effects: shadows, normal mapping, light cookies, and highly detailed specular highlights are not supported.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)
Deferred rendering path in the Built-In Render Pipeline 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-order-landing.html)
Rendering order in the Built-In Render Pipeline
