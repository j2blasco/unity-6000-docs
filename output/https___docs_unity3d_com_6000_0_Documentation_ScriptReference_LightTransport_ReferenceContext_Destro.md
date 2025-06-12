* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.DestroyEvent.html

#  [ReferenceContext](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LightTransport.ReferenceContext.html).DestroyEvent
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
* * *
