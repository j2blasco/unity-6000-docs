* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Other.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Group commands with the Category block


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-alpha-to-mask.html)
Reduce aliasing with AlphaToMask mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
Adding material properties to shaders
# Group commands with the Category block
Use the **Category** block to group commands that set the render state, so that you can “inherit” the grouped rendering state within the block.
For example, your **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) object might have multiple [SubShaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader.html), each of which requires [blending](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Blend.html) set to additive. You can use the Category block for that:
```
Shader "example" {
Category {
    Blend One One
    SubShader {
        // ...
    }
    SubShader {
        // ...
    }
    // ...
}
}

```

The Category block does not have an impact on shader performance; it is essentially the same as copy-pasting the code.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-alpha-to-mask.html)
Reduce aliasing with AlphaToMask mode
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-change-properties.html)
Adding material properties to shaders
