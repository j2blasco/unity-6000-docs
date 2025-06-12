* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixelBilinear.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).GetPixelBilinear
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
public [Color](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Color.html) GetPixelBilinear(float u, float v, float w, int mipLevel = 0); 
### Parameters
Parameter | Description  
---|---  
u | The u coordinate of the pixel to get.  
v | The v coordinate of the pixel to get.  
w | The w coordinate of the pixel to get.  
mipLevel | The mipmap level to read from. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
### Returns
**Color** The pixel color. 
### Description
Gets the filtered pixel color at the normalized coordinates (`u`, `v`, `w`).
This method gets pixel data from the texture in CPU memory. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true`.  
  
Unity uses bilinear filtering to return the pixel color.  
  
The lower left corner is (0, 0, 0). If the pixel coordinate is outside the texture's dimensions, Unity clamps or repeats it, depending on the texture's [TextureWrapMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureWrapMode.html).  
  
You can't use `GetPixelBilinear` with textures that use Crunch texture compression. Use [GetPixels32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixels32.html) instead.  
  
Additional resources: [GetPixel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.GetPixel.html).
* * *
