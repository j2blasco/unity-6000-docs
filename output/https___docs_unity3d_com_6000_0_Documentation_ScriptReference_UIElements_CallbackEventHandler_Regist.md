* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.RegisterCallbackOnce.html

#  [CallbackEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.html).RegisterCallbackOnce
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
public void RegisterCallbackOnce(EventCallback<TEventType> callback, [UIElements.TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) useTrickleDown); 
### Parameters
Parameter | Description  
---|---  
callback | The event handler to add.  
useTrickleDown | By default, this callback is called during the BubbleUp phase. Pass `TrickleDown.TrickleDown` to call this callback during the TrickleDown phase.  
### Description
Adds an event handler to the instance. If the event handler has already been registered for the same phase (either TrickleDown or BubbleUp) then this method has no effect. The event handler is automatically unregistered after it has been invoked exactly once. 
* * *
## Declaration
public void RegisterCallbackOnce(EventCallback<TEventType,TUserArgsType> callback, TUserArgsType userArgs, [UIElements.TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) useTrickleDown); 
### Parameters
Parameter | Description  
---|---  
callback | The event handler to add.  
userArgs | Data to pass to the callback.  
useTrickleDown | By default, this callback is called during the BubbleUp phase. Pass TrickleDown.TrickleDown to call this callback during the TrickleDown phase.  
### Description
Adds an event handler to the instance. If the event handler has already been registered for the same phase (either TrickleDown or BubbleUp) then this method has no effect. The event handler is automatically unregistered after it has been invoked exactly once. 
* * *
