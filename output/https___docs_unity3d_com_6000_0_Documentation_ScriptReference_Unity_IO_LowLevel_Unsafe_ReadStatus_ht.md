* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.html

# ReadStatus
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
The state of an asynchronous file request.
These enumerations represent the raw underlying states of an asynchronous file request.  
  
When submitted, all requests enter the [ReadStatus.InProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.InProgress.html) state while they are pending execution or in progress. On completion, the state changes to [ReadStatus.Complete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Complete.html), [ReadStatus.Truncated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html) or [ReadStatus.Failed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html). If the read is canceled before completion, the state becomes [ReadStatus.Canceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Canceled.html).  
  
A truncated read occurs when attempting to access beyond the end of a file.
### Properties
Property | Description  
---|---  
[Complete](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Complete.html) | The asynchronous file request completed successfully and all read operations within it were completed in full.  
[InProgress](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.InProgress.html) | The asynchronous file request is in progress.  
[Failed](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Failed.html) | One or more of the asynchronous file request's read operations have failed.  
[Truncated](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Truncated.html) | The asynchronous file request has completed but one or more of the read operations were truncated.  
[Canceled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.IO.LowLevel.Unsafe.ReadStatus.Canceled.html) | The asynchronous file request was canceled before the read operations were completed.  
* * *
