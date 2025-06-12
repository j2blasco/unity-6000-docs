* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.ReadBuffer.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).ReadBuffer
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
The memory that the [BufferSlice<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferSlice_1.html) points to can be transferred into a [NativeArray<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArray_1.html). This is an asynchronous operation. Pass an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) created with [IDeviceContext.CreateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.CreateEvent.html) to track the completion status, if desired. This method returns immediately after enqueuing the command in the context.  
  
**Note:** [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) is single-use. Once an [EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) has been passed to this function, it may not be passed to subsequent [IDeviceContext.WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) or [IDeviceContext.ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) calls. Doing so will result in undefined behavior.
```
          IDeviceContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();
uint length = 8;
var input = new NativeArray<byte>((int)length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
for (int i = 0; i < length; ++i)
    input[i] = (byte)i;
var output = new NativeArray<byte>((int)length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
BufferID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) id = ctx.CreateBuffer(8);
var writeEvent = ctx.CreateEvent();
ctx.WriteBuffer(id.Slice<byte>(), input, writeEvent);
var readEvent = ctx.CreateEvent();
ctx.ReadBuffer(id.Slice<byte>(), output, readEvent);
bool flushOk = ctx.Flush();
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(flushOk);
bool eventOk = ctx.Wait(writeEvent);
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(eventOk);  
  
// Contents of the buffer is now available in the CPU side memory array output.  
  
input.Dispose();
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(ctx.IsCompleted(readEvent));
ctx.DestroyEvent(readEvent);
ctx.DestroyEvent(writeEvent);
ctx.DestroyBuffer(id);
for (int i = 0; i < length; ++i)
    Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)((byte)i, output[i]);
output.Dispose();
ctx.Dispose();
```

How to read back a buffer.
* * *
