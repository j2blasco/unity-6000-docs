* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-detect.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Fixing hitches or stalls](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
  * [Asynchronous shader compilation in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
  * Detect asynchronous shader compilation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
Enable or disable asynchronous shader compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html)
Troubleshooting asynchronous shader compilation
# Detect asynchronous shader compilation
You can use C# APIs to monitor the state of asynchronous **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) compilation, and perform operations when this state changes.
This is most likely useful in [advanced rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html); if the placeholder shader pollutes your generated data, you can wait until compilation is complete, discard the polluted data, and regenerate a new set with the correct shader variants.
If you already know which material you are interested in, you can use `ShaderUtil.IsPassCompiled` to check the compilation status of the shader variant. When the status changes _Uncompiled_ to _Compiled_ , compilation is complete.
If you do not know which material you are interested in, or if you are interested in more than one material, you can use `ShaderUtil.anythingCompiling` to detect whether Unity is compiling any shader variants asynchronously. When this changes from `true` to `false`, all current compilation is complete.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
Enable or disable asynchronous shader compilation
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-avoid-cyan-placeholder-shaders.html)
Troubleshooting asynchronous shader compilation
