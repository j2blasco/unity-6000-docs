* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [GPU render state commands in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
  * Cull command in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html)
Conservative command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Offset.html)
Offset command in ShaderLab reference
# Cull command in ShaderLab reference
Sets which polygons the GPU should cull, based on the direction that they are facing relative to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera).
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**Cull** | Yes | Yes | Yes | Yes  
## Syntax
This command makes a change to the render state. Use it in a `Pass` block to set the render state for that Pass, or use it in a `SubShader` block to set the render state for all Passes in that SubShader.
**Signature** | **Example syntax** | **Function**  
---|---|---  
`Cull <state>` | `Cull Back` | Sets which polygons the GPU should cull, based on the direction that they face relative to the camera.  
## Parameters
**Parameter** | **Value** | **Function**  
---|---|---  
**state** | `Back` | Cull polygons that face away from the camera. This is called back-face culling.  
  
This is the default value.  
| `Front` | Cull polygons that face towards the camera. This is called front-face culling.  
  
Use this for turning geometry inside-out.  
| `Off` | Do not cull polygons based on the direction that they face.  
  
Use this for special effects, such as transparent objects or double-sided walls.  
## Additional resources
  * [Set the culling mode in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Conservative.html)
Conservative command in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Offset.html)
Offset command in ShaderLab reference
