* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-introduction.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * Introduction to the deferred rendering path


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
Render passes in the Deferred rendering path in URP
# Introduction to the deferred rendering path
The Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) in the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) first creates a G-buffer, which is a set of textures that stores information about the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene), then uses the information to light all the **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) at once.
## Terrain blending accuracy
In Deferred+, the **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) might look different because of the way Unity combines terrain layers.
  * In the **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path, Unity uses multi-pass rendering to calculate lighting for four layers at a time, and alpha-blends after each set of four layers.
  * In the Deferred rendering path, Unity combines terrain layers in the G-buffer pass using hardware blending, four layers at a time, then calculates lighting only once during the Deferred rendering pass.


The approach in the Deferred rendering path limits how correct the combination of property values is. For example, **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) normals cannot be correctly combined using the alpha blend equation alone, because one terrain layer might contain coarse terrain detail while another layer might contain fine detail. Averaging or summing normals results in a loss of accuracy.
![Terrain layers rendered with the Forward rendering path](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-deferred/terrain-layers-forward.png) Terrain layers rendered with the Forward rendering path ![Terrain layers rendered with the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-deferred/terrain-layers-deferred.png) Terrain layers rendered with the Deferred rendering path
## Default shader compatibility
Unity uses a forward render pass to render the following default **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader):
  * Complex Lit: The lighting model is too complex to fit into the G-buffer.
  * Baked Lit or Lit: There’s no realtime lighting, so Unity renders the data into the Emissive/GI/Lighting field of the G-buffer. This is quicker than using a deferred render pass.


## Additional resources
  * [Introduction to rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-introduction-urp.html)
  * [Render passes in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
  * [Make a shader compatible with Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/render-passes-deferred.html)
Render passes in the Deferred rendering path in URP
