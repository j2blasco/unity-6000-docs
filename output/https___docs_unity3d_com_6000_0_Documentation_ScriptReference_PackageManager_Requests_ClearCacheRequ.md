* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.ClearCacheRequest.html

# ClearCacheRequest
class in UnityEditor.PackageManager.Requests
/
Inherits from:[PackageManager.Requests.Request](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.html)
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
Represents an asynchronous request to clear the global package cache on the disk.
The PackageManager [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class returns a ClearCacheRequest instance when you call the [Client.ClearCache](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.ClearCache.html) method to empty the global package cache. Use this object to determine when the request is complete and if it succeeded. 
### Inherited Members
### Properties
Property | Description  
---|---  
[Error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.Error.html) | The error returned by the request, if any.  
[IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.IsCompleted.html) | Whether the request is complete.  
[Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.Status.html) | The request status.  
* * *
