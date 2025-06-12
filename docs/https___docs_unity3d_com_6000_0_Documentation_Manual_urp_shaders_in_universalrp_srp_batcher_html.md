* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp-srp-batcher.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * Make a URP shader compatible with the SRP Batcher


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
ShaderLab Pass tags in URP reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/shader-keywords-macros.html)
Shader keywords and macros reference in URP
# Make a URP shader compatible with the SRP Batcher
To ensure that a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) is SRP Batcher compatible:
  * Declare all Material properties in a single CBUFFER called `UnityPerMaterial`.
  * Declare all built-in engine properties, such as `unity_ObjectToWorld` or `unity_WorldTransformParams`, in a single CBUFFER called `UnityPerDraw`.


For more information on the SRP Batcher, refer to the documentation on the [Scriptable Render Pipeline (SRP) Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
ShaderLab Pass tags in URP reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/shader-keywords-macros.html)
Shader keywords and macros reference in URP
