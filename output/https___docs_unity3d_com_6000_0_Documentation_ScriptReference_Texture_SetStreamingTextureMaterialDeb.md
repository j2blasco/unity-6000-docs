* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.SetStreamingTextureMaterialDebugProperties.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).SetStreamingTextureMaterialDebugProperties
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public static void SetStreamingTextureMaterialDebugProperties(); 
### Description
This function sets mipmap streaming debug properties on all materials known by the mipmap streaming system.
You can use this function to set up debug shader properties on the materials of all renderers in the scene. To set up renderers and cameras for the mipmap streaming system, see [Texture Streaming](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming.html).  
  
For every streaming Texture a material uses, this function sets up two properties that are called `(Texture property name)_MipInfo` and `(Texture property name)_StreamInfo`. Respectively, they contain the following values: 
  * [streamingMipmapsMaxLevelReduction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-streamingMipmapsMaxLevelReduction.html), minus the number of mips that Unity has stripped in the texture.
  * [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html).
  * [desiredMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-desiredMipmapLevel.html).
  * [loadedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-loadedMipmapLevel.html).


  * [streamingMipmapsPriority](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-streamingMipmapsPriority.html).
  * Time stamp of the latest texture upload.
  * Streaming status code.
  * Unused / 0.


Note that the streaming status code value is set even for non-streaming Textures. The codes set by the mipmap streaming system are: 
  * -1: Texture is correctly streaming.
  * 0: The Mipmap Streaming system does not know this Texture.
  * 1: Mipmap Streaming is disabled for the active Quality level.
  * 2: No texture.
  * 3: Texture has no mipmaps generated, cannot stream.
  * 4: Texture is not set to stream.
  * 5: Texture cannot be asynchronously streamed (player only).
  * 7: Texture has an invalid streaming index within the mipmap streaming system: report a bug.
  * 8: Texture is manually streaming through the use of [requestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html).


Use these properties in your own debug shaders to visualize the current streaming state of any Textures.  
  
For example, when you use this function in a scene with a renderer that has a material with a Texture property named "MainTex", it sets two `float4` properties called `MainTex_MipInfo` and `MainTex_StreamInfo` on the material. The former property contains Streaming Mip Level, Texture Original Mipmap Count, Desired Streaming Mip Level, and Loaded Mip Level in its x, y, z, and w fields while the latter property contains the Texture's Streaming Priority, time stamp of its latest GPU upload, Streaming Status Code and 0 in its x, y, z, and w fields.  
  
For lightmaps, this function sets the `unity_Lightmap_MipInfo` and `unity_Lightmap_StreamInfo` properties.  
  
