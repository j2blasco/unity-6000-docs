* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.html

# TextureImporterFormat
enumeration
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
### Description
Imported texture format for [TextureImporter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter.html).
Most of the values match the ones in [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html), with addition of the "Automatic" ones that pick the best format based on platform and texture type or usage.  
  
Additional resources: TextureImporter.textureFormat.
### Properties
Property | Description  
---|---  
[Automatic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.Automatic.html) | Choose texture format automatically based on the texture parameters.  
[DXT1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.DXT1.html) |  DXT1 (BC1) compressed texture format.  
[DXT5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.DXT5.html) |  DXT5 (BC3) compressed texture format.  
[RGB16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB16.html) |  RGB565 texture format.  
[RGB24](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB24.html) |  RGB24 texture format.  
[Alpha8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.Alpha8.html) |  Alpha8 texture format.  
[R16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.R16.html) |  R16 texture format.  
[R8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.R8.html) |  R8 texture format.  
[RG16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RG16.html) |  RG16 texture format.  
[ARGB16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ARGB16.html) |  ARGB4444 texture format.  
[RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBA32.html) |  RGBA32 texture format.  
[ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ARGB32.html) |  ARGB32 texture format.  
[RGBA16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBA16.html) |  RGBA4444 texture format.  
[RHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RHalf.html) |  RHalf half-precision floating point texture format.  
[RGHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGHalf.html) |  RGHalf half-precision floating point texture format.  
[RGBAHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBAHalf.html) |  RGBAHalf half-precision floating point texture format.  
[RFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RFloat.html) |  RFloat floating point texture format.  
[RGFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGFloat.html) |  RGFloat floating point texture format.  
[RGBAFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBAFloat.html) |  RGBAFloat floating point RGBA texture format.  
[RGB9E5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB9E5.html) |  TextureFormat.RGB9e5Float packed unsigned floating point texture format with shared exponent.  
[BC4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.BC4.html) |  BC4 compressed texture format.  
[BC5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.BC5.html) |  BC5 compressed texture format.  
[BC6H](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.BC6H.html) |  BC6H compressed HDR texture format.  
[BC7](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.BC7.html) |  BC7 compressed texture format.  
[DXT1Crunched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.DXT1Crunched.html) | DXT1 (BC1) compressed texture format using Crunch compression for smaller storage sizes.  
[DXT5Crunched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.DXT5Crunched.html) | DXT5 (BC3) compressed texture format using Crunch compression for smaller storage sizes.  
[PVRTC_RGB2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.PVRTC_RGB2.html) | PowerVR/iOS PVRTC_RGB2 compressed texture format.  
[PVRTC_RGBA2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.PVRTC_RGBA2.html) | PowerVR/iOS PVRTC_RGBA2 compressed texture format.  
[PVRTC_RGB4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.PVRTC_RGB4.html) | PowerVR/iOS PVRTC_RGB4 compressed texture format.  
[PVRTC_RGBA4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.PVRTC_RGBA4.html) | PowerVR/iOS PVRTC_RGBA4 compressed texture format.  
[ETC_RGB4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC_RGB4.html) | ETC 4 bits/pixel compressed RGB texture format.  
[EAC_R](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.EAC_R.html) | ETC2/EAC compressed 4 bits / pixel unsigned R texture format.  
[EAC_R_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.EAC_R_SIGNED.html) | ETC2/EAC compressed 4 bits / pixel signed R texture format.  
[EAC_RG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.EAC_RG.html) | ETC2/EAC compressed 8 bits / pixel unsigned RG texture format.  
[EAC_RG_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.EAC_RG_SIGNED.html) | ETC2/EAC compressed 4 bits / pixel signed RG texture format.  
[ETC2_RGB4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC2_RGB4.html) | ETC2 compressed 4 bits / pixel RGB texture format.  
[ETC2_RGB4_PUNCHTHROUGH_ALPHA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC2_RGB4_PUNCHTHROUGH_ALPHA.html) | ETC2 compressed 4 bits / pixel RGB + 1-bit alpha texture format.  
[ETC2_RGBA8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC2_RGBA8.html) | ETC2 compressed 8 bits / pixel RGBA texture format.  
[ASTC_4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_4x4.html) | ASTC compressed RGB(A) texture format, 4x4 block size.  
[ASTC_5x5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_5x5.html) | ASTC compressed RGB(A) texture format, 5x5 block size.  
[ASTC_6x6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_6x6.html) | ASTC compressed RGB(A) texture format, 6x6 block size.  
[ASTC_8x8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_8x8.html) | ASTC compressed RGB(A) texture format, 8x8 block size.  
[ASTC_10x10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_10x10.html) | ASTC compressed RGB(A) texture format, 10x10 block size.  
[ASTC_12x12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_12x12.html) | ASTC compressed RGB(A) texture format, 12x12 block size.  
[ETC_RGB4Crunched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC_RGB4Crunched.html) | ETC_RGB4 compressed texture format using Crunch compression for smaller storage sizes.  
[ETC2_RGBA8Crunched](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ETC2_RGBA8Crunched.html) | ETC2_RGBA8 compressed color with alpha channel texture format using Crunch compression for smaller storage sizes.  
[ASTC_HDR_4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_4x4.html) | ASTC compressed RGB(A) HDR texture format, 4x4 block size.  
[ASTC_HDR_5x5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_5x5.html) | ASTC compressed RGB(A) HDR texture format, 5x5 block size.  
[ASTC_HDR_6x6](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_6x6.html) | ASTC compressed RGB(A) HDR texture format, 6x6 block size.  
[ASTC_HDR_8x8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_8x8.html) | ASTC compressed RGB(A) HDR texture format, 8x8 block size.  
[ASTC_HDR_10x10](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_10x10.html) | ASTC compressed RGB(A) HDR texture format, 10x10 block size.  
[ASTC_HDR_12x12](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.ASTC_HDR_12x12.html) | ASTC compressed RGB(A) HDR texture format, 12x12 block size.  
[RG32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RG32.html) |  RG32 texture format.  
[RGB48](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB48.html) |  RGB48 texture format.  
[RGBA64](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBA64.html) |  RGBA64 texture format.  
[R8_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.R8_SIGNED.html) |  R8_SIGNED texture format.  
[RG16_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RG16_SIGNED.html) |  RG16_SIGNED texture format.  
[RGB24_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB24_SIGNED.html) |  RGB24_SIGNED texture format.  
[RGBA32_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBA32_SIGNED.html) |  RGBA32_SIGNED texture format.  
[R16_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.R16_SIGNED.html) |  R16_SIGNED texture format.  
[RG32_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RG32_SIGNED.html) |  RG32_SIGNED texture format.  
[RGB48_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGB48_SIGNED.html) |  RGB48_SIGNED texture format.  
[RGBA64_SIGNED](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporterFormat.RGBA64_SIGNED.html) |  RGBA64_SIGNED texture format.  
* * *
