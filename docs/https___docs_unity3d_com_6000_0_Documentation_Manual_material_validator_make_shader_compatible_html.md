* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/material-validator-make-shader-compatible.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Materials](https://docs.unity3d.com/6000.0/Documentation/Manual/Materials.html)
  * [Material Validator in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-troubleshooting.html)
  * Make a shader compatible with the Material Validator in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-validator-validate.html)
Validate and correct materials in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialValidator.html)
Material Validator window reference for the Built-In Render Pipeline
# Make a shader compatible with the Material Validator in the Built-In Render Pipeline
The Material Validator works with any Materials that use Unity’s [Standard shader](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-StandardShader.html) or [surface shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)A streamlined way of writing shaders for the Built-in Render Pipeline. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#SurfaceShader). However, custom **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) require a pass named `“META”`. Most custom shaders that support lightmapping already have this pass defined. See documentation on [Lightmapping and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html) for more details. 
Carry out the following steps to make your custom shader compatible with the Material Validator:
  1. Add the following pragma to the meta pass: `#pragma shader_feature EDITOR_VISUALIZATION`
  2. In the `UnityMetaInput` structure, assign the **specular color** The color of a specular highlight.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#specularcolor) of the Material to the field called `SpecularColor`, as shown in the code example below.


Here is an example of a custom meta pass:
```
Pass
{
    Name "META" 
    Tags { "LightMode"="Meta" }

    Cull Off

    CGPROGRAM
    #pragma vertex vert_meta
    #pragma fragment frag_meta

    #pragma shader_feature _EMISSION
    #pragma shader_feature _METALLICGLOSSMAP
    #pragma shader_feature _ _SMOOTHNESS_TEXTURE_ALBEDO_CHANNEL_A
    #pragma shader_feature ___ _DETAIL_MULX2
    #pragma shader_feature EDITOR_VISUALIZATION

    float4 frag_meta(v2f_meta i) : SV_TARGET
    {
        UnityMetaInput input;
        UNITY_INITIALIZE_OUTPUT(UnityMetaInput, input);
        float4 materialSpecularColor = float4(1.0f, 0.0f, 0.0f, 1.0f);
        float4 materialAlbedo = float4(0.0f, 1.0f, 0.0f, 1.0f);
        input.SpecularColor = materialSpecularColor;
        input.Albedo = materialAlbedo;

        return UnityMetaFragment(input);
    }  
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/material-validator-validate.html)
Validate and correct materials in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/MaterialValidator.html)
Material Validator window reference for the Built-In Render Pipeline
