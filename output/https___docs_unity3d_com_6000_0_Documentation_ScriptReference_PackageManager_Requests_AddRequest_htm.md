* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.AddRequest.html

# AddRequest
class in UnityEditor.PackageManager.Requests
/
Inherits from:[PackageManager.Requests.Request_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request_1.html)
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
Represents an asynchronous request to add a package to the project.
The PackageManager [Client](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.html) class returns an AddRequest instance when you call the [Client.Add](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Client.Add.html) method to add a package to your project. Use this object to determine when the request is complete and to access the result.  
  
Once the request is complete, you can retrieve the [PackageInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.PackageInfo.html) instance from the Result property. 
### Inherited Members
### Properties
Property | Description  
---|---  
[Error](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.Error.html) | The error returned by the request, if any.  
[IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.IsCompleted.html) | Whether the request is complete.  
[Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request.Status.html) | The request status.  
[Result](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Requests.Request_1.Result.html) | The response to the request.  
* * *
