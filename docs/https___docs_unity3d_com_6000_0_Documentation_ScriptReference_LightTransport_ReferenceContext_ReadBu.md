* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.ReadBuffer.html

#  [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html).ReadBuffer
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
public void ReadBuffer(BufferSlice<T> src, NativeArray<T> dst); 
## Declaration
public void ReadBuffer(BufferSlice<T> src, NativeArray<T> dst, [LightTransport.EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) id); 
### Parameters
Parameter | Description  
---|---  
src | The buffer slice to read from.  
dst | The array in the CPU memory that the contents of the buffer should be written to. The array must remain valid until the read operation is complete. Related content: [IDeviceContext.Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Wait.html).  
id | The ID of the event to use to track completion of the read.  
### Description
Read contents of a buffer from the context.
The memory that the buffer slice points to can be transferred into a [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html). On the reference context this method is equivalent to [ReferenceContext.GetNativeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.GetNativeArray.html) because they both finish the read immediately without the need for synchronization.  
  
**Note:** [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) is single-use. Once an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) has been passed to this function, it may not be passed to subsequent [IDeviceContext.WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) or [IDeviceContext.ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) calls. Doing so will result in undefined behavior.
* * *
