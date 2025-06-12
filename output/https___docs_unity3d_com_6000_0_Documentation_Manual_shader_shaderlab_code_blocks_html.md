* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shader languages reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shaders-reference.html)
  * [ShaderLab language reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)
  * [Pass in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader-pass.html)
  * Shader code blocks in ShaderLab reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)
Pass tags in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
GPU render state commands in ShaderLab reference
# Shader code blocks in ShaderLab reference
This page contains information about using **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code blocks. For information about writing HLSL itself, refer to [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html).
## HLSL
`HLSLPROGRAM` and `HLSLINCLUDE` are compatible with all **render pipelines** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline).
**Signature** | **Function**  
---|---  
`HLSLPROGRAM`  
`[source code for shader programs]`  
`ENDHLSL` | Creates a shader program block. Unity adds the HLSL shader program to the pass that includes this shader program block.  
`HLSLINCLUDE`  
`[code that you want to share]`  
`ENDHLSL` | Creates a shader include block. Unity includes this code in all shader programs that are defined in `HLSLPROGRAM` blocks, anywhere in this source file.  
## CG
`CGPROGRAM` and `CGINCLUDE` are compatible only with the Built-In Render Pipeline. For most uses, use `HLSLPROGRAM` and `HLSLINCLUDE` instead, unless you write [surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader).
If you use `CGPROGRAM`, Unity includes several of Unity’s built-in shader include files by default, enabling you to use built-in variables and functions. As a result, shaders that use `CGPROGRAM` might not work if you change the keyword to `HLSLPROGRAM`. 
**Note** : Although [the shader library files in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html) have a .cginc file extension, they contain HLSL code rather than CG code.
**Signature** | **Function**  
---|---  
`CGPROGRAM`  
`[source code for shader programs]`  
`ENDCG` | Creates a shader program block. Unity adds the shader program to the pass that includes this shader program block.  
`CGINCLUDE`  
`[code that you want to share]`  
`ENDCG` | Create a shader include block. Unity includes this code in all shader programs that are defined in `CGPROGRAM` blocks, anywhere in this source file.  
## Additional resources
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * [Import a file from the shader library in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html)
  * [Shader methods in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)
Pass tags in ShaderLab reference
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Commands.html)
GPU render state commands in ShaderLab reference
