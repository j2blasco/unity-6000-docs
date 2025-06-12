* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels.html

#  [CubemapArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.html).SetPixels
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-CubemapArray.html "Go to CubemapArray Component in the Manual")
## Declaration
public void SetPixels(Color[] colors, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face, int arrayElement, int miplevel); 
## Declaration
public void SetPixels(Color[] colors, [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face, int arrayElement); 
### Parameters
Parameter | Description  
---|---  
colors | The array of pixel colours to use. This is a 2D image flattened to a 1D array.  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
face | The [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) to write `colors` to.  
arrayElement | The array slice to write `colors` to.  
### Description
Sets the pixel colors of an entire mipmap level of a face of a slice.
This method sets pixel data for the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.Apply.html) after `SetPixels` to upload the changed pixels to the GPU.  
  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.Apply.html) is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it.  
  
`colors` must contain the pixels row by row, starting at the bottom left of the face texture. The size of the array must be the width × height of the mipmap level.  
  
`SetPixels` might be slower than some other texture methods because it converts the [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct into the format the texture uses. To set pixel data more quickly, use [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixelData.html) instead.  
  
You can use `SetPixels` with the following [texture formats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html): 
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


For all other formats, `SetPixels` fails. Unity throws an exception when `SetPixels` fails.  
  
Additional resources: [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.GetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixels32.html), [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.SetPixelData.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapArray.Apply.html), [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html).
* * *
