* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.DestroyEvent.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).DestroyEvent
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
public void DestroyEvent([LightTransport.EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) id); 
### Parameters
Parameter | Description  
---|---  
id | ID of the event to destroy.  
### Description
Destroy the event with the given ID. You should call this to free temporary resources associated with an event. Attempting to use the event after it has been destroyed, for example using [IDeviceContext.Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Wait.html) or [IDeviceContext.IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.IsCompleted.html) will result in undefined behavior.
```
// Create context.
using var ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();  
  
// Create buffer.
BufferID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.BufferID.html) buffer = ctx.CreateBuffer(sizeof(int) * 8);
using var array = new NativeArray<int>(8, Allocator.Persistent[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html), NativeArrayOptions.ClearMemory[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.NativeArrayOptions.ClearMemory.html));  
  
// Write to buffer and wait for completion.
EventID[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) evt = ctx.CreateEvent();
ctx.WriteBuffer(buffer.Slice<int>(), array, evt);
var flushOk = ctx.Flush();
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(flushOk);
var waitOk = ctx.Wait(evt);
Assert.IsTrue[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Assert.IsTrue.html)(waitOk);  
  
// Cleanup. After this point, we may no longer use `evt`.
ctx.DestroyEvent(evt);
ctx.DestroyBuffer(buffer);
```

Proper usage of DestroyEvent.
* * *
