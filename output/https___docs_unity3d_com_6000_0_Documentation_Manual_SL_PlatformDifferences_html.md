* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * Writing shaders for different graphics APIs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html)
Pass information to the shader compiler in HLSL
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GLSLShaderPrograms.html)
GLSL in Unity
# Writing shaders for different graphics APIs
In some cases, there are differences in how graphics rendering behaves between different graphics APIs. Most of the time the Unity Editor hides the differences, but there are some situations where the Editor cannot do this for you. These situations, and the actions you need to take if they occur, are listed below.
## Render Texture coordinates
Vertical Texture coordinate conventions differ between two types of platforms: Direct3D-like and OpenGL-like.
  * **Direct3D-like** : The coordinate is 0 at the top and increases downward. This applies to Direct3D, Metal and consoles.
  * **OpenGL-like** : The coordinate is 0 at the bottom and increases upward. This applies to OpenGL and OpenGL ES.


This difference tends not to have any effect on your project, other than when rendering into a [Render Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture). When rendering into a Texture on a Direct3D-like platform, Unity internally flips rendering upside down. This makes the conventions match between platforms, with the OpenGL-like platform convention the standard.
Image Effects and rendering in UV space are two common cases in the **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) where you need to take action to ensure that the different coordinate conventions do not create problems in your project.
### Image Effects
When you use [Image Effects](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest) and anti-aliasing, the resulting source Texture for an Image Effect is not flipped to match the OpenGL-like platform convention. In this case, Unity renders to the screen to get anti-aliasing and then resolves rendering into a Render Texture for further processing with an Image Effect.
If your Image Effect is a simple one that processes one Render Texture at a time, [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html) deals with the inconsistent coordinates. However, if you’re processing more than one [Render Texture](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html) together in your [Image Effect](https://docs.unity3d.com/Packages/com.unity.postprocessing@latest), the Render Textures are likely to come out at different vertical orientations in Direct3D-like platforms and when you use anti-aliasing. To standardize the coordinates, you need to manually “flip” the screen Texture upside down in your **Vertex Shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) so that it matches the OpenGL-like coordinate standard.
The following code sample demonstrates how to do this:
```
// Flip sampling of the Texture:
// The main Texture
// texel size will have negative Y).

#if UNITY_UV_STARTS_AT_TOP
if (_MainTex_TexelSize.y < 0)
        uv.y = 1-uv.y;
#endif


```

A similar situation occurs with [GrabPass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html). The resulting render Texture might not actually be turned upside down on Direct3D-like (non-OpenGL-like) platforms. If your Shader code samples GrabPass Textures, use the `ComputeGrabScreenPos` function from the [UnityCG include](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html) file.
### Rendering in UV space
When rendering in Texture coordinate (UV) space for special effects or tools, you might need to adjust your Shaders so that rendering is consistent between Direct3D-like and OpenGL-like systems. You also might need to adjust your rendering between rendering into the screen and rendering into a Texture. Adjust these by flipping the Direct3D-like projection upside down so its coordinates match the OpenGL-like projection coordinates.
The [built-in variable](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UnityShaderVariables.html) `ProjectionParams.x` contains a `+1` or `–1` value. `-1` indicates a projection has been flipped upside down to match OpenGL-like projection coordinates, while `+1` indicates it hasn’t been flipped. You can check this value in your Shaders and then perform different actions. The example below checks if a projection has been flipped and, if so, flips and then returns the UV coordinates to match.
```
float4 vert(float2 uv : TEXCOORD0) : SV_POSITION
{
    float4 pos;
    pos.xy = uv;
    // This example is rendering with upside-down flipped projection,
    // so flip the vertical UV coordinate too
    if (_ProjectionParams.x < 0)
        pos.y = 1 - pos.y;
    pos.z = 0;
    pos.w = 1;
    return pos;
}

```

## Clip space coordinates
Similar to Texture coordinates, the clip space coordinates (also known as post-projection space coordinates) differ between Direct3D-like and OpenGL-like platforms:
  * **Direct3D-like** : The clip space depth goes from +1.0 at the near plane to 0.0 at the far plane. This applies to Direct3D, Metal and consoles.
  * **OpenGL-like** : The clip space depth goes from –1.0 at the near plane to +1.0 at the far plane. This applies to OpenGL and OpenGL ES.


Inside Shader code, you can use the `UNITY_NEAR_CLIP_VALUE` [built-in macro](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html) to get the near plane value based on the platform.
Inside script code, use [GL.GetGPUProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html) to convert from Unity’s coordinate system (which follows OpenGL-like conventions) to Direct3D-like coordinates if that is what the platform expects.
## Precision of Shader computations
To avoid precision issues, make sure that you test your Shaders on the target platforms. The GPUs in mobile devices and PCs differ in how they treat floating point types. PC GPUs treat all floating point types (float, half and fixed) as the same - they do all calculations using full 32-bit precision, while many mobile device GPUs do not do this.
For more information, refer to [Use 16-bit precision in shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Use16BitPrecisionInShaders.html).
## Shader data types support
When writing shaders in Unity, it’s important to note that Unity defines `half` as either `float` or `min16float`. If **Shader Precision Model** is set to **Platform Default** , then `half` is `float` on macOS and `min16float` on iOS/tvOS. If **Shader Precision Model** is set to **Unified** , then `half` is `min16float` on macOS/tvOS/iOS.
From Unity 6 onwards, the size and alignment of `min16float` on Metal are 4 bytes on any CPU visible buffer, such as vertex shader input, constant buffers, and structured buffers. Therefore, the size and alignment of `half` is always the same regardless of the platform or **project settings** A broad collection of settings which allow you to configure how Physics, Audio, Networking, Graphics, Input and many other areas of your project behave. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/comp-ManagerGroup.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ProjectSettings). On previous versions of Unity, as the size and alignment of `min16float` was 2 bytes, the layout of buffers containing `half` varied depending on the platform and selected **Shader Precision Model** setting. Because of this issue, iOS and tvOS users had to add C# code as a workaround when uploading data to GPU buffers on iOS/tvOS, which no longer applies to Unity 6. To enable the old behavior when compiling with FXC in Unity 6, you can include `#pragma metal_fxc_allow_float16_in_cpu_visible_buffers` in your shader.
## Const declarations in Shaders
Use of `const` differs between Microsoft HLSL (see [msdn.microsoft.com](http://msdn.microsoft.com)) and OpenGL’s GLSL (see [Wikipedia](https://en.wikipedia.org/wiki/OpenGL_Shading_Language)) Shader language.
  * Microsoft’s HLSL `const` has much the same meaning as it does in C# and C++ in that the variable declared is read-only within its scope but can be initialized in any way.
  * OpenGL’s GLSL `const` means that the variable is effectively a compile time constant, and so it must be initialized with compile time constraints (either literal values or calculations on other `const`s).


It is best to follow the OpenGL’s GLSL semantics and only declare a variable as `const` when it is truly invariant. Avoid initializing a `const` variable with some other **mutable** You can change the contents of a mutable package. This is the opposite of **immutable**. Only **Local package****s** and **Embedded package****s** are mutable.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mutable) values (for example, as a local variable in a function). This also works in Microsoft’s HLSL, so using `const` in this way avoids confusing errors on some platforms.
## Using buffers with GPU buffers
If you use buffers to declare variables in your shader, then set values using the data from a GPU [compute buffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html) or [graphics buffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html), the data layouts might not match depending on the graphics API. This means you might overwrite data or set variables to the wrong values.
For example if you use `cbuffer` or Unity’s [constant buffer macro](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html), depending on the constant buffer’s data layout and the graphics API, a `float3` might become a `float4`, or a `float` might become a `float2`.
You can do the following to make sure all graphics APIs compile a buffer with the same data layout:
  * Use `float4` and `float4x4` instead of `float3` and `float3x3`, because `float4` variables are the same size on all graphics APIs, while `float3` variables can become a different size on some graphics APIs.
  * Declare variables in decreasing size order, for example `float4` then `float2` then `float`, so all graphics APIs structure the data in the same way.


For example:
```
cbuffer myConstantBuffer {
    float4x4 matWorld;
    float4 vObjectPosition; // Uses a float4 instead of a float3
    float arrayIndex;
}

```

## Semantics used by Shaders
To get Shaders working on all platforms, some Shader values should use these semantics:
  * **Vertex Shader output (clip space) position** : `SV_POSITION`. Sometimes Shaders use POSITION semantics to get Shaders working on all platforms.
  * **Fragment Shader output color** : `SV_Target`. Sometimes Shaders use `COLOR` or `COLOR0` to get Shaders working on all platforms.


When rendering Meshes as Points, output `PSIZE` semantics from the vertex Shader (for example, set it to 1). Some platforms, such as OpenGL ES or Metal, treat point size as “undefined” when it’s not written to from the Shader.
See documentation on [Shader semantics](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-VertexProgramInputs.html) for more details.
## Direct3D Shader compiler syntax
Direct3D platforms use Microsoft’s [HLSL Shader compiler](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html). The HLSL compiler is stricter than other compilers about various subtle Shader errors. For example, it doesn’t accept function output values that aren’t initialized properly.
The most common situations that you might run into using this are:
  * A [Surface Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader) vertex modifier that has an `out` parameter. In a surface shader, initialize the output like this:

```
  void vert (inout appdata_full v, out Input o)
      {
        **UNITY_INITIALIZE_OUTPUT(Input,o);**
        // ...
      }

```

  * Partially initialized values. For example, a function returns `float4` but the code only sets the `.xyz` values of it. Set all values or change to `float3` if you only need three values.
  * Using `tex2D` in the Vertex Shader. This is not valid, because UV derivatives don’t exist in the vertex Shader. You need to sample an explicit mip level instead; for example, use `tex2Dlod` (`tex, float4(uv,0,0)`). You also need to add `#pragma target 3.0` as `tex2Dlod` is a Shader model 3.0 feature.


## DirectX 11 (DX11) HLSL syntax in Shaders
Some parts of the [Surface Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html) compilation pipeline do not understand DirectX 11-specific HLSL (Microsoft’s shader language) syntax.
If you’re using HLSL features like `StructuredBuffers`, `RWTextures` and other non-DirectX 9 syntax, wrap them in a DirectX X11-only preprocessor macro as shown in the example below.
```
#ifdef SHADER_API_D3D11
// DirectX11-specific code, for example
StructuredBuffer<float4> myColors;
RWTexture2D<float4> myRandomWriteTexture;
#endif

```

## The Depth (Z) direction in Shaders
Depth (Z) direction differs on different Shader platforms.
**DirectX 11, DirectX 12, Metal: Reversed direction**
  * The depth (Z) buffer is 1.0 at the near plane, decreasing to 0.0 at the far plane.
  * Clip space range is [near,0] (meaning the near plane distance at the near plane, decreasing to 0.0 at the far plane).


**Other platforms: Traditional direction**
  * The depth (Z) buffer value is 0.0 at the near plane and 1.0 at the far plane.
  * Clip space depends on the specific platform: 
    * On Direct3D-like platforms, the range is [0,far] (meaning 0.0 at the near plane, increasing to the far plane distance at the far plane).
    * On OpenGL-like platforms, the range is [-near,far] (meaning minus the near plane distance at the near plane, increasing to the far plane distance at the far plane).


Note that reversed direction depth (Z), combined with a floating point **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer), significantly improves depth buffer precision against the traditional direction. The advantages of this are less conflict for Z coordinates and better shadows, especially when using small near planes and large far planes.
So, when you use Shaders from platforms with the depth (Z) reversed:
  * UNITY_REVERSED_Z is defined.
  * `_CameraDepth` Texture texture range is 1 (near) to 0 (far).
  * Clip space range is within “near” (near) to 0 (far).


