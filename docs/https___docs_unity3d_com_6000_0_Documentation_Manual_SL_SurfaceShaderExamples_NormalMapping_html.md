* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-NormalMapping.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
  * Normal mapping Surface Shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
Surface Shader examples in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-Reflection.html)
Reflection Surface Shader examples in the Built-In Render Pipeline
# Normal mapping Surface Shader example in the Built-In Render Pipeline
![Shader example that uses normal mapping.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderDiffuseBump.jpg) Shader example that uses normal mapping. ```
  Shader "Example/Diffuse Bump" {
    Properties {
      _MainTex ("Texture", 2D) = "white" {}
      _BumpMap ("Bumpmap", 2D) = "bump" {}
    }
    SubShader {
      Tags { "RenderType" = "Opaque" }
      CGPROGRAM
      #pragma surface surf Lambert
      struct Input {
        float2 uv_MainTex;
        float2 uv_BumpMap;
      };
      sampler2D _MainTex;
      sampler2D _BumpMap;
      void surf (Input IN, inout SurfaceOutput o) {
        o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
        o.Normal = UnpackNormal (tex2D (_BumpMap, IN.uv_BumpMap));
      }
      ENDCG
    } 
    Fallback "Diffuse"
  }

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
Surface Shader examples in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-Reflection.html)
Reflection Surface Shader examples in the Built-In Render Pipeline
