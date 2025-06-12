* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-crossplatform.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Compute shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html)
  * Writing compute shaders for multiple platforms


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-run.html)
Run a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPerformance.html)
Optimize shaders
# Writing compute shaders for multiple platforms
## Cross-platform best practices
DirectX 11 (DX11) supports many actions that are not supported on other platforms (such as [Metal](https://developer.apple.com/metal/) or [OpenGL ES](https://www.opengl.org/)). Therefore, you should always ensure your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) has well-defined behavior on platforms that offer less support, rather than only on DX11. Here are few things to consider:
  * Out-of-bounds memory accesses are bad. DX11 might consistently return zero when reading, and read some writes without issues, but platforms that offer less support might crash the GPU when doing this. Watch out for DX11-specific hacks, buffer sizes not matching with multiple of your thread group size, trying to read neighboring data elements from the beginning or end of the buffer, and similar incompatibilities.
  * Initialize your resources. The contents of new buffers and Textures are undefined. Some platforms might provide all zeroes, but on others, there could be anything including NaNs. 
  * Bind all the resources your compute shader declares. Even if you know for sure that the shader does not use resources in its current state because of branching, you must still ensure a resource is bound to it.


## Platform-specific differences
  * [Metal](https://developer.apple.com/metal/) (for iOS and tvOS platforms) does not support atomic operations on Textures. Metal also does not support `GetDimensions` queries on buffers. Pass the buffer size info as constant to the shader if needed.
  * [OpenGL ES](https://www.opengl.org/) 3.1 (for (Android, iOS, tvOS platforms) only guarantees support for 4 compute buffers at a time. Actual implementations typically support more, but in general if developing for OpenGL ES, you should consider grouping related data in structs rather than having each data item in its own buffer.
  * OpenGL (ES) and [Vulkan](https://www.vulkan.org/) require an image format qualifier for `RWTextures<T>` that are not write-only.  
Unity derives this qualifier from the type T in the angle-brackets. The format qualifier needs to match the [GraphicsFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormat.html)/[RenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html) of the [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) that is bound to the RWTexture. The following table maps Unity RenderTexture GraphicsFormats and RenderTextureFormats to their corresponding HLSL type and image format qualifier:

GraphicsFormat | RenderTextureFormat | HLSL type | GLSL image format qualifier  
---|---|---|---  
R32G32B32A32_SFloat | ARGBFloat | float4 | rgba32f  
R16G16B16A16_SFloat | ARGBHalf | min16float4/half4 | rgba16f  
R32G32_SFloat | RGFloat | float2 | rg32f  
R16G16_SFloat | RGHalf | min16float2/half2 | rg16f  
B10G11R11_UFloatPack32 | RGB111110Float | min10float3 | r11f_g11f_b10f  
R32_SFloat | RFloat | float | r32f  
R16_SFloat | RHalf | min16float/half | r16f  
R16G16B16A16_UNorm | ARGB64 | unorm min16float4/half4 | rgba16  
A2B10G10R10_UNormPack32 | ARGB2101010 | unorm min10float4 | rgb10_a2  
R8G8B8A8_UNorm | ARGB32 | unorm float4 | rgba8  
R16G16_UNorm | RG32 | unorm min16float2/half2 | rg16  
R8G8_UNorm | RG16 | unorm float2 | rg8  
R16_UNorm | R16 | unorm min16float/half | r16  
R8_UNorm | R8 | unorm float | r8  
R16G16B16A16_SNorm | unsupported | snorm min16float4/half4 | rgba16_snorm  
R8G8B8A8_SNorm | unsupported | snorm float4 | rgba8_snorm  
R16G16_SNorm | unsupported | snorm min16float2/half2 | rg16_snorm  
R8G8_SNorm | unsupported | snorm float2 | rg8_snorm  
R16_SNorm | unsupported | snorm min16float/half | r16_snorm  
R8_SNorm | unsupported | snorm float | r8_snorm  
R32G32B32A32_SInt | ARGBInt | int4 | rgba32i  
R16G16B16A16_SInt | unsupported | min16int4 | rgba16i  
R8G8B8A8_SInt | unsupported | min12int4 | rgba8i  
R32G32_SInt | RGInt | int2 | rg32i  
R16G16_SInt | unsupported | min16int2 | rg16i  
R8G8_SInt | unsupported | min12int2 | rg8i  
R32_SInt | RInt | int | r32i  
R16_SInt | unsupported | min16int | r16i  
R8_SInt | unsupported | min12int | r8i  
R32G32B32A32_UInt | unsupported | uint4 | rgba32i  
R16G16B16A16_UInt | RGBAUShort | min16uint4 | rgba16ui  
R8G8B8A8_UInt | unsupported | unsupported | rgba8ui  
R32G32_UInt | unsupported | uint2 | rg32ui  
R16G16_UInt | unsupported | min16uint2 | rg16ui  
R8G8_UInt | unsupported | unsupported | rg8ui  
R32_UInt | unsupported | uint | r32ui  
R16_UInt | unsupported | min16uint | r16ui  
R8_UInt | unsupported | unsupported | r8ui  
A2B10G10R10_UIntPack32 | unsupported | unsupported | rgb10_a2ui  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-run.html)
Run a compute shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPerformance.html)
Optimize shaders
