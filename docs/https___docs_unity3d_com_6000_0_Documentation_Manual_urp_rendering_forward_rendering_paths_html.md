* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/forward-rendering-paths.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * Forward and Forward+ rendering paths in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-set.html)
Set the rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
Deferred rendering path in URP
# Forward and Forward+ rendering paths in URP
The Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) has the following forward **rendering paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath):
  * Forward
  * Forward+


## Forward rendering path
The **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path is the default rendering path in URP. Unity lights each **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) in turn, and there’s a limit to the number of lights that can affect each GameObject. 
## Forward+ rendering path
The Forward+ rendering path is similar to the Forward rendering path, but there’s no limit to the number of lights that can affect each GameObject. There’s still a limit on the number of lights visible per-camera.
Using the Forward+ rendering path reduces the number of lights Unity calculates for each GameObject. Unity divides the screen into tiles, then identifies which lights affect which tiles. When Unity calculates the lighting for a GameObject, it uses only the lights that affect the tile the GameObject is in. 
![An example of the Lighting Complexity Debug Draw Mode using the Forward+ rendering path. Each grid square is a tile, and each value represents the number of lights affecting the tile.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/lighting-complexity.png) An example of the Lighting Complexity [Debug Draw Mode](https://docs.unity3d.com/6000.0/Documentation/Manual/GIVis.html) using the Forward+ rendering path. Each grid square is a tile, and each value represents the number of lights affecting the tile.
Unity ignores the following settings if you select the Forward+ rendering path:
  * **Additional Lights** in the URP Asset.
  * **Main Light** in the URP Asset.
  * **Additional Lights** > **Per Object Limit** in the URP Asset.
  * **Reflection Probes** > **Probe Blending** in the Lighting window.


## Additional resources
  * [Light limits in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting/light-limits-in-urp.html)
  * [Introduction to rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-set.html)
Set the rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
Deferred rendering path in URP
