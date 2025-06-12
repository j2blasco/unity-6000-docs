* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransDiffuse.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Transparent Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html)
  * Transparent Diffuse


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
Transparent Vertex-Lit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransSpecular.html)
Transparent Specular
# Transparent Diffuse
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
![Example of a shader using the alpha channel of the main texture, and a diffuse lighting model.](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Shader-TransDiffuse.jpg) Example of a shader using the alpha channel of the main texture, and a diffuse lighting model.
## Transparent Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
This shader can make **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh) geometry partially or fully transparent by reading the alpha channel of the main texture. In the alpha, 0 (black) is completely transparent while 255 (white) is completely opaque. If your main texture does not have an alpha channel, the object will appear completely opaque.
Using transparent objects in your game can be tricky, as there are traditional graphical programming problems that can present sorting issues in your game. For example, if you see odd results when looking through two windows at once, you’re experiencing the classical problem with using transparency. The general rule is to be aware that there are some cases in which one transparent object may be drawn in front of another in an unusual way, especially if the objects are intersecting, enclose each other or are of very different sizes. For this reason, you should use transparent objects if you need them, and try not to let them become excessive. You should also make your designer(s) aware that such sorting problems can occur, and have them prepare to change some design to work around these issues.
## Diffuse Properties
Diffuse computes a simple (Lambertian) lighting model. The lighting on the surface decreases as the angle between it and the light decreases. The lighting depends only on this angle, and does not change as the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) moves or rotates around.
## Performance
Generally, this shader is cheap to render. For more details, please view the [Shader Peformance page](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html).
TransDiffuse
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
Transparent Vertex-Lit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransSpecular.html)
Transparent Specular
