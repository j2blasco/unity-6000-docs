* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-introduction.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * Introduction to compute shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
Compute shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-create.html)
Create a compute shader
# Introduction to compute shaders
Compute shaders are **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) programs that run on the GPU, outside of the normal rendering pipeline.
They can be used for massively parallel GPGPU algorithms, or to accelerate parts of game rendering. In order to efficiently use them, an in-depth knowledge of GPU architectures and parallel algorithms is often needed; as well as knowledge of [DirectCompute](http://msdn.microsoft.com/en-us/library/windows/desktop/ff476331.aspx), [OpenGL Compute](https://www.khronos.org/opengl/wiki/Compute_Shader), [CUDA](http://en.wikipedia.org/wiki/CUDA), or [OpenCL](http://en.wikipedia.org/wiki/OpenCL).
Compute shaders in Unity closely match [ DirectX](https://en.wikipedia.org/wiki/DirectX) 11 DirectCompute technology. Platforms where compute shaders work:
  * Windows and Windows Store, with a DirectX 11 or DirectX 12 graphics API and Shader Model 5.0 GPU
  * macOS and iOS using [Metal graphics](https://developer.apple.com/metal/) API
  * Android, Linux and Windows platforms with [Vulkan](https://www.khronos.org/vulkan/) API
  * Modern [OpenGL](https://www.opengl.org/) platforms (OpenGL 4.3 on Linux or Windows; OpenGL ES 3.1 on Android). Note that Mac OS X does not support OpenGL 4.3
  * Modern consoles


## Cross-platform support
As with regular shaders, Unity is capable of [translating](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html) compute shaders from HLSL to other shader languages. Therefore, for the easiest cross-platform builds, you should write compute shaders in HLSL. However, there are some factors that need to be considered when doing this.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
Compute shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-create.html)
Create a compute shader
