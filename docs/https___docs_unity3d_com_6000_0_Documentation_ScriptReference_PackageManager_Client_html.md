* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html

# Client
class in UnityEditor.PackageManager
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
Use the Unity Package Manager Client class to manage the packages used in a project.
**Note:** You can only call the Client methods in sequence. If you try to add or remove multiple packages at the same time, the outcome is nondeterministic. For example, if you call the [Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Remove.html) method on a package while a `Remove` operation is already in progress or queued, might overwrite the current operation and only handle the latest `Remove` operation.
### Static Properties
Property | Description  
---|---  
[LogLevel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.LogLevel.html) | Gets or sets the log level that the Package Manager uses when logging to the Editor.log and upm.log files. Defaults to LogLevel.Info.  
### Static Methods
Method | Description  
---|---  
[Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Add.html) | Adds a package dependency to the project. Requesting a new or different dependency often leads to changing installed packages, but only after the Package Manager constructs a dependency graph to solve any version conflicts. For more information, see Dependency and resolution.  
[AddAndRemove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.AddAndRemove.html) | Adds package dependencies to the project and removes package dependencies from the project. Requesting different dependencies often leads to changing installed packages, but only after the Package Manager constructs a dependency graph to solve any version conflicts. For more information, see Dependency and resolution. Calling this function is much more efficient than calling the Add and Remove functions several times because for this function, the Package Manager only has to solve the dependency list once, instead of constructing a new dependency graph after each call.  
[ClearCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.ClearCache.html) | Empties the package cache.  
[Embed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Embed.html) |  Embeds a package inside the project.  
[List](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.List.html) | Lists the packages the project depends on.  
[Pack](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Pack.html) | Creates a GZip tarball file from a package folder. The format and content of the file is the same as if the package was published to a package registry.  
[Remove](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Remove.html) | Removes a package dependency from the project. Removing a dependency often leads to changing installed packages, but only after the Package Manager constructs a dependency graph to solve any version conflicts. For more information, see Dependency and resolution.  
[Resolve](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Resolve.html) | Forces the Package Manager to resolve the project's packages, reinstalling any altered or missing package and removing extraneous packages.  
[Search](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Search.html) | Searches for the given package.  
[SearchAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.SearchAll.html) | Searches for all discoverable packages compatible with the current Unity version.  
* * *
