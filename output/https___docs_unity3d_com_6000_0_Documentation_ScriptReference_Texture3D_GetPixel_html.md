* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixel.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).GetPixel
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
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetPixel(int x, int y, int z, int mipLevel = 0); 
### Parameters
Parameter | Description  
---|---  
x | The x coordinate of the pixel to get. The range is `0` through the (texture width - 1).  
y | The y coordinate of the pixel to get. The range is `0` through the (texture height - 1).  
z | The z coordinate of the pixel to get. The range is `0` through the (texture depth - 1).  
mipLevel | The mipmap level to sample. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color** The pixel color. 
### Description
Gets the pixel color at coordinates (`x`, `y`, `z`).
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
The lower left corner is (0, 0, 0). If the pixel coordinate is outside the texture's dimensions, Unity clamps or repeats it, depending on the texture's [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).  
  
`GetPixel` might be slower than some other texture methods because it converts the format the texture uses into [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html). `GetPixel` also needs to decompress compressed textures, and use memory to store the decompressed area. To get pixel data more quickly, use [GetPixelData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelData.html) instead.  
  
If you need to get a large block of pixels, it might be faster to use [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html) or [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels.html).  
  
You can't use `GetPixel` with textures that use Crunch texture compression.  
  
Additional resources: [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html), [GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels.html), [SetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixel.html), [GetPixelBilinear](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelBilinear.html).
* * *
