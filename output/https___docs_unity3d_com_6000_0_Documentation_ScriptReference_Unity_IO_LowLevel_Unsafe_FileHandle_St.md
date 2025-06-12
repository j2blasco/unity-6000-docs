* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Status.html

#  [FileHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.html).Status
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
[Unity.IO.LowLevel.Unsafe.FileStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.html) Status; 
### Description
The current status of this FileHandle.
After you call [AsyncReadManager.OpenFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html), the FileHandle enters the [FileStatus.Pending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Pending.html) state. Once the open operation completes, the status changes to either [FileStatus.Open](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Open.html) or [FileStatus.Closed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileStatus.Closed.html) (if the file failed to open).  
  
Note: When the close operation completes, the FileHandle is disposed and becomes invalid. You can use the JobHandle returned by [Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) to check for close operation completion.
* * *
