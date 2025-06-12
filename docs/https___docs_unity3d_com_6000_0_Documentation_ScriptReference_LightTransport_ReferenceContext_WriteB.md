* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.WriteBuffer.html

#  [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html).WriteBuffer
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
public void WriteBuffer(BufferSlice<T> dst, NativeArray<T> src); 
## Declaration
public void WriteBuffer(BufferSlice<T> dst, NativeArray<T> src, [LightTransport.EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) id); 
### Parameters
Parameter | Description  
---|---  
dst | The buffer slice to write to.  
src | The array in the CPU memory that should be written to the buffer. The array must remain valid until the write operation is complete.  
id | The ID of the event to use to track completion of the write.  
### Description
Write data into the memory buffer allocated by the context.
The [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html) implementation of the WriteBuffer method is blocking and returns immediately after writing data into the underlying NativeArray.  
  
**Note:** [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) is single-use. Once an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) has been passed to this function, it may not be passed to subsequent [IDeviceContext.WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) or [IDeviceContext.ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) calls. Doing so will result in undefined behavior.
* * *
