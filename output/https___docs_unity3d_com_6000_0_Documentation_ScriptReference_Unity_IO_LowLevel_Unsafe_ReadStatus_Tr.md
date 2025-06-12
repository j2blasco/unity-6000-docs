* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html

#  [ReadStatus](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.html).Truncated
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
The asynchronous file request has completed but one or more of the read operations were truncated.
A truncated read occurs when the [ReadCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html) describing the read operation specifies a `Size` and `Offset` that extends past the end of the target file. After the read operation is complete, use [ReadHandle.GetBytesRead](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadHandle.GetBytesRead.html) to get the total number of bytes read for a request, or ReadHandle.GetBytesReadAtIndex to get the number of bytes read for a single [ReadCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html). A truncated read does not typically indicate a problem; all data in the file is read and no extra bytes are copied to your read buffer.
* * *
