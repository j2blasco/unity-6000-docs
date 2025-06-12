* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [SubShader in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
  * GrabPass directive in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html)
UsePass directive in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
Pass in ShaderLab reference
# GrabPass directive in ShaderLab reference
GrabPass is a command that creates a special type of Pass that grabs the contents of the frame buffer into a texture. This texture can be used in subsequent Passes to do advanced image based effects.
This command can significantly increase both CPU and GPU frame times. You should generally avoid using this command other than for quick prototyping, and attempt to achieve your effect in other ways. If you do use this command, try to reduce the number of screen grabbing operations as much as possible; either by reducing your usage of this command, or by using the signature that grabs the screen to a named texture if applicable.
## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**GrabPass** | No | No | No | Yes  
## Syntax
Use this command in a SubShader block.
Note that the two different signatures have different functionality, and different performance implications. Using a named texture can result in significantly fewer screen grabbing operations, which can reduce the impact of this resource-intensive command.
**Signature** | **Function**  
---|---  
`GrabPass { }` | Grabs the frame buffer contents into a texture that you can use in subsequent Passes in the same SubShader.  
  
Reference the texture using the name __GrabTexture_.  
  
When you use this signature, Unity grabs the screen every time it renders a batch that contains this command. This means that Unity can grab the screen multiple times per frame: once for each batch.  
`GrabPass { "ExampleTextureName" }` | Grabs the frame buffer contents into a texture that you can access in subsequent Passes in the same frame, across multiple SubShaders.  
  
Reference the texture using the given name.  
  
When you use this signature, Unity grabs the screen the first time in a frame that it renders a batch that contains this command with a given texture name.  
## Additional resources
  * [Get the current framebuffer with the GrabPass command](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-grabpass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html)
UsePass directive in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
Pass in ShaderLab reference
