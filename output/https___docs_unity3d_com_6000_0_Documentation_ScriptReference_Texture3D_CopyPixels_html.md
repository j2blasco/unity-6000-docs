* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.CopyPixels.html

#  [Texture3D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.html).CopyPixels
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
public void CopyPixels([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src); 
## Declaration
public void CopyPixels([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int srcElement, int srcMip, int dstElement, int dstMip); 
## Declaration
public void CopyPixels([Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html) src, int srcElement, int srcMip, int srcX, int srcY, int srcWidth, int srcHeight, int dstElement, int dstMip, int dstX, int dstY); 
### Parameters
Parameter | Description  
---|---  
src | The source texture.  
srcElement | The element in the source texture to copy from. For example, the [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `src` is a 2D texture.  
srcMip | The mipmap level to copy from. The range is `0` through the source texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
dstElement | The depth slice to copy to in this 3D texture.  
dstMip | The mipmap level to write to. The range is `0` through this texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
srcX | The starting x coordinate of `src` to copy from. `0` is the left of the texture.  
srcY | The starting y coordinate of `src` to copy from. `0` is the bottom of the texture.  
srcWidth | The width of `src` to copy.  
srcHeight | The height of `src` to copy.  
dstX | The x coordinate of this texture to copy to.  
dstY | The y coordinate to this texture to copy to.  
### Description
Copies pixel data from another texture on the CPU.
This method copies pixel data from a source texture to this one on the CPU. [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) must be `true` for both the texture and `src`, and you must call [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) after `CopyPixels` to upload the changed pixels to the GPU.  
  
[Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html) is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it. If you only need to copy pixels on the GPU, [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) with [GraphicsTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.GraphicsTexture.html) parameters is faster to use instead.  
  
To use `CopyPixels`, the size to be copied must be the same in both textures. Use the region-based overload to specify a smaller region than a full mipmap level.  
  
Crunch compressed texture formats are not supported in the element-based overload. Compressed texture formats are not supported at all for for the region-based overload. Unity throws a `UnityException` if either texture is unreadable, and throws an `ArgumentException` if `CopyPixels` fails.  
  
Additional resources: [Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.Apply.html), [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html), [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture3D.SetPixels.html).
* * *
