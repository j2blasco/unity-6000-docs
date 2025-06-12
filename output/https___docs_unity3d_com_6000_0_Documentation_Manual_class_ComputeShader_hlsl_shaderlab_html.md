* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-hlsl-shaderlab.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * Use HLSL and ShaderLab in a compute shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-create.html)
Create a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-run.html)
Run a compute shader
# Use HLSL and ShaderLab in a compute shader
## Use texture samplers
Textures and samplers aren’t separate objects in Unity, so to use them in compute **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) you must follow one of the following Unity-specific rules:
  * Use the same name as the Texture name, with `sampler` at the beginning (for example, `Texture2D MyTex`; `SamplerState samplerMyTex`). In this case, the sampler is initialized to that Texture’s filter/wrap/aniso settings.
  * Use a predefined sampler. For this, the name has to have `Linear` or `Point` (for filter mode) and `Clamp` or `Repeat` (for wrap mode). For example, `SamplerState MyLinearClampSampler` creates a sampler that has Linear filter mode and Clamp wrap mode.


For more information, see documentation on [Sampler States](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SamplerStates.html).
## Use keywords
You can use keywords to produce multiple variants of compute shaders, the same as you can for graphics shaders.
For general information on variants, see [Shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant). For information on how to implement these features in compute shaders, see [Declaring and using shader keywords in HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html) and the [ComputeShader API documentation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeShader.html).
## HLSL-only or GLSL-only compute shaders
Usually, compute shader files are written in [HLSL](https://en.wikipedia.org/wiki/High-Level_Shading_Language), and compiled or translated into all necessary platforms automatically. However, it is possible to either prevent translation to other languages (that is, only keep HLSL platforms), or to write [GLSL](https://en.wikipedia.org/wiki/OpenGL_Shading_Language) compute code manually.
The following information only applies to HLSL-only or GLSL-only compute shaders, not cross-platform builds. This is because this information can result in compute shader source being excluded from some platforms. 
  * Compute shader source surrounded by `CGPROGRAM` and `ENDCG` keywords is not processed for non-HLSL platforms.
  * Compute shader source surrounded by `GLSLPROGRAM` and `ENDGLSL` keywords is treated as GLSL source, and emitted verbatim. This only works when targeting OpenGL or GLSL platforms. You should also note that while automatically translated shaders follow HLSL data layout on buffers, manually written GLSL shaders follow GLSL layout rules.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-create.html)
Create a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-run.html)
Run a compute shader
