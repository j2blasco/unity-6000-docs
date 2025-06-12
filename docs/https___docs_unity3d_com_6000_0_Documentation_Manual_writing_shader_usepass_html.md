* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-usepass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * Include a shader pass with the UsePass command


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)
Add a shader pass in a custom shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
Writing HLSL shader programs
# Include a shader pass with the UsePass command
The UsePass command inserts a named Pass from another **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object. You can use this command to reduce code duplication in shader source files.
## Example
This example code creates a **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) called ContainsNamedPass, which contains a Pass called ExampleNamedPass.
```
Shader "Examples/ContainsNamedPass"
{
    SubShader
    {
        Pass
        {    
              Name "ExampleNamedPass"
            
              // The rest of the Pass contents go here.
        }
    }
}

```

This example code creates a Shader object called UseNamedPass, which uses the named Pass from the example code above.
```
Shader "Examples/UsesNamedPass"
{
    SubShader
    {
        UsePass "Examples/ContainsNamedPass/EXAMPLENAMEDPASS"
    }
}

```

## Additional resources
  * [UsePass directive in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html)
Add a shader pass in a custom shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
Writing HLSL shader programs
