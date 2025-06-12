* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkSizeInMBForPlatform.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetShaderChunkSizeInMBForPlatform
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
public static void SetShaderChunkSizeInMBForPlatform([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) buildTarget, int sizeInMegabytes); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The build target to set the shader chunk size for.  
sizeInMegabytes | The chunk size in megabytes.  
### Description
Sets the default size for compressed shader variant chunks on the build target.
Unity stores multiple [shader variants](https://docs.unity3d.com/6000.0/Documentation/Manual/shadervariants.html) in compressed chunks. You can use `SetDefaultShaderChunkSizeInMBForPlatform` to set the maximum size of each chunk.  
  
This parameter overrides [PlayerSettings.SetDefaultShaderChunkSizeInMB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetDefaultShaderChunkSizeInMB.html) on the build target.  
  
You can use this parameter with [PlayerSettings.SetShaderChunkCountForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetShaderChunkCountForPlatform.html) to limit the amount of memory Unity uses for shader variants.  
  
Additional resources: [PlayerSettings.GetShaderChunkSizeInMBForPlatform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetShaderChunkSizeInMBForPlatform.html).
* * *
