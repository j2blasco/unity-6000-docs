* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.SetScriptingDefineSymbols.html

#  [PlayerSettings](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PlayerSettings.html).SetScriptingDefineSymbols
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
public static void SetScriptingDefineSymbols([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, string defines); 
## Declaration
public static void SetScriptingDefineSymbols([Build.NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html) buildTarget, string[] defines); 
### Parameters
Parameter | Description  
---|---  
buildTarget | The [NamedBuildTarget](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.NamedBuildTarget.html).  
defines | Symbols for this build target are passed as an array or as a string separated by semicolons.  
### Description
Set user-specified symbols for script compilation for the given build target.
To see defines string values go to Edit > Project Settings > Player Settings > Scripting Compilation > Scripting Define Symbols.  
  
Additional resources: [Platform Dependent Compilation](https://docs.unity3d.com/6000.0/Documentation/Manual/platform-dependent-compilation.html).
* * *
