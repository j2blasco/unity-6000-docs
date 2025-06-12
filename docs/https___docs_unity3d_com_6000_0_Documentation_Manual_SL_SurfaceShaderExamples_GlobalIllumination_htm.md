* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
  * Global illumination Surface Shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-ToonRamp.html)
Toon shading Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html)
Tessellation Surface Shader examples in the Built-In Render Pipeline
# Global illumination Surface Shader example in the Built-In Render Pipeline
We’ll start with a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that mimics Unity’s built-in GI:
```
    Shader "Example/CustomGI_ToneMapped" {
        Properties {
            _MainTex ("Albedo (RGB)", 2D) = "white" {}
        }
        SubShader {
            Tags { "RenderType"="Opaque" }
            
            CGPROGRAM
            #pragma surface surf StandardDefaultGI
    
            #include "UnityPBSLighting.cginc"
    
            sampler2D _MainTex;
    
            inline half4 LightingStandardDefaultGI(SurfaceOutputStandard s, half3 viewDir, UnityGI gi)
            {
                return LightingStandard(s, viewDir, gi);
            }
    
            inline void LightingStandardDefaultGI_GI(
                SurfaceOutputStandard s,
                UnityGIInput data,
                inout UnityGI gi)
            {
                LightingStandard_GI(s, data, gi);
            }
    
            struct Input {
                float2 uv_MainTex;
            };
    
            void surf (Input IN, inout SurfaceOutputStandard o) {
                o.Albedo = tex2D(_MainTex, IN.uv_MainTex);
            }
            ENDCG
        }
        FallBack "Diffuse"
    }

```

Now, let’s add some tone mapping on top of the GI:
```
    Shader "Example/CustomGI_ToneMapped" {
        Properties {
            _MainTex ("Albedo (RGB)", 2D) = "white" {}
            _Gain("Lightmap tone-mapping Gain", Float) = 1
            _Knee("Lightmap tone-mapping Knee", Float) = 0.5
            _Compress("Lightmap tone-mapping Compress", Float) = 0.33
        }
        SubShader {
            Tags { "RenderType"="Opaque" }
            
            CGPROGRAM
            #pragma surface surf StandardToneMappedGI
    
            #include "UnityPBSLighting.cginc"
    
            half _Gain;
            half _Knee;
            half _Compress;
            sampler2D _MainTex;
    
            inline half3 TonemapLight(half3 i) {
                i *= _Gain;
                return (i > _Knee) ? (((i - _Knee)*_Compress) + _Knee) : i;
            }
    
            inline half4 LightingStandardToneMappedGI(SurfaceOutputStandard s, half3 viewDir, UnityGI gi)
            {
                return LightingStandard(s, viewDir, gi);
            }
    
            inline void LightingStandardToneMappedGI_GI(
                SurfaceOutputStandard s,
                UnityGIInput data,
                inout UnityGI gi)
            {
                LightingStandard_GI(s, data, gi);
    
                gi.light.color = TonemapLight(gi.light.color);
                #ifdef DIRLIGHTMAP_SEPARATE
                    #ifdef LIGHTMAP_ON
                        gi.light2.color = TonemapLight(gi.light2.color);
                    #endif
                    #ifdef DYNAMICLIGHTMAP_ON
                        gi.light3.color = TonemapLight(gi.light3.color);
                    #endif
                #endif
                gi.indirect.diffuse = TonemapLight(gi.indirect.diffuse);
                gi.indirect.specular = TonemapLight(gi.indirect.specular);
            }
    
            struct Input {
                float2 uv_MainTex;
            };
    
            void surf (Input IN, inout SurfaceOutputStandard o) {
                o.Albedo = tex2D(_MainTex, IN.uv_MainTex);
            }
            ENDCG
        }
        FallBack "Diffuse"
    }

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-ToonRamp.html)
Toon shading Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderTessellation.html)
Tessellation Surface Shader examples in the Built-In Render Pipeline
