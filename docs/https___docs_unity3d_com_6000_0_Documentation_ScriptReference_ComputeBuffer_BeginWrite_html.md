* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.BeginWrite.html

#  [ComputeBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.html).BeginWrite
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
public NativeArray<T> BeginWrite(int computeBufferStartIndex, int count); 
### Parameters
Parameter | Description  
---|---  
computeBufferStartIndex | Offset in number of elements to which the write operation will occur  
count | Maximum number of elements which will be written  
### Returns
**NativeArray <T>** A NativeArray of size count 
### Description
Begins a write operation to the buffer
Use this to begin a write operation on the buffer. Using this method results in fewer memory copies than using [ComputeBuffer.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetData.html), and is therefore faster. For compatibility reasons, you can only call this method on buffers where the [ComputeBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html) is [ComputeBufferMode.SubUpdates](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.SubUpdates.html). If you call this method on a buffer with a different [ComputeBufferMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBufferMode.html), Unity will throw an exception.  
  
The returned native array points directly to GPU memory if possible. If it it not possible to write directly to GPU memory, the returned native array points to a temporary buffer in CPU memory. Whether it is possible to write directly to GPU memory depends on many factors, including buffer mode, active graphics device, and hardware support.  
  
Because of this, the contents of the returned array are not guaranteed to reflect the data content of the GPU side buffer. You should therefore use the returned array only for writing to, and not for reading from.  
  
When you have written to the array, call [ComputeBuffer.EndWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.EndWrite.html) to complete the operation and mark the returned NativeArray as unusable.  
  
The performance of this method will vary depending on whether it can write directly to GPU memory or not, but it will always result in fewer memory copies than using SetData.  
  
The data written to the returned native array must follow the data layout rules of the graphics API in use. See [Compute Shaders](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ComputeShader.html) for cross-platform compatibility information.  
  
Additional resources: [ComputeBuffer.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.SetData.html), [ComputeBuffer.EndWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ComputeBuffer.EndWrite.html)
* * *
