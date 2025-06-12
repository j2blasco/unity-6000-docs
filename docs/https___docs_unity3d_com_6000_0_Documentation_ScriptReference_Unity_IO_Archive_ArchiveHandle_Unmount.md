* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.Unmount.html

#  [ArchiveHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.Archive.ArchiveHandle.html).Unmount
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
## Declaration
public [Unity.Jobs.JobHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Jobs.JobHandle.html) Unmount(); 
### Returns
**JobHandle** Returns the JobHandle of the unmount operation. 
### Description
Removes the archive from its mount point.
You must call this function for archives that mounted successfully or failed, otherwise you will have a memory leak.
* * *
