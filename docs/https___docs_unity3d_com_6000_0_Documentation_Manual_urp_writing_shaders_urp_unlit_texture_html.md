* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-texture.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/shaders-in-universalrp.html)
  * [Writing custom shaders in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-custom-shaders-urp.html)
  * [Examples of writing a custom shader in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-landing.html)
  * Draw a texture in a shader in URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-color.html)
Write an unlit shader with color input in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html)
Visualize normal vectors in a shader in URP
# Draw a texture in a shader in URP
The Unity **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in this example draws a texture on the **mesh** The main graphics primitive of Unity. Meshes make up a large part of your 3D worlds. Unity supports triangulated or Quadrangulated polygon meshes. Nurbs, Nurms, Subdiv surfaces must be converted to polygons. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/mesh.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Mesh).
Use the Unity shader source file from section [URP unlit shader with color input](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-color.html) and make the following changes to the **ShaderLab** Unity’s language for defining the structure of Shader objects. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Shader.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ShaderLab) code:
  1. In the Properties block, replace the existing code with the `_BaseMap` property definition.
```
Properties
{
    [MainTexture] _BaseMap("Base Map", 2D) = "white" {}
}

```

When you declare a texture property in the Properties block, Unity adds the `_BaseMap` property with the label **Base Map** to the Material, and adds the Tiling and the Offset controls.
![Texture property with Tiling and Offset controls](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/unlit-shader-tutorial-texture-property-in-inspector.png) “Texture property with Tiling and Offset controls”
When you declare a property with the `[MainTexture]` attribute, Unity uses this property as the [main texture](https://docs.unity3d.com/ScriptReference/Material-mainTexture.html) of the Material.
> **Note** : For compatibility reasons, the `_MainTex` property name is a reserved name. Unity uses a property with the name `_MainTex` as the [main texture](https://docs.unity3d.com/ScriptReference/Material-mainTexture.html) even it does not have the `[MainTexture]` attribute.
  2. In `struct Attributes` and `struct Varyings`, add the `uv` variable for the UV coordinates on the texture:
```
float2 uv           : TEXCOORD0;

```

  3. Define the texture as a 2D texture and specify a sampler for it. Add the following lines before the CBUFFER block:
```
TEXTURE2D(_BaseMap);
SAMPLER(sampler_BaseMap);

```

The TEXTURE2D and the SAMPLER macros are defined in one of the files referenced in `Core.hlsl`.
  4. For tiling and offset to work, it’s necessary to declare the texture property with the `_ST` suffix in the ‘CBUFFER’ block. The `_ST` suffix is necessary because some macros (for example, `TRANSFORM_TEX`) use it.
> **Note** : To ensure that the Unity shader is SRP Batcher compatible, declare all Material properties inside a single `CBUFFER` block with the name `UnityPerMaterial`. For more information on the SRP Batcher, refer to the documentation on the [Scriptable Render Pipeline (SRP) Batcher](https://docs.unity3d.com/Manual/SRPBatcher.html).
```
CBUFFER_START(UnityPerMaterial)
    float4 _BaseMap_ST;
CBUFFER_END

```

  5. To apply the tiling and offset transformation, add the following line in the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader):
```
OUT.uv = TRANSFORM_TEX(IN.uv, _BaseMap);

```

The `TRANSFORM_TEX` macro is defined in the `Macros.hlsl` file. The `#include` declaration contains a reference to that file.
  6. In the fragment shader, use the `SAMPLE_TEXTURE2D` macro to sample the texture:
```
half4 frag(Varyings IN) : SV_Target
{
    half4 color = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, IN.uv);
    return color;
}

```



Now you can select a texture in the **Base Map** field in the **Inspector** A Unity window that displays information about the currently selected GameObject, asset or project settings, allowing you to inspect and edit the values. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/UsingTheInspector.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Inspector) window. The shader draws that texture on the mesh.
![Base Map texture on a Material](https://docs.unity3d.com/6000.0/Documentation/uploads/urp/shader-examples/unlit-shader-tutorial-texture-with-scene.png) Base Map texture on a Material
Below is the complete ShaderLab code for this example.
```
// This shader draws a texture on the mesh.
Shader "Example/URPUnlitShaderTexture"
{
    // The _BaseMap variable is visible in the Material's Inspector, as a field
    // called Base Map.
    Properties
    {
        [MainTexture] _BaseMap("Base Map", 2D) = "white" {}
    }

    SubShader
    {
        Tags { "RenderType" = "Opaque" "RenderPipeline" = "UniversalPipeline" }

        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag

            #include "Packages/com.unity.render-pipelines.universal/ShaderLibrary/Core.hlsl"

            struct Attributes
            {
                float4 positionOS   : POSITION;
                // The uv variable contains the UV coordinate on the texture for the
                // given vertex.
                float2 uv           : TEXCOORD0;
            };

            struct Varyings
            {
                float4 positionHCS  : SV_POSITION;
                // The uv variable contains the UV coordinate on the texture for the
                // given vertex.
                float2 uv           : TEXCOORD0;
            };

            // This macro declares _BaseMap as a Texture2D object.
            TEXTURE2D(_BaseMap);
            // This macro declares the sampler for the _BaseMap texture.
            SAMPLER(sampler_BaseMap);

            CBUFFER_START(UnityPerMaterial)
                // The following line declares the _BaseMap_ST variable, so that you
                // can use the _BaseMap variable in the fragment shader. The _ST
                // suffix is necessary for the tiling and offset function to work.
                float4 _BaseMap_ST;
            CBUFFER_END

            Varyings vert(Attributes IN)
            {
                Varyings OUT;
                OUT.positionHCS = TransformObjectToHClip(IN.positionOS.xyz);
                // The TRANSFORM_TEX macro performs the tiling and offset
                // transformation.
                OUT.uv = TRANSFORM_TEX(IN.uv, _BaseMap);
                return OUT;
            }

            half4 frag(Varyings IN) : SV_Target
            {
                // The SAMPLE_TEXTURE2D marco samples the texture with the given
                // sampler.
                half4 color = SAMPLE_TEXTURE2D(_BaseMap, sampler_BaseMap, IN.uv);
                return color;
            }
            ENDHLSL
        }
    }
}

```

Section [Visualizing normal vectors](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html) shows how to visualize normal vectors on the mesh.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-color.html)
Write an unlit shader with color input in URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/writing-shaders-urp-unlit-normals.html)
Visualize normal vectors in a shader in URP
