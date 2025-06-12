* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Search.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).Search
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
public static [PackageManager.Requests.SearchRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.SearchRequest.html) Search(string packageIdOrName); 
## Declaration
public static [PackageManager.Requests.SearchRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.SearchRequest.html) Search(string packageIdOrName, bool offlineMode); 
### Parameters
Parameter | Description  
---|---  
packageIdOrName | The [name](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-manifestPkg.html#name.html) or ID of the package. `ArgumentException` is thrown if `packageIdOrName` is `null` or empty.   
offlineMode | Specifies whether or not the Package Manager requests the latest information about the project's packages from the remote Unity package registry. When `offlineMode` is `true`, the [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) object returned by the Package Manager contains information obtained from the local package cache, which could be out of date.  
### Returns
**SearchRequest** A [SearchRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.SearchRequest.html) instance, which you can use to get the array of [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) objects representing the packages matching the search criteria from the `SearchRequest.Result` property. 
### Description
Searches for the given package.
This operation issues a request to the main Unity package registry.  
  
`Search()` is an asynchronous operation. Before the operation is complete, you can use the `SearchRequest` instance to monitor the asynchronous operation.  
  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, see the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page. 
* * *
