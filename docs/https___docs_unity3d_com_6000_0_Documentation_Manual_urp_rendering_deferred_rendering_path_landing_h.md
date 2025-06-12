* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * Deferred rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html)
Forward and Forward+ rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html)
Introduction to the deferred rendering path
# Deferred rendering path in URP
![Scene rendered with the Deferred Rendering Path](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-deferred/deferred-intro-image.png) Scene rendered with the Deferred Rendering Path
Resources for using the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), which has no limit on the number of lights that can affect an opaque **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject).
**Page** | **Description**  
---|---  
[Introduction to the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html) | Learn about how the Deferred rendering path works, and its limitations.  
[Render passes in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html) | Learn about the sequence of render pass events in the Deferred rendering path.  
[G-buffer layout in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html) | Understand how Unity stores material attributes in the geometry buffer (G-buffer) in the Deferred rendering path.  
[Enable accurate G-buffer normals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html) | Configure how Unity encodes normals when it stores them in the G-buffer.  
[Make a shader compatible with the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html) | Use the `LightMode` tag in a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) to make the shader compatible with the Deferred rendering path.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html)
Forward and Forward+ rendering paths in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html)
Introduction to the deferred rendering path
