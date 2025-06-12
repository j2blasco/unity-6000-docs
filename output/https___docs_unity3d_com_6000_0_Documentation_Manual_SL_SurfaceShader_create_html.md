* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShader-create.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * Create a surface shader in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-RenderPipeline.html)
Surface Shaders and rendering paths in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderLighting.html)
Set the lighting model in a Surface Shader in the Built-In Render Pipeline
# Create a surface shader in the Built-In Render Pipeline
Follow these steps:
  1. Add a `CGPROGRAM` block to the `SubShader` block in your **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code, not the `Pass` block. Unity automatically creates multiple passes when it compiles the **surface shader** A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader).
  2. Add a `#pragma surface [surfaceFunction] [lightModel]` directive.


Surface shaders aren’t compatible with `HLSLPROGRAM` blocks, but you can use HLSL inside a `CGPROGRAM` block. For more information, refer to [Shader code blocks in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html).
## Example
```
Shader "Example/Diffuse Simple" {
  SubShader {
    Tags { "RenderType" = "Opaque" }

    CGPROGRAM

    #pragma surface surf Lambert

    struct Input {
        float4 color : COLOR;
    };

    void surf (Input IN, inout SurfaceOutput o) {
        o.Albedo = 1;
    }

    ENDCG
  }
  Fallback "Diffuse"
}

```

Here’s how it looks like on a model with two [Lights](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Light.html) set up: 
![Basic surface shader example.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderSimple.jpg) Basic surface shader example.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-RenderPipeline.html)
Surface Shaders and rendering paths in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderLighting.html)
Set the lighting model in a Surface Shader in the Built-In Render Pipeline
