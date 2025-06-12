* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-mipmapLimitGroup.html

#  [Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html).mipmapLimitGroup
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
mipmapLimitGroup; 
### Description
The name of the texture mipmap limit group that this texture is associated with. (Read Only)
If this texture has a mipmap limit group assignment, this texture respects the [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) of that group. If this texture does not have a group assignment, or the indicated group does not exist, this texture takes the [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) instead. If you construct or import this texture, assign it to a mipmap limit group that does not yet exist, then create that mipmap limit group, this texture respects the [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) of that new group.  
  
Set this property in the constructor or in the texture importer, because you cannot set this property after creating the texture. If the texture has no mipmaps, this property has no effect.  
  
Additional resources: [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html), [TextureImporter.mipmapLimitGroupName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-mipmapLimitGroupName.html).
* * *
