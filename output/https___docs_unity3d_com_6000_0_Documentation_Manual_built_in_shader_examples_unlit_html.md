* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-unlit.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * Simple unlit shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-checkerboard.html)
Checkerboard pattern shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-mesh-normals.html)
Mesh normals shader example in the Built-In Render Pipeline
# Simple unlit shader example in the Built-In Render Pipeline
![A purple cat-like character lit using simple shading.](https://docs.unity3d.com/6000.0/Documentation/uploads/SL/ExampleUnlitTextured.png) A purple cat-like character lit using simple shading. ```
Shader "Unlit/SimpleUnlitTexturedShader"
{
    Properties
    {
        // we have removed support for texture tiling/offset,
        // so make them not be displayed in material inspector
        [NoScaleOffset] _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader
    {
        Pass
        {
            HLSLPROGRAM
            // use "vert" function as the vertex shader
            #pragma vertex vert
            // use "frag" function as the pixel (fragment) shader
            #pragma fragment frag

            #include "UnityCG.cginc"

            // vertex shader inputs
            struct appdata
            {
                float4 vertex : POSITION; // vertex position
                float2 uv : TEXCOORD0; // texture coordinate
            };

            // vertex shader outputs ("vertex to fragment")
            struct v2f
            {
                float2 uv : TEXCOORD0; // texture coordinate
                float4 vertex : SV_POSITION; // clip space position
            };

            // vertex shader
            v2f vert (appdata v)
            {
                v2f o;
                // transform position to clip space
                // (multiply with model*view*projection matrix)
                o.vertex = mul(UNITY_MATRIX_MVP, v.vertex);
                // just pass the texture coordinate
                o.uv = v.uv;
                return o;
            }
            
            // texture we will sample
            sampler2D _MainTex;

            // pixel shader; returns low precision ("fixed4" type)
            // color ("SV_Target" semantic)
            fixed4 frag (v2f i) : SV_Target
            {
                // sample texture and return it
                fixed4 col = tex2D(_MainTex, i.uv);
                return col;
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-checkerboard.html)
Checkerboard pattern shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-mesh-normals.html)
Mesh normals shader example in the Built-In Render Pipeline
