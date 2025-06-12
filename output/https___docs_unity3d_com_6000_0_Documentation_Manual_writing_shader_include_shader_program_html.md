* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-include-shader-program.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * Duplicate HLSL in multiple programs


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-add-shader-program.html)
Add an HLSL shader program
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-shader-input.html)
Shader input
# Duplicate HLSL in multiple programs
To include HLSL code in other `HLSLPROGRAM` sections, you can use the `HLSLINCLUDE` directive.
## Example
```
Shader "Examples/ExampleShader"
{
    SubShader
    {

        HLSLINCLUDE
            // HLSL code that you want to share goes here
        ENDHLSL

        Pass
        {                
              Name "ExampleFirstPassName"
              Tags { "LightMode" = "ExampleLightModeTagValue" }

              // ShaderLab commands to set the render state go here

              HLSLPROGRAM
                // This HLSL shader program automatically includes the contents of the HLSLINCLUDE block above
                // HLSL shader code goes here
              ENDHLSL
        }

        Pass
        {                
              Name "ExampleSecondPassName"
              Tags { "LightMode" = "ExampleLightModeTagValue" }

              // ShaderLab commands to set the render state go here

              HLSLPROGRAM
                // This HLSL shader program automatically includes the contents of the HLSLINCLUDE block above
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
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-add-shader-program.html)
Add an HLSL shader program
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-shader-input.html)
Shader input
