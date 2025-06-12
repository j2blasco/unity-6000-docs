* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/decal-shader.html

  * [Visual effects](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects.html)
  * [Decals and projectors](https://docs.unity3d.com/6000.0/Documentation/Manual/visual-effects-decals.html)
  * [Decals in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-landing.html)
  * Create a decal via a Decal Projector in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html)
Create a decal via a Decal Renderer Feature in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-reference.html)
Decal Renderer Feature reference
# Create a decal via a Decal Projector in URP
The [Decal Projector](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-projector-reference.html) component can project a Material as a decal if the Material uses a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) Graph with the Decal Material type.
![Shader Graph with the Decal Material type](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-shader-graph-material-type.png)  
_Shader Graph with the Decal Material type_
URP contains the pre-built Decal Shader (`Shader Graphs/Decal`).
![Decal Material properties.](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-material-properties.png)  
_Decal Material properties and advanced options._
##  Create custom Decal shaders
The pre-built `Shader Graphs/Decal` shader serves as a simple example. You can create your own decal shaders that render decals in a way that suits your project best.
To create a custom decal Shader Graph, select the **Decal** value in Material property of the shader target.
![Shader Graph, Decal Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-shader-graph-material-type.png) Shader Graph, Decal Material
Enabling one of the following properties override the equivalent Lit Shader property on the surface of the Material.
To improve performance, pack data for different surface properties into a single texture. This way the shader performs fewer samples and Unity stores fewer textures.
For example, the following Shader Graph uses a **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) and a mask map to drive all properties in the shader. This decal is used for the damaged tarmac effect, and a hardcoded roughness value of 0 suites the use case.
![Decal Graph](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-graph.png) Decal Graph
The shader samples the mask and uses the color for setting the Ambient Occlusion values (Red channel), smoothness values (Green channel), Emission intensity values (Blue channel), and alpha values for the entire decal. Decals are often blended using single alpha values for all properties. The following image shows the mask map for the example tarmac cracks:  
![Decal Mask](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/decal/decal-mask.png)  
_Example of mask map that packs Ambient Occlusion, Smoothness, Emission, and alpha values of a decal atlas into a single texture._
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-create.html)
Create a decal via a Decal Renderer Feature in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/renderer-feature-decal-reference.html)
Decal Renderer Feature reference
