* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.PackTextures.html

#  [Texture2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html).PackTextures
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
public Rect[] PackTextures(Texture2D[] textures, int padding, int maximumAtlasSize, bool makeNoLongerReadable); 
### Parameters
Parameter | Description  
---|---  
textures | Array of textures to pack into the atlas.  
padding | Padding in pixels between the packed textures.  
maximumAtlasSize | Maximum size of the resulting texture.  
makeNoLongerReadable | Should the texture be marked as no longer readable?  
### Returns
**Rect[]** An array of rectangles containing the UV coordinates in the atlas for each input texture, or null if packing fails. 
### Description
Packs multiple Textures into a texture atlas.
This function will replace the current texture with the atlas made from the supplied textures. The size, format and mipmaps of any of the textures can change after packing.  
  
The resulting texture atlas will be as large as needed to fit all input textures but only up to `maximumAtlasSize` in each dimension. If the input textures can't all fit into a texture atlas of the desired size then they will be scaled down to fit.  
  
If you have compressed all input textures, and the following conditions are met, Unity also compresses the output atlas:  
  
If input textures are compressed and have mipmaps, the following conditions will cause the atlas to created as an uncompressed texture: 
  * If the input textures are compressed but some have mipmaps and others have none, atlas format falls back to being uncompressed.
  * If the compressed input textures have mipmaps and padding > 0, atlas format falls back to being uncompressed.


If any of the input images have mipmaps and the padding value is greater than zero, the atlas texture is uncompressed. This is because of alignment restrictions on the compressed data. If you have not compressed one or more input textures, the atlas remains in the uncompressed format [RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html). If the texture atlas remains compressed and has a padding value is greater than zero, the padding value is rounded up to the next multiple of four. This happens because of alignment restrictions on compressed data.  
  
This is a shortlist of compressed formats. You can find the full list in [TextureFormat](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.html): 
  * ETC
  * ETC2
  * EAC
  * DXT
  * ASTC
  * PVRTC


However, the atlas packing code doesn't support every compression format. Of the available formats, the atlas packing code only supports the following: If all other conditions are met, and input textures are using one of these formats, the texture atlas will be compressed. 
  * ARGB4444
  * ETC
  * ETC2
  * DXT1
  * DXT5
  * BC7
  * ASTC 4x4


All input textures must have the same compression format or be a mixture of compatible compression formats, otherwise atlas format falls back to uncompressed.  
  
You can mix these types in an atlas, where they stay compressed: 
  * [DXT1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT1.html) and TextureFormat::pref:DXT5 result in a [DXT5](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.DXT5.html) atlas.
  * [ETC2_RGB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ETC2_RGB.html), [ETC_RGB4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ETC_RGB4.html), and [ETC2_RGBA8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ETC2_RGBA8.html) result in a [ETC2_RGBA8](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.ETC2_RGBA8.html) atlas.


However, if the input textures mix formats, such as BC7 with ASTC 4x4 or DXT5, this causes the atlas packing code to fall back to [RGBA32](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureFormat.RGBA32.html).  
  
If none of the input textures have mipmaps, the atlas also has no mipmaps.  
  
If `makeNoLongerReadable` is `true` then the texture will be marked as no longer readable and memory will be freed after uploading to the GPU. By default `makeNoLongerReadable` is set to `false`.
```
using UnityEngine;  
  
public class Example : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    // Source textures.
    Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)[] atlasTextures;  
  
    // Rectangles for individual atlas textures.
    Rect[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html)[] rects;  
  
    void Start()
    {
        // Pack the individual textures into the smallest possible space,
        // while leaving a two pixel gap between their edges.
        Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html) atlas = new Texture2D[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.html)(8192, 8192);
        rects = atlas.PackTextures(atlasTextures, 2, 8192);
    }
}

```

* * *
