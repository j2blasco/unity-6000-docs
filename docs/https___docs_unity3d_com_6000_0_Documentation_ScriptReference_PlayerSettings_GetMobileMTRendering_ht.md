* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetMobileMTRendering.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetMobileMTRendering
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
public static bool GetMobileMTRendering([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html). (Only iOS, tvOS and Android).  
### Returns
**bool** Returns true if multithreaded rendering option for build target is enabled. 
### Description
Check if multithreaded rendering option for mobile platform is enabled.
* * *
**Obsolete** Use GetMobileMTRendering(NamedBuildTarget buildTarget) instead.
## Declaration
public static bool GetMobileMTRendering([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup); 
### Parameters
Parameter | Description  
---|---  
targetGroup | Mobile platform (Only iOS, tvOS and Android).  
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
