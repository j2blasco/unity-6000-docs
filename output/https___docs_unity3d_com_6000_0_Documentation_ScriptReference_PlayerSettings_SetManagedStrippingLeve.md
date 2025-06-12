* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetManagedStrippingLevel.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetManagedStrippingLevel
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
public static void SetManagedStrippingLevel([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) level); 
**Obsolete** Use SetManagedStrippingLevel(NamedBuildTarget buildTarget, ManagedStrippingLevel level) instead.
## Declaration
public static void SetManagedStrippingLevel([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup, [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) level); 
### Parameters
Parameter | Description  
---|---  
level | The desired managed code stripping level.  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Description
Sets the managed code stripping level for specified build target.
During the build process, Unity strips unused code from your project's managed and dynamically linked libraries. Stripping code results in a much smaller executable but can remove code you'd like to use.  
  
The [ManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ManagedStrippingLevel.html) Enum defines the options you can use to specify the rate at which Unity should remove unused code or to disable code stripping altogether.  
  
Additional resources: [GetManagedStrippingLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetManagedStrippingLevel.html), [Managed code stripping](https://docs.unity3d.com/6000.0/Documentation/Manual/ManagedCodeStripping.html).  
  
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
