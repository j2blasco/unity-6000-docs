* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-required-directives.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader language reference for the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference.html)
  * Surface Shader required directives reference for the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference.html)
Surface Shader language reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-optional-directives.html)
Surface Shader optional directives reference for the Built-In Render Pipeline
# Surface Shader required directives reference for the Built-In Render Pipeline
  * `surfaceFunction` - which Cg function has surface **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code. The function should have the form of `void surf (Input IN, inout SurfaceOutput o)`, where Input is a structure you have defined. Input should contain any texture coordinates and extra automatic variables needed by surface function.
  * `lightModel` - lighting model to use. Built-in ones are physically based `Standard` and `StandardSpecular`, as well as simple non-physically based `Lambert` (diffuse) and `BlinnPhong` (specular). See [Custom Lighting Models](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderLighting.html) page for how to write your own. 
    * `Standard` lighting model uses `SurfaceOutputStandard` output struct, and matches the Standard (metallic workflow) shader in Unity.
    * `StandardSpecular` lighting model uses `SurfaceOutputStandardSpecular` output struct, and matches the Standard (specular setup) shader in Unity.
    * `Lambert` and `BlinnPhong` lighting models are not physically based (coming from Unity 4.x), but the shaders using them can be faster to render on low-end hardware.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference.html)
Surface Shader language reference for the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/surface-shaders-language-reference-optional-directives.html)
Surface Shader optional directives reference for the Built-In Render Pipeline
