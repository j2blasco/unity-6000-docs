* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.BuildUtilities.RegisterShouldIncludeInBuildCallback.html

#  [BuildUtilities](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.BuildUtilities.html).RegisterShouldIncludeInBuildCallback
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
## Declaration
public static void RegisterShouldIncludeInBuildCallback([PackageManager.IShouldIncludeInBuildCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.html) cb); 
### Parameters
Parameter | Description  
---|---  
cb | Object of a class that implements the IShouldIncludeInBuildCallback interface.  
### Description
Registers a callback object for a package.
During a build operation, the Unity Package Manager invokes the [IShouldIncludeInBuildCallback.ShouldIncludeInBuild](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.ShouldIncludeInBuild.html) method for each managed plugin (DLL) in the package whose name is [IShouldIncludeInBuildCallback.PackageName](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.PackageName.html). The callback implementation must return **true** for plugins that should be included in the build and **false** for plugins that should be excluded from the build.  
  
Only one [IShouldIncludeInBuildCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.IShouldIncludeInBuildCallback.html) callback object can be registered per package.
* * *
