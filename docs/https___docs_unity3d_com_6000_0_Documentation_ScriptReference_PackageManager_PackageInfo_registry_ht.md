* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-registry.html

#  [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html).registry
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
[PackageManager.RegistryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RegistryInfo.html) registry; 
### Description
The registry where the Package Manager might find this package.
This value always returns a registry, even if the package's [source](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo-source.html) is not [PackageSource.Registry](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageSource.Registry.html) (such as an embedded package or a Git dependency). In that case, this value is set to the closest registry match even if the package isn't actually on that registry. For example, if your project uses a [scoped registry](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html) with the `com.example.myscope` scope, and your embedded package is named `com.example.myscope.mypackage`, this property will be the [RegistryInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.RegistryInfo.html) from the matching scoped registry.  
  
For more information, see "Managing scoped registries for a project" in [Scoped Registries](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-scoped.html). 
* * *
