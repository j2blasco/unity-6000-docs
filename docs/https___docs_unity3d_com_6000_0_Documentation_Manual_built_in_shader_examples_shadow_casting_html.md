* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-shadow-casting.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [HLSL shader examples in the Built-in Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
  * Shadow casting shader example in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
Ambient light shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-receive-shadows.html)
Receiving shadows shader example in the Built-In Render Pipeline
# Shadow casting shader example in the Built-In Render Pipeline
![A cat-like character floats above a plane and casts a shadow onto it.](https://docs.unity3d.com/6000.0/Documentation/uploads/SL/ExampleShadowCasting.png) A cat-like character floats above a plane and casts a shadow onto it.
Our **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) currently can neither receive nor cast shadows. Let’s implement shadow casting first.
In order to cast shadows, a shader has to have a **ShadowCaster** [pass type](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PassTags.html) in any of its [subshaders](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SubShader.html) or any [fallback](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Fallback.html). The ShadowCaster pass is used to render the object into the shadowmap, and typically it is fairly simple - the **vertex shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) only needs to evaluate the vertex position, and the fragment shader pretty much does not do anything. The shadowmap is only the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer), so even the color output by the fragment shader does not really matter.
This means that for a lot of shaders, the shadow caster pass is going to be almost exactly the same (unless object has custom vertex shader based deformations, or has alpha cutout / semitransparent parts). The easiest way to pull it in is via [UsePass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-UsePass.html) shader command:
```
Pass
{
    // regular lighting pass
}
// pull in shadow caster from VertexLit built-in shader
UsePass "Legacy Shaders/VertexLit/SHADOWCASTER"

```

However we’re learning here, so let’s do the same thing “by hand” so to speak. For shorter code, we’ve replaced the lighting pass (“ForwardBase”) with code that only does untextured ambient. Below it, there’s a “ShadowCaster” pass that makes the object support shadow casting.
```
Shader "Lit/Shadow Casting"
{
    SubShader
    {
        // very simple lighting pass, that only does non-textured ambient
        Pass
        {
            Tags {"LightMode"="ForwardBase"}
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"
            struct v2f
            {
                fixed4 diff : COLOR0;
                float4 vertex : SV_POSITION;
            };
            v2f vert (appdata_base v)
            {
                v2f o;
                o.vertex = UnityObjectToClipPos(v.vertex);
                half3 worldNormal = UnityObjectToWorldNormal(v.normal);
                // only evaluate ambient
                o.diff.rgb = ShadeSH9(half4(worldNormal,1));
                o.diff.a = 1;
                return o;
            }
            fixed4 frag (v2f i) : SV_Target
            {
                return i.diff;
            }
            ENDHLSL
        }

        // shadow caster rendering pass, implemented manually
        // using macros from UnityCG.cginc
        Pass
        {
            Tags {"LightMode"="ShadowCaster"}

            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #pragma multi_compile_shadowcaster
            #include "UnityCG.cginc"

            struct v2f { 
                V2F_SHADOW_CASTER;
            };

            v2f vert(appdata_base v)
            {
                v2f o;
                TRANSFER_SHADOW_CASTER_NORMALOFFSET(o)
                return o;
            }

            float4 frag(v2f i) : SV_Target
            {
                SHADOW_CASTER_FRAGMENT(i)
            }
            ENDHLSL
        }
    }
}

```

Now there’s a plane underneath, using a regular built-in Diffuse shader, so that we can see our shadows working (remember, our current shader does not support _receiving_ shadows yet!).
We’ve used the **#pragma multi_compile_shadowcaster** directive. This causes the shader to be compiled into several variants with different preprocessor macros defined for each (see [multiple shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-MultipleProgramVariants.html) page for details). When rendering into the shadowmap, the cases of point lights vs other light types need slightly different shader code, that’s why this directive is needed.
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-diffuse-lighting-with-ambient-light.html)
Ambient light shader example in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples-receive-shadows.html)
Receiving shadows shader example in the Built-In Render Pipeline
