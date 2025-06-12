* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixel.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).SetPixel
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
public void SetPixel(int x, int y, [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color, int mipLevel = 0); 
### Parameters
Parameter | Description  
---|---  
x | The x coordinate of the pixel to set. The range is `0` through (texture width - 1).  
y | The y coordinate of the pixel to set. The range is `0` through (texture height - 1).  
color | The color to set.  
mipLevel | The mipmap level to write to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Description
Sets the pixel color at coordinates (`x`,`y`).
This method sets pixel data for the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) after `SetPixel` to upload the changed pixels to the GPU.  
  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it.  
  
`SetPixel` might be slower than some other texture methods because it converts the [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct into the format the texture uses. To set pixel data more quickly, use [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixelData.html) instead.  
  
The lower left corner is (0, 0). If the pixel coordinate is outside the texture's dimensions, Unity clamps or repeats it, depending on the texture's [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).  
  
If you need to get a large block of pixels, it might be faster to use [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels32.html).  
  
You can use `SetPixel` with the following [texture formats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html): 
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


For all other formats, Unity ignores `SetPixel`.  
  
Additional resources: [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [SetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixelData.html), [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixel.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html).
```
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) texture = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(128, 128);
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = texture;  
  
        for (int y = 0; y < texture.height; y++)
        {
            for (int x = 0; x < texture.width; x++)
            {
                Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) color = ((x & y) != 0 ? Color.white[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-white.html) : Color.gray[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color-gray.html));
                texture.SetPixel(x, y, color);
            }
        }
        texture.Apply();
    }
}

```

* * *
