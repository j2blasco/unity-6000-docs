* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html

# ReadCommand
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
Describes the offset, size, and destination buffer of a single read operation.
If the asynchronous file read request results in a [ReadStatus.Truncated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html) or [ReadStatus.Failed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html) state the `Size` field will be updated with the actual number of bytes read.
### Properties
Property | Description  
---|---  
[Buffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.Buffer.html) | The buffer that receives the read data.  
[Offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.Offset.html) | The offset where the read begins, within the file.  
[Size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) | The size of the read in bytes.  
* * *
