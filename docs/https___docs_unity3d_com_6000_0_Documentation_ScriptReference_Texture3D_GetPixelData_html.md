* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).GetPixelData
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
public NativeArray<T> GetPixelData(int mipLevel); 
### Parameters
Parameter | Description  
---|---  
mipLevel | The mipmap level to read from. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**NativeArray <T>** A native array that points directly to the texture's data buffer in CPU memory. 
### Description
Gets the raw data from a texture.
This method returns a [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html) that points directly to the texture's data on the CPU and has the size of the mipmap level. The array doesn't contain a copy of the data, so `GetPixelData` doesn't allocate any memory.  
  
For example, if the texture is 16 × 16 × 16 pixels and RGBA32 format, and you set `mipLevel` to `1`, the method returns an array with 512 elements (8 × 8 × 8 pixels) and a size of 2048 bytes if you use [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) for `T` (4 bytes per pixel). You can use the experimental [GraphicsFormatUtility.ComputeMipmapSize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Experimental.Rendering.GraphicsFormatUtility.ComputeMipmapSize.html) API to calculate the size of a mipmap level.  
  
You usually use a struct for `T` that matches the structure of a pixel in the texture, for example [Color32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html) if the texture format uses RGBA pixels in 32-bit format, such as [TextureFormat.RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html).  
  
You can read from and write to the returned array to get and change the data directly in CPU memory. If you write to the array, you must then call the [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) method to upload the texture to the GPU.  
  
Use the returned array immediately. If you store the array and use it later, it might not point to the correct memory location if the texture has been modified or updated.  
  
If you use a small type for `T` such as `byte`, `GetPixelData` may fail because the `NativeArray` would exceed the maximum length (`Int32.MaxValue`). To avoid this, use a larger type or struct.  
  
`GetPixelData` throws an exception when it fails.  
  
Additional resources: [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels.html), [SetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels32.html), [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html).
```
using UnityEngine;  
  
public class ExampleScript : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    public void Start()
    {
        // Create a 3D texture
        var m_Texture3D = new Texture3D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html)(16, 16, 16, TextureFormat.RGBA32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html), true);  
  
        // Use GetPixelData to get an array that points to mipmap level 1
        var mip1Data = m_Texture3D.GetPixelData<Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)>(1);  
  
        // Fill pixels in mipmap level 1 with white
        for (int i = 0; i < mip1Data.Length; i++)
        {
            mip1Data[i] = new Color32[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color32.html)(255, 255, 255, 255);
        }  
  
        // Copy the texture changes to the GPU
        m_Texture3D.Apply(false);
    }
}

```

* * *
