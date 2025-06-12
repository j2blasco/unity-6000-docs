* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.WriteBuffer.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).WriteBuffer
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
This is an asynchronous operation. Pass an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) created with [IDeviceContext.CreateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.CreateEvent.html) to track the completion status, if desired. The WriteBuffer method returns immediately after enqueuing the command in the context.  
  
**Note:** [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) is single-use. Once an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) has been passed to this function, it may not be passed to subsequent [IDeviceContext.WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) or [IDeviceContext.ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) calls. Doing so will result in undefined behavior.
```
          IDeviceContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();
uint length = 8;
var input = new NativeArray<byte>((int)length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
for (int i = 0; i < length; ++i)
    input[i] = (byte)i;
BufferID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) id = ctx.CreateBuffer(8);
var writeEvent = ctx.CreateEvent();
ctx.WriteBuffer(id.Slice<byte>(), input, writeEvent);
bool flushOk = ctx.Flush();
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(flushOk);
bool eventOk = ctx.Wait(writeEvent);
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(eventOk);
ctx.DestroyEvent(writeEvent);  
  
// The contents of the input buffer has now been transferred into the buffer allocated by the context.  
  
input.Dispose();
ctx.DestroyBuffer(id);
ctx.Dispose();
```

* * *
