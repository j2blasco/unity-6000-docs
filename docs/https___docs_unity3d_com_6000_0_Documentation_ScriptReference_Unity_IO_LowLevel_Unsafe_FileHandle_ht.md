* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.html

# FileHandle
struct in Unity.IO.LowLevel.Unsafe
/
Implemented in:[UnityEngine.CoreModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.CoreModule.html)
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
A handle to an asynchronously opened file.
Opening a file with [AsyncReadManager.OpenFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.OpenFileAsync.html) returns a FileHandle instance. You can use this handle to check the status of the asynchronous open operation.  
  
Use [AsyncReadManager.Read](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.Read.html) to read the data in the file after the open operation is complete. This will automatically wait for the open operation to complete, and give the ReadHandle a WaitingOnJob ReadStatus while it does so. If using [AsyncReadManager.ReadDeferred](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.ReadDeferred.html) instead, you should make sure that the passed in JobHandle waits on this [JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.JobHandle.html) to schedule the read job after the open operation finishes.  
  
Always call [Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) on the FileHandle when finished to avoid memory leaks and holding a file open. You must call close even if the open operation failed, to dispose of the FileHandle.  
  
To write to a file, use the standard .NET File APIs, such as System.IO.StreamWriter. You must close this FileHandle before you can read or write to the file with other APIs. (If a file is held open by the [AsyncReadManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.html)'s file cache, you can use [AsyncReadManager.CloseCachedFileAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.AsyncReadManager.CloseCachedFileAsync.html) to close it, but do not use that API to close files for which you have a FileHandle as these are not in the cache.) 
### Properties
Property | Description  
---|---  
[JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.JobHandle.html) | The JobHandle of the asynchronous file open operation begun by the call to AsyncReadManager.OpenFileAsync that returned this FileHandle instance.  
[Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Status.html) | The current status of this FileHandle.  
### Public Methods
Method | Description  
---|---  
[Close](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.Close.html) | Asynchronously closes the file referenced by this FileHandle and disposes the FileHandle instance.  
[IsValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.FileHandle.IsValid.html) | Reports whether this FileHandle instance is valid.  
* * *
