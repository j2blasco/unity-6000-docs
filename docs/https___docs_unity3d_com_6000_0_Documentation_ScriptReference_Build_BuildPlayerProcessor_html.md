* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.html

# BuildPlayerProcessor
class in UnityEditor.Build
Leave feedback
  

Implements interfaces:[IOrderedCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IOrderedCallback.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
Extend BuildPlayerProcessor to receive callbacks during a player build.
Additional resources: [IFilterBuildAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IFilterBuildAssemblies.html), [IPostBuildPlayerScriptDLLs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPostBuildPlayerScriptDLLs.html), [IUnityLinkerProcessor](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IUnityLinkerProcessor.html), [IPreprocessBuildWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPreprocessBuildWithReport.html), [IPostprocessBuildWithReport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IPostprocessBuildWithReport.html).
### Properties
Property | Description  
---|---  
[callbackOrder](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor-callbackOrder.html) | Returns the relative callback order for callbacks. Callbacks with lower values are called before ones with higher values.  
### Public Methods
Method | Description  
---|---  
[PrepareForBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.BuildPlayerProcessor.PrepareForBuild.html) | Implement this function to receive a callback before a player build starts.  
* * *
