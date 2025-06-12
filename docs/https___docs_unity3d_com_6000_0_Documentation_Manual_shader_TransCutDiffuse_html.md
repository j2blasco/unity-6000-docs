* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutDiffuse.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Transparent Cutout Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentCutoutFamily.html)
  * Transparent Cutout Diffuse


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
Transparent Cutout Vertex-Lit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutSpecular.html)
Transparent Cutout Specular
# Transparent Cutout Diffuse
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
![Transparent Cutout Diffuse shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Shader-TransCutoutDiffuse.jpg) Transparent Cutout Diffuse shader.
## Transparent Cutout Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
Cutout shader is an alternative way of displaying transparent objects. Differences between Cutout and regular [Transparent](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html) shaders are:
  * This shader cannot have partially transparent areas. Everything will be either fully opaque or fully transparent.
  * Objects using this shader can cast and receive shadows!
  * The graphical sorting problems normally associated with Transparent shaders do not occur when using this shader.


This shader uses an alpha channel contained in the **Base** Texture to determine the transparent areas. If the alpha contains a blend between transparent and opaque areas, you can manually determine the cutoff point for the which areas will be shown. You change this cutoff by adjusting the **Alpha Cutoff** slider.
## Diffuse Properties
Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) moves or rotates around.
## Performance
Generally, this shader is cheap to render. For more details, please view the [Shader Peformance page](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html).
TransCutDiffuse
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
Transparent Cutout Vertex-Lit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutSpecular.html)
Transparent Cutout Specular
