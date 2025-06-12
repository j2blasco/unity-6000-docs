* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels32.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).SetPixels32
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture3D.html "Go to Texture3D Component in the Manual")
## Declaration
public void SetPixels32(Color32[] colors, int miplevel); 
## Declaration
public void SetPixels32(Color32[] colors); 
### Parameters
Parameter | Description  
---|---  
colors | The array of pixel colours to use. This is a 3D texture flattened to a 1D array.  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Description
Sets the pixel colors of an entire mipmap level.
This method sets pixel data for the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) after `SetPixels32` to upload the changed pixels to the GPU.  
  
`colors` must contain the pixels slice by slice starting at the front of the texture. Each slice must contain the pixels row by row, starting at the bottom left of the texture. The size of the array must be the width × height × depth of the mipmap level.  
  
A single call to `SetPixels32` is usually faster than multiple calls to [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixel.html), especially for large textures.  
  
`SetPixels32` might be slower than some other texture methods because it converts the [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) struct into the format the texture uses. To set pixel data more quickly, use [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixelData.html) instead.  
  
You can use `SetPixel32` with the following [texture formats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html): 
  * Alpha8
  * ARGB32
  * ARGB4444
  * BGRA32
  * R16
  * R16_SIGNED
  * R8
  * R8_SIGNED
  * RFloat
  * RG16
  * RG16_SIGNED
  * RG32
  * RG32_SIGNED
  * RGB24
  * RGB24_SIGNED
  * RGB48
  * RGB48_SIGNED
  * RGB565
  * RGB9e5Float
  * RGBA32
  * RGBA32_SIGNED
  * RGBA4444
  * RGBA64
  * RGBA64_SIGNED
  * RGBAFloat
  * RGBAHalf
  * RGFloat
  * RGHalf
  * RHalf


For all other formats, `SetPixels32` fails. Unity throws an exception when `SetPixels32` fails.  
  
Additional resources: [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels.html), [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixelData.html), [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html), [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html), [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html).
* * *