However, the following macros and functions automatically work out any differences in depth (Z) directions:
  * `Linear01Depth(float z)`
  * `LinearEyeDepth(float z)`
  * UNITY_CALC_FOG_FACTOR(coord)


### Fetching the depth Buffer
If you are fetching the depth (Z) buffer value manually, you might want to check the buffer direction. The following is an example of this:
```
float z = tex2D(_CameraDepthTexture, uv);
#if defined(UNITY_REVERSED_Z)
    z = 1.0f - z;
#endif

```

### Using clip space
If you are using clip space (Z) depth manually, you might also want to abstract platform differences by using the following macro:
`float clipSpaceRange01 = UNITY_Z_0_FAR_FROM_CLIPSPACE(rawClipSpace);`
**Note** : This macro does not alter clip space on OpenGL or OpenGL ES platforms, so it returns within “-near”1 (near) to far (far) on these platforms.
### Projection matrices
[GL.GetGPUProjectionMatrix()](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GL.GetGPUProjectionMatrix.html) returns a z-reverted matrix if you are on a platform where the depth (Z) is reversed. However, if you’re composing from projection matrices manually (for example, for custom shadows or depth rendering), you need to revert depth (Z) direction yourself where it applies via script.
An example of this is below:
```
var shadowProjection = Matrix4x4.Ortho(...); //shadow camera projection matrix
var shadowViewMat = ...     //shadow camera view matrix
var shadowSpaceMatrix = ... //from clip to shadowMap texture space

//'m_shadowCamera.projectionMatrix' is implicitly reversed
//when the engine calculates device projection matrix from the camera projection
m_shadowCamera.projectionMatrix = shadowProjection;

//'shadowProjection' is manually flipped before being concatenated to 'm_shadowMatrix'
//because it is seen as any other matrix to a Shader.
if(SystemInfo.usesReversedZBuffer)
{
    shadowProjection[2, 0] = -shadowProjection[2, 0];
    shadowProjection[2, 1] = -shadowProjection[2, 1];
    shadowProjection[2, 2] = -shadowProjection[2, 2];
    shadowProjection[2, 3] = -shadowProjection[2, 3];
}
    m_shadowMatrix = shadowSpaceMatrix * shadowProjection * shadowViewMat;

```

### Depth (Z) bias
Unity automatically deals with depth (Z) bias to ensure it matches Unity’s depth (Z) direction. However, if you are using a native code rendering plugin, you need to negate (reverse) depth (Z) bias in your C or C++ code.
#### Tools to check for depth (Z) direction
  * Use [SystemInfo.usesReversedZBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-usesReversedZBuffer.html) to find out if you are on a platform using reversed depth (Z).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-pragma-directives.html)
Pass information to the shader compiler in HLSL
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GLSLShaderPrograms.html)
GLSL in Unity
