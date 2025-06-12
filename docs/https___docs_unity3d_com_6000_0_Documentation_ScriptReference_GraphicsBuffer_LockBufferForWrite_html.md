* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.LockBufferForWrite.html

#  [GraphicsBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.html).LockBufferForWrite
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
public NativeArray<T> LockBufferForWrite(int bufferStartIndex, int count); 
### Parameters
Parameter | Description  
---|---  
bufferStartIndex | The index of an element where the write operation begins.  
count | Maximum number of elements which will be written  
### Returns
**NativeArray <T>** A NativeArray of size count 
### Description
Begins a write operation to the buffer
Use this to begin a write operation on the buffer. Using this method results in fewer memory copies than using [GraphicsBuffer.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html), and is therefore faster. For compatibility reasons, you can only call this method on buffers where the buffer has been created with the GraphicsBuffer.UsageFlag.LockBufferForWrite flag set. Unity will throw an exception if called on a buffer where this flag was not passed on creation.  
  
The returned native array points directly to GPU memory if possible. If it is not possible to write directly to GPU memory, the returned native array points to a temporary buffer in CPU memory. Whether it is possible to write directly to GPU memory depends on many factors, including buffer usage, active graphics device, and hardware support.  
  
Because of this, the contents of the returned array are undefined. They may reflect data on the GPU, but no guarantees are made. You may therefore use the returned array only for writing to, not reading from, the GPU.  
  
When you have written to the array, call [GraphicsBuffer.UnlockBufferAfterWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UnlockBufferAfterWrite.html) to complete the operation and mark the returned NativeArray as unusable.  
  
The performance of this method will vary depending on whether it can write directly to GPU memory or not, but it will always result in fewer memory copies than using SetData.  
  
The data written to the returned native array must follow the data layout rules of the graphics API in use. See [[Compute Shaders]] for cross-platform compatibility information. Linear writes and no reads are recommended since the buffer might point to write combined memory.  
  
Additional resources: [GraphicsBuffer.SetData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.SetData.html), [GraphicsBuffer.UnlockBufferAfterWrite](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GraphicsBuffer.UnlockBufferAfterWrite.html)
* * *
