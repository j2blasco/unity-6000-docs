* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Offset.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
  * Offset command in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html)
Cull command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html)
Stencil command in ShaderLab reference
# Offset command in ShaderLab reference
Sets the depth bias on the GPU.
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Offset** | Yes | Yes | Yes | Yes  
## Syntax
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
**Signature** | **Example syntax** | **Function**  
---|---|---  
`Offset <factor>, <units>` | `Offset 1, 1` | Draw geometry closer to or further away from the camera, based on the given values.  
## Parameters
**Parameter** | **Value** | **Function**  
---|---|---  
**factor** | Float, range –1 through 1. | Scales the maximum Z slope, also called the depth slope, to produce a variable depth offset for each polygon.  
  
Polygons that are not parallel to the near and far clip planes have Z slope. Adjust this value to avoid visual artifacts on such polygons.  
**units** | Float, range –1 through 1. | Scales the minimum resolvable depth buffer value, to produce a constant depth offset. The minimum depth resolvable depth buffer value (one _unit_) varies by device.  
  
A negative value means that the GPU draws the polygon closer to the camera. A positive value means that the GPU draws the polygon further away from the camera.  
## Additional resources
  * [Set the depth bias in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-depth-bias.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html)
Cull command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Stencil.html)
Stencil command in ShaderLab reference
