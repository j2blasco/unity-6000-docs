* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * Usage and Performance of Built-in Shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
Legacy prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalFamily.html)
Normal Shader Family
# Usage and Performance of Built-in Shaders
Shaders in Unity are used through **Materials** An asset that defines how a surface should be rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Material), which essentially combine **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code with parameters like textures. An in-depth explanation of the Shader/Material relationship can be read [here](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html).
Material properties will appear in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) when either the Material itself or a **GameObject** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject) that uses the Material is selected. The Material Inspector looks like this:
Each Material will look a little different in the Inspector, depending on the specific shader it is using. The shader iself determines what kind of properties will be available to adjust in the Inspector. Material inspector is described in detail in [Material reference page](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Material.html). Remember that a shader is implemented through a Material. So while the shader defines the properties that will be shown in the Inspector, each Material actually contains the adjusted data from sliders, colors, and textures. The most important thing to remember about this is that a single shader can be used in multiple Materials, but a single Material cannot use multiple shaders.
## Shader names
Changing the name of a Legacy Shader can affect its functionality. This is because prior to Unity 5.0, some of the functionality of a shader was determined by its path and name. This is still how the Legacy Shaders work. For more information, see [Legacy shader names](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html#legacyShaderNames)
## Performance Considerations
There are a number of factors that can affect the overall performance of your game. This page will talk specifically about the performance considerations for [Built-in Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html). Performance of a shader mostly depends on two things: shader itself and which [Rendering Path](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) is used by the project or specific **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera). For performance tips when writing your own shaders, see [ShaderLab Shader Performance](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPerformance.html) page.
### Rendering Paths and shader performance
From the rendering paths Unity supports, [Deferred Shading](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)A rendering path in the Built-in Render Pipeline that places no limit on the number of Lights that can affect a GameObject. All Lights are evaluated per-pixel, which means that they all interact correctly with normal maps and so on. Additionally, all Lights can have cookies and shadows. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-DeferredShading.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Deferredshading) and [Vertex Lit](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-VertexLit.html) paths have the most predictable performance. In Deferred shading, each object is generally drawn once, no matter what lights are affecting it. Similarly, in Vertex Lit each object is generally drawn once. So then, the performance differences in shaders mostly depend on how many textures they use and what calculations they do.
### Shader Performance in Forward rendering path
In [Forward](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html) rendering path, performance of a shader depends on **both** the shader itself and the lights in the **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene). The following section explains the details. There are two basic categories of shaders from a performance perspective, **Vertex-Lit** , and **Pixel-Lit**.
**Vertex-Lit** shaders in **Forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) path are always cheaper than Pixel-Lit shaders. These shaders work by calculating lighting based on the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) vertices, using all lights at once. Because of this, no matter how many lights are shining on the object, it will only have to be drawn once.
**Pixel-Lit** shaders calculate final lighting at each **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) that is drawn. Because of this, the object has to be drawn once to get the ambient & main directional light, and once for each additional light that is shining on it. Thus the formula is N rendering passes, where N is the final number of pixel lights shining on the object. This increases the load on the CPU to process and send off commands to the graphics card, and on the graphics card to process the vertices and draw the pixels. The size of the Pixel-lit object on the screen will also affect the speed at which it is drawn. The larger the object, the slower it will be drawn.
So pixel lit shaders come at performance cost, but that cost allows for some spectacular effects: shadows, normal-mapping, good looking specular highlights and light cookies, just to name a few.
Remember that lights can be forced into a pixel (“important”) or vertex/SH (“not important”) mode. Any vertex lights shining on a Pixel-Lit shader will be calculated based on the object’s vertices or whole object, and will not add to the rendering cost or visual effects that are associated with pixel lights.
## General shader performance
Out of [Built-in Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html), they come roughly in this order of increasing complexity:
  * **Unlit**. This is just a texture, not affected by any lighting.
  * **VertexLit**.
  * **Diffuse**.
  * **Normal mapped**. This is a bit more expensive than Diffuse: it adds one more texture (normal map), and a couple of shader instructions.
  * **Specular**. This adds specular highlight calculation.
  * **Normal Mapped Specular**. Again, this is a bit more expensive than Specular.
  * **Parallax Normal mapped**. This adds parallax normal-mapping calculation.
  * **Parallax Normal Mapped Specular**. This adds both parallax normal-mapping and specular highlight calculation.


## Mobile simplified shaders
Additionally, Unity has several simplified shaders targeted at mobile platforms, under “Mobile” category. These shaders work on other platforms as well, so if you can live with their simplifications (e.g. approximate specular, no per-material color support etc.), try using them!
To see the specific simplifications that have been made for each shader, look at the `.shader` files from the “built-in shaders” package and the information is listed at the top of the file in some comments.
Some examples of changes that are common across the Mobile shaders are:
  * There is no material color or main color for tinting the shader.
  * For the shaders taking a **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), the tiling and offset from the base texture is used.
  * The particle shaders do not support `AlphaTest` or `ColorMask`.
  * Limited feature and lighting support - e.g. some shaders only support one directional light.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
Legacy prebuilt shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalFamily.html)
Normal Shader Family
