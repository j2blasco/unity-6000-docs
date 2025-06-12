* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).GetPixels
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
public Color[] GetPixels(int miplevel = 0); 
### Parameters
Parameter | Description  
---|---  
miplevel | The mipmap level to get. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color[]** An array that contains the pixel colors. 
### Description
Gets the pixel color data for a mipmap level as [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) structs.
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The array contains the pixels row by row, starting at the bottom left of the texture. The size of the array is the width × height of the mipmap level.  
  
Each pixel is a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct. `GetPixels` might be slower than some other texture methods because it converts the format the texture uses into [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html). `GetPixels` also needs to decompress compressed textures, and use memory to store the decompressed area. To get pixel data more quickly, use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixelData.html) instead.  
  
A single call to `GetPixels` is usually faster than multiple calls to [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixel.html), especially for large textures.  
  
If `GetPixels` fails, Unity throws an exception. `GetPixels` might fail if the array contains too much data. Use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixelData.html) or [GetRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetRawTextureData.html) instead for very large textures.  
  
You can't use `GetPixel` with textures that use Crunch texture compression. Use [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels32.html) instead.
```
using UnityEngine;  
  
public class Texture2DExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) source;
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) destination;  
  
    void Start()
    {
        // Get a copy of the color data from the source Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html), in high-precision float format.
        // Each element in the array represents the color data for an individual pixel.
        int sourceMipLevel = 0;
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] pixels = source.GetPixels(sourceMipLevel);  
  
        // If required, manipulate the pixels before applying them to the destination Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).
        // This example code reverses the array, which rotates the image 180 degrees.
        System.Array.Reverse(pixels, 0, pixels.Length);  
  
        // Set the pixels of the destination Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).
        int destinationMipLevel = 0;
        destination.SetPixels(pixels, destinationMipLevel);  
  
        // Apply changes to the destination Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html), which uploads its data to the GPU.
        destination.Apply();
    }
}

```

Additional resources: [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html), [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixelData.html), [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels32.html).
* * *
## Declaration
public Color[] GetPixels(int x, int y, int blockWidth, int blockHeight, int miplevel = 0); 
### Parameters
Parameter | Description  
---|---  
x | The starting x position of the section to fetch.  
y | The starting y position of the section to fetch.  
blockWidth | The width of the section to fetch.  
blockHeight | The height of the section to fetch.  
miplevel | The mipmap level to read from. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color[]** An array that contains the pixel colors. 
### Description
Gets the pixel color data for part of a mipmap level as [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) structs.
This version of `GetPixels` returns part of a mipmap level instead of the whole mipmap level.
```
// Get a rectangular area of a texture and place it into
// a new texture the size of the rectangle.
using UnityEngine;
using System.Collections;  
  
public class ExampleClass : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Source texture and the rectangular area we want to extract.
    public Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) sourceTex;
    public Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) sourceRect;  
  
    void Start()
    {
        int x = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(sourceRect.x);
        int y = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(sourceRect.y);
        int width = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(sourceRect.width);
        int height = Mathf.FloorToInt[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Mathf.FloorToInt.html)(sourceRect.height);  
  
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] pix = sourceTex.GetPixels(x, y, width, height);
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) destTex = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(width, height);
        destTex.SetPixels(pix);
        destTex.Apply();  
  
        // Set the current object's texture to show the
        // extracted rectangle.
        GetComponent<Renderer[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Renderer.html)>().material.mainTexture = destTex;
    }
}

```

* * *
