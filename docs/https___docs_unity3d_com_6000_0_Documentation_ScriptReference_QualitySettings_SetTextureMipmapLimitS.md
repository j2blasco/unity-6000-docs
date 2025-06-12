* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).SetTextureMipmapLimitSettings
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-QualitySettings.html "Go to QualitySettings Component in the Manual")
## Declaration
public static void SetTextureMipmapLimitSettings(string groupName, [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) textureMipmapLimitSettings); 
### Parameters
Parameter | Description  
---|---  
groupName | Name of the texture mipmap limit group to modify.  
textureMipmapLimitSettings | The new texture mipmap limit settings to apply.  
### Description
Applies new [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) to the indicated texture mipmap limit group.
Throws an exception if Unity cannot find `groupName`.  
  
At run time, if [TextureMipmapLimitSettings.limitBias](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings-limitBias.html) corresponds to a mip level that has been stripped, Unity sets the value to the closest mip level that has not been stripped. For additional information regarding mipmap stripping, see [PlayerSettings.mipStripping](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings-mipStripping.html).  
  
Additional resources: [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html), [GetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetTextureMipmapLimitSettings.html).
* * *
