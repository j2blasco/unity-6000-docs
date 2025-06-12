* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Lighting in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/lighting-landing.html)
  * [Shadows in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/Shadows-in-URP.html)
  * [Screen space ambient occlusion (SSAO) in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
  * Introduction to screen space ambient occlusion in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
Screen space ambient occlusion (SSAO) in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/add-ssao-renderer-feature-to-renderer.html)
Add a Screen Space Ambient Occlusion Renderer Feature to a URP Renderer
# Introduction to screen space ambient occlusion in URP
The Screen Space **Ambient Occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) effect darkens creases, holes, intersections and surfaces that are close to each other in real-time. In the real world, such areas tend to block out or occlude **ambient light** Light that doesn’t come from any specific direction, and contributes equal light in all directions to the Scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientlight), so they appear darker.
URP implements the Screen Space Ambient Occlusion (SSAO) effect as a [Renderer Feature](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-renderer-feature.html). It works with every **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) provides as well as any custom opaque Shader Graphs you create.
**Note** : The SSAO effect is a Renderer Feature and works independently from the **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing) effects in URP. This effect does not depend on or interact with Volumes.
The following images show a **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) with the Ambient Occlusion effect turned off, on, and only the Ambient Occlusion texture.
![Scene with Ambient Occlusion effect turned off.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/scene-ssao-off.png) Scene with Ambient Occlusion effect turned off. ![Scene with Ambient Occlusion effect turned on.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/scene-ssao-on.png) Scene with Ambient Occlusion effect turned on. ![Scene with only the Ambient Occlusion texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/post-proc/ssao/scene-ssao-only-ao.png) Scene with only the Ambient Occlusion texture.
## Implementation details
The SSAO Renderer Feature uses normal vectors for calculating how exposed each point on a surface is to ambient lighting.
URP 10.0 implements the `DepthNormals` Pass block that generates the the normal texture `_CameraNormalsTexture` for the current frame. By default, the SSAO Renderer Feature uses this texture to calculate Ambient Occlusion values.
If you implement your custom SRP and if you do not want to implement the `DepthNormals` Pass block in your shaders, you can use the SSAO Renderer Feature and set its **Source** property to **Depth**. In this case, Unity does not use the `DepthNormals` Pass to generate the normal vectors, it reconstructs the normal vectors using the depth texture instead.
Selecting the option **Depth** in the **Source** property enables the **Normal Quality** property. The options in this property (Low, Medium, and High) determine the number of samples of the depth texture that Unity takes when reconstructing the normal vector from the depth texture. The number of samples per quality level: Low: 1, Medium: 5, High: 9.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/post-processing-ssao-landing.html)
Screen space ambient occlusion (SSAO) in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/add-ssao-renderer-feature-to-renderer.html)
Add a Screen Space Ambient Occlusion Renderer Feature to a URP Renderer
