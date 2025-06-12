* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-disable-dynamic-batching.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Disable dynamic batching of a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-prioritize-lower-quality-shaders.html)
Prioritize lower quality shaders with the LOD command
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-get-tag-value.html)
Get tag values in a script
# Disable dynamic batching of a shader
The `DisableBatching` SubShader Tag prevents Unity from applying [Dynamic Batching](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)An automatic Unity process which attempts to render multiple meshes as if they were a single mesh for optimized graphics performance. The technique transforms all of the GameObject vertices on the CPU and groups many similar vertices together. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/DrawCallBatching.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DynamicBatching) to geometry that uses this SubShader.
This is useful for **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) programs that perform object space operations. Dynamic Batching transforms all geometry into world space, meaning that shader programs can no longer access object space. Shader programs that rely on object space therefore do not render correctly. To avoid this problem, use this SubShader Tag to prevent Unity from applying Dynamic Batching.
## Examples
This example code creates a SubShader with a DisableBatching value of `True`:
```
Shader "ExampleShader" {

    SubShader {

        Tags { "DisableBatching" = "True" }
        Pass {
            …
        }

    }

}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-prioritize-lower-quality-shaders.html)
Prioritize lower quality shaders with the LOD command
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-get-tag-value.html)
Get tag values in a script
