* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [Pass in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
  * Pass block in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
Pass in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html)
Name directive in ShaderLab reference
# Pass block in ShaderLab reference
To define a Pass in **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), use a `Pass` block. This page contains information on using `Pass` blocks. For information on how a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object works, and the relationship between **Shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), SubShaders and Passes, see [Shader object fundamentals](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html).
Inside the `Pass` block, you can:
  * Assign a name to the Pass, using a Name block. See [ShaderLab: assigning a name to a Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html).
  * Assign key-value pairs of data to the Pass, using a Tags block. See [ShaderLab: assigning tags to a Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
  * Perform operations using ShaderLab commands. See [ShaderLab: using commands](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).
  * Add shader code to the Pass, using a shader code block. See [ShaderLab: shader code blocks](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html).
  * Specify package requirements using the `PackageRequirements` block. This makes Unity only run the Pass if the required packages are installed. See [ShaderLab: specifying package requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PackageRequirements.html).


## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: Pass block** | Yes | Yes | Yes | Yes  
## Syntax
**Signature** | **Function**  
---|---  
`Pass`  
`{`  
`<optional: name>`  
`<optional: tags>`  
`<optional: commands>`  
`<optional: shader code>`  
`}` | Defines a Pass.  
## Additional resources
  * [Add a shader pass in a custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
Pass in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html)
Name directive in ShaderLab reference
