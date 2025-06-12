* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.html

# ArchiveHandle
struct in Unity.IO.Archive
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
Represents an asynchronous operation handle that references an archive.
Additional resources: [ArchiveFileInterface.MountAsync](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveFileInterface.MountAsync.html)
### Properties
Property | Description  
---|---  
[Compression](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Compression.html) | The type of compression the archive uses.  
[IsStreamed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.IsStreamed.html) | Indicates if the archive contains streamed blocks.  
[JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.JobHandle.html) | JobHandle of the mount operation.  
[Status](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Status.html) | Status of the archive mount operation.  
### Public Methods
Method | Description  
---|---  
[GetFileInfo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.GetFileInfo.html) | Retrieves information about files included in the archive.  
[GetMountPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.GetMountPath.html) | Retrieves the path where the archive was mounted.  
[Unmount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Unmount.html) | Removes the archive from its mount point.  
* * *
