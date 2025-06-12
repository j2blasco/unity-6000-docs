* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-depth-bias.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Set the depth bias in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html)
Set the culling mode in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-zclip.html)
Set the depth clip mode in a shader
# Set the depth bias in a shader
Depth bias, also called depth offset, is a setting on the GPU that determines the depth at which it draws geometry. Adjust the depth bias to force the GPU to draw geometry on top of other geometry that is at the same depth. This can help you to avoid unwanted visual effects such as z-fighting and shadow acne.
To set the depth bias for specific geometry, use this command or a [RenderStateBlock](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderStateBlock.html). To set the global depth bias, which affects all geometry, use [CommandBuffer.SetGlobalDepthBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.SetGlobalDepthBias.html). The GPU applies the depth bias for specific geometry in addition to the global depth bias.
To reduce shadow acne, you can achieve a similar visual effect with the **light bias** settings; however, these settings work differently, and they do not change the state on the GPU. For more information, see [Shadow troubleshooting](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html).
# Example
This example code demonstrates the syntax for using this command in a Pass block. 
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
              // Sets the depth offset for this geometry so that the GPU draws this geometry closer to the camera
              // You would typically do this to avoid z-fighting
              Offset -1, -1

              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [Offset command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Offset.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html)
Set the culling mode in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-zclip.html)
Set the depth clip mode in a shader
