* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardEventBase_1.GetPooled.html

#  [KeyboardEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.KeyboardEventBase_1.html).GetPooled
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
public static T GetPooled(char c, [KeyCode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/KeyCode.html) keyCode, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
c | The character for this event.  
keyCode | The key code for this event.  
modifiers | Event modifier keys that are active for this event.  
### Returns
**T** An initialized event. 
### Description
Gets a keyboard event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
public static T GetPooled([Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) systemEvent); 
### Parameters
Parameter | Description  
---|---  
systemEvent | A keyboard IMGUI event.  
### Returns
**T** An initialized event. 
### Description
Gets a keyboard event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
