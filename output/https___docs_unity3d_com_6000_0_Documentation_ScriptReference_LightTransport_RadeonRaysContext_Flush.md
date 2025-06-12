* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.Flush.html

#  [RadeonRaysContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html).Flush
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
public bool Flush(); 
### Returns
**bool** True if the flush was successful. 
### Description
Flush the device context.
Start execution of the enqueued operations. On some platforms the underlying implementation or driver flushes automatically, on others it is up to the user to call Flush. The Flush method returns immediately.
```
          IDeviceContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) ctx = new RadeonRaysContext[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.RadeonRaysContext.html)();
ctx.Initialize();
const int sizeInBytes = 4;
var bufferID = ctx.CreateBuffer(sizeInBytes);
using var results = new NativeArray<float>(1, Allocator.Temp[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Temp.html));
var readEvent = ctx.CreateEvent();
ctx.ReadBuffer(bufferID.Slice<byte>(), results.Reinterpret<byte>(4), readEvent);
ctx.Flush();
ctx.DestroyEvent(readEvent);
ctx.DestroyBuffer(bufferID);
ctx.Dispose();
```

How to use Flush.
* * *
