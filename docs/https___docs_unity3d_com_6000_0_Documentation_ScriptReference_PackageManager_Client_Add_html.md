* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Add.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).Add
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
public static [PackageManager.Requests.AddRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.AddRequest.html) Add(string identifier); 
### Parameters
Parameter | Description  
---|---  
identifier | A string representing the package to be added:   
  
- To install a specific version of a package, use a package identifier ("name@version"). This is the only way to install a [pre-release](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-preview.html) version.   
- To install the latest compatible ([released](https://docs.unity3d.com/6000.0/Documentation/Manual/pack-safe.html)) version of a package, specify only the package [name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html).   
- To install a git package, specify a [git url](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-git.html).   
- To install a [local](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html) package, specify a value in the format "file:/path/to/package/folder".   
- To install a [local tarball](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-localpath.html) package, specify a value in the format "file:/path/to/package-file.tgz".   
  
`ArgumentException` is thrown if `identifier` is `null` or empty.   
### Returns
**AddRequest** An [AddRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.AddRequest.html) instance, which you can use to get the [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) representing the package that was added to the project from the `AddRequest.Result` property. 
### Description
Adds a package dependency to the project. Requesting a new or different dependency often leads to changing installed packages, but only after the Package Manager constructs a dependency graph to solve any version conflicts. For more information, see [Dependency and resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html).
`Add()` is an asynchronous operation. Before the operation is complete, you can use the `AddRequest` instance to monitor the asynchronous operation.  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, see the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page. 
* * *
