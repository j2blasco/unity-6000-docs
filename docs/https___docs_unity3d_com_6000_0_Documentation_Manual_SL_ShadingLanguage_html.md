* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShadingLanguage.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * Introduction to writing shaders in code


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
Writing shaders in code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)
Shader object fundamentals
# Introduction to writing shaders in code
How you write custom **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in Unity depends on the **render pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) you use:
  * For guidance and examples for the Built-in Render Pipeline, see [Example shaders for the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html).
  * For guidance and examples for the the Universal Render Pipeline (URP), see [URP: Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html).
  * It is not recommended to write your own shader programs for HDRP, due to the complexity of the code. Instead, use [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html) to create Shader objects without writing code.
  * For an example of a simple vertex and fragment shader for a custom Scriptable Render Pipeline, see [Creating a simple render loop in a custom render pipeline](https://docs.unity3d.com/Packages/com.unity.render-pipelines.core@17.0/manual/index.html).


## Languages
When you write shaders for Unity, you use the following languages:
  * A programming language called HLSL. Use this to write the shader programs themselves. For more information on HLSL, see [HLSL in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html).
  * A Unity-specific language called ShaderLab. Use this to define a [Shader object](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), which acts as a container for your shader programs. For more information on ShaderLab, see [ShaderLab](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html)Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab).


You do not need to use different languages for different platforms; Unity compiles your HLSL and ShaderLab code into different languages for different graphics APIs. For more information, see [Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html).
**Note:** You can also directly write your shader programs in GLSL and Metal if you want. This is not recommended or needed as part of a normal workflow. For more information on using GLSL, see [GLSL in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GLSLShaderPrograms.html).
### ShaderLab
ShaderLab is a declarative language that you use in shader source files. It uses a nested-braces syntax to describe a Shader object.
There are many things that you can define in ShaderLab, but the most common are:
  * Defining the overall structure of the Shader object. See [ShaderLab: creating a Shader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html), [ShaderLab: creating a SubShader](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader.html), and [ShaderLab: creating a Pass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pass.html).
  * Using code blocks to add shader programs written in HLSL. See [ShaderLab: adding shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html).
  * Using commands to set the render state of the GPU before it executes a shader program, or to perform an operation involving another Pass. See [ShaderLab: commands](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Reference.html).
  * Exposing properties from your shader code so you can edit them in the material **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) and save as part of a material asset. See [ShaderLab: defining material properties](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Properties.html).
  * Specifying package requirements for SubShaders and Passes. This enables Unity to run certain SubShaders and Passes only when particular packages are installed in the Unity project. See [ShaderLab: specifying package requirements](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PackageRequirements.html).
  * Defining fallback behavior for when Unity cannot run any of the SubShaders with a Shader object on the current hardware. See [ShaderLab: assigning a fallback](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html).


## Different ways of writing shaders
There are different ways of writing shaders:
  * The most common way is to write vertex and fragment shaders in HLSL. For more information, see [Writing vertex and fragment shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html).
  * In the Built-in Render Pipeline, you can also write Surface Shaders. They are a simplified way of writing shaders that interact with lighting. For more information, see [Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader).
  * For backwards compatibility reasons, Unity also supports “fixed function style” ShaderLab commands. These let you write shaders in ShaderLab, without using HLSL. This is no longer recommended, but it is documented on the page [ShaderLab legacy functionality](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-legacy.html).


## Writing shaders for different graphics APIs
In some cases, you must write your shader code differently depending on the graphics API that you are targeting. For information on this, see [Writing shaders for different graphics APIs](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html).
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
Writing shaders in code
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)
Shader object fundamentals
