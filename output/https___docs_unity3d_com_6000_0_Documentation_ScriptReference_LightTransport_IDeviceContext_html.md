* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.html

# IDeviceContext
interface in UnityEngine.LightTransport
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
### Description
Interface for a device.
Abstraction layer for memory, synchronization, and compute provided by different devices.
### Public Methods
Method | Description  
---|---  
[CreateBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.CreateBuffer.html) | Create a new buffer for a number of elements with a given stride.  
[CreateEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.CreateEvent.html) | Creates a new event.  
[DestroyBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.DestroyBuffer.html) | Destroy the buffer with the given ID.  
[DestroyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.DestroyEvent.html) | Destroy the event with the given ID. You should call this to free temporary resources associated with an event. Attempting to use the event after it has been destroyed, for example using IDeviceContext.Wait or IDeviceContext.IsCompleted will result in undefined behavior.  
[Flush](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Flush.html) | Flush the device context.  
[Initialize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Initialize.html) | Initialize.  
[IsCompleted](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.IsCompleted.html) | Returns true if the asynchronous operation completed.  
[ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) | Read contents of a buffer from the context.  
[Wait](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.Wait.html) | Wait for an asynchronous event.  
[WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) | Write data into the memory buffer allocated by the context.  
* * *
