* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.html

# RenderTextureFormat
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
Format of a [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html).
Note that a particular render texture format might not be supported by the current platform or GPU. Use [SystemInfo.SupportsRenderTextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo.SupportsRenderTextureFormat.html) to check before using.  
  
Additional resources: [RenderTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture.html) class.
### Properties
Property | Description  
---|---  
[ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html) | Color render texture format, 8 bits per channel.  
[Depth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Depth.html) | A depth render texture format.  
[ARGBHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGBHalf.html) | Color render texture format, 16 bit floating point per channel.  
[Shadowmap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Shadowmap.html) | A native shadowmap render texture format.  
[RGB565](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGB565.html) | Color render texture format.  
[ARGB4444](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB4444.html) | Color render texture format, 4 bit per channel.  
[ARGB1555](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB1555.html) | Color render texture format, 1 bit for Alpha channel, 5 bits for Red, Green and Blue channels.  
[Default](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.Default.html) | Default color render texture format: will be chosen accordingly to Frame Buffer format and Platform.  
[ARGB2101010](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB2101010.html) | Color render texture format. 10 bits for colors, 2 bits for alpha.  
[DefaultHDR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.DefaultHDR.html) | Default HDR color render texture format: will be chosen accordingly to Frame Buffer format and Platform.  
[ARGB64](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB64.html) | Four color render texture format, 16 bits per channel, fixed point, unsigned normalized.  
[ARGBFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGBFloat.html) | Color render texture format, 32 bit floating point per channel.  
[RGFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGFloat.html) | Two color (RG) render texture format, 32 bit floating point per channel.  
[RGHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGHalf.html) | Two color (RG) render texture format, 16 bit floating point per channel.  
[RFloat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RFloat.html) | Scalar (R) render texture format, 32 bit floating point.  
[RHalf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RHalf.html) | Scalar (R) render texture format, 16 bit floating point.  
[R8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.R8.html) | Single channel (R) render texture format, 8 bit integer.  
[ARGBInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGBInt.html) | Four channel (ARGB) render texture format, 32 bit signed integer per channel.  
[RGInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGInt.html) | Two channel (RG) render texture format, 32 bit signed integer per channel.  
[RInt](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RInt.html) | Scalar (R) render texture format, 32 bit signed integer.  
[BGRA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.BGRA32.html) | Color render texture format, 8 bits per channel.  
[RGB111110Float](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGB111110Float.html) | Color render texture format. R and G channels are 11 bit floating point, B channel is 10 bit floating point.  
[RG32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RG32.html) | Two color (RG) render texture format, 16 bits per channel, fixed point, unsigned normalized.  
[RGBAUShort](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RGBAUShort.html) | Four channel (RGBA) render texture format, 16 bit unsigned integer per channel.  
[RG16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.RG16.html) | Two channel (RG) render texture format, 8 bits per channel.  
[BGRA10101010_XR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.BGRA10101010_XR.html) | Color render texture format, 10 bit per channel, extended range.  
[BGR101010_XR](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.BGR101010_XR.html) | Color render texture format, 10 bit per channel, extended range.  
[R16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.R16.html) | Single channel (R) render texture format, 16 bit integer.  
* * *
