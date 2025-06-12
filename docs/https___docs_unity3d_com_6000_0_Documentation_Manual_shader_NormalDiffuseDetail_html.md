* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDiffuseDetail.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Normal Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalFamily.html)
  * Diffuse Detail


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDecal.html)
Decal
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html)
Transparent Shader Family
# Diffuse Detail
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
![Diffuse Detail shader.](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Shader-NormalDiffuseDetail.jpg) Diffuse Detail shader.
## Diffuse Detail Properties
This shader is a version of the regular Diffuse shader with additional data. It allows you to define a second “Detail” texture that will gradually appear as the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) gets closer to it. It can be used on **terrain** The landscape in your scene. A Terrain GameObject adds a large flat plane to your scene and you can use the Terrain’s Inspector window to create a detailed landscape. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/terrain-UsingTerrains.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Terrain), for example. You can use a base low-resolution texture and stretch it over the entire terrain. When the camera gets close the low-resolution texture will get blurry, and we don’t want that. To avoid this effect, create a generic Detail texture that will be tiled over the terrain. This way, when the camera gets close, the additional details appear and the blurry effect is avoided.
The Detail texture is put “on top” of the base texture. Darker colors in the detail texture will darken the main texture and lighter colors will brighten it. Detail texture are usually gray-ish.
## Performance
This shader is pixel-lit, and approximately equivalent to the Diffuse shader. It is marginally more expensive due to additional texture.
NormalDiffuseDetail
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDecal.html)
Decal
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html)
Transparent Shader Family
