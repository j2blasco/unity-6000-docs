* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.GetPooled.html

#  [PointerEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerEventBase_1.html).GetPooled
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
public static T GetPooled([Event](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Event.html) systemEvent); 
### Parameters
Parameter | Description  
---|---  
systemEvent | An IMGUI mouse event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
public static T GetPooled([Touch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Touch.html) touch, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
touch | A <see cref="Touch" /> structure from the InputManager.  
modifiers | The modifier keys held down during the event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
public static T GetPooled([PenData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PenData.html) pen, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
pen | A <see cref="PenData" /> structure from the InputManager containing pen event information.  
modifiers | The modifier keys held down during the event.  
### Returns
**T** An initialized event. 
### Description
Gets a pointer event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
public static T GetPooled([UIElements.IPointerEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) triggerEvent); 
### Parameters
Parameter | Description  
---|---  
triggerEvent | The event that sent this event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
