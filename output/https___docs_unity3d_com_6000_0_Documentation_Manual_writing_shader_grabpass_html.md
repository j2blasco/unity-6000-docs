* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-grabpass.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * Get the current framebuffer with the GrabPass command in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html)
Use built-in shader functions in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
HLSL shader examples in the Built-in Render Pipeline
# Get the current framebuffer with the GrabPass command in the Built-In Render Pipeline
GrabPass is a command that creates a special type of Pass that grabs the contents of the frame buffer into a texture. This texture can be used in subsequent Passes to do advanced image based effects.
This command can significantly increase both CPU and GPU frame times. You should generally avoid using this command other than for quick prototyping, and attempt to achieve your effect in other ways. If you do use this command, try to reduce the number of screen grabbing operations as much as possible; either by reducing your usage of this command, or by using the signature that grabs the screen to a named texture if applicable.
GrabPass works only on the frame buffer. You cannot use this command to grab the contents of other render targets, the **depth buffer** A memory store that holds the z-value depth of each pixel in an image, where the z-value is the depth for each rendered pixel from the projection plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#depthbuffer), and so on.
## Examples
This example for the Built-in **Render Pipeline** A series of operations that take the contents of a Scene, and displays them on a screen. Unity lets you choose from pre-built render pipelines, or write your own. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/render-pipelines.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Renderpipeline) demonstrates using `GrabPass` to invert the colors of the render target. Note that this is not an efficient way to achieve this effect, and is intended only to demonstrate the use of GrabPass; the same effect could be achieved more efficiently using an invert blend mode.
```
Shader "GrabPassInvert"
{
    SubShader
    {
        // Draw after all opaque geometry
        Tags { "Queue" = "Transparent" }

        // Grab the screen behind the object into _BackgroundTexture
        GrabPass
        {
            "_BackgroundTexture"
        }

        // Render the object with the texture generated above, and invert the colors
        Pass
        {
            HLSLPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            struct v2f
            {
                float4 grabPos : TEXCOORD0;
                float4 pos : SV_POSITION;
            };

            v2f vert(appdata_base v) {
                v2f o;
                // use UnityObjectToClipPos from UnityCG.cginc to calculate 
                // the clip-space of the vertex
                o.pos = UnityObjectToClipPos(v.vertex);

                // use ComputeGrabScreenPos function from UnityCG.cginc
                // to get the correct texture coordinate
                o.grabPos = ComputeGrabScreenPos(o.pos);
                return o;
            }

            sampler2D _BackgroundTexture;

            half4 frag(v2f i) : SV_Target
            {
                half4 bgcolor = tex2Dproj(_BackgroundTexture, i.grabPos);
                return 1 - bgcolor;
            }
            ENDHLSL
        }

    }
}


```

## 
## Provide fragment color as input
Some GPUs (most notably PowerVR-based ones on iOS) allow you to do a form of programmable blending by providing current fragment color as input to the Fragment **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) (refer to `EXT_shader_framebuffer_fetch` on [khronos.org](https://www.khronos.org/registry/gles/extensions/EXT/EXT_shader_framebuffer_fetch.txt)). This process is sometimes called framebuffer fetch.
To do this, use the `inout` color argument when you write a fragment shader. For example:
```
HLSLPROGRAM
// only compile Shader for platforms that can potentially
// do it (currently gles,gles3,metal)
#pragma only_renderers framebufferfetch

void frag (v2f i, inout half4 ocol : SV_Target)
{
    // ocol can be read (current framebuffer color)
    // and written into (will change color to that one)
    // ...
}
ENDHLSL

```

## Additional resources
  * [GrabPass directive in ShaderLab reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html)
Use built-in shader functions in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/built-in-shader-examples.html)
HLSL shader examples in the Built-in Render Pipeline
