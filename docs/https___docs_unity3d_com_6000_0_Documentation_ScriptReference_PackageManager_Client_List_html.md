* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.List.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).List
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
public static [PackageManager.Requests.ListRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ListRequest.html) List(); 
## Declaration
public static [PackageManager.Requests.ListRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ListRequest.html) List(bool offlineMode); 
## Declaration
public static [PackageManager.Requests.ListRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ListRequest.html) List(bool offlineMode, bool includeIndirectDependencies); 
### Parameters
Parameter | Description  
---|---  
offlineMode | Specifies whether or not the Package Manager requests the latest information about the project's packages from the remote Unity package registry. When `offlineMode` is `true`, the [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) objects in the [PackageCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageCollection.html) returned by the Package Manager contain information obtained from the local package cache, which could be out of date.  
includeIndirectDependencies | Set to `true` to include indirect dependencies in the [PackageCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageCollection.html) returned by the Package Manager. Indirect dependencies include packages referenced in the manifests of project packages or in the manifests of other indirect dependencies. Set to `false` to include only the packages listed directly in the project manifest.   
**Note:** The version reported might not match the version requested in the project manifest. For more information, see [Dependency and resolution](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-dependencies.html).  
### Returns
**ListRequest** A [ListRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ListRequest.html) instance, which you can use to get the [PackageCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageCollection.html) representing the packages used in the project from the `ListRequest.Result` property. 
### Description
Lists the packages the project depends on.
Computes and returns the set of all packages that the project depends on (the resolved dependency graph) without physically downloading or installing any packages. The operation result contains only the resolved dependency graph as a [PackageCollection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageCollection.html).  
  
`List()` is an asynchronous operation. Before the operation is complete, you can use the `ListRequest` instance to monitor the asynchronous operation.  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, see the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page. Additional resources: [PackageInfo.GetAllRegisteredPackages](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.GetAllRegisteredPackages.html)
* * *
