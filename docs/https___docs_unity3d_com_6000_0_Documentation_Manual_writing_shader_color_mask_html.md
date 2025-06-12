* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-color-mask.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Set the color channels the GPU renders to


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-blending-modes.html)
Set the blending mode in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-alpha-to-mask.html)
Reduce aliasing with AlphaToMask mode
# Set the color channels the GPU renders to
By default, the GPU writes to all channels (RGBA). For some effects you might want to leave certain channels unmodified; for example, you can disable color rendering to render uncolored shadows. Another common use case is to disable color writes completely so that you can populate one buffer with data without writing to others; for example, you might want to populate the **stencil buffer** A memory store that holds an 8-bit per-pixel value. In Unity, you can use a stencil buffer to flag pixels, and then only render to pixels that pass the stencil operation. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#stencilbuffer) without writing to the render target.
## Examples
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
              // Enable writing only to the RGB channels for this Pass, which disables writing to the alpha channel
              ColorMask RGB

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
         // Enable writing only to the RGB channels for this SubShader, which disables writing to the alpha channel
         ColorMask RGB

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
  * [ColorMask command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ColorMask.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-blending-modes.html)
Set the blending mode in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-alpha-to-mask.html)
Reduce aliasing with AlphaToMask mode
