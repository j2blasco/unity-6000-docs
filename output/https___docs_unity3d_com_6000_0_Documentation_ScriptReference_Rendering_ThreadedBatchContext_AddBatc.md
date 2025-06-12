* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.AddBatch.html

#  [ThreadedBatchContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ThreadedBatchContext.html).AddBatch
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
public [Rendering.BatchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchID.html) AddBatch(NativeArray<MetadataValue> batchMetadata, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) buffer); 
## Declaration
public [Rendering.BatchID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchID.html) AddBatch(NativeArray<MetadataValue> batchMetadata, [GraphicsBufferHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBufferHandle.html) buffer, uint bufferOffset, uint windowSize); 
### Parameters
Parameter | Description  
---|---  
batchMetadata | Metadata properties for this batch.  
buffer | The `GraphicsBufferHandle` of the `GraphicsBuffer` associated with this batch.  
bufferOffset | Offset of the buffer to be bound. Defaults to zero (start of the buffer).  
windowSize | Amount of data in the buffer to be bound, starting from the bufferOffset value. Defaults to zero. If this is a constant buffer, this value must be less or equal to [SystemInfo.maxConstantBufferSize].  
### Returns
**BatchID** ID of the batch that Unity creates. 
### Description
Thread-safe alias for [BatchRendererGroup.AddBatch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.BatchRendererGroup.AddBatch.html).
* * *
