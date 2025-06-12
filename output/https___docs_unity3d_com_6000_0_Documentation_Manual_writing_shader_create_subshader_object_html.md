* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-subshader-object.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * Add a subshader in a custom shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html)
Create a shader file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)
Add a shader pass in a custom shader
# Add a subshader in a custom shader
A **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object contains one or more SubShaders. SubShaders let you define different GPU settings and shader programs for different hardware, **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), and runtime settings. Some **Shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) contain only a single SubShader; others contain multiple SubShaders to support a range of different configurations.
For information on how a Shader object works, and the relationship between Shader objects, SubShaders and Passes, see [Shader objects introduction](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html).
In **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), you define a SubShader by placing a `SubShader` block inside a `Shader` block.
## Example
This example code demonstrates the syntax for creating a Shader object that contains a single SubShader, which in turn contains a single Pass.
```
Shader "Examples/SinglePass"
{
    SubShader
    {
        Tags { "ExampleSubShaderTagKey" = "ExampleSubShaderTagValue" }
        LOD 100

         // ShaderLab commands that apply to the whole SubShader go here. 

        Pass
        {                
              Name "ExamplePassName"
              Tags { "ExamplePassTagKey" = "ExamplePassTagValue" }

              // ShaderLab commands that apply to this Pass go here.

              // HLSL code goes here.
        }
    }
}

```

## Additional resources
  * [SubShader block in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader.html)
  * [SubShader tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Shader.html)
Create a shader file
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)
Add a shader pass in a custom shader
