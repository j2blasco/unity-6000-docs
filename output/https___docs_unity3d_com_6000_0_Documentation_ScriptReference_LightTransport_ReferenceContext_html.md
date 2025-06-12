* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html

# ReferenceContext
class in UnityEngine.LightTransport
Leave feedback
  

Implements interfaces:[IDeviceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html)
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
### Description
The [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html) implements the [IDeviceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html) interface.
The implementation favors correctness and simplicity over performance. It runs on CPU without multithreading, asynchronous execution or any other optimizations. The class is meant for debugging and is not intended for production use.
### Constructors
Constructor | Description  
---|---  
[ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext-ctor.html) | Constructor.  
### Public Methods
Method | Description  
---|---  
[CreateBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.CreateBuffer.html) | Create a new buffer for a number of elements with a given stride.  
[CreateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.CreateEvent.html) | Creates a new event.  
[DestroyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.DestroyBuffer.html) | Destroy the buffer with the given ID.  
[DestroyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.DestroyEvent.html) | Destroy the event with the given ID. You should call this to free temporary resources associated with an event. Attempting to use the event after it has been destroyed, for example using IDeviceContext.Wait or IDeviceContext.IsCompleted will result in undefined behavior.  
[Dispose](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.Dispose.html) | Dispose.  
[Flush](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.Flush.html) | Flush the device context.  
[GetNativeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.GetNativeArray.html) | Get the NativeArray used for storing buffers in the context.  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.Initialize.html) | Initialize the device context.  
[IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.IsCompleted.html) | Returns true if the asynchronous operation completed.  
[ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.ReadBuffer.html) | Read contents of a buffer from the context.  
[Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.Wait.html) | Wait for an asynchronous event.  
[WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.WriteBuffer.html) | Write data into the memory buffer allocated by the context.  
* * *
