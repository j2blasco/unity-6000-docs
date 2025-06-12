* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentFamily.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * Transparent Shader Family


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDiffuseDetail.html)
Diffuse Detail
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
Transparent Vertex-Lit
# Transparent Shader Family
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces these **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
The Transparent shaders are used for fully- or semi-transparent objects. Using the alpha channel of the **Base** texture, you can determine areas of the object which can be more or less transparent than others. This can create a great effect for glass, HUD interfaces, or sci-fi effects.
## [Transparent Vertex-Lit](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
![shader-TransVertexLit](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransVertex.jpg) shader-TransVertexLit
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
## [Transparent Diffuse](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransDiffuse.html)
![shader-TransDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransDiffuse.jpg) shader-TransDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransDiffuse.html)
## [Transparent Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransSpecular.html)
![shader-TransSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransSpec.jpg) shader-TransSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map


**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransSpecular.html)
## [Transparent Normal mapped](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransBumpedDiffuse.html)
![shader-TransBumpedDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransBump.jpg) shader-TransBumpedDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) normal map, no alpha channel required


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransBumpedDiffuse.html)
## [Transparent Normal mapped Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransBumpedSpecular.html)
![shader-TransBumpedSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransBumpSpec.jpg) shader-TransBumpedSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map, no alpha channel required


**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransBumpedSpecular.html)
## [Transparent Parallax](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxDiffuse.html)
![shader-TransParallaxDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransParallaxBump.jpg) shader-TransParallaxDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** normal map with alpha channel for Parallax Depth


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxDiffuse.html)
## [Transparent Parallax Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxSpecular.html)
![shader-TransParallaxSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransParallaxBumpSpec.jpg) shader-TransParallaxSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map with alpha channel for Parallax Depth


**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxSpecular.html)
TransparentFamily
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDiffuseDetail.html)
Diffuse Detail
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransVertexLit.html)
Transparent Vertex-Lit
