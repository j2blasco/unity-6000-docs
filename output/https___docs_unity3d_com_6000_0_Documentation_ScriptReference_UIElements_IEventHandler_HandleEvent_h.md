* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.HandleEvent.html

#  [IEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IEventHandler.html).HandleEvent
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
public void HandleEvent([UIElements.EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) evt); 
### Parameters
Parameter | Description  
---|---  
evt | The event to handle.  
### Description
Handles an event according to its propagation phase and current target, by executing the element's default action or callbacks associated with the event. 
The [EventDispatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventDispatcher.html) might invoke this method multiple times for the same event: once for each propagation phase and each target along the event's propagation path if it has matching callbacks or overrides default actions for the event.  
  
**Note:** Do not use this method to intercept all events whose propagation path includes this element. There is no guarantee that it will or will not be invoked for a propagation phase or target along the propagation path if that target has no callbacks for the event and has no default action override that can receive the event.   
  
Additional resources: [CallbackEventHandler.RegisterCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallback.html), [CallbackEventHandler.HandleEventBubbleUp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventBubbleUp.html)
* * *
