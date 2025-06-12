* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-depth-only.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Examples of writing a custom shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html)
  * Write a depth-only pass in a Universal Render Pipeline shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html)
Visualize normal vectors in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html)
Reconstruct world space positions in a shader in URP
# Write a depth-only pass in a Universal Render Pipeline shader
To create a depth prepass that writes the depth of objects before the opaque and transparent passes, add a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) pass that has the `DepthOnly` tag.
Add this pass if you enable a setting that requires a depth prepass, otherwise Unity might render incorrectly. For example, if you enable **Depth Priming** in the [Universal Render Pipleine (URP) Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html), opaque objects are invisible.
**Important** : To render correctly, make sure that every shader pass renders the same number of fragments in the same positions. For example, use an include or a macro to share the same code between passes, especially if you change the positions of vertices, use alpha clipping, or use effects like dithering. 
## Add a depth-only pass
The following example shows how to add a depth-only pass to a shader:
```
Shader "Example/CustomShader"
{
    SubShader
    {

        Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }

        // Add a depth-only pass
        Pass
        {
            Name "DepthOnlyPass"
            Tags { "LightMode" = "DepthOnly" }

            // Write depth to the depth buffer
            ZWrite On

            // Don't write to the color buffer
            ColorMask 0 

            ...
        }

        // The forward pass. This pass also writes depth by default.
        Pass
        {
            Name "ForwardPass"
            Tags { "LightMode" = "UniversalForward" }

            ...
        }
    }
}

```

## Add a depth and normals pass
The recommended best practice is to also add a pass that has the `DepthNormals` tag, to write both the depth and normals of objects. Otherwise, if you enable features like screen space **ambient occlusion** A method to approximate how much ambient light (light not coming from a specific direction) can hit a point on a surface.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Ambientocclusion) (SSAO), Unity might not render objects correctly.
For more information about outputting normals, refer to [Visualize normal vectors in a shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html).
For example:
```
Pass
{
    Name "DepthNormalsPass"
    Tags { "LightMode" = "DepthNormals" }

    // Write depth to the depth buffer
    ZWrite On

    ...

    float4 frag(Varyings input) : SV_TARGET
    {
        // Return the normal as a value between 0 and 1
        float3 normalWS = normalize(input.normalWS);
        return float4(normalWS * 0.5 + 0.5, 1);
    }}

```

## Additional resources
  * [ShaderLab Pass tags](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html)
  * [Shader methods](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods.html)
  * [Universal Render Pipleine (URP) Asset](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-universal-renderer.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html)
Visualize normal vectors in a shader in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-reconstruct-world-position.html)
Reconstruct world space positions in a shader in URP
