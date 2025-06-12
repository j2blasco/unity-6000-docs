* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.CopyTexture.html

#  [CommandBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CommandBuffer.html).CopyTexture
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
public void CopyTexture([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) src, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dst); 
## Declaration
public void CopyTexture([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) src, int srcElement, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dst, int dstElement); 
## Declaration
public void CopyTexture([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) src, int srcElement, int srcMip, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dst, int dstElement, int dstMip); 
## Declaration
public void CopyTexture([Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) src, int srcElement, int srcMip, int srcX, int srcY, int srcWidth, int srcHeight, [Rendering.RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html) dst, int dstElement, int dstMip, int dstX, int dstY); 
### Parameters
Parameter | Description  
---|---  
src | The source texture or [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).  
dst | The destination texture or [RenderTargetIdentifier](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.RenderTargetIdentifier.html).  
srcElement | The element in the source texture to copy from. For example, the [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `src` is a 2D texture.  
srcMip | The mipmap level to copy from. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
dstElement | The element in the source texture to copy to. For example, the [CubemapFace](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CubemapFace.html) in a Cubemap or the slice in a texture array. Set the value to `0` if `dst` is a 2D texture.  
dstMip | The mipmap level to write to. The range is `0` through the texture's [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html). The default value is `0`.  
srcX | The starting x coordinate of `src` to copy from. `0` is the left of the texture.  
srcY | The starting y coordinate of `src` to copy from. `0` is the bottom of the texture.  
srcWidth | The width of `src` to copy.  
srcHeight | The height of `src` to copy.  
dstX | The x coordinate of `dst` to copy to.  
dstY | The y coordinate to `dst` to copy to.  
### Description
Adds a command to copy pixel data from one texture to another.
This method adds a command to copy pixel data from one texture to another on the GPU. If you set [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) to `true` for both `src` and `dst` textures, the method also copies pixel data on the CPU.  
  
If you set [Texture.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) to `false`, `CopyTexture` is one of the fastest ways to copy a texture. But to use `CopyTexture`, the following must be the same in both the source and destination texture areas: 
  * Format. You can also use two compatible formats - for example, [TextureFormat.ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ARGB32.html) and [RenderTextureFormat.ARGB32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTextureFormat.ARGB32.html).
  * Size.
  * [RenderTexture.antiAliasing](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-antiAliasing.html) values, if the textures are render textures.


You might be able to copy between incompatible formats depending on your graphics API. For example, on some APIs you can copy between formats with the same bit width.  
  
Depending on your graphics API, you might not be able to copy between different types of textures. For more information on compatibility, see [SystemInfo.copyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SystemInfo-copyTextureSupport.html) and [CopyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html).  
  
If `src` is a depth-only render texture, you must copy the whole texture, not part of it. A depth-only render texture has its color buffer set to a [color format](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-graphicsFormat.html) of `None` and its depth buffer set to a valid [RenderTexture.depthStencilFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderTexture-depthStencilFormat.html).  
  
Compressed texture formats add some restrictions to the CopyTexture with a region variant. For example, PVRTC formats are not supported since they are not block-based (for these formats you can only copy whole texture or whole mipmap level). For block-based formats (for instance, DXT, ETC), the region size and coordinates must be a multiple of compression block size (4 pixels for DXT).  
  
Even if you set `Texture.isReadable` to true, this method doesn't copy pixel data on the CPU if you copy only a region of a compressed texture.  
  
Additional resources: [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html), [CopyTextureSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.CopyTextureSupport.html).
* * *
