* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-blending-modes.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Set the blending mode in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-stencil.html)
Check or write to the stencil buffer in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-color-mask.html)
Set the color channels the GPU renders to
# Set the blending mode in a shader
The `Blend` command determines how the GPU combines the output of the fragment **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) with the render target.
The functionality of this command depends on the blending operation, which you can set using the BlendOp command. Note that while blending itself is supported on all graphics APIs and hardware, some blending operations have more limited support.
Enabling blending disables some optimizations on the GPU (mostly hidden surface removal/Early-Z), which can lead to increased GPU frame times.
## Common blend types
Here is the syntax for the most common blend types:
```
Blend SrcAlpha OneMinusSrcAlpha // Traditional transparency
Blend One OneMinusSrcAlpha // Premultiplied transparency
Blend One One // Additive
Blend OneMinusDstColor One // Soft additive
Blend DstColor Zero // Multiplicative
Blend DstColor SrcColor // 2x multiplicative

```

## Examples
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
              // Enable regular alpha blending for this Pass
      Blend SrcAlpha OneMinusSrcAlpha
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

This example code demonstrates the syntax for using this command in a SubShader block.
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // Enable regular alpha blending for this SubShader
         Blend SrcAlpha OneMinusSrcAlpha

         // The rest of the code that defines the SubShader goes here.        

        Pass
        {    
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [Blend command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Blend.html)
  * [BlendOp command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BlendOp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-stencil.html)
Check or write to the stencil buffer in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-color-mask.html)
Set the color channels the GPU renders to
