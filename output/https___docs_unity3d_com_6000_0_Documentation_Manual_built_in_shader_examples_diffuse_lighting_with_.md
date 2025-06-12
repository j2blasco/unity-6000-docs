* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * Ambient light shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-simple-diffuse-lighting.html)
Simple diffuse lighting shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-shadow-casting.html)
Shadow casting shader example in the Built-In Render Pipeline
# Ambient light shader example in the Built-In Render Pipeline
![A cat-like character lit using ambient lighting.](https://docs.unity3d.com/6000.0/Documentation/uploads/SL/ExampleDiffuseAmbientLighting.png) A cat-like character lit using ambient lighting.
The example above does not take any ambient lighting or light probes into account. Let’s fix this! It turns out we can do this by adding just a single line of code. Both ambient and [light probe](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)Light probes store information about how light passes through space in your scene. A collection of light probes arranged within a given space can improve lighting on moving objects and static LOD scenery within that space. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#LightProbe) data is passed to **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) in Spherical Harmonics form, and **ShadeSH9** function from **UnityCG.cginc** [include file](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html) does all the work of evaluating it, given a world space normal.
```
Shader "Lit/Diffuse With Ambient"
{
    Properties
    {
        [NoScaleOffset] _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Pass
        {
            Tags {"LightMode"="ForwardBase"}
        
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            #include "UnityLightingCommon.cginc"

            struct v2f
            {
                float2 uv : TEXCOORD0;
                fixed4 diff : COLOR0;
                float4 vertex : SV_POSITION;
            };

            v2f vert (appdata_base v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                half3 worldNormal = UnityObjectToWorldNormal(v.normal);
                half nl = max(0, dot(worldNormal, _WorldSpaceLightPos0.xyz));
                o.diff = nl * _LightColor0;

                // the only difference from previous shader:
                // in addition to the diffuse lighting from the main light,
                // add illumination from ambient or light probes
                // ShadeSH9 function from UnityCG.cginc evaluates it,
                // using world space normal
                o.diff.rgb += ShadeSH9(half4(worldNormal,1));
                return o;
            }
            
            sampler2D _MainTex;

            fixed4 frag (v2f i) : SV_Target
            {
                fixed4 col = tex2D(_MainTex, i.uv);
                col *= i.diff;
                return col;
            }
            ENDHLSL
        }
    }
}

```

This shader is in fact starting to look very similar to the built-in [Legacy Diffuse](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-NormalDiffuse.html) shader!
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-simple-diffuse-lighting.html)
Simple diffuse lighting shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-shadow-casting.html)
Shadow casting shader example in the Built-In Render Pipeline
