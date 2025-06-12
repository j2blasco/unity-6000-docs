* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetOverrideShaderChunkSettingsForPlatform.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetOverrideShaderChunkSettingsForPlatform
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
## Declaration
public static void SetOverrideShaderChunkSettingsForPlatform([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) buildTarget, bool value); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The build target to set the override for.  
value | Set the value to `true` if you want settings for the `buildTarget` to override the default settings.  
### Description
Enable this to override the default shader variant chunk settings.
If you set `SetOverrideShaderChunkSettingsForPlatform` to `true` for a build target, you can do the following: 
  * Use [PlayerSettings.SetShaderChunkCountForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkCountForPlatform.html) to override [PlayerSettings.SetDefaultShaderChunkCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkCount.html).
  * Use [PlayerSettings.SetShaderChunkSizeInMBForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkSizeInMBForPlatform.html) to override [PlayerSettings.SetDefaultShaderChunkSizeInMB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkSizeInMB.html).


Additional resources: [PlayerSettings.GetOverrideShaderChunkSettingsForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetOverrideShaderChunkSettingsForPlatform.html).
* * *
