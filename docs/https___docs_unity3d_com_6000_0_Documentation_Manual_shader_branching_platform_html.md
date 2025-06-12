* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-platform.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)
  * [Writing custom shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/writing-custom-shaders.html)
  * [Writing shaders in code](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-writing.html)
  * [Branch in a shader via built-in macros](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-built-in-macros.html)
  * Branch based on platform features


[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-shader-model.html)
Branch based on shader model 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-unity-version.html)
Branch based on Unity version
# Branch based on platform features
Direct use of these platform macros is discouraged, as they don’t always contribute to the future-proofing of your code. For example, if you’re writing a **Shader** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) that checks for D3D11, you may want to ensure that, in the future, the check is extended to include Vulkan. Instead, Unity defines several helper macros (in [`HLSLSupport.cginc`](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-BuiltinIncludes.html)):
**Macro:** | **Use:**  
---|---  
`UNITY_BRANCH` | Add this before conditional statements to tell the compiler that this should be compiled into an actual branch. Expands to `[branch]` when on HLSL platforms.  
`UNITY_FLATTEN` | Add this before conditional statements to tell the compiler that this should be flattened to avoid an actual branch instruction. Expands to `[flatten]` when on HLSL platforms.  
`UNITY_LOOP` | This macro makes Unity generate code that instructs the shader compiler to keep the `for` loop as a loop instead of unrolling it into a fixed set of operations. For an example of how to use the macro, refer to [Render additional lights in a shader](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/use-built-in-shader-methods-additional-lights-fplus.html).  
`UNITY_NO_SCREENSPACE_SHADOWS` | Defined on platforms that do not use cascaded screenspace shadowmaps (mobile platforms).  
`UNITY_NO_LINEAR_COLORSPACE` | Defined on platforms that do not support Linear color space (mobile platforms).  
`UNITY_NO_RGBM` | Defined on platforms where RGBM **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) for **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) is not used (mobile platforms).  
`UNITY_NO_DXT5nm` | Defined on platforms that do not use DXT5nm normal-map compression (mobile platforms).  
`UNITY_FRAMEBUFFER_FETCH_AVAILABLE` | Defined on platforms where “framebuffer color fetch” functionality can be available (generally iOS platforms).  
`UNITY_USE_RGBA_FOR_POINT_SHADOWS` | Defined on platforms where point light shadowmaps use RGBA Textures with encoded depth (other platforms use single-channel floating point Textures).  
`UNITY_ATTEN_CHANNEL` | Defines which channel of light attenuation Texture contains the data; used in per-pixel lighting code. Defined to either ‘r’ or ‘a’.  
`UNITY_HALF_TEXEL_OFFSET` | Defined on platforms that need a half-texel offset adjustment in mapping texels to **pixels** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel).  
`UNITY_UV_STARTS_AT_TOP` | Always defined with value of 1 or 0. A value of 1 is on platforms where Texture V coordinate is 0 at the “top” of the Texture. Direct3D-like platforms use value of 1; OpenGL-like platforms use value of 0.  
`UNITY_MIGHT_NOT_HAVE_DEPTH_Texture` | Defined if a platform might emulate shadow maps or depth Textures by manually rendering depth into a Texture.  
`UNITY_PROJ_COORD(a)` | Given a 4-component vector, this returns a Texture coordinate suitable for projected Texture reads. On most platforms this returns the given value directly.  
`UNITY_NEAR_CLIP_VALUE` | Defined to the value of near **clipping plane** A plane that limits how far or close a camera can see from its current position. A camera’s viewable range is between the far and near clipping planes. See far clipping plane and near clipping plane. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#clippingplane). Direct3D-like platforms use 1.0 while OpenGL-like platforms use –1.0.  
`UNITY_VPOS_TYPE` | Defines the data type required for pixel position input (VPOS): `float2` on D3D9, `float4` elsewhere.  
`UNITY_CAN_COMPILE_TESSELLATION` | Defined when the Shader compiler “understands” the tessellation Shader HLSL syntax (currently only D3D11).  
`UNITY_INITIALIZE_OUTPUT(type,name)` | Initializes the variable _name_ of given _type_ to zero.  
`UNITY_COMPILER_HLSL`, `UNITY_COMPILER_HLSL2GLSL`, `UNITY_COMPILER_CG` | Indicates which Shader compiler is being used to compile Shaders. See documentation on [Shader compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-compilation.html) for more details. Use this if you run into very specific Shader syntax handling differences between the compilers, and want to write different code for each compiler.  
  * `UNITY_REVERSED_Z` - defined on plaftorms using reverse Z buffer. Stored Z values are in the range 1..0 instead of 0..1.


## Additional resources
  * [HLSL pragma directives reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-PragmaDirectives.html)
  * [HLSL pragma target command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-target.html)
  * [HLSL pragma require command reference](https://docs.unity3d.com/6000.0/Documentation/Manual/SL-Pragma-require.html)


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-shader-model.html)
Branch based on shader model 
[](https://docs.unity3d.com/6000.0/Documentation/Manual/shader-branching-unity-version.html)
Branch based on Unity version
