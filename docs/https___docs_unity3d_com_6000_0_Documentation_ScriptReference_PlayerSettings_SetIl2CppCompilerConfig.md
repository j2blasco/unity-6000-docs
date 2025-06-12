* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetIl2CppCompilerConfiguration.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetIl2CppCompilerConfiguration
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
public static void SetIl2CppCompilerConfiguration([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, [Il2CppCompilerConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.html) configuration); 
**Obsolete** Use SetIl2CppCompilerConfiguration(NamedBuildTarget buildTarget, Il2CppCompilerConfiguration configuration) instead.
## Declaration
public static void SetIl2CppCompilerConfiguration([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup, [Il2CppCompilerConfiguration](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Il2CppCompilerConfiguration.html) configuration); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
targetGroup | Build target group.  
configuration | Compiler configuration.  
### Description
Sets compiler configuration used when compiling generated C++ code for a particular build target.
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
