* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedVertexLit.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-landing.html)
  * [Legacy prebuilt shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Built-inShaderGuide.html)
  * [Reflective Shader Family](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveFamily.html)
  * Reflective Normal mapped Vertex-lit


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedUnlit.html)
Reflective Normal Mapped Unlit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
Writing custom shaders
# Reflective Normal mapped Vertex-lit
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
## Reflective Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
This shader will simulate reflective surfaces such as cars, metal objects etc. It requires an environment **Cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) which will define what exactly is reflected. The main texture’s alpha channel defines the strength of reflection on the object’s surface. Any **scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene) lights will add illumination on top of what is reflected.
## Vertex-Lit Properties
**Note.** Unity 5 introduced the [Standard Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) which replaces this shader.
This shader is **Vertex-Lit** , which is one of the simplest shaders. All lights shining on it are rendered in a single pass and calculated at vertices only.
Because it is vertex-lit, it won’t display any pixel-based rendering effects, such as light cookies, normal mapping, or shadows. This shader is also much more sensitive to tesselation of the models. If you put a point light very close to a cube using this shader, the light will only be calculated at the corners. Pixel-lit shaders are much more effective at creating a nice round highlight, independent of tesselation. If that’s an effect you want, you may consider using a pixel-lit shader or increase tesselation of the objects instead.
## Special Properties
This shader is a good alternative to Reflective Normal mapped. If you do not need the object itself to be affected by **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) lights, but do want the reflection to be affected by a **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), this shader is for you. This shader is vertex-lit, so it is rendered more quickly than its Reflective Normal mapped counterpart.
## Performance
Generally, this shader is not expensive to render. For more details, please view the [Shader Peformance page](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-Performance.html).
ReflectiveBumpedVertexLit
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-ReflectiveBumpedUnlit.html)
Reflective Normal Mapped Unlit
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
Writing custom shaders
