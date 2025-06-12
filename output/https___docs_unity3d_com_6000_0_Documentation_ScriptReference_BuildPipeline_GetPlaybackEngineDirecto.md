* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.GetPlaybackEngineDirectory.html

#  [BuildPipeline](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildPipeline.html).GetPlaybackEngineDirectory
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
## Declaration
public static string GetPlaybackEngineDirectory([BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html) options); 
## Declaration
public static string GetPlaybackEngineDirectory([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) buildTargetGroup, [BuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTarget.html) target, [BuildOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.html) options); 
### Parameters
Parameter | Description  
---|---  
target | Build target.  
options | Build options.  
buildTargetGroup | Build target group.  
### Description
Returns the path of a player directory. For ex., Editor\Data\PlaybackEngines\AndroidPlayer.
In some cases the player directory path can be affected by [BuildOptions.Development](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildOptions.Development.html).
* * *
