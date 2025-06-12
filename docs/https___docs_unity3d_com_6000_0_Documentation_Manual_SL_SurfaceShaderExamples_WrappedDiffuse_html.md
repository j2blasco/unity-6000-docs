* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
  * Wrapped diffuse Surface Shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-Decals.html)
Decals Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-ToonRamp.html)
Toon shading Surface Shader example in the Built-In Render Pipeline
# Wrapped diffuse Surface Shader example in the Built-In Render Pipeline
The following example shows **Wrapped Diffuse** , a modification of **Diffuse** lighting where illumination “wraps around” the edges of objects. It’s useful for simulating subsurface scattering effects. Only the `CGPROGRAM` section changes, so once again, the surrounding **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) code is omitted:
```
    ...ShaderLab code...
    CGPROGRAM
    #pragma surface surf WrapLambert

    half4 LightingWrapLambert (SurfaceOutput s, half3 lightDir, half atten) {
        half NdotL = dot (s.Normal, lightDir);
        half diff = NdotL * 0.5 + 0.5;
        half4 c;
        c.rgb = s.Albedo * _LightColor0.rgb * (diff * atten);
        c.a = s.Alpha;
        return c;
    }

    struct Input {
        float2 uv_MainTex;
    };
    
    sampler2D _MainTex;
        void surf (Input IN, inout SurfaceOutput o) {
        o.Albedo = tex2D (_MainTex, IN.uv_MainTex).rgb;
    }
    ENDCG
    ...ShaderLab code...

```

Here’s how it looks like with a Texture and without a Texture, with one directional Light in the **Scene** A Scene contains the environments and menus of your game. Think of each unique Scene file as a unique level. In each Scene, you place your environments, obstacles, and decorations, essentially designing and building your game in pieces. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CreatingScenes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Scene): 
![Shader using a wrapped diffuse texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderDiffuseWrap.jpg) ![Shader without a texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderDiffuseWrapNoTex.png)
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-Decals.html)
Decals Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-ToonRamp.html)
Toon shading Surface Shader example in the Built-In Render Pipeline
