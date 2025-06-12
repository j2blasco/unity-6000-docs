* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationEventBase_1.GetPooled.html

#  [NavigationEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationEventBase_1.html).GetPooled
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
public static T GetPooled([EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
modifiers | The modifier keys held down during the event.  
deviceType | The type of device this event was created from.  
### Returns
**T** An initialized navigation event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained from this method should be released back to the pool using Dispose(). 
* * *
