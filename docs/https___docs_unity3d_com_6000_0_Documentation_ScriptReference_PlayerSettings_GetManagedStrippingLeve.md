* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetManagedStrippingLevel.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetManagedStrippingLevel
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
public static [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) GetManagedStrippingLevel([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Returns
**ManagedStrippingLevel** Returns the default [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) for the build target you select. 
### Description
Gets the managed code stripping level set for the build target you select
* * *
**Obsolete** Use GetManagedStrippingLevel(NamedBuildTarget buildTarget) instead.
## Declaration
public static [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) GetManagedStrippingLevel([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup); 
### Parameters
Parameter | Description  
---|---  
targetGroup | The target platform group whose code stripping level you want to retrieve.  
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
