* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.html

# IShouldIncludeInBuildCallback
interface in UnityEditor.PackageManager
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-PackageManager.html "Go to PackageManager Component in the Manual")
### Description
Interface used by the Package Manager to request build information about packages.
During a build, the [ShouldIncludeInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.ShouldIncludeInBuild.html) method is invoked on each managed plugin (DLL) inside the package whose name is [PackageName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.PackageName.html).  
  
Register your implementation with the Package Manager using [BuildUtilities.RegisterShouldIncludeInBuildCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.BuildUtilities.RegisterShouldIncludeInBuildCallback.html). You can only register one implementation of this interface per package.  
  
Additional resources: [BuildUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.BuildUtilities.html).
### Properties
Property | Description  
---|---  
[PackageName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.PackageName.html) | The package name.  
### Public Methods
Method | Description  
---|---  
[ShouldIncludeInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.ShouldIncludeInBuild.html) | Determines whether to include a managed plugin in a build.  
* * *
