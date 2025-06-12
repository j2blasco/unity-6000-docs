* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/SL-SamplerStates.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Writing a custom shader in ShaderLab and HLSL](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-landing.html)
  * [Writing HLSL shader programs](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-writing-shader-programs-hlsl.html)
  * [Shader input](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-shader-shader-input.html)
  * Texture samplers


[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-VertexProgramInputs.html)
Input vertex data into a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-include-directives.html)
Include another HLSL file in a shader
# Texture samplers
Most of the time when sampling textures in **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader), the texture sampling state should come from [texture settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html) – essentially, textures and samplers are coupled together. This is default behavior when using DX9-style shader syntax:
```
sampler2D _MainTex;
// ...
half4 color = tex2D(_MainTex, uv);

```

Using sampler2D, sampler3D, samplerCUBE HLSL keywords declares both texture and sampler.
Most of the time this is what you want, and is the only supported option on older graphics APIs (OpenGL ES).
## Separate textures and samplers
Many graphics APIs and GPUs allow using fewer samplers than textures, and coupled texture+sampler syntax might not allow more complex shaders to be written. For example, Direct3D 11 allows using up to 128 textures in a single shader, but only up to 16 samplers.
Unity allows declaring textures and samplers using DX11-style HLSL syntax, with a special naming convention to match them up: samplers that have names in the form of “sampler”+TextureName will take sampling states from that texture.
The shader snippet from section above could be rewritten in DX11-style HLSL syntax, and it would do the same thing:
```
Texture2D _MainTex;
SamplerState sampler_MainTex; // "sampler" + “_MainTex”
// ...
half4 color = _MainTex.Sample(sampler_MainTex, uv);

```

However, this way, a shader could be written to “reuse” samplers from other textures, while sampling more than one texture. In the example below, three textures are sampled, but only one sampler is used for all of them:
```
Texture2D _MainTex;
Texture2D _SecondTex;
Texture2D _ThirdTex;
SamplerState sampler_MainTex; // "sampler" + “_MainTex”
// ...
half4 color = _MainTex.Sample(sampler_MainTex, uv);
color += _SecondTex.Sample(sampler_MainTex, uv);
color += _ThirdTex.Sample(sampler_MainTex, uv);

```

Unity provides several shader macros to help with declaring and sampling textures using this “separate samplers” approach, see [built-in macros](https://docs.unity3d.com/6000.0/Documentation/Manual/use-built-in-shader-methods-birp.html). The example above could be rewritten this way, using said macros:
```
UNITY_DECLARE_TEX2D(_MainTex);
UNITY_DECLARE_TEX2D_NOSAMPLER(_SecondTex);
UNITY_DECLARE_TEX2D_NOSAMPLER(_ThirdTex);
// ...
half4 color = UNITY_SAMPLE_TEX2D(_MainTex, uv);
color += UNITY_SAMPLE_TEX2D_SAMPLER(_SecondTex, _MainTex, uv);
color += UNITY_SAMPLE_TEX2D_SAMPLER(_ThirdTex, _MainTex, uv);

```

The above would compile on all platforms supported by Unity, but would fallback to using three samplers on older platforms like DX9.
## Inline sampler states
In addition to recognizing HLSL SamplerState objects named as “sampler”+TextureName, Unity also recognizes some other patterns in sampler names. This is useful for declaring simple hardcoded sampling states directly in the shaders. An example:
```
Texture2D _MainTex;
SamplerState my_point_clamp_sampler;
// ...
half4 color = _MainTex.Sample(my_point_clamp_sampler, uv);

```

The name “my_point_clamp_sampler” will be recognized as a sampler that should use Point (nearest) texture filtering, and Clamp texture wrapping mode.
Sampler names recognized as “inline” sampler states (all case insensitive):
  * “Point”, “Linear” or “Trilinear” (required) set up texture filtering mode.
  * “Clamp”, “Repeat”, “Mirror” or “MirrorOnce” (required) set up texture wrap mode.
    * Wrap modes can be specified per-axis (UVW), e.g. “ClampU_RepeatV”.
  * “Compare” (optional) set up sampler for depth comparison; use with HLSL SamplerComparisonState type and SampleCmp / SampleCmpLevelZero functions.
  * “AnisoX” (where X can be 2/4/8 or 16, for example, `Aniso8`) can be added to request anisotropic filtering.


Here’s an example of sampling texture with `sampler_linear_repeat` and `sampler_point_repeat` SamplerStates respectively, illustrating how the name controls filtering mode:
![Left: sampling a texture with sampler_linear_repeat. Right: sampling a texture with sampler_point_repeat.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SamplerStates1.jpg) Left: sampling a texture with `sampler_linear_repeat`. Right: sampling a texture with `sampler_point_repeat`.
Here’s an example with `SmpClampPoint`, `SmpRepeatPoint`, `SmpMirrorPoint`, `SmpMirrorOncePoint`, `Smp_ClampU_RepeatV_Point` SamplerStates respectively, illustrating how the name controls wrapping mode. In the last example, different wrap modes are set for horizontal (U) and vertical (V) axes. In all cases, texture coordinates go from –2.0 to +2.0.
![Illustration of how different sampler states work. From left to right: SmpClampPoint, SmpRepeatPoint, SmpMirrorPoint, SmpMirrorOncePoint, Smp_ClampU_RepeatV_Point.](https://docs.unity3d.com/6000.0/Documentation/uploads/Main/SamplerStates2.png) Illustration of how different sampler states work. From left to right: `SmpClampPoint`, `SmpRepeatPoint`, `SmpMirrorPoint`, `SmpMirrorOncePoint`, `Smp_ClampU_RepeatV_Point`.
Just like separate texture + sampler syntax, inline sampler states are not supported on some platforms. Currently they are implemented on Direct3D 11/12 and Metal.
Note that “MirrorOnce” texture wrapping mode is not supported on most mobile GPUs/APIs, and will fallback to Mirror mode when support is not present.
Note that the “AnisoX” filtering modes are a best effort based on the platform capabilities and selected API. The actual value will be clamped based on the maximum supported anisotropic level (including disabled in cases where no anisotropic filtering is supported).   
  

## Texture/Sampler declaration macros
**Macro:** | **Use:**  
---|---  
`UNITY_DECLARE_TEX2D(name)` | Declares a Texture and Sampler pair.  
`UNITY_DECLARE_TEX2D_NOSAMPLER(name)` | Declares a Texture without a Sampler.  
`UNITY_DECLARE_TEX2DARRAY(name)` | Declares a Texture array Sampler variable.  
`UNITY_SAMPLE_TEX2D(name,uv)` | Sample from a Texture and Sampler pair, using given Texture coordinate.  
`UNITY_SAMPLE_TEX2D_SAMPLER( name,samplername,uv)` | Sample from Texture (name), using a Sampler from another Texture (samplername).  
`UNITY_SAMPLE_TEX2DARRAY(name,uv)` | Sample from a Texture array with a float3 UV; the z component of the coordinate is array element index.  
`UNITY_SAMPLE_TEX2DARRAY_LOD(name,uv,lod)` | Sample from a Texture array with an explicit mipmap level.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-VertexProgramInputs.html)
Input vertex data into a shader
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-include-directives.html)
Include another HLSL file in a shader
