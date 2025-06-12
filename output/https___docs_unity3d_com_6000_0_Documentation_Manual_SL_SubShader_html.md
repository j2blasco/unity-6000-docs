* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [SubShader in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
  * SubShader block in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
SubShader in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html)
LOD directive in ShaderLab reference
# SubShader block in ShaderLab reference
To define a SubShader in **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), you use a `SubShader` block. This page contains information on using SubShader blocks.
Inside the `SubShader` block, you can:
  * Assign a **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) (level of detail) value to the SubShader, using the `LOD` block. See [assigning a LOD value to a SubShader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html).
  * Assign key-value pairs of data to the SubShader, using the `Tags` block. See [ShaderLab: assigning tags to a SubShader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html).
  * Add GPU instructions or **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code to the SubShader, using ShaderLab commands. See [ShaderLab: using commands](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).
  * Define one or more Passes, using the `Pass` block. See [ShaderLab: defining a Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
  * Specify package requirements using the `PackageRequirements` block. This makes Unity only run the SubShader if the required packages are installed. See [ShaderLab: specifying package requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PackageRequirements.html).


## Render pipeline compatibility
**Feature name** | **Universal**Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
**ShaderLab: SubShader block** | Yes | Yes | Yes | Yes  
## Syntax
**Signature** | **Function**  
---|---  
`SubShader`  
`{`  
`<optional: LOD>`  
`<optional: tags>`  
`<optional: commands>`  
`<One or more Pass definitions>`  
`}` | Defines a SubShader.  
  
You can define as many Passes as you like within a SubShader.  
## Additional resources
  * [Add a subshader in a custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-subshader-object.html)
  * [Add a shader pass in a custom shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-object.html)
SubShader in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderLOD.html)
LOD directive in ShaderLab reference
