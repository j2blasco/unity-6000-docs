* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.SetBatchBuffer.html

#  [ThreadedBatchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.html).SetBatchBuffer
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
public void SetBatchBuffer([Rendering.BatchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchID.html) batchID, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) buffer); 
### Parameters
Parameter | Description  
---|---  
batchID | Unity changes the batch with this ID.  
buffer | The `GraphicsBufferHandle` of the `GraphicsBuffer` to be associated with the batch.  
### Description
Change the `GraphicsBuffer` associated with the given batch. Thread-safe alias for [BatchRendererGroup.SetBatchBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.SetBatchBuffer.html).
* * *
