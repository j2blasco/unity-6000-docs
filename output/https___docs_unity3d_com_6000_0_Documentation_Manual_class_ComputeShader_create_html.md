* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-create.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * Create a compute shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-introduction.html)
Introduction to compute shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-hlsl-shaderlab.html)
Use HLSL and ShaderLab in a compute shader
# Create a compute shader
Similar to [shader assets](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html), compute **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) assets are files in your project. with a _.compute_ file extension. They are written in DirectX 11 style [HLSL](http://msdn.microsoft.com/en-us/library/windows/desktop/bb509561.aspx) language, with a minimal number of #pragma compilation directives to indicate which functions to compile as compute shader kernels.
## Check if a platform supports compute shaders
Compute shader support can be queried at runtime using [SystemInfo.supportsComputeShaders](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-supportsComputeShaders.html).
## Create a compute shader asset
Here’s a basic example of a compute shader file, which fills the output texture with red:
```
// test.compute

#pragma kernel FillWithRed

RWTexture2D<float4> res;

[numthreads(1,1,1)]
void FillWithRed (uint3 dtid : SV_DispatchThreadID)
{
    res[dtid.xy] = float4(1,0,0,1);
}

```

The language is standard DX11 HLSL, with an additional `#pragma kernel FillWithRed` directive. One compute shader Asset file must contain at least one`compute kernel` that can be invoked, and that function is indicated by the `#pragma directive`. There can be more kernels in the file; just add multiple `#pragma kernel` lines.
When using multiple `#pragma kernel` lines, note that comments of the style `// text` are not permitted on the same line as the `#pragma kernel` directives, and cause compilation errors if used.
The `#pragma kernel` line can optionally be followed by a number of preprocessor macros to define while compiling that kernel, for example:
```
#pragma kernel KernelOne SOME_DEFINE DEFINE_WITH_VALUE=1337
#pragma kernel KernelTwo OTHER_DEFINE
// ...

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-introduction.html)
Introduction to compute shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-hlsl-shaderlab.html)
Use HLSL and ShaderLab in a compute shader
