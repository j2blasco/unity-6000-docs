* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
  * Conservative command in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ColorMask.html)
ColorMask command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html)
Cull command in ShaderLab reference
# Conservative command in ShaderLab reference
Enables or disables conservative **rasterization** The process of generating an image by calculating pixels for each polygon or triangle in the geometry. This is an alternative to ray tracing.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Rasterization). 
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Conservative** | Yes | Yes | Yes | Yes  
## Syntax
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
**Signature** | **Example syntax** | **Function**  
---|---|---  
`Conservative <enabled>` | `Conservative True` | Enables or disables conservative rasterization.  
  
Requires DX 11.3+, or GL_NV_conservative_raster.  
## Parameters
**Parameter** | **Value** | **Function**  
---|---|---  
**enabled** | `True` | Enables conservative rasterization.  
| `False` | Disables conservative rasterization.  
## Additional resources
  * [Enable conservative rasterization in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-conservative-rasterization.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ColorMask.html)
ColorMask command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html)
Cull command in ShaderLab reference
