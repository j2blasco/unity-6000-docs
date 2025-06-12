* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.IsCompleted.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).IsCompleted
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
public bool IsCompleted([LightTransport.EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) id); 
### Parameters
Parameter | Description  
---|---  
id | ID of the event to query.  
### Returns
**bool** True if the asynchronous operation has completed. 
### Description
Returns true if the asynchronous operation completed.
This method returns immediately and does not wait for the operation to complete. Use Flush to force the device implementation to start processing commands. Use [IDeviceContext.Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Wait.html) to busy-wait for a specific event.
```
          IDeviceContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();
uint length = 8;
var input = new NativeArray<byte>((int)length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
for (int i = 0; i < length; ++i)
{
    input[i] = (byte)i;
}
var output = new NativeArray<byte>((int)length, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html));
BufferID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) id = ctx.CreateBuffer(8);
var writeEvent = ctx.CreateEvent();
ctx.WriteBuffer(id.Slice<byte>(), input, writeEvent);
var readEvent = ctx.CreateEvent();
ctx.ReadBuffer(id.Slice<byte>(), output, readEvent);
bool flushOk = ctx.Flush();
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(flushOk);
input.Dispose();
var watchDogTimeout = Time.realtimeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html) + 5.0f;
while (!ctx.IsCompleted(readEvent))
{
    Thread.Sleep(10);
    if (Time.realtimeSinceStartup[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Time-realtimeSinceStartup.html) > watchDogTimeout)
        Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(false, "watchdog timeout");
}  
  
// The event has completed.
ctx.DestroyEvent(readEvent);
ctx.DestroyEvent(writeEvent);  
  
ctx.DestroyBuffer(id);
for (int i = 0; i < length; ++i)
    Assert.AreEqual[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.AreEqual.html)((byte)i, output[i]);
output.Dispose();
ctx.Dispose();
```

How to check if an asynchronous operation has completed.
* * *
