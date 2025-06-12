* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IFilterBuildAssemblies.html

# IFilterBuildAssemblies
interface in UnityEditor.Build
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
Implement this interface to receive a callback to filter assemblies away from the build.
### Public Methods
Method | Description  
---|---  
[OnFilterAssemblies](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Build.IFilterBuildAssemblies.OnFilterAssemblies.html) | Will be called after building script assemblies, but makes it possible to filter away unwanted scripts to be included.  
* * *
