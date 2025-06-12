* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.GetScriptingDefineSymbols.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).GetScriptingDefineSymbols
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
public static string GetScriptingDefineSymbols([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
### Returns
**string** A string containing the symbols for the given build target name. 
### Description
Gets the user-specified symbols for script compilation for the build target you select.
* * *
## Declaration
public static void GetScriptingDefineSymbols([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, out string[] defines); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
defines | A string array where Unity stores the symbols for the given build target name.  
### Description
Gets the user-specified symbols for script compilation for the build target you select.
* * *
