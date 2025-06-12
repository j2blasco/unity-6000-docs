* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetApiCompatibilityLevel.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetApiCompatibilityLevel
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
public static [ApiCompatibilityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApiCompatibilityLevel.html) GetApiCompatibilityLevel([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Returns
**ApiCompatibilityLevel** Returns the ApiCompatibilityLevel associated with a [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html). 
### Description
Gets .NET API compatibility level for specified build target.
* * *
**Obsolete** Use GetApiCompatibilityLevel(NamedBuildTarget buildTarget) instead.
## Declaration
public static [ApiCompatibilityLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ApiCompatibilityLevel.html) GetApiCompatibilityLevel([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) buildTargetGroup); 
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
