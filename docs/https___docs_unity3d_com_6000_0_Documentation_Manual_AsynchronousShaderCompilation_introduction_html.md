* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Fixing hitches or stalls](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reduce-stalling.html)
  * [Asynchronous shader compilation in the Editor](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
  * Introduction to asynchronous shader compilation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
Asynchronous shader compilation in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
Enable or disable asynchronous shader compilation
# Introduction to asynchronous shader compilation
Shader objects can contain of hundreds or thousands of [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant). If the Editor compiled all variants when loading a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object, the import process would be very slow. Instead, the Editor compiles shader variants on-demand, the first time it encounters them.
Compiling these shader variants can cause the Editor to stall for milliseconds or even seconds, depending on the graphics API and the complexity of the **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject). To avoid these stalls, you can use asynchronous shader compilation to compile the shader variants in the background, and use placeholder Shader objects in the meantime.
## How asynchronous shader compilation works
Asynchronous shader compilation works like this:
  1. When the Editor first encounters an uncompiled shader variant, it adds the shader variant to a compilation queue on a job thread. The progress bar in the bottom right corner of the Editor shows the status of the compilation queue.
  2. While the shader variant is loading, Editor renders the geometry with a placeholder shader, which appears as a plain cyan color.
  3. When the Editor has finished compiling the shader variant, it renders the geometry using the shader variant.

![Unity renders shader variants that are still compiling with a cyan dummy Shader until compilation has finished. The bottom right progress bar indicates the compilation queue progress.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/cyan_dummy_shaders.png) Unity renders shader variants that are still compiling with a cyan dummy Shader until compilation has finished. The bottom right progress bar indicates the compilation queue progress.
## Exceptions
The following exceptions apply:
  * If you draw geometry using [`DrawProcedural`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.DrawProcedural.html) or [`CommandBuffer.DrawProcedural`](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.DrawProcedural.html), the Editor doesn’t use a placeholder shader. Instead, the Editor just skips rendering this geometry until it has compiled the shader variant.
  * The Unity Editor does not use asynchronous shader compilation with **Blit** A shorthand term for “bit block transfer”. A blit operation is the process of transferring blocks of data from one place in memory to another.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#blit) operations. This is to guarantee correct output in the most common use cases.


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html)
Asynchronous shader compilation in the Editor
[](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation-enable-or-disable.html)
Enable or disable asynchronous shader compilation
