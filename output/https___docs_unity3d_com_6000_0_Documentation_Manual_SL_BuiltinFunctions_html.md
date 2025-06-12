* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinFunctions.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-built-in-birp-landing.html)
  * [Writing custom shaders in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shaders-birp.html)
  * [Shader methods in the Built-In Render Pipeline](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html)
  * Use built-in shader functions in the Built-In Render Pipeline


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html)
Import a file from the shader library in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-grabpass.html)
Get the current framebuffer with the GrabPass command in the Built-In Render Pipeline
# Use built-in shader functions in the Built-In Render Pipeline
Unity has a number of built-in utility functions in UnityCG.cginc designed to make writing **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) simpler and easier.
## Transform positions
**Function:** | **Description:**  
---|---  
`float4 UnityObjectToClipPos(float3 pos)` | Transforms a point from object space to the **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera)’s clip space in homogeneous coordinates. This is the equivalent of **mul(UNITY_MATRIX_MVP, float4(pos, 1.0))** , and should be used in its place.  
`float3 UnityObjectToViewPos(float3 pos)` | Transforms a point from object space to view space. This is the equivalent of **mul(UNITY_MATRIX_MV, float4(pos, 1.0)).xyz** , and should be used in its place.  
### Transform other values
**Function:** | **Description:**  
---|---  
`float3 WorldSpaceViewDir (float4 v)` | Returns world space direction (not normalized) from given object space vertex position towards the camera.  
`float3 ObjSpaceViewDir (float4 v)` | Returns object space direction (not normalized) from given object space vertex position towards the camera.  
`float2 ParallaxOffset (half h, half height, half3 viewDir)` | calculates UV offset for parallax normal mapping.  
`fixed Luminance (fixed3 c)` | Converts color to luminance (grayscale).  
`fixed3 DecodeLightmap (fixed4 color)` | Decodes color from Unity **lightmap** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) (RGBM or dLDR depending on platform).  
`float4 EncodeFloatRGBA (float v)` | Encodes (0..1) range float into RGBA color, for storage in low precision render target.  
`float DecodeFloatRGBA (float4 enc)` | Decodes RGBA color into a float.  
`float2 EncodeFloatRG (float v)` | Encodes (0..1) range float into a float2.  
`float DecodeFloatRG (float2 enc)` | Decodes a previously-encoded RG float.  
`float2 EncodeViewNormalStereo (float3 n)` | Encodes view space normal into two numbers in 0..1 range.  
`float3 DecodeViewNormalStereo (float4 enc4)` | Decodes view space normal from enc4.xy.  
## Forward rendering helper functions
These functions are only useful when using **forward rendering** A rendering path that renders each object in one or more passes, depending on lights that affect the object. Lights themselves are also treated differently by Forward Rendering, depending on their settings and intensity. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/RenderTech-ForwardRendering.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#ForwardRendering) (ForwardBase or ForwardAdd pass types).
**Function:** | **Description:**  
---|---  
`float3 WorldSpaceLightDir (float4 v)` | Computes world space direction (not normalized) to light, given object space vertex position.  
`float3 ObjSpaceLightDir (float4 v)` | Computes object space direction (not normalized) to light, given object space vertex position.  
`float3 Shade4PointLights (...)` | Computes illumination from four point lights, with light data tightly packed into vectors. Forward rendering uses this to compute per-vertex lighting.  
## Screen-space helper functions
The following functions are helpers to compute coordinates used for sampling screen-space textures. They return `float4` where the final coordinate to sample texture with can be computed via perspective division (for example `xy/w`).
The functions also take care of [platform differences](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PlatformDifferences.html) in **render texture** A special type of Texture that is created and updated at runtime. To use them, first create a new Render Texture and designate one of your Cameras to render into it. Then you can use the Render Texture in a Material just like a regular Texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-RenderTexture.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#RenderTexture) coordinates.
**Function:** | **Description:**  
---|---  
`float4 ComputeScreenPos (float4 clipPos)` | Computes texture coordinate for doing a screenspace-mapped texture sample. Input is clip space position.  
`float4 ComputeGrabScreenPos (float4 clipPos)` | Computes texture coordinate for sampling a [GrabPass](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-GrabPass.html) texure. Input is clip space position.  
## Vertex-lit helper functions
These functions are only useful when using per-vertex lit shaders (“Vertex” pass type).
**Function:** | **Description:**  
---|---  
`float3 ShadeVertexLights (float4 vertex, float3 normal)` | Computes illumination from four per-vertex lights and ambient, given object space position & normal.  
## Shadow mapping macros
Declaring and sampling shadow maps can be very different depending on the platform. Unity has several macros to help with this:
**Macro:** | **Use:**  
---|---  
`UNITY_DECLARE_SHADOWMAP(tex)` | Declares a shadowmap Texture variable with name “tex”.  
`UNITY_SAMPLE_SHADOW(tex,uv)` | Samples shadowmap Texture “tex” at given “uv” coordinate (XY components are Texture location, Z component is depth to compare with). Returns single float value with the shadow term in 0..1 range.  
`UNITY_SAMPLE_SHADOW_PROJ(tex,uv)` | Similar to above, but does a projective shadowmap read. “uv” is a float4, all other components are divided by .w for doing the lookup.  
The format of `tex` must be [RenderTextureFormat.Shadowmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Shadowmap.html).
**NOTE:** Not all graphics cards support shadowmaps. Use [SystemInfo.SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html) to check for support.
## Depth Texture helper macros
Most of the time, Depth Texture are used to render Depth from the Camera. The [UnityCG.cginc include file](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html) contains some macros to deal with the above complexity in this case:
  * **COMPUTE_EYEDEPTH(i)** : computes eye space depth of the vertex and outputs it in **o**. Use it in a vertex program when **not** rendering into a depth texture.
  * **DECODE_EYEDEPTH(i)/LinearEyeDepth(i)** : given high precision value from depth texture **i** , returns corresponding eye space depth.
  * **Linear01Depth(i)** : given high precision value from depth texture **i** , returns corresponding linear depth in range between 0 and 1.
  * **UNITY_TRANSFER_DEPTH(o)** : Deprecated. Computes the eye space depth of the vertex and outputs it in **o** (which must be a float2). On platforms with native depth textures this macro does nothing, because the Z buffer value is rendered implicitly.
  * **UNITY_OUTPUT_DEPTH(i)** : Deprecated. Returns eye space depth from **i** (which must be a float2). On platforms with native depth textures this macro always returns zero, because the Z buffer value is rendered implicitly.


