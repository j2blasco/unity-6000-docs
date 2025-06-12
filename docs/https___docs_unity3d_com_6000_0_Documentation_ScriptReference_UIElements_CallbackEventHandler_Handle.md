* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.HandleEventTrickleDown.html

#  [CallbackEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.html).HandleEventTrickleDown
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
protected void HandleEventTrickleDown([UIElements.EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) evt); 
### Parameters
Parameter | Description  
---|---  
evt | The event instance.  
### Description
Executes logic on this element during the TrickleDown phase, immediately after this element's TrickleDown callbacks. Calling StopPropagation will prevent further invocations of this method along the propagation path. 
This method is designed to be overriden by subclasses. Use it to implement event handling without registering callbacks, which guarantees precedences of callbacks registered by users of the subclass.  
  
Use [EventInterestAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventInterestAttribute.html) on this method to specify a range of event types that this method needs to receive. Events that don't fall into the specified types might not be sent to this method. 
* * *
