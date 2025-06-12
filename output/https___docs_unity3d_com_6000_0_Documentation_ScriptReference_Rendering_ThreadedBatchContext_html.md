* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.html

# ThreadedBatchContext
struct in UnityEngine.Rendering
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
Thread-safe and Burst-safe API for interacting with a [BatchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.html) from Burst jobs.
### Properties
Property | Description  
---|---  
[batchRendererGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext-batchRendererGroup.html) | An internal handle to the BatchRendererGroup object that created this threaded context.  
### Public Methods
Method | Description  
---|---  
[AddBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.AddBatch.html) | Thread-safe alias for BatchRendererGroup.AddBatch.  
[RemoveBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.RemoveBatch.html) | Thread-safe alias for BatchRendererGroup.RemoveBatch.  
[SetBatchBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.SetBatchBuffer.html) | Change the GraphicsBuffer associated with the given batch. Thread-safe alias for BatchRendererGroup.SetBatchBuffer.  
* * *
