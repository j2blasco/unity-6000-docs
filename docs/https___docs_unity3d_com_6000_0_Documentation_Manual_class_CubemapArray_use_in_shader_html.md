* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-use-in-shader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Cubemaps](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)
  * Sample a cubemap array in a shader


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-create.html)
Create a cubemap array
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray.html)
Preview a cubemap array
# Sample a cubemap array in a shader
Here is an example of a **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that uses a **cubemap** A collection of six square textures that can represent the reflections in an environment or the skybox drawn behind your geometry. The six squares form the faces of an imaginary cube that surrounds an object; each face represents the view along the directions of the world axes (up, down, left, right, forward and back). [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cubemap-landing.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Cubemap) array.
```
Shader "CubemapArrayShaderExample" {
Properties {
    _MainTex ("CubemapArray", CubeArray) = "" {}
    _Mip ("Mip", Float) = 0.0
    _Intensity ("Intensity", Float) = 1.0
    _SliceIndex ("Slice", Int) = 0
    _Exposure ("Exposure", Float) = 0.0
}

SubShader {
    Tags {"Queue"="Transparent" "IgnoreProjector"="True" "RenderType"="Transparent" "ForceSupported" = "True"}

    Pass {

        HLSLPROGRAM
        #pragma vertex vert
            #pragma fragment frag
            #pragma require sampleLOD
            #pragma require cubearray
            #include "UnityCG.cginc"
    
    
    
            struct appdata {
                float4 pos : POSITION;
                float3 nor : NORMAL;
            };
    
            struct v2f {
                float3 uv : TEXCOORD0;
                float4 pos : SV_POSITION;
            };
    
            uniform int _SliceIndex;
            float _Mip;
            half _Alpha;
            half _Intensity;
            float _Exposure;
    
           v2f vert (appdata v) {
                v2f o;
                o.pos = UnityObjectToClipPos(v.pos);
                float3 viewDir = -normalize(ObjSpaceViewDir(v.pos));
                o.uv = reflect(viewDir, v.nor);
                return o;
            }
    
            half4 _MainTex_HDR;
            UNITY_DECLARE_TEXCUBEARRAY(_MainTex);
            fixed4 frag (v2f i) : COLOR0
            {
                fixed4 c = UNITY_SAMPLE_TEXCUBEARRAY(_MainTex, float4(i.uv, _SliceIndex));
                fixed4 cmip = UNITY_SAMPLE_TEXCUBEARRAY_LOD(_MainTex, float4(i.uv, _SliceIndex), _Mip);
                if (_Mip >= 0.0)
                    c = cmip;
                c.rgb = DecodeHDR (c, _MainTex_HDR) * _Intensity;
                c.rgb *= exp2(_Exposure);
                c = lerp (c, c.aaaa, _Alpha);
                return c;
            }
            ENDHLSL
        }
    }
    Fallback Off
}


```

If you use this shader with the Cubemap Array created in the example on the [Create a cubemap array](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-create.html) page, the result looks like this:
![A sphere with the rainbow color pattern the shader draws.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/cubemap-array-shader-example.png) A sphere with the rainbow color pattern the shader draws.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray-create.html)
Create a cubemap array
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray.html)
Preview a cubemap array
