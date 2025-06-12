* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ColorMask.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
  * ColorMask command in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BlendOp.html)
BlendOp command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html)
Conservative command in ShaderLab reference
# ColorMask command in ShaderLab reference
Sets the color channel writing mask, which prevents the GPU from writing to channels in the render target.
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ColorMask** | Yes | Yes | Yes | Yes  
## Syntax
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
**Signature** | **Example syntax** | **Function**  
---|---|---  
`ColorMask <channels>` | `ColorMask RGB` | Write to the given channels of the default render target.  
`ColorMask <channels> <render target>` | `ColorMask RGB 2` | As above, but for a given render target.  
## Parameters
**Parameter** | **Value** | **Function**  
---|---|---  
**render target** | Integer, 0 through 7. | The render target index.  
**channels** | `0` | Disables color writes to the R, G, B, and A channels.  
| `R` | Enables color writes to the red channel.  
| `G` | Enables color writes to the green channel.  
| `B` | Enables color writes to the blue channel.  
| `A` | Enables color writes to the alpha channel.  
| Any combination of `R`, `G`, `B`, and `A` without spaces. For example: `RB` | Enables color writes to the given channels.  
## Additional resources
  * [Set the color channels the GPU renders to](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-color-mask.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BlendOp.html)
BlendOp command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html)
Conservative command in ShaderLab reference
