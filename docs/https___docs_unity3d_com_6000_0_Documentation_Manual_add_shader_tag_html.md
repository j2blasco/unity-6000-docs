* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/add-shader-tag.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Configure when and if Unity uses a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags.html)
  * Add a shader tag to a SubShader or Pass


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html)
Introduction to shader tags
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-pipeline.html)
Set a shader to require URP or HDRP
# Add a shader tag to a SubShader or Pass
In **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab), you assign tags to a SubShader or Pass by placing a `Tags` block inside the block.
Note that both SubShaders and Passes use the `Tags` block, but they work differently. Assigning SubShader tags to a Pass has no effect, and vice versa. The difference is where you put the `Tags` block:
  * To define Pass tags, place the `Tags` block inside a `Pass` block.
  * To define SubShader tags, place the `Tags` block inside a `SubShader` block but outside a `Pass` block.


# Example in a Pass block
```
Shader "Examples/ExampleRequireOptions"
{
    SubShader
    {
        Pass
        {    
              Tags { "RequireOptions" = "SoftVegetation" }
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [SubShader tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShaderTags.html)
  * [Pass tags in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-introduction.html)
Introduction to shader tags
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-tags-pipeline.html)
Set a shader to require URP or HDRP
