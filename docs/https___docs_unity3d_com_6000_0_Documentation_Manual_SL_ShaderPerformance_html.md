* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderPerformance.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * Optimize shaders


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-crossplatform.html)
Writing compute shaders for multiple platforms
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
Shaders in URP
# Optimize shaders
This page contains information on optimizing your **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) for runtime performance, especially on mobile platforms that have limited GPU performance.
## Avoid complex calculations
To avoid complex calculations, do the following for example:
  * Use lookup textures instead of resource-intensive functions such as `pow`, `log` and `sin`.
  * Use Unity HLSL functions, such as `normalize` and `dot`, instead of writing your own. This ensures that the driver can generate better code.


## Avoid repeated calculations
To avoid shaders repeating calculations, do the following for example:
  * Move calculations from the fragment shader to the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader), so they run only for every vertex, not every fragment.
  * Do calculations in a C# script instead, then use the calculated value in the shader.
  * Avoid unnecessary calculations. For example, remove code that supports multiple colors per material if you always use the same color.


## Use lower precision data types
Use `half` instead of `float` for all variables except world space coordinates and texture coordinates. For more information, refer to [Use 16-bit precision in shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Use16BitPrecisionInShaders.html).
## Use casts instead of suffixes
Unity doesn’t support suffixes, so a value like `2.0h` becomes a full `float`. This means when the GPU does calculations, it might have to convert other values to `float` and back. This can slow down the shader.
To prevent this, use casts instead of suffixes. For example, use `half(2.0)` instead of `2.0h`.
## Avoid discarding pixels or channels
To avoid shaders slowing down, avoid the following resource-intensive methods:
  * The `discard` method in the fragment shader.
  * [ColorMask](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html) on mobile platforms.


## Avoid writing to the depth buffer
To ensure mobile GPUs can use early depth testing to speed up rendering, don’t write to the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer) in the fragment shader. 
For more information about depth testing, refer to [ShaderLab command: ZTest](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ZTest.html).
## Additional resources
  * [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html)
  * [Metal requirements and compatibility](https://docs.unity3d.com/6000.0/Documentation/Manual/metal-requirements-and-compatibility.html)
  * [Optimize surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderOptimize.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader-crossplatform.html)
Writing compute shaders for multiple platforms
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
Shaders in URP
