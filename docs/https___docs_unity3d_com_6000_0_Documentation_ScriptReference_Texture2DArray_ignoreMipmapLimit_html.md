* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-ignoreMipmapLimit.html

#  [Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html).ignoreMipmapLimit
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Texture2DArray.html "Go to Texture2DArray Component in the Manual")
ignoreMipmapLimit; 
### Description
This property causes a texture to ignore all texture mipmap limit settings.
When this property is `true`, Unity always uploads the texture to the GPU at full resolution, disregarding the active quality setting's global texture mipmap limit and texture mipmap limit group settings, even if this texture has a texture mipmap limit group set.  
  
When this property is `false`, the texture respects the active quality setting's global texture mipmap limit, unless the texture is part of a [mipmapLimitGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-mipmapLimitGroup.html).  
  
When changing this property at runtime: if this causes the actual mipmap limit for this texture to change, then the texture will be reuploaded to the GPU. For an optimal workflow, set this property in the constructor or in the texture importer to immediately upload the texture with the currently active mipmap limits properly applied or ignored. If the texture has no mipmaps, this property has no effect. Note that this can only be toggled at runtime if the Texture is [readable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html). By default, this property is set to `true` when created in a script, which means all mipmap levels are uploaded.  
  
Additional resources: [TextureImporter.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-ignoreMipmapLimit.html), [MipmapLimitDescriptor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MipmapLimitDescriptor.html), [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html).
* * *
