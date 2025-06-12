* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-add-shader-program.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * Add an HLSL shader program


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-introduction.html)
Shader program fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-include-shader-program.html)
Duplicate HLSL in multiple programs
# Add an HLSL shader program
To add HLSL code, you can use the `HLSLPROGRAM` directive.
## Example
```
Shader "Examples/ExampleShader"
{
    SubShader
    {
        Pass
        {                
              Name "ExamplePassName"
              Tags { "LightMode" = "ExampleLightModeTagValue" }

              // ShaderLab commands to set the render state go here

              HLSLPROGRAM
                // HLSL shader code goes here
              ENDHLSL
        }
    }
}

```

## Additional resources
  * [ShaderLab: adding shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-shaderlab-code-blocks.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-programs-introduction.html)
Shader program fundamentals
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-include-shader-program.html)
Duplicate HLSL in multiple programs
