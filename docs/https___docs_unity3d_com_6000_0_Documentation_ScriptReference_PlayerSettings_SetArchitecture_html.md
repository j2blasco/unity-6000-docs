* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetArchitecture.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetArchitecture
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
public static void SetArchitecture([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, int architecture); 
**Obsolete** Use SetArchitecture(NamedBuildTarget buildTarget, int architecture) instead.
## Declaration
public static void SetArchitecture([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup, int architecture); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
architecture | An integer value associated with the architecture of the build target. 0 - None, 1 - ARM64, 2 - Universal.  
### Description
Sets the architecture for the given build target.
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
