* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * Introduction to surface shaders in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
Writing Surface Shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders-output.html)
Surface Shader output structures in the Built-In Render Pipeline
# Introduction to surface shaders in the Built-In Render Pipeline
In the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline), Surface **Shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) are a streamlined way of writing shaders that interact with lighting.
## Render pipeline compatibility
**Feature name** | **Universal Render Pipeline (URP)** | **High Definition Render Pipeline (HDRP)** | **Custom SRP** | **Built-in Render Pipeline**  
---|---|---|---|---  
****Surface Shaders**** | No | No | No | Yes  
To create custom lighting in URP and HDRP, do one the following instead:
  * For a streamlined way of creating **Shader objects** An instance of the Shader class, a Shader object is container for shader programs and GPU instructions, and information that tells Unity how to use them. Use them with materials to determine the appearance of your scene. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-objects.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shaderobject), refer to [Shader Graph](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-graph.html).
  * Copy and modify the shader code URP or HDRP provides in the package files. Modifying might be difficult because the shader code is large and complex. For more information about finding package files, refer to [Inspecting packages](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-inspect.html).


## Overview
Writing shaders that interact with lighting is complex. There are different light types, different shadow options, different **rendering paths** The technique that a render pipeline uses to render graphics. Choosing a different rendering path affects how lighting and shading are calculated. Some rendering paths are more suited to different platforms and hardware than others. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderingPaths.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderingPath) (forward and deferred rendering), and the shader should somehow handle all that complexity.
Surface Shaders is a code generation approach that makes it much easier to write lit shaders than using low level [vertex/pixel shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html).
For some examples, take a look at [Surface Shader Examples](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html).
## How it works
You define a “surface function” that takes any UVs or data you need as input, and fills in output structure `SurfaceOutput`. SurfaceOutput basically describes _properties of the surface_ (its albedo color, normal, emission, specularity etc.). You write this code in HLSL.
Surface Shader compiler then figures out what inputs are needed, what outputs are filled and so on, and generates actual [vertex&pixel shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html), as well as rendering passes to handle forward and deferred rendering.
## Surface Shaders and DirectX 11 HLSL syntax
Currently some parts of surface shader compilation pipeline do not understand [DirectX 11](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingDX11GL3Features.html)-specific HLSL syntax, so if you’re using HLSL features like StructuredBuffers, RWTextures and other non-DX9 syntax, you have to wrap it into a DX11-only preprocessor macro.
See [Platform Specific Differences](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) and [Using HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html) pages for details.
## Additional resources
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
Writing Surface Shaders
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders-output.html)
Surface Shader output structures in the Built-In Render Pipeline
