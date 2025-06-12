* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetDefaultScriptingBackend.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetDefaultScriptingBackend
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
public static [ScriptingImplementation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.html) GetDefaultScriptingBackend([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Returns
**ScriptingImplementation** A ScriptingImplementation object that describes the default scripting backend for the build target you select. 
### Description
Returns the default [ScriptingImplementation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.html) for the build target you select.
* * *
**Obsolete** Use GetDefaultScriptingBackend(NamedBuildTarget buildTarget) instead.
## Declaration
public static [ScriptingImplementation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ScriptingImplementation.html) GetDefaultScriptingBackend([BuildTargetGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BuildTargetGroup.html) targetGroup); 
### Parameters
Parameter | Description  
---|---  
targetGroup | The platform group to retrieve the scripting backend for.  
### Returns
**ScriptingImplementation** A ScriptingImplementation object that describes the default scripting backend used on that build target. 
### Description
BuildTargetGroup is marked for deprecation in the future. Use [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) instead.
* * *
