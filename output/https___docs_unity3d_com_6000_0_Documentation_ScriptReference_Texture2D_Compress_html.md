* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Compress.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).Compress
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
public void Compress(bool highQuality); 
### Description
Compress texture at runtime to DXT/BCn or ETC formats.
Use this to compress textures at runtime. Compressed textures use less graphics memory and are faster to render. For more information on texture compression, see [Texture compression](https://docs.unity3d.com/6000.0/Documentation/Manual/texture-compression-formats.html).  
  
The format that Unity compresses the texture to depends on the platform, and the properties of the texture.  
  
texture will be in [DXT1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT1.html) (BC1) format if the original texture had no alpha channel, and in [DXT5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT5.html) (BC3) format if it had alpha channel. If the original texture was [R8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.R8.html), the compressed format will be [BC4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.BC4.html). If the original texture was [RG16](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RG16.html), the compressed format will be [BC5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.BC5.html).  
  
On Android, iOS and tvOS, this will compress the texture to the ETC/EAC family of formats.  
  
Passing `true` for `highQuality` parameter will dither the source texture during compression, which helps to reduce compression artifacts but is slightly slower. This parameter is ignored for ETC compression.  
  
If the graphics card does not support compression or the texture is already in compressed format, then Compress does nothing.  
  
In the Editor scripts, you probably want to use [EditorUtility.CompressTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressTexture.html), which compresses using slower, but higher quality compression. It can also compress into other compressed formats.  
  
You can also load already precompressed data into a texture using [LoadRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.LoadRawTextureData.html) function.  
  
Additional resources: [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.SetPixels.html), [EditorUtility.CompressTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorUtility.CompressTexture.html), [LoadRawTextureData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.LoadRawTextureData.html).
* * *
