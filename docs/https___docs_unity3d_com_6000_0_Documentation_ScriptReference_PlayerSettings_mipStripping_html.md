* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).mipStripping
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PlayerSettings.html "Go to PlayerSettings Component in the Manual")
mipStripping; 
### Description
Enable mip stripping for all platforms.
If you enable this setting, Unity strips unused mips at build time.   
  
When Unity builds your game or application, it can strip unused mips from textures in your Project. Stripping unused mips can make the resulting executable smaller. The top mip for any mip chain contributes 75% of the size on disk, so mip stripping can save disk space and improve download times.   
  
If you enable Mip Stripping, Unity examines the Quality Settings for the current platform at build time. If a mip level is excluded from every Quality Setting for the current platform, Unity strips those mips from the build.   
  
Mip Stripping depends on the [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) and [TextureMipmapLimitGroups](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitGroups.html) setup, and it will only affect textures that are also affected by mipmap limits.  
  
For example, for any platform in a project, if you do the following: 
  * Set **Global Mipmap Limit** (QualitySettings.globalTextureMipmapLimit) to **Half Resolution** (1) or lower resolution for every Quality level on that platform 
  * Enable **Texture Mipmap Stripping**


then every readonly Texture2D in the project will be built without mips higher than the Global Mipmap Limit level. If QualitySettings.globalTextureMipmapLimit is set to Full Resolution (0) for any quality level, the Mip Stripping setting won't do anything. ![](https://docs.unity3d.com/6000.0/Documentation/StaticFiles/ScriptRefImages/mipmap-stripping.png)  
  
At run time, if you use [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) or [QualitySettings.SetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html) to set a mip level that has been stripped, Unity sets the value to the closest mip level that has not been stripped.  
  
However, you need to be aware of the following: 
  * Texture Mip Stripping is not compatible with crunch compressed textures, due to the non-constant compression ratio of this compression format. 
  * Use caution if you use functionality such as [the mipmap streaming API](https://docs.unity3d.com/6000.0/Documentation/Manual/TextureStreaming-API.html), [Texture.width](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-width.html) or [Texture.mipmapCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-mipmapCount.html) as they do not reflect the texture's original state once mips have been stripped. For example, for a 1024x1024 texture, a [Texture2D.desiredMipmapLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D-desiredMipmapLevel.html) value of 0 in the Editor refers to a 1024x1024 mip. If we stripped 2 mips at build time from that same texture, a Texture2D.desiredMipmaplevel value of 0 refers to a 256x256 mip in the Player. 


  
  
For information on how to get Unity to ignore the Mipmap limit for a particular texture, refer to [TextureImporter.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureImporter-ignoreMipmapLimit.html).
* * *
