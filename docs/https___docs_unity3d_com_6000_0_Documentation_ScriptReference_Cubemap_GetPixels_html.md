* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.GetPixels.html

#  [Cubemap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).GetPixels
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
public Color[] GetPixels([CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face, int miplevel); 
## Declaration
public Color[] GetPixels([CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) face); 
### Parameters
Parameter | Description  
---|---  
face | The [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) to read from.  
miplevel | The mipmap level to get. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color[]** An array that contains the pixel colors. 
### Description
Gets the pixel color data for a mipmap level of a face as [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) structs.
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The array contains the pixels row by row, starting at the bottom left of the face texture. The size of the array is the width × height of the mipmap level.  
  
Each pixel is a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct. `GetPixels` might be slower than some other texture methods because it converts the format the texture uses into [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html). `GetPixels` also needs to decompress compressed textures, and use memory to store the decompressed area. To get pixel data more quickly, use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.GetPixelData.html) instead.  
  
A single call to `GetPixels` is usually faster than multiple calls to [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.GetPixel.html), especially for large textures.  
  
If `GetPixels` fails, Unity throws an exception. `GetPixels` might fail if the array contains too much data. Use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.GetPixelData.html) instead for very large textures.  
  
You can't use `GetPixel` with textures that use Crunch texture compression.
```
using UnityEngine;  
  
public class CubemapExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) source;
    public Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html) destination;  
  
    void Start()
    {
        // Get a copy of the color data from the source Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html), in high-precision float format.
        // Each element in the array represents the color data for an individual pixel.
        CubemapFace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) sourceFace = CubemapFace.PositiveX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.PositiveX.html);
        int sourceMipLevel = 0;
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] pixels = source.GetPixels(sourceFace, sourceMipLevel);  
  
        // If required, manipulate the pixels before applying them to the destination texture.
        // This example code reverses the array, which rotates the image 180 degrees.
        System.Array.Reverse(pixels, 0, pixels.Length);  
  
        // Set the pixels of the destination Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html).
        CubemapFace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) destinationFace = CubemapFace.PositiveX[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.PositiveX.html);
        int destinationMipLevel = 0;
        destination.SetPixels(pixels, destinationFace, destinationMipLevel);  
  
        // Apply changes to the destination Cubemap[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.html), which uploads its data to the GPU.
        destination.Apply();
    }
}

```

Additional resources: [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.SetPixels.html), [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.GetPixelData.html), [mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html).
* * *
