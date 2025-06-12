* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransparentCutoutFamily.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * Transparent Cutout Shader Family


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxSpecular.html)
Transparent Parallax Specular
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
Transparent Cutout Vertex-Lit
# Transparent Cutout Shader Family
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces these **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
The Transparent Cutout shaders are used for objects that have fully opaque and fully transparent parts (no partial transparency). Things like chain fences, trees, grass, etc.
## [Transparent Cutout Vertex-Lit](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
![shader-TransCutVertexLit](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransCutoutVertex.jpg) shader-TransCutVertexLit
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
## [Transparent Cutout Diffuse](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutDiffuse.html)
![shader-TransCutDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransCutoutDiffuse.jpg) shader-TransCutDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutDiffuse.html)
## [Transparent Cutout Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutSpecular.html)
![shader-TransCutSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransCutoutSpec.jpg) shader-TransCutSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map


**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutSpecular.html)
## [Transparent Cutout Bumped](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
![shader-TransCutBumpedDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransCutoutBump.jpg) shader-TransCutBumpedDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for Transparency Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap) normal map, no alpha channel required


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedDiffuse.html)
## [Transparent Cutout Bumped Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedSpecular.html)
![shader-TransCutBumpedSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-TransCutoutBumpSpec.jpg) shader-TransCutBumpedSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for combined Transparency Map/Specular Map
  * One **Normal map** normal map, no alpha channel required


**Note:** One limitation of this shader is that the **Base** texture’s alpha channel doubles as a Specular Map for the Specular shaders in this family.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutBumpedSpecular.html)
TransparentCutoutFamily
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransParallaxSpecular.html)
Transparent Parallax Specular
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-TransCutVertexLit.html)
Transparent Cutout Vertex-Lit
