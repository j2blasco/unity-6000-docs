* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/set-culling-mode.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Setting the render state on the GPU](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-render-state-commands.html)
  * Set the culling mode in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-conservative-rasterization.html)
Enable conservative rasterization in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-depth-bias.html)
Set the depth bias in a shader
# Set the culling mode in a shader
Culling is the process of determining what not to draw. Culling improves rendering efficiency, by not wasting GPU time drawing things that would not be visible in the final image.
By default, the GPU performs back-face culling; this means that it does not draw polygons that face away from the viewer. In general, the more you can reduce the rendering workload, the better; you should therefore change this setting only when necessary.
## Example
```
Shader "Examples/CommandExample"
{
    SubShader
    {
         // The rest of the code that defines the SubShader goes here.

        Pass
        {    
              // Disable culling for this Pass.
              // You would typically do this for special effects, such as transparent objects or double-sided walls.
              Cull Off
            
              // The rest of the code that defines the Pass goes here.
        }
    }
}

```

## Additional resources
  * [Cull command in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Cull.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-conservative-rasterization.html)
Enable conservative rasterization in a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-set-depth-bias.html)
Set the depth bias in a shader
