* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-render-pipeline.html)
  * [Rendering paths in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-rendering-paths.html)
  * Forward rendering path in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)
Introduction to rendering paths in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)
Deferred rendering path in the Built-In Render Pipeline 
# Forward rendering path in the Built-In Render Pipeline
The Forward **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) renders each **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in one or more render passes, depending on the lights that affect the object.
Lights themselves are also treated differently by the **Forward rendering** path, depending on their settings and intensity. For more information, refer to [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html).
## Render passes
For each GameObject, Unity first renders the Base Pass, which renders the following:
  * One per-pixel light that affects the GameObject.
  * All the per-vertex and spherical harmonics (SH) lights that affect the GameObject.
  * **Lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) data for the GameObject
  * Ambient lighting
  * Emissive lighting
  * Shadows from directional lights


**Note:** Lightmapped objects don’t receive lighting from SH lights.
Unity then renders one Additional Pass for each per-pixel light that affects the GameObject. Unity doesn’t render shadows for these lights.
## Additional resources
  * [Introduction to rendering paths](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-paths-introduction.html)
  * [Per-pixel and per-vertex lights](https://docs.unity3d.com/6000.0/Documentation/Manual/PerPixelLights-BuiltIn.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)
Introduction to rendering paths in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)
Deferred rendering path in the Built-In Render Pipeline 