You can use `Camera.SetReplacementShader` to set a custom Unity shader that a camera renders debugging information for, using the materials you have set up. The following example shader uses these setup properties:
```
          Shader[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Shader.html) "Show Mipmap Streaming[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.Streaming.html)" {
    Properties
    {
        _MainTex("", 2D) = "white" {}
        _Control("Control (RGBA)", 2D) = "red" {}
        _Splat3("Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) 3 (A)", 2D) = "white" {}
        _Splat2("Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) 2 (B)", 2D) = "white" {}
        _Splat1("Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) 1 (G)", 2D) = "white" {}
        _Splat0("Layer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.GraphView.GraphView.Layer.html) 0 (R)", 2D) = "white" {}
        _BaseMap("", 2D) = "white" {}
        _Cutoff("Cutoff", float) = 0.5
    }  
  

    CGINCLUDE
// Common code used by most of the things below
#include "UnityCG.cginc"
    struct v2f
    {
        float4 pos : SV_POSITION;
        float2 uv : TEXCOORD0;
    };
    uniform float4 _MainTex_ST;
    uniform float4 _MainTex_TexelSize;
    uniform float4 _MainTex_MipInfo;  
  
    UNITY_DECLARE_TEX2D(_MainTex);
    UNITY_DECLARE_TEX2D(_SceneViewMipcolorsTexture);  
  
    uint GetMipCount(Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex)
    {
#if defined(SHADER_API_D3D11) || defined(SHADER_API_D3D12) || defined(SHADER_API_D3D11_9X) || defined(SHADER_API_XBOXONE) || defined(SHADER_API_PSSL)
    #define MIP_COUNT_SUPPORTED 1
#endif
#if (defined(SHADER_API_OPENGL) || defined(SHADER_API_VULKAN)) && !defined(SHADER_STAGE_COMPUTE)
        // OpenGL only supports TextureSize for width, height, depth
        // TextureQueryLevels (GL_ARB_Texture_query_levels) needs OpenGL 4.3 or above and doesn't compile in compute shaders
        // tex.GetDimensions converted to TextureQueryLevels
    #define MIP_COUNT_SUPPORTED 1
#endif
        // Metal doesn't support high enough OpenGL version  
  
#if defined(MIP_COUNT_SUPPORTED)
        uint mipLevel, width, height, mipCount;
        mipLevel = width = height = mipCount = 0;
        tex.GetDimensions(mipLevel, width, height, mipCount);
        return mipCount;
#else
        return 0;
#endif
    }  
  
    float4 GetStreamingMipColor(uint mipCount, float4 mipInfo)
    {
        // alpha is amount to blend with source color (0.0 = use original, 1.0 = use new color)  
  
        // mipInfo :
        // x = quality setings minStreamingMipLevel
        // y = original mip count for Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
        // z = desired on screen mip level
        // w = loaded mip level
        uint originalTextureMipCount = uint(mipInfo.y);  
  
        // If material/shader mip info (original mip level) has not been set it’s either not a streamed Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
        // or no renderer is updating it
        if (originalTextureMipCount == 0)
            return float4(0.0, 0.0, 1.0, 0.5);  
  
        uint desiredMipLevel = uint(mipInfo.z);
        uint mipCountDesired = uint(originalTextureMipCount) - uint(desiredMipLevel);
        if (mipCount == 0)
        {
            // Can't calculate, use the passed value
            mipCount = originalTextureMipCount - uint(mipInfo.w);
        }  
  
        if (mipCount < mipCountDesired)
        {
            // red tones when not at the desired mip level (reduction due to budget). Brighter is further from original, alpha 0 when at desired
            float ratioToDesired = float(mipCount) / float(mipCountDesired);
            return float4(1.0, 0.0, 0.0, 1.0 - ratioToDesired);
        }
        else if (mipCount >= originalTextureMipCount)
        {
            // original color when at (or beyond) original mip count
            return float4(1.0, 1.0, 1.0, 0.0);
        }
        else
        {
            // green tones when not at the original mip level. Brighter is closer to original, alpha 0 when at original
            float ratioToOriginal = float(mipCount) / float(originalTextureMipCount);
            return float4(0.0, 1.0, 0.0, 1.0 - ratioToOriginal);
        }
    }  
  
    float3 GetDebugStreamingMipColorBlended(float3 originalColor, Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) tex, float4 mipInfo)
    {
        uint mipCount = GetMipCount(tex);
        float4 mipColor = GetStreamingMipColor(mipCount, mipInfo);
        return lerp(originalColor, mipColor.rgb, mipColor.a);
    }  
  
    v2f vert(appdata_base v)
    {
        v2f o;
        o.pos = UnityObjectToClipPos(v.vertex);
        o.uv = TRANSFORM_TEX(v.texcoord, _MainTex);  
  
        return o;
    }  
  
    fixed4 frag(v2f i) : COLOR
    {
        fixed4 col = UNITY_SAMPLE_TEX2D(_MainTex, i.uv);
        half4 res;
        res.rgb = GetDebugStreamingMipColorBlended(col.rgb, _MainTex, _MainTex_MipInfo);
        res.a = col.a;
        return res;
    }  
  
    struct v2fGrass
    {
        float4 pos : SV_POSITION;
        fixed4 color : COLOR;
        float2 uv : TEXCOORD0;
    };  
  
    fixed4 fragGrass(v2fGrass i) : COLOR
    {
        fixed4 col = UNITY_SAMPLE_TEX2D(_MainTex, i.uv);
        half4 res;
        res.rgb = GetDebugStreamingMipColorBlended(col.rgb, _MainTex, _MainTex_MipInfo);
        res.a = col.a * i.color.a;
        return res;
    }  
  
    ENDCG  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "Opaque" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM  
  
// As both normal opaque shaders and terrain splat shaders
// have "Opaque" render type, we need to do some voodoo
// to make both work.  
  
#pragma vertex vertWTerrain
#pragma fragment fragWTerrain
#pragma target 2.0
#pragma exclude_renderers gles  
  
            struct v2fterr
            {
                float4 pos : SV_POSITION;
                float2 uvnormal : TEXCOORD0;
                float4 uv[3] : TEXCOORD2;
                float nonterrain  : TEXCOORD5;
            };  
  
            uniform float4 _Splat0_ST, _Splat1_ST, _Splat2_ST, _Splat3_ST, _Splat4_ST;
            uniform float4 _Splat0_TexelSize, _Splat1_TexelSize, _Splat2_TexelSize, _Splat3_TexelSize, _Splat4_TexelSize;
            uniform float4 _BaseMap_TexelSize;  
  
            v2fterr vertWTerrain(appdata_base v)
            {
                v2fterr o;
                o.pos = UnityObjectToClipPos(v.vertex);
                // assume it's not a terrain if _Splat0_TexelSize is not set up.
                float nonterrain = _Splat0_TexelSize.z == 0.0 ? 1 : 0;
                // collapse/don't draw terrain's add pass in this mode, since it looks really bad if first pass
                // and add pass blink depending on which gets drawn first with this replacement shader
                // TODO: make it display mips properly even for two-pass terrains.
                o.pos *= _MainTex_TexelSize.z == 0.0 && _Splat0_TexelSize.z != 0.0 ? 0 : 1;
                // normal Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) UV
                o.uvnormal = TRANSFORM_TEX(v.texcoord, _MainTex);
                // terrain splat UVs
                float2 baseUV = v.texcoord.xy;
                o.uv[0].xy = baseUV;
                o.uv[0].zw = half2(0, 0);
                o.uv[1].xy = TRANSFORM_TEX(baseUV, _Splat0);
                o.uv[1].zw = TRANSFORM_TEX(baseUV, _Splat1);
                o.uv[2].xy = TRANSFORM_TEX(baseUV, _Splat2);
                o.uv[2].zw = TRANSFORM_TEX(baseUV, _Splat3);  
  
                o.nonterrain = nonterrain;
                return o;
            }  
  
            UNITY_DECLARE_TEX2D(_Control);
            UNITY_DECLARE_TEX2D(_Splat0);
            UNITY_DECLARE_TEX2D(_Splat1);
            UNITY_DECLARE_TEX2D(_Splat2);
            UNITY_DECLARE_TEX2D(_Splat3);
            UNITY_DECLARE_TEX2D(_BaseMap);
            fixed4 fragWTerrain(v2fterr i) : COLOR
            {
                // sample regular Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html)
                fixed4 colnormal = UNITY_SAMPLE_TEX2D(_MainTex, i.uvnormal);  
  
                // sample splatmaps
                half4 splat_control = UNITY_SAMPLE_TEX2D(_Control, i.uv[0].xy);
                half3 splat_color = splat_control.r * UNITY_SAMPLE_TEX2D(_Splat0, i.uv[1].xy).rgb;
                splat_color += splat_control.g * UNITY_SAMPLE_TEX2D(_Splat1, i.uv[1].zw).rgb;
                splat_color += splat_control.b * UNITY_SAMPLE_TEX2D(_Splat2, i.uv[2].xy).rgb;
                splat_color += splat_control.a * UNITY_SAMPLE_TEX2D(_Splat3, i.uv[2].zw).rgb;  
  
                // lerp between normal and splatmaps
                half3 col = lerp(splat_color, colnormal.rgb, (half)i.nonterrain);  
  
                half4 res;
                // TODO: Take splat mips into account
                res.rgb = GetDebugStreamingMipColorBlended(col.rgb, _MainTex, _MainTex_MipInfo);
                res.a = colnormal.a;  
  
                return res;
            }  
  
            ENDCG
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "Transparent" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            Cull Off
                CGPROGRAM
#pragma vertex vert
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
            ENDCG
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TransparentCutout" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            AlphaTest Greater[_Cutoff]
            CGPROGRAM
#pragma vertex vert
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
            ENDCG
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TreeBark" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
#pragma vertex vertTreeBark
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
#include "UnityCG.cginc"
#include "UnityBuiltin3xTreeLibrary.cginc"
            v2f vertTreeBark(appdata_full v)
            {
                v2f o;
                TreeVertBark(v);
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TreeLeaf" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
#pragma vertex vertTreeLeaf
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
#include "UnityCG.cginc"
#include "UnityBuiltin3xTreeLibrary.cginc"
            v2f vertTreeLeaf(appdata_full v)
            {
                v2f o;
                TreeVertLeaf(v);
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
            AlphaTest GEqual[_Cutoff]
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TreeOpaque" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            CGPROGRAM
#pragma vertex vertTree
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
#include "TerrainEngine.cginc"
            struct appdata
            {
                float4 vertex : POSITION;
                fixed4 color : COLOR;
                float2 texcoord : TEXCOORD0;
            };
            v2f vertTree(appdata v)
            {
                v2f o;
                TerrainAnimateTree(v.vertex, v.color.w);
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TreeTransparentCutout" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            Cull Off
                CGPROGRAM
#pragma vertex vertTree
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
#include "TerrainEngine.cginc"
            struct appdata
            {
                float4 vertex : POSITION;
                fixed4 color : COLOR;
                float4 texcoord : TEXCOORD0;
            };
            v2f vertTree(appdata v)
            {
                v2f o;
                TerrainAnimateTree(v.vertex, v.color.w);
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
            AlphaTest GEqual[_Cutoff]
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "TreeBillboard" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            Cull Off
            ZWrite Off
                      CGPROGRAM
#pragma vertex vertTree
#pragma fragment frag
#pragma target 2.0
#pragma exclude_renderers gles
#include "TerrainEngine.cginc"
            v2f vertTree(appdata_tree_billboard v)
            {
                v2f o;
                TerrainBillboardTree(v.vertex, v.texcoord1.xy, v.texcoord.y);
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv.x = v.texcoord.x;
                o.uv.y = v.texcoord.y > 0;
                return o;
            }  
  
            ENDCG  
  
            SetTexture[_MainTex] { combine primary, Texture[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) }
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "GrassBillboard" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            Cull Off
                                           CGPROGRAM
#pragma vertex vertGrass
#pragma fragment fragGrass
#pragma target 2.0
#pragma exclude_renderers gles
#include "TerrainEngine.cginc"
            v2fGrass vertGrass(appdata_full v)
            {
                v2fGrass o;
                WavingGrassBillboardVert(v);
                o.color = v.color;
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
            AlphaTest Greater[_Cutoff]
        }
    }  
  
    SubShader
    {
        Tags { "ForceSupported" = "True" "RenderType" = "Grass" }
        Pass[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderData.Pass.html)
        {
            Cull Off
                      CGPROGRAM
#pragma vertex vertGrass
#pragma fragment fragGrass
#pragma target 2.0
#pragma exclude_renderers gles
#include "TerrainEngine.cginc"
            v2fGrass vertGrass(appdata_full v)
            {
                v2fGrass o;
                WavingGrassVert(v);
                o.color = v.color;
                o.pos = UnityObjectToClipPos(v.vertex);
                o.uv = v.texcoord;
                return o;
            }  
  
            ENDCG
            AlphaTest Greater[_Cutoff]
        }
    }  
  
    Fallback Off
}

```

