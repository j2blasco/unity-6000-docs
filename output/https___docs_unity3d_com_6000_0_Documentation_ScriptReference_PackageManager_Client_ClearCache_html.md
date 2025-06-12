* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.ClearCache.html

#  [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html).ClearCache
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
public static [PackageManager.Requests.ClearCacheRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ClearCacheRequest.html) ClearCache(); 
### Returns
**ClearCacheRequest** A [ClearCacheRequest](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ClearCacheRequest.html) instance, which you can use to get the [StatusCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.StatusCode.html) to know if the operation completed successfully. 
### Description
Empties the package cache.
Empties the [global package cache](https://docs.unity3d.com/6000.0/Documentation/Manual/upm-cache.html). Clearing the cache will free disk space. However, if a package removed from the cache needs to be installed in a project, it will be downloaded. As a result, reinstalling the package will take longer.  
  
`ClearCache()` is an asynchronous operation. Before the operation is complete, you can use the `ClearCacheRequest` instance to monitor the asynchronous operation.  
  
**Note:** Make sure any other Client operations have completed before calling this method. For more information, refer to the note on the [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class reference page. 
* * *
