* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).GetPixels
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
public Color[] GetPixels(int miplevel); 
## Declaration
public Color[] GetPixels(); 
### Parameters
Parameter | Description  
---|---  
miplevel | The mipmap level to get. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color[]** An array that contains the pixel colors. 
### Description
Gets the pixel color data for a mipmap level as [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) structs.
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The array contains the pixels slice by slice starting at the front of the texture. Each slice contains the pixels row by row, starting at the bottom left of the texture. The size of the array is the width × height × depth of the mipmap level.  
  
Each pixel is a [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) struct. `GetPixels` might be slower than some other texture methods because it converts the format the texture uses into [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html). `GetPixels` also needs to decompress compressed textures, and use memory to store the decompressed area. To get pixel data more quickly, use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html) instead.  
  
A single call to `GetPixels` is usually faster than multiple calls to [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixel.html), especially for large textures.  
  
If `GetPixels` fails, Unity throws an exception. `GetPixels` might fail if the array contains too much data. Use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html) instead for very large textures.  
  
You can't use `GetPixel` with textures that use Crunch texture compression. Use [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html) instead.
```
using UnityEngine;  
  
public class Texture3DExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) source;
    public Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html) destination;  
  
    void Start()
    {
        // Get a copy of the color data from the source Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html), in high-precision float format.
        // Each element in the array represents the color data for an individual pixel.
        int sourceMipLevel = 0;
        Color[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html)[] pixels = source.GetPixels(sourceMipLevel);  
  
        // If required, manipulate the pixels before applying them to the destination texture.
        // This example code reverses the array, which rotates the image 180 degrees.
        System.Array.Reverse(pixels, 0, pixels.Length);  
  
        // Set the pixels of the destination Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).
        int destinationMipLevel = 0;
        destination.SetPixels(pixels, destinationMipLevel);  
  
        // Apply changes to the destination Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html), which uploads its data to the GPU.
        destination.Apply();
    }
}

```

Additional resources: [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixel.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels32.html), [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixel.html), [GetPixelBilinear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelBilinear.html), [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html), [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html), [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) functions.
* * *
