* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.Apply.html

#  [Texture2DArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.html).Apply
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
## Declaration
public void Apply(bool updateMipmaps = true, bool makeNoLongerReadable = false); 
### Parameters
Parameter | Description  
---|---  
updateMipmaps | When the value is `true`, Unity recalculates mipmap levels, using mipmap level 0 as the source. The default value is `true`.  
makeNoLongerReadable | When the value is `true`, Unity deletes the texture in CPU memory after it uploads it to the GPU, and sets [isReadable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture-isReadable.html) to `false`. The default value is `false`.  
### Description
Copies changes you've made in a CPU texture to the GPU.
For most types of textures, Unity can store a copy of the texture in both CPU and GPU memory.  
  
The CPU copy is optional. If the CPU copy exists, you can read from and write to the CPU copy more flexibly than the GPU copy. But to render the updated texture, you must use `Apply` to copy it from the CPU to the GPU.  
  
If you set `makeNoLongerReadable` to `true`, Unity deletes the CPU copy of the texture after it uploads it to the GPU. This means Unity can't reload the texture. Even if `Apply` is called on a texture asset with data stored on disk, Unity will no longer try to reload from disk if once it discards the CPU copy, since the readable texture data might have been altered. This is relevant when using mipmap limits in your project to reduce the amount of uploaded mips (see for instance [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html)). Both runtime textures and readable texture assets will stop following the quality settings after discarding the CPU copy in `Apply`. The uploaded resolution of the textures remains fixed at what was uploaded to the GPU at the time Unity discards the CPU copy. If this is undesirable, make sure to have the texture uploaded at full resolution, either at import/construction time or by using [Texture2DArray.ignoreMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray-ignoreMipmapLimit.html) at runtime.  
  
You usually only set `updateMipmaps` to `false` if you've already updated the mipmap levels, for example using [SetPixels](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2DArray.SetPixels.html).  
  
`Apply` is an expensive operation because it copies all the pixels in the texture even if you've only changed some of the pixels, so change as many pixels as possible before you call it.  
  
Additional resources: [Texture2D.Apply](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Texture2D.Apply.html)
* * *
