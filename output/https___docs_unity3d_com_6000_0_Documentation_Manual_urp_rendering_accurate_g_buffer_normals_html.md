* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/accurate-g-buffer-normals.html

  * [Rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/rendering-and-post-processing.html)
  * [Render pipelines](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)
  * [Using the Universal Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/universal-render-pipeline.html)
  * [Get started with URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/introduction-landing.html)
  * [Universal Render Pipeline fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-concepts.html)
  * [Rendering paths in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering-paths-landing.html)
  * [Deferred rendering path in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/deferred-rendering-path-landing.html)
  * Enable accurate G-buffer normals in the Deferred rendering path in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html)
G-buffer layout in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
Make a shader compatible with the Deferred rendering path in URP
# Enable accurate G-buffer normals in the Deferred rendering path in URP
In the Deferred **rendering path** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath), Unity stores normals in the G-buffer.
By default, Unity encodes each normal in the RGB channel of a normal texture, using 8 bits each for x, y and z. The values are quantized with the loss of accuracy. This increases performance, especially on mobile GPUs, but might lead to color banding artifacts on smooth surfaces.
To improve the quality of the normals, you can enable the **Accurate G-buffer normals** property in the Universal Renderer asset. Follow these steps:
  1. In the **Project** window, select the Universal Renderer asset.
  2. In the ****Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector)** window, go to the **Renderer** section.
  3. Set **Accurate G-buffer normals** to **On**.


When you set **Accurate G-buffer normals** to **On** , Unity uses octahedron encoding. The values of normal vectors are more accurate, but the encoding and decoding operations put extra load on the GPU. The precision of the encoded normal vectors is similar to the precision of the sampled values in the **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path.
The following illustration shows the visual difference between the two options when the **Camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) is very close to the **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject):
![Accurate G-buffer normals, visual difference between the two options.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/rendering-deferred/difference-accurate-g-buffer-normals-on-off.png) Accurate G-buffer normals, visual difference between the two options.
This option does not support the following:
  * Decal normal blending when used with the [Screen Space decal technique](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal.html).  

  * **Terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain) blending with more than four Terrain layers, because normals in different layers encoded using octahedron encoding cannot be blended together because of the bitwise nature of the encoding (2 x 12 bits).


## Additional resources
  * [G-buffer layout in the Deferred rendering path](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html)
  * [Normals](https://docs.unity3d.com/6000.0/Documentation/Manual/StandardShaderMaterialParameterNormalMapSurfaceNormals.html)The direction perpendicular to the surface of a mesh, represented by a Vector. Unity uses normals to determine object orientation and apply shading. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-vectors.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normal)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/g-buffer-layout.html)
G-buffer layout in the Deferred rendering path in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/rendering/make-shader-compatible-with-deferred.html)
Make a shader compatible with the Deferred rendering path in URP
