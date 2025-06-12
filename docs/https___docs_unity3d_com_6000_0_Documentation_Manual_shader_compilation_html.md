* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Troubleshooting shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-troubleshooting.html)
  * [Reducing the size or number of shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
  * Shader compilation


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
Reducing the size or number of shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
Reducing shader variants
# Shader compilation
Every time you build your project, the Unity Editor compiles all the shaders that your build requires: every required **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) variant, for every required graphics API.
When you’re working in the Unity Editor, the Editor does not compile everything upfront. This is because compiling every variant for every graphics API can take a very long time. 
Instead, Unity Editor does this:
  * When it imports a shader asset, it performs some minimal processing (such as Surface Shader generation).
  * When it needs to show a shader variant, it checks the `Library/ShaderCache` folder.
  * If it finds a previously compiled shader variant that uses identicial source code, it uses that.
  * If it does not find a match, it compiles the required shader variant and saves the result to the cache. 
    * **Note:** If you enable [Asynchronous shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/AsynchronousShaderCompilation.html), it does this in the background and shows a placeholder shader in the meantime.


Shader compilation is carried out using a process called `UnityShaderCompiler`. Multiple `UnityShaderCompiler` processes can be started (generally one per CPU core in your machine), so that at player build time shader compilation can be done in parallel. While the Editor is not compiling shaders, the compiler processes do nothing and do not consume computer resources.
The shader cache folder can become quite large, if you have a lot of shaders that are changed often. It is safe to delete this folder; it just causes Unity to recompile the shader variants.
At player build time, all the “not yet compiled” shader variants are compiled, so that they are in the game data even if the editor did not happen to use them.
## Different shader compilers
Different platforms use different shader compilers for [shader program](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html) compilation as follows:
  * Platforms that use DirectX use Microsoft’s FXC HLSL compiler.
  * Platforms that use OpenGL (Core & ES) use Microsoft’s FXC HLSL compiler, followed by bytecode translation into GLSL using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Platforms that use Metal use Microsoft’s FXC HLSL compiler, followed by bytecode translation into Metal, using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Platforms that use Vulkan use Microsoft’s FXC HLSL compiler, followed by bytecode translation into SPIR-V, using [HLSLcc](https://github.com/Unity-Technologies/HLSLcc).
  * Other platforms, such as console platforms, use their respective compilers.
  * [Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) use HLSL and [MojoShader](https://icculus.org/mojoshader/) for code generation analysis step.


You can configure various shader compiler settings using [pragma directives](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html).
## The Caching Shader Preprocessor
Shader compilation involves several steps. One of the first steps is preprocessing. During this step, a program called a **preprocessor** prepares the shader source code for the compiler.
In previous versions of Unity, the Editor used the preprocessor provided by the shader compiler for the current platform. Now, Unity uses its own preprocessor, also called the Caching Shader Preprocessor.
The Caching Shader Preprocessor is optimized for faster shader import and compilation. It works by caching intermediate preprocessing data, so the Editor only needs to parse include files when their contents change, which makes compiling multiple variants of the same shader more efficient.
For detailed information on the differences between the Caching Shader Preprocessor and the previous behavior, see the Unity forum: [New shader preprocessor](https://forum.unity.com/threads/new-shader-preprocessor.790328/).
## Build time stripping
While building the game, Unity can detect that some of the internal shader variants are not used by the game, and exclude (“strip”) them from build data. For more information, see [Shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)A verion of a shader program that Unity generates according to a specific combination of shader keywords and their status. A Shader object can contain multiple shader variants. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shadervariant).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-reducing.html)
Reducing the size or number of shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-variants-landing.html)
Reducing shader variants
