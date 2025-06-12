* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html

#  [Texture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture.html).isReadable
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
isReadable; 
### Description
Whether Unity stores an additional copy of this texture's pixel data in CPU-addressable memory.
This is required for methods that read, write, and manipulate the pixel data on the CPU, such as [Texture2D.GetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.GetPixels.html) or [ImageConversion.EncodeToPNG](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ImageConversion.EncodeToPNG.html). It is not required for methods that perform all their work on the GPU, such as [Graphics.CopyTexture](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.CopyTexture.html) or [Graphics.Blit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Graphics.Blit.html).  
  
By default, this is `false` for texture assets that you import into your project. To toggle this, use the **Read/Write Enabled** setting in the [Texture Import Settings](https://docs.unity3d.com/6000.0/Documentation/Manual/class-TextureImporter.html), or set [TextureImporter.isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-isReadable.html).  
  
By default, this is `true` when you create a texture from a script.  
  
**Note:** Readable textures use more memory than non-readable textures. You should only make a texture readable when you need to, and you should make textures non-readable when you are done working with the data on the CPU.  
  
To make a texture non-readable at runtime, call the `Apply` method for your type of texture, for example [Texture2D.Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html) or [Cubemap.Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cubemap.Apply.html) and set the `makeNoLongerReadable` parameter to `true`.
* * *
