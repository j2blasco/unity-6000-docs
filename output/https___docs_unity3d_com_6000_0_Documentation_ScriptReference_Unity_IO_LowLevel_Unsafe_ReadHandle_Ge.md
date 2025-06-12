* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadHandle.GetBytesReadArray.html

#  [ReadHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadHandle.html).GetBytesReadArray
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
public ulong* GetBytesReadArray(); 
### Returns
**ulong*** An unsafe pointer to the array storing the number of bytes read for each ReadCommand in the request. 
### Description
Returns an array containing the number of bytes read by the [ReadCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html) operations during the asynchronous file read request, where each index corresponds to the ReadCommand index.
It is not safe to retain the pointer after the ReadHandle has been disposed, as it will have been freed internally.  
  
The number of entries in the array is equal to [ReadHandle.ReadCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadHandle.ReadCount.html), so this can be used to find the maximum size of the array. This field (and the array itself) is resized at the start of the read.  
  
A truncated read occurs when the [ReadCommand](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.html) describing the read operation specifies a [ReadCommand.Size](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.Size.html) and [ReadCommand.Offset](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadCommand.Offset.html) that extends past the end of the target file.
* * *
