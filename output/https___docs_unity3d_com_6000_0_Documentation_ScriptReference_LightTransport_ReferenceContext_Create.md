* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.CreateEvent.html

#  [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html).CreateEvent
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
public [LightTransport.EventID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.EventID.html) CreateEvent(); 
### Returns
**EventID** ID of newly created event. 
### Description
Creates a new event.
The event may be passed to [IDeviceContext.ReadBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.ReadBuffer.html) and [IDeviceContext.WriteBuffer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.WriteBuffer.html) to track when the corresponding read or write finishes. Once the event is no longer needed, it should be destroyed using [IDeviceContext.DestroyEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.IDeviceContext.DestroyEvent.html).
* * *
