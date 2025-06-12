* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmaps-TechnicalInformation.html

  * [Lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/LightingOverview.html)
  * [Direct and indirect lighting](https://docs.unity3d.com/6000.0/Documentation/Manual/direct-and-indirect-lighting.html)
  * [Lighting data](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmap-data-landing.html)
  * Lightmap data format


[](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)
Global Illumination (GI) cache
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html)
Light Probe data format
# Lightmap data format
Unity stores **lightmaps** A pre-rendered texture that contains the effects of light sources on static objects in the scene. Lightmaps are overlaid on top of scene geometry to create the effect of lighting. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Lightmapping.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Lightmap) with different compressions and encoding schemes, depending on the target platform and the compression setting in the Lighting Window.
## Encoding schemes
Unity projects can use two techniques to encode baked light intensity ranges into low dynamic range textures when this is needed:
  * **RGBM encoding**. RGBM encoding stores a color in the **RGB** channels and a multiplier (**M**) in the alpha channel. The range of RGBM lightmaps goes from 0 to 34.49(52.2) in linear space, and from 0 to 5 in gamma space.
  * **Double Low Dynamic Range (dLDR) encoding**. dLDR encoding is used on mobile platforms by simply mapping a range of [0, 2] to [0, 1]. Baked light intensities that are above a value of 2 will be clamped. The decoding value is computed by multiplying the value from the lightmap texture by 2 when gamma space is used, or 4.59482(22.2) when linear space is used. Some platforms store lightmaps as dLDR because their hardware compression produces poor-looking artifacts when using RGBM.


When Linear Color Space is used, the lightmap texture is marked as sRGB and the final value used by the **shaders** A program that runs on the GPU. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/Shaders.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Shader) (after sampling and decoding) will be in Linear Color Space. When Gamma Color Space is used, the final value will be in Gamma Color Space.
**Note** : When encoding is used, the values stored in the lightmaps (GPU texture memory) are always in Gamma Color Space. 
The **Decode Lightmap** shader function from the _UnityCG.cginc_ shader include file handles the decoding of lightmap values after the value is read from the lightmap texture in a shader.
## HDR lightmap support
You can use HDR lightmaps on Windows, Mac, Linux, iOS, tvOS, and Android. To control the encoding/compression of the lightmaps for these platforms, go to **Edit** > **Project Settings** > **Player** > **Other Settings** > **Lightmap Encoding**.
Choosing **High Quality** will enable **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR) lightmap support, whereas **Normal Quality** will switch to using **RGBM** encoding. **Low Quality** will switch to **dLDR** encoding on mobile platforms, on other platforms it’s equivalent to **Normal Quality**.
When lightmap **Compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) is enabled in the Lighting Window, the lightmaps will be compressed using the **BC6H** compression format on desktop and console platforms. For mobile platforms, Unity selects the HDR format according to the table below.
## Advantages of High Quality (BC6H) lightmaps
  * HDR lightmaps don’t use any encoding scheme to encode lightmap values, so the supported range is only limited by the 16-bit floating point **texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat) that goes from 0 to 65504. 
  * BC6H format quality is superior to DXT5 + RGBM format encoding, and it doesn’t produce any of the color banding artifacts that RGBM encoding has. 
  * Shaders that need to sample HDR lightmaps are a few ALU instructions shorter because there is no need to decode the sampled values. 
  * BC6H format has the same GPU memory requirements as DXT5.


Here is the list of encoding schemes and their **texture compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) formats per target platform:
**Target platform** | **Encoding** | **Compression - size (bits per pixel)**  
---|---|---  
Standalone(PC, Mac, Linux) | RGBM / HDR | DXT5 / BC6H - 8 bpp  
**WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) 2.0 | RGBM / RGBM / HDR | DXT5 - 8 bpp  
iOS ASTC (1) | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / RGB9E5 - 32 bpp  
iOS PVRTC | dLDR / RGBM / HDR | PVRTC RGB - 4 bpp / ETC2 RGBA - 8 bpp / RGB9E5 - 32 bpp  
tvOS | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / RGB9E5 - 32 bpp  
Android ASTC (2) | dLDR / RGBM / HDR | ASTC - 3.56 bpp / ASTC - 3.56 bpp / ASTC HDR - 3.56 bpp  
Android ETC2 | dLDR / RGBM / HDR | ETC2 RGB - 4 bpp / ETC2 RGBA - 8 bpp / ASTC HDR - 3.56 bpp  
Android ETC | dLDR / RGBM / HDR | ETC1 RGB - 4 bpp / ETC2 RGBA - 8 bpp / ASTC HDR - 3.56 bpp  
[1] The texture compression format used for lightmaps on **iOS** depends on the _Texture compression format_ setting in the [Player Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/iphone.html).
[2] The texture compression format used for lightmaps on **Android** depends on [Player settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettingsAndroid.html#Rendering) and [build settings](https://docs.unity3d.com/6000.0/Documentation/Manual/android-build-settings.html). Refer to [Texture compression settings](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html#texture-compression) for more details on how these settings interact.
## Precomputed real-time Global Illumination (GI)
The inputs to the GI system have a different range and encoding to the output. Surface albedo is 8-bit unsigned integer RGB in gamma space and emission is 16-bit floating point RGB in linear space. For more information on providing custom inputs using a meta pass, refer to [Lightmapping and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/MetaPass.html).
The irradiance output texture is stored using the RGB9E5 shared exponent floating point format if the graphics hardware supports it, or RGBM with a range of 5 as fallback. The range of RGB9E5 lightmaps is [0, 65408]. For details on the RGB9E5 format, refer to [Khronos.org: EXT_texture_shared_exponent](https://www.khronos.org/registry/OpenGL/extensions/EXT/EXT_texture_shared_exponent.txt).
## Additional resources
  * [Texture Importer Override](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)
  * [Texture Types](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
  * [Global Illumination](https://docs.unity3d.com/6000.0/Documentation/Manual/lighting-window.html)A group of techniques that model both direct and indirect lighting to provide realistic lighting results.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#globalillumination)


* * *
  * 2019–04–26 Page amended 
  * Baked lightmaps added in Unity [2017.2](https://docs.unity3d.com/2017.2/Documentation/Manual/30_search.html?q=newin20172) NewIn20172
  * HDR lightmap support added in Unity [2017.3](https://docs.unity3d.com/2017.3/Documentation/Manual/30_search.html?q=newin20173) NewIn20173
  * Lightmap encoding settings for mobile platform added in Unity [2019.1](https://docs.unity3d.com/2019.1/Documentation/Manual/30_search.html?q=newin20191) NewIn20191
  * Update lightmap texture compression formats for Android and iOS


* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/GICache.html)
Global Illumination (GI) cache
[](https://docs.unity3d.com/6000.0/Documentation/Manual/LightProbes-TechnicalInformation.html)
Light Probe data format
