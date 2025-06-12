* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * Introduction to rendering paths in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
Rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-comparison.html)
Choose a rendering path in URP
# Introduction to rendering paths in URP
You can select one of the following **rendering paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP):
  * Forward
  * Forward+
  * Deferred


Each rendering path affects how Unity draws and lights objects, which affects lighting results and rendering time. The effects depend on the platform you build for. 
For more information about choosing a rendering path, refer to [Choose a rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-comparison.html).
## Rendering path requirements in URP
**Feature** | **Forward** | **Forward+** | **Deferred**  
---|---|---|---  
Minimum **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) model | 2.0 | 2.0 | 4.5  
OpenGL and OpenGL ES support | Yes | Yes | No  
## Additional resources
  * [Understanding Rendering Paths](https://learn.unity.com/tutorial/understanding-rendering-paths) on the Unity Learn site
  * [Unity LTS 2022 Release Live!](https://www.youtube.com/watch?v=oUQapNQgpRI&t=8183s) - a Unity YouTube video that demonstrates the Forward+ rendering path


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
Rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-comparison.html)
Choose a rendering path in URP
