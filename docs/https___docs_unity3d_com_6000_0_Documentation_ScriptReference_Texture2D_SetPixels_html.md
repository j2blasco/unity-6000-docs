* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).SetPixels
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
public void SetPixels(Color[] colors, int miplevel = 0); 
### Parameters
Parameter | Description  
---|---  
colors | The array of pixel colours to use. This is a 2D image flattened to a 1D array.  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Description
Sets the pixel colors of an entire mipmap level.
This method sets pixel data for the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) after `SetPixels` to upload the changed pixels to the GPU.  
  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it.  
  
`colors` must contain the pixels row by row, starting at the bottom left of the texture. The size of the array must be the width × height of the mipmap level.  
  
A single call to `SetPixels` is usually faster than multiple calls to [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html), especially for large textures.  
  
`SetPixels` might be slower than some other texture methods because it converts the [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct into the format the texture uses. To set pixel data more quickly, use [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixelData.html) instead.  
  
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
  
Additional resources: [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels32.html), [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixelData.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html), [GetRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetRawTextureData.html), [LoadRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.LoadRawTextureData.html), [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html) rend = GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>();  
  
        // Duplicate the original texture and assign to the material
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = Instantiate(rend.material.mainTexture) as Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html);
        rend.material.mainTexture = texture;  
  
        // Create the colors to use
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] colors = new Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[3];
        colors[0] = Color.red[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-red.html);
        colors[1] = Color.green[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-green.html);
        colors[2] = Color.blue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-blue.html);
        int mipCount = Mathf.Min[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.Min.html)(3, texture.mipmapCount);  
  
        // For each mipmap level, use GetPixels to fetch an array of pixel data, and use SetPixels to fill the mipmap level with one color.
        for (int mip = 0; mip < mipCount; ++mip)
        {
            Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] cols = texture.GetPixels(mip);
            for (int i = 0; i < cols.Length; ++i)
            {
                cols[i] = Color.Lerp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.Lerp.html)(cols[i], colors[mip], 0.33f);
            }
            texture.SetPixels(cols, mip);
        }
        // Copy the changes to the GPU. and don't recalculate mipmap levels.
        texture.Apply(false);
    }
}

```

* * *
## Declaration
public void SetPixels(int x, int y, int blockWidth, int blockHeight, Color[] colors, int miplevel = 0); 
### Parameters
Parameter | Description  
---|---  
x | The x coordinate to place the block of pixels at. The range is `0` through (texture width - 1).  
y | The y coordinate to place the block of pixels at. The range is `0` through (texture height - 1).  
blockWidth | The width of the block of pixels to set.  
blockHeight | The height of the block of pixels to set.  
colors | The array of pixel colours to use. This is a 2D image flattened to a 1D array. Must be `blockWidth` x `blockHeight` in length.  
miplevel | The mipmap level to write `colors` to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Description
Sets the pixel colors of part of a mipmap level.
This version of `SetPixels` sets part of a mipmap level instead of the whole mipmap level.
* * *
