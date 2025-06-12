* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-shader-pass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * Add a shader pass in a custom shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-subshader-object.html)
Add a subshader in a custom shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-usepass.html)
Include a shader pass with the UsePass command
# Add a shader pass in a custom shader
A Pass is the fundamental element of a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object. It contains instructions for setting the state of the GPU, and the shader programs that run on the GPU. 
Simple Shader objects might contain only a single Pass, but more complex shaders can contain multiple Passes. You can use separate Passes to define parts of your **Shader object** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject) that work differently; for example, parts that require a change to the render state, different shader programs, or a different `LightMode` Pass tag.
**Note** : In render pipelines based on the Scriptable **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), you can use a RenderStateBlock to change the render state on the GPU, without requiring a separate Pass.
To define a regular Pass in **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), you place a `Pass` block inside a `SubShader` block.
You can also define two special types of Pass, using the `UsePass` or `GrabPass` commands. For information on those commands, see [ShaderLab commands: UsePass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html) or [ShaderLab commands: GrabPass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html).
## Name a shader pass
A Pass can have a name. You need to reference a Pass by name in the `UsePass` command, and in some C# APIs. The name of a Pass is visible in the [Frame Debugger](https://docs.unity3d.com/6000.0/Documentation/Manual/FrameDebugger.html) tool.
To assign a name to a Pass in ShaderLab, you place a `Name` block inside a `Pass` block.
Internally, Unity converts the name to uppercase. When you reference the name in ShaderLab code, you must use the uppercase variant; for example, if the value is “example”, you must reference it as EXAMPLE.
If more than one Pass in the same SubShader has the same name, Unity uses the first Pass in the code.
### Using the Pass name with C# scripts
To access the name of a Pass from C# **scripts** A piece of code that allows you to create your own Components, trigger game events, modify Component properties over time and respond to user input in any way you like. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/creating-scripts.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scripts), you can use APIs such as [Material.FindPass](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.FindPass.html), [Material.GetPassName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetPassName.html), or [ShaderData.Pass.Name](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.Name.html).
**Note:** [Material.GetShaderPassEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.GetShaderPassEnabled.html) and [Material.SetShaderPassEnabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Material.SetShaderPassEnabled.html) do not reference Passes by name; instead, they reference Passes using the value of the [LightMode tag](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html).
## Example
This example code demonstrates the syntax for creating a Shader object that contains a single SubShader, which in turn contains a single Pass.
```
Shader "Examples/SinglePass"
{
    SubShader
    {
        Pass
        {                
              Name "ExamplePassName"
              Tags { "ExampleTagKey" = "ExampleTagValue" }

              // ShaderLab commands go here.

              // HLSL code goes here.
        }
    }
}

```

## Additional resources
  * [Pass block in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)
  * [Shader code blocks in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html)
  * [Name directive in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Name.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-create-subshader-object.html)
Add a subshader in a custom shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-usepass.html)
Include a shader pass with the UsePass command