**Note:** On DX11/12 and Metal, the Z buffer range is 1–0 and UNITY_REVERSED_Z is defined. On other platforms, the range is 0–1.
For example, this shader would render depth of its **GameObjects** The fundamental object in Unity scenes, which can represent characters, props, scenery, cameras, waypoints, and more. A GameObject’s functionality is defined by the Components attached to it. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-GameObject.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#GameObject):
```
Shader "Render Depth" {
    SubShader {
        Tags { "RenderType"="Opaque" }
        Pass {
            HLSLPROGRAM

            #pragma vertex vert
            #pragma fragment frag
            #include "UnityCG.cginc"

            struct v2f {
                float4 pos : SV_POSITION;
                float2 depth : TEXCOORD0;
            };

            v2f vert (appdata_base v) {
                v2f o;
                o.pos = UnityObjectToClipPos(v.vertex);
                UNITY_TRANSFER_DEPTH(o.depth);
                return o;
            }

            half4 frag(v2f i) : SV_Target {
                UNITY_OUTPUT_DEPTH(i.depth);
            }
            ENDHLSL
        }
    }
}

```

* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html)
Import a file from the shader library in the Built-In Render Pipeline
[](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-grabpass.html)
Get the current framebuffer with the GrabPass command in the Built-In Render Pipeline
