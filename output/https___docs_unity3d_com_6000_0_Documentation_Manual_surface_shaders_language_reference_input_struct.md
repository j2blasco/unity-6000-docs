* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-input-structure.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader language reference for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference.html)
  * Surface Shader input structure reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-optional-directives.html)
Surface Shader optional directives reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
Shader methods in the Built-In Render Pipeline
# Surface Shader input structure reference for the Built-In Render Pipeline
The input structure `Input` generally has any texture coordinates needed by the **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader). Texture coordinates must be named “`uv`” followed by texture name (or start it with “`uv2`” to use second texture coordinate set).
Additional values that can be put into Input structure:
  * `float3 viewDir` - contains view direction, for computing Parallax effects, rim lighting etc.
  * `float4` with `COLOR` semantic - contains interpolated per-vertex color.
  * `float4 screenPos` - contains screen space position for reflection or screenspace effects. Note that this is not suitable for [GrabPass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html); you need to compute custom UV yourself using `ComputeGrabScreenPos` function.
  * `float3 worldPos` - contains world space position.
  * `float3 worldRefl` - contains world reflection vector _if**surface shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) does not write to o.Normal_. See Reflect-Diffuse shader for example.
  * `float3 worldNormal` - contains world normal vector _if surface shader does not write to o.Normal_.
  * `float3 worldRefl; INTERNAL_DATA` - contains world reflection vector _if surface shader writes to o.Normal_. To get the reflection vector based on per-pixel **normal map** A type of Bump Map texture that allows you to add surface detail such as bumps, grooves, and scratches to a model which catch the light as if they are represented by real geometry.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Normalmap), use `WorldReflectionVector (IN, o.Normal)`. See Reflect-Bumped shader for example.
  * `float3 worldNormal; INTERNAL_DATA` - contains world normal vector _if surface shader writes to o.Normal_. To get the normal vector based on per-pixel normal map, use `WorldNormalVector (IN, o.Normal)`.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-optional-directives.html)
Surface Shader optional directives reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
Shader methods in the Built-In Render Pipeline
