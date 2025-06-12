* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-ToonRamp.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Writing Surface Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-surface-shaders.html)
  * [Surface Shader examples in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples.html)
  * Toon shading Surface Shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
Wrapped diffuse Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
Global illumination Surface Shader example in the Built-In Render Pipeline
# Toon shading Surface Shader example in the Built-In Render Pipeline
The following example shows a “Ramp” lighting model that uses a Texture ramp to define how surfaces respond to the angles between the light and the normal. This can be used for a variety of effects, and is especially effective when used with **Toon** lighting.
```
    ...ShaderLab code...
    CGPROGRAM
    #pragma surface surf Ramp

    sampler2D _Ramp;

    half4 LightingRamp (SurfaceOutput s, half3 lightDir, half atten) {
        half NdotL = dot (s.Normal, lightDir);
        half diff = NdotL * 0.5 + 0.5;
        half3 ramp = tex2D (_Ramp, float2(diff)).rgb;
        half4 c;
        c.rgb = s.Albedo * _LightColor0.rgb * ramp * atten;
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
![Shader using both a lighting ramp texture and a diffuse texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderToonRamp.jpg) ![Shader using only a lighting ramp texture.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderToonRampNoTex.jpg)
![A lighting ramp texture example.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SurfaceShaderToonRampItself.png) A lighting ramp texture example.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-WrappedDiffuse.html)
Wrapped diffuse Surface Shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SurfaceShaderExamples-GlobalIllumination.html)
Global illumination Surface Shader example in the Built-In Render Pipeline
