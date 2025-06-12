* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-custom-shader.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Motion vectors in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-landing.html)
  * Output a motion vector texture in a custom shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-render-pass.html)
Motion vectors render pass in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html)
Sample motion vectors in a shader in URP
# Output a motion vector texture in a custom shader in URP
For URP to render the **MotionVectors** pass for a **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), make sure that its active SubShader contains a pass with the following [LightMode tag](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html#lightmode):
```
Tags { "LightMode" = "MotionVectors" }

```

For example:
```
Shader “Example/MyCustomShaderWithPerObjectMotionVectors"
{
    SubShader
    {
        // ...other passes, SubShader tags and commands
    
        Pass
        {
            Tags { "LightMode" = "MotionVectors" }
            ColorMask RG
            
            HLSLPROGRAM
            
            // Your shader code goes here.
            
            ENDHLSL
        }
    }
}

```

For an example of adding motion vector pass support for features such as alpha clipping, **LOD** The _Level Of Detail_ (LOD) technique is an optimization that reduces the number of triangles that Unity has to render for a GameObject when its distance from the Camera increases. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LevelOfDetail.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LOD) cross-fade, or alembic animation, refer to the implementation of the `MotionVectors` pass in URP pre-built ShaderLab shaders, for example, the `Unlit.shader` file. The rendering of your `MotionVectors` pass should match your non-motion-vector passes and should reflect any custom deformation and/or vertex animation a pass is performing.
If a custom shader is only intended for objects with transform motion or skinned animation, without using alpha clipping, LOD cross-fade, alembic animation, custom deformation, or vertex animation, the motion vector fallback shader provided by URP might be enough. To add the pre-built fallback shader, add the following ShaderLab command to your SubShader blocks:
```
Shader “Example/MyCustomShaderWithPerObjectMotionVectorFallback"
{
    SubShader
    {
        // ...other passes, SubShader tags, and commands
    
        UsePass "Hidden/Universal Render Pipeline/ObjectMotionVectorFallback/MOTIONVECTORS"
    }
}

```

**Note:** In Unity versions earlier than 2023.2, URP would automatically use the fallback pass for all SubShader blocks which don’t have a pass tagged with the `MotionVectors` [LightMode tag](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-shaders/urp-shaderlab-pass-tags.html). Starting from Unity 2023.2, this fallback logic is disabled for the following reasons:
  * The fallback logic was only an initial implementation detail meant for URP’s own Materials.
  * URP Materials now use material-type-specific motion vector passes to support features like alpha clip, LOD cross-fade, or alembic animation, making the fallback obsolete.
  * The fallback logic was causing unintended visual artifacts for content which it was not applicable to (for example, decals which should not draw any object motion vectors).


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-render-pass.html)
Motion vectors render pass in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/features/motion-vectors-sample.html)
Sample motion vectors in a shader in URP