* * *
## Declaration
public static void SetStreamingTextureMaterialDebugProperties(int materialTextureSlot); 
### Parameters
Parameter | Description  
---|---  
materialTextureSlot | The material texture slot to refer to when setting up mipmap streaming debug properties.  
### Description
This function sets mipmap streaming debug properties on all materials known by the mipmap streaming system, using data specific to a given material texture slot.
You can use this overload to easily debug any given material texture slot on the materials of all renderers in the scene.  
  
Instead of setting two properties for each material texture property, this function sets the following properties: 
  * A 2D texture property called `unity_MipmapStreaming_DebugTex`.
  * A vector property called `unity_MipmapStreaming_DebugTex_MipInfo`.
  * A vector property called `unity_MipmapStreaming_DebugTex_StreamInfo`.


The values set for these properties correspond to the data known by the mipmap streaming system for the texture in the indicated material texture slot, even if that texture is not streaming.  
  
The mipmap streaming system uses the order in which texture properties appear in the `Properties` block of shaders to determine what a given slot number corresponds to.  
  
Additionally: if `materialTextureSlot` is `-1`, the mipmap streaming system, where it makes sense, aggregates the data of all textures on materials known by the system and sets the previously mentioned properties using that aggregated data. 
  * `unity_MipmapStreaming_DebugTex` is set using the texture assigned to material texture slot 0.
  * `unity_MipmapStreaming_DebugTex_MipInfo` is set to (0, 0, 0, 0), the values are too specific to individual textures to be aggregated.
  * `unity_MipmapStreaming_DebugTex_StreamInfo` is set to (0, Time stamp of the latest texture upload on the material, Packed Streaming Status Code + Streaming Status Flags, 0).


Note that the Streaming Status Codes reserve the 0-15 values. The streaming status flags set by the mipmap streaming system when aggregation occurs are: 
  * 16: The material has Textures that are streaming.
  * 32: The material has Textures that are not streaming.
  * 64: The material has Textures that have issues preventing them from streaming.
  * 128: The material has Textures that are streaming manually through the use of [requestedMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-requestedMipmapLevel.html).
  * No flags set: The material has no Textures.


* * *
