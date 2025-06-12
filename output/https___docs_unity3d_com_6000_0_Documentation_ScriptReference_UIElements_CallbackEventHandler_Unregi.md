* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.UnregisterCallback.html

#  [CallbackEventHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.CallbackEventHandler.html).UnregisterCallback
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
public void UnregisterCallback(EventCallback<TEventType> callback, [UIElements.TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) useTrickleDown); 
### Parameters
Parameter | Description  
---|---  
callback | The callback to remove. If this callback was never registered, nothing happens.  
useTrickleDown | Set this parameter to true to remove the callback from the TrickleDown phase. Set this parameter to false to remove the callback from the BubbleUp phase.  
### Description
Remove callback from the instance. 
* * *
## Declaration
public void UnregisterCallback(EventCallback<TEventType,TUserArgsType> callback, [UIElements.TrickleDown](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TrickleDown.html) useTrickleDown); 
### Parameters
Parameter | Description  
---|---  
callback | The callback to remove. If this callback was never registered, nothing happens.  
useTrickleDown | Set this parameter to true to remove the callback from the TrickleDown phase. Set this parameter to false to remove the callback from the BubbleUp phase.  
### Description
Remove callback from the instance. 
* * *
