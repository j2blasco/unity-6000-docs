* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.html

# FileStatus
enumeration
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
### Description
The possible statuses of a [FileHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.html).
Additional resources: [FileHandle.Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Status.html), [AsyncReadManager.OpenFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html)
### Properties
Property | Description  
---|---  
[Closed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Closed.html) | The file has been closed.  
[Pending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Pending.html) | The asynchronous operation to open the file is still in progress.  
[Open](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Open.html) | The file is open for reading.  
[OpenFailed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.OpenFailed.html) | The request to open this file has failed. You must still dispose of the FileHandle using FileHandle.Close.  
* * *
