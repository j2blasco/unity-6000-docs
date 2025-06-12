* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-pipeline.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Set a shader to require URP or HDRP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html)
Add a shader tag to a SubShader or Pass
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompilationAPIs.html)
Set a shader to require a graphics API or platform
# Set a shader to require URP or HDRP
The `RenderPipeline` tag tells Unity whether a SubShader is compatible with the Universal **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) (URP) or the High Definition Render Pipeline (HDRP).
## Example
This example code declares that a SubShader is compatible with URP:
```
Shader "ExampleShader" {
    SubShader {
        Tags { "RenderPipeline" = "UniversalPipeline" }
        Pass {
            …
        }
    }
}

```

## Additional resources
  * [SubShader tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html)
Add a shader tag to a SubShader or Pass
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-ShaderCompilationAPIs.html)
Set a shader to require a graphics API or platform
