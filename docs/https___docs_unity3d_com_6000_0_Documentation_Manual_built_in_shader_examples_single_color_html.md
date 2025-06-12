* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-single-color.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * Single color shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
HLSL shader examples in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-checkerboard.html)
Checkerboard pattern shader example in the Built-In Render Pipeline
# Single color shader example in the Built-In Render Pipeline
![A cat-like character rendered using a single color, to create a silhouette.](https://docs.unity3d.com/6000.0/Documentation/uploads/SL/ExampleSingleColor.png) A cat-like character rendered using a single color, to create a silhouette. ```
Shader "Unlit/SingleColor"
{
    Properties
    {
        // Color property for material inspector, default to white
        _Color ("Main Color", Color) = (1,1,1,1)
    }
    SubShader
    {
        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            
            // vertex shader
            // this time instead of using "appdata" struct, just spell inputs manually,
            // and instead of returning v2f struct, also just return a single output
            // float4 clip position
            float4 vert (float4 vertex : POSITION) : SV_POSITION
            {
                return mul(UNITY_MATRIX_MVP, vertex);
            }
            
            // color from the material
            fixed4 _Color;

            // pixel shader, no inputs needed
            fixed4 frag () : SV_Target
            {
                return _Color; // just return it
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
HLSL shader examples in the Built-in Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-checkerboard.html)
Checkerboard pattern shader example in the Built-In Render Pipeline
