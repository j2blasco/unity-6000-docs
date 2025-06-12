* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/texture-formats-reference.html

  * [Materials and shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/materials-and-shaders.html)
  * [Textures](https://docs.unity3d.com/6000.0/Documentation/Manual/Textures-landing.html)
  * [Get started with textures](https://docs.unity3d.com/6000.0/Documentation/Manual/textures-getting-started.html)
  * [Texture formats in memory](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-compression-formats.html)
  * GPU texture formats reference


[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html)
Choose a GPU texture format by platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html)
Mipmaps
# GPU texture formats reference
## Texture formats, by quality
The table below shows each format available in Unity, and their quality details. 
****Texture format** A file format for handling textures during real-time rendering by 3D graphics hardware, such as a graphics card or mobile device. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureFormat)** | **Description** | **Channels** | **Quality** | **Bits per**pixel** The smallest unit in a computer image. Pixel size depends on your screen resolution. Pixel lighting is calculated at every screen pixel. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/ShadowPerformance.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#pixel)** | **Size of 1024x1024 texture, in MB**  
---|---|---|---|---|---  
**Alpha 8** | Uncompressed single channel (A) | A | High | 8 | 1  
**R 8** | Uncompressed single channel (R) | R | High | 8 | 1  
**R 16 bit** | Uncompressed single channel (R), very high precision | R | Very high | 16 | 2  
**R Float** |  **HDR** high dynamic range  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#HDR), uncompressed single channel (R), very high precision | R | Very high | 32 | 4  
**R Compressed BC4** | Compressed single channel (R) | R | High | 4 | 0.5  
**R Compressed EAC 4 bit** | Compressed single channel (R) | R | High | 4 | 0.5  
**RG 32 bit** | Uncompressed two channel (RG), very high precision | RG | Very high | 32 | 4  
**RG Float** | HDR, uncompressed two channel (RG), very high precision | RG | Very high | 64 | 8  
**RG Compressed BC5** | Compressed two channel (RG) | RG | High | 8 | 1  
**RG Compressed EAC 8 bit** | Compressed two channel (RG) | RG | High | 8 | 1  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | Compressed RGBA, with alpha values fully opaque or fully transparent | RGBA | Medium | 4 | 0.5  
**RGB 16 bit** | Also known as RGB 565. Quantized RGB | RGB | Medium | 16 | 2  
**RGB 24 bit** | Uncompressed RGB. Converted to RGBA 32 bit for the GPU | RGB | High | 24 disk, 32 GPU | 3 disk, 4 GPU  
**RGB 48 bit** | Uncompressed RGB, very high precision. Converted to RGBA 64 bit for the GPU | RGB | Very high | 48 disk, 64 GPU | 6 disk, 8 GPU  
**RGB Compressed BC6H** | HDR, compressed RGB, 0 to +64k range | RGB | High | 8 | 1  
**RGB Compressed DXT1** | Also known as BC1. Compressed RGB | RGB | Medium | 4 | 0.5  
**RGB Compressed ETC** | Compressed RGB | RGB | Low | 4 | 0.5  
**RGB Compressed ETC2** | Compressed RGB | RGB | Medium | 4 | 0.5  
**RGB Compressed PVRTC 2 bits** | Compressed RGB, texture required to be square | RGB | Low | 2 | 0.25  
**RGB Compressed PVRTC 4 bits** | Compressed RGB, texture required to be square | RGB | Medium | 4 | 0.5  
**RGB Crunched DXT1** | Also known as BC1. Compressed RGB, with additional on-disk Crunch **compression** A method of storing data that reduces the amount of storage space it requires. See [Texture Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride), [Animation Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AnimationClip.html#AssetProperties), [Audio Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/class-AudioClip.html), [Build Compression](https://docs.unity3d.com/6000.0/Documentation/Manual/ReducingFilesize.html).  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#compression) | RGB | Low to medium | Variable | Variable  
**RGB Crunched ETC** | Compressed RGB, with additional on-disk Crunch compression | RGB | Low | Variable | Variable  
**RGB(A) Compressed ASTC HDR** | HDR, compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to High | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
**RGB(A) Compressed ASTC** | Compressed RGB or RGBA, size & quality dependent on block size | RGB or RGBA | Low to high | 12x12: 0.89, 10x10: 1.28, 8x8: 2, 6x6: 3.56, 5x5: 5.12, 4x4: 8 | 12x12: 0.11, 10x10: 0.16, 8x8: 0.25, 6x6: 0.45, 5x5: 0.64, 4x4: 1.0  
**RGB(A) Compressed BC7** | Compressed RGB or RGBA | RGB or RGBA | High | 8 | 1  
**RGB9e5 32 Bit Shared Exponent Float** | HDR, quantized RGB, 0 to +64k range | RGB | Medium | 32 | 4  
**RGBA 16 bit (4444)** | Quantized RGBA | RGBA | Medium | 16 | 2  
**RGBA 32 bit** | Uncompressed RGBA | RGBA | High | 32 | 4  
**RGBA 64 bit** | Uncompressed RGBA, very high precision | RGBA | Very high | 64 | 8  
**RGBA Float** | HDR, uncompressed RGBA, very high precision | RGBA | Very high | 128 | 16  
**RGBA Compressed ETC2** | Compressed RGBA | RGBA | Medium | 8 | 1  
**RGBA Compressed PVRTC 2 bits** | Compressed RGBA, texture required to be square | RGBA | Low | 2 | 0.25  
**RGBA Compressed PVRTC 4 bits** | Compressed RGBA, texture required to be square | RGBA | Medium | 4 | 0.5  
**RGBA Crunched DXT5** | Also known as BC3. Compressed RGBA. With additional on-disk Crunch compression | RGBA | Low to medium | Variable | Variable  
**RGBA Crunched ETC2** | Compressed RGBA, with additional on-disk Crunch compression | RGBA | Low to medium | Variable | Variable  
**RGBA Half** | HDR, half-precision (FP16) RGBA, –64k to +64k range | RGBA | High | 64 | 8  
## Supported texture formats, by platform
The table below shows each texture format available in Unity, and the platforms that support them. 
**Texture format** | **Windows** | **macOS** | **Linux** | **Android** | **iOS & tvOS** | **Web (Desktop Browsers)** | **Web (iOS and Android browser)**  
---|---|---|---|---|---|---|---  
**Alpha 8** | yes | yes | yes | yes | yes | yes | yes  
**R 8** | yes | yes | yes | yes | yes | yes | yes  
**R 16 bit** | yes | yes | yes | partial (4) | partial (4) | **yes (10)** | yes (10)  
**R Float** | yes | yes | yes | yes | yes | yes | yes  
**R Compressed BC4** | yes | yes | yes | no | no | **yes** | no  
**R Compressed EAC 4 bit** | no | no | no | partial (9) | yes | no | yes  
**RG 32 bit** | yes | yes | yes | partial (4) | yes | no | no  
**RG Float** | yes | yes | yes | yes | yes | yes | yes  
**RG Compressed BC5** | yes | yes | yes | no | no | **yes** | no  
**RG Compressed EAC 8 bit** | no | no | no | partial (9) | yes | no | yes  
**RGB + 1-bit Alpha Compressed ETC2 4 bits** | no | no | no | partial (9) | yes | no | yes  
**RGB 16 bit** , also known as RGB 565 | yes | yes | yes | yes | yes | yes | yes  
**RGB 24 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGB 48 bit** | yes | yes | yes | partial (4) | yes | no | no  
**RGB Compressed BC6H** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGB Compressed DXT1** , also known as BC1 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB Compressed ETC** | no | no | no | yes | yes | no | yes  
**RGB Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGB Compressed PVRTC 2 bits** | no | no | no | no (8) | yes | no | no  
**RGB Compressed PVRTC 4 bits** | no | no | no | no (8) | yes | no | no  
**RGB Crunched DXT1** , also known as BC1 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGB Crunched ETC** | no | no | no | yes | yes | no | yes  
**RGB(A) Compressed ASTC HDR** | no | no | no | partial (7) | partial (7) | no | partial (7)  
**RGB(A) Compressed ASTC** | no | no | no | partial (5) | yes (6) | no | yes (6 and 9)  
**RGB(A) Compressed BC7** | yes (1) | yes (1) | yes | no | no | **yes (1)** | no  
**RGB9e5 32 Bit Shared Exponent Float** | yes | yes | yes | yes | yes | yes | yes)  
**RGBA 16 bit (4444)** | yes | yes | yes | yes | yes | yes | yes  
**RGBA 32 bit** | yes | yes | yes | yes | yes | yes | yes  
**RGBA 64 bit** | yes | yes | yes | partial (4) | yes | no | no  
**RGBA Float** | yes | yes | yes | yes | yes | yes | yes  
**RGBA Compressed DXT5** , also known as BC3 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA Compressed ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGBA Compressed PVRTC 2 bits** | no | no | no | no (8) | yes | no | no  
**RGBA Compressed PVRTC 4 bits** | no | no | no | no (8) | yes | no | no  
**RGBA Crunched DXT5** , also known as BC3 | yes | yes | yes | no (3) | no | partial (2) | no  
**RGBA Crunched ETC2** | no | no | no | partial (9) | yes | no | yes  
**RGBA Half** | yes | yes | yes | yes | yes | yes | yes  
**Notes:**
  1. Except on pre-DX11 level GPUs, or macOS when using **WebGL** A JavaScript API that renders 2D and 3D graphics in a web browser. The Unity Web build option allows Unity to publish content as JavaScript programs which use HTML5 technologies and the WebGL rendering API to run Unity content in a web browser. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#WebGL) or OpenGL. When not supported, BC6H textures get decompressed to RGBA Half, and BC7 get decompressed to RGBA32 at load time.
  2. With [linear rendering](https://docs.unity3d.com/6000.0/Documentation/Manual/color-spaces-landing.html) on web browsers that don’t support sRGB DXT, textures are decompressed to RGBA32 at load time.
  3. Except on Android devices with NVIDIA Tegra GPUs; these do support DXT/BC formats.
  4. Requires GL_EXT_texture_norm16 or corresponding Vulkan capability on Android.
  5. Requires Vulkan or [GL_KHR_texture_compression_astc_ldr](https://opengles.gpuinfo.org/listreports.php?extension=GL_KHR_texture_compression_astc_ldr) OpenGL ES extension.
  6. Except on Apple A7 chip devices (2013).
  7. Android: requires [GL_KHR_texture_compression_astc_hdr](https://opengles.gpuinfo.org/listreports.php?extension=GL_KHR_texture_compression_astc_hdr) extension. iOS: requires A13 or later chip (2019). WebGL: requires [WEBGL_compressed_texture_astc](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc) extension and [HDR profile](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc/getSupportedProfiles). When not supported, the texture is decompressed to RGB9E5 format, losing the alpha channel.
  8. Except on Android devices with Imagination PowerVR GPUs; these do support PVRTC formats.
  9. Requires [WEBGL_compressed_texture_astc](https://developer.mozilla.org/en-US/docs/Web/API/WEBGL_compressed_texture_astc) extension.
  10. Requires [EXT_texture_norm16](https://developer.mozilla.org/en-US/docs/Web/API/EXT_texture_norm16) extension and WebGL 2.


## Supported texture formats in Web
The following table provides the supported texture formats for the Web platform.
**Format** | **Description**  
---|---  
**ASTC** | Adaptive Scalable **Texture Compression** 3D Graphics hardware requires Textures to be compressed in specialized formats which are optimized for fast Texture sampling. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporterOverride)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#TextureCompression) (ASTC) is an advanced lossy texture compression format. Widely used for mobile browsers / devices.  
**DXT** | Also known as S3 Texture Compression (S3TC), DXT is mainly used for desktop browsers and devices.  
**ETC2** | Ericsson Texture Compression (ETC) is an older lossy texture compression format, lower quality than ASTC, used for mobile browsers / devices.  
## Additional resources:
  * [Texture Inspector window reference](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html)
  * [Texture compression in Web](https://docs.unity3d.com/6000.0/Documentation/Manual/webgl-texture-compression.html)
  * [Texture Compression format in Android](https://docs.unity3d.com/6000.0/Documentation/Manual/android-requirements-and-compatibility.html#texture-compression)


TextureImporterOverride
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-choose-format-by-platform.html)
Choose a GPU texture format by platform
[](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-mipmaps-introduction.html)
Mipmaps
