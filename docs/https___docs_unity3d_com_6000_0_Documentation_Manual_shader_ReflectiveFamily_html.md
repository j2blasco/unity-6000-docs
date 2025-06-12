* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveFamily.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * Reflective Shader Family


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-SelfIllumParallaxSpecular.html)
Self-Illuminated Parallax Specular
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveVertexLit.html)
Reflective Vertex-Lit
# Reflective Shader Family
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces these **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
**Reflective** shaders will allow you to use a **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) which will be reflected on your **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh). You can also define areas of more or less reflectivity on your object through the alpha channel of the **Base** texture. High reflectivity is a great effect for glosses, oils, chrome, etc. Low reflectivity can add effect for metals, liquid surfaces, or video monitors.
## [Reflective Vertex-Lit](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveVertexLit.html)
![shader-ReflectiveVertexLit](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflVertex.jpg) shader-ReflectiveVertexLit
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveVertexLit.html)
## [Reflective Diffuse](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveDiffuse.html)
![shader-ReflectiveDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflDiffuse.jpg) shader-ReflectiveDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveDiffuse.html)
## [Reflective Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveSpecular.html)
![shader-ReflectiveSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflSpec.jpg) shader-ReflectiveSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map


**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveSpecular.html)
## [Reflective Normal mapped](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedDiffuse.html)
![shader-ReflectiveBumpedDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflBump.jpg) shader-ReflectiveBumpedDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), no alpha channel required


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedDiffuse.html)
## [Reflective Normal Mapped Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedSpecular.html)
![shader-ReflectiveBumpedSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflBumpSpec.jpg) shader-ReflectiveBumpedSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas & Specular Map combined
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required


**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedSpecular.html)
## [Reflective Parallax](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveParallaxDiffuse.html)
![shader-ReflectiveParallaxDiffuse](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflParallaxBump.jpg) shader-ReflectiveParallaxDiffuse
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveParallaxDiffuse.html)
## [Reflective Parallax Specular](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveParallaxSpecular.html)
![shader-ReflectiveParallaxSpecular](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflParallaxBumpSpec.jpg) shader-ReflectiveParallaxSpecular
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas & Specular Map
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , with alpha channel for Parallax Depth


**Note:** One consideration for this shader is that the **Base** texture’s alpha channel will double as both the reflective areas and the Specular Map.
[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveParallaxSpecular.html)
## [Reflective Normal mapped Unlit](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedUnlit.html)
![shader-ReflectiveBumpedUnlit](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflBumpUnlit.jpg) shader-ReflectiveBumpedUnlit
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedUnlit.html)
## [Reflective Normal mapped Vertex-Lit](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedVertexLit.html)
![shader-ReflectiveBumpedVertexLit](https://docs.unity3d.com/6000.0/Documentation/uploads/Shaders/Thumb-ReflBumpVertex.jpg) shader-ReflectiveBumpedVertexLit
**Assets needed:**
  * One **Base** texture with alpha channel for defining reflective areas
  * One **Reflection** Cubemap for Reflection Map
  * One **Normal map** , no alpha channel required


[» More details](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedVertexLit.html)
ReflectiveFamily
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-SelfIllumParallaxSpecular.html)
Self-Illuminated Parallax Specular
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveVertexLit.html)
Reflective Vertex-Lit
