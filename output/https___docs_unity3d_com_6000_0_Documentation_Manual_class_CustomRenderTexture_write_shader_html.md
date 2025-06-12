* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-write-shader.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Rendering to a texture](https://docs.unity3d.com/6000.0/Documentation/Manual/render-texture-landing.html)
  * [Drawing to textures with shaders via Custom Render Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-landing.html)
  * Write a shader for a Custom Render Texture


[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-create.html)
Create a Custom Render Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-configure.html)
Control when a Custom Render Texture updates
# Write a shader for a Custom Render Texture
To update a Custom **Render Texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) manually, you can write a specialized Custom Render Texture **shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader).
To help you write your Custom Render Texture shaders, here are two example frameworks that contain utility functions and built-in helper variables.
The following shader example fills the texture with a color multiplied by a color. When you write a shader for a Custom Render Texture, you must do the following:
  * `#include "UnityCustomRenderTexture.cginc"`.
  * Use the provided **Vertex Shader** A program that runs on each vertex of a 3D model when the model is being rendered. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#vertexshader) `CustomRenderTextureVertexShader`.
  * Use the provided input structure `v2f_customrendertexture` for the **pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel) shader.

```
Shader "CustomRenderTexture/Simple"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _Tex("InputTex", 2D) = "white" {}
     }

     SubShader
     {
        Lighting Off
        Blend One Zero

        Pass
        {
            HLSLPROGRAM
            #include "UnityCustomRenderTexture.cginc"
            #pragma vertex CustomRenderTextureVertexShader
            #pragma fragment frag
            #pragma target 3.0

            float4      _Color;
            sampler2D   _Tex;

            float4 frag(v2f_customrendertexture IN) : COLOR
            {
                return _Color * tex2D(_Tex, IN.localTexcoord.xy);
            }
            ENDHLSL
            }
    }
}

```

The following example is a shader for a material you can use to initialize a Custom Render Texture. When you write a shader for an initialization Material, the following steps are mandatory:
  * `#include "UnityCustomRenderTexture.cginc"`
  * Use the provided Vertex Shader `CustomRenderTextureVertexShader`
  * Use the provided input structure `v2f_customrendertexture` for the pixel shader.

```
Shader "CustomRenderTexture/CustomTextureInit"
{
    Properties
    {
        _Color ("Color", Color) = (1,1,1,1)
        _Tex("InputTex", 2D) = "white" {}
    }

    SubShader
    {
        Lighting Off
        Blend One Zero

        Pass
        {
            HLSLPROGRAM
            #include "UnityCustomRenderTexture.cginc"

            #pragma vertex InitCustomRenderTextureVertexShader
            #pragma fragment frag
            #pragma target 3.0

            float4      _Color;
            sampler2D   _Tex;

            float4 frag(v2f_init_customrendertexture IN) : COLOR
            {
                return _Color * tex2D(_Tex, IN.texcoord.xy);
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-create.html)
Create a Custom Render Texture
[](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CustomRenderTexture-configure.html)
Control when a Custom Render Texture updates
