* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.GetTextureMipmapLimitSettings.html

#  [QualitySettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.html).GetTextureMipmapLimitSettings
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
public static [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html) GetTextureMipmapLimitSettings(string groupName); 
### Parameters
Parameter | Description  
---|---  
groupName | Name of the texture mipmap limit group to scan.  
### Returns
**TextureMipmapLimitSettings** Structure containing the settings for the indicated `groupName`. 
### Description
Retrieves a copy of the TextureMipmapLimitSettings from a texture mipmap limit group.
Throws an exception if Unity cannot find `groupName`.  
  
Additional resources: [TextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextureMipmapLimitSettings.html), [SetTextureMipmapLimitSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/QualitySettings.SetTextureMipmapLimitSettings.html).
* * *
