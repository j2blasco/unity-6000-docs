* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBias.html

#  [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html).limitBias
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
limitBias; 
### Description
The new value to apply on top of the global texture mipmap limit. Can act as an offset (default) or an override to it.
By default, this is equal to `0`.  
  
If [limitBiasMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBiasMode.html) is set to [TextureMipmapLimitBiasMode.OffsetGlobalLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitBiasMode.OffsetGlobalLimit.html), `limitBias` acts as an offset to the current quality level's [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html). For example, if the global texture mipmap limit is `1` (half size) and `limitBias` is also `1`, the final combined value for textures that are affected by these settings is `2`. (quarter size)  
  
If [limitBiasMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBiasMode.html) is set to [TextureMipmapLimitBiasMode.OverrideGlobalLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitBiasMode.OverrideGlobalLimit.html), `limitBias` ignores the global texture mipmap limit and acts as an override. For example, if [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html) is `2` (quarter size), and `limitBias` is `0` (full resolution), the final combined value for textures that are affected by these settings is `0` (full resolution).  
  
Additional resources: [limitBiasMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBiasMode.html), [QualitySettings.globalTextureMipmapLimit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings-globalTextureMipmapLimit.html).
* * *
