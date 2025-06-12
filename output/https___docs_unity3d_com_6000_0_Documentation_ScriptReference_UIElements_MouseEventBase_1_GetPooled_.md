* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEventBase_1.GetPooled.html

#  [MouseEventBase<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseEventBase_1.html).GetPooled
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
public static T GetPooled([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position, int button, int clickCount, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) delta, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
position | The mouse position.  
button | The mouse button pressed.  
clickCount | The number of consecutive mouse clicks received.  
delta | The relative movement of the mouse compared to the mouse position when the last event was received.  
modifiers | The modifier keys held down during the event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
public static T GetPooled([UIElements.IMouseEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IMouseEvent.html) triggerEvent); 
### Parameters
Parameter | Description  
---|---  
triggerEvent | The event that sent this event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
## Declaration
protected static T GetPooled([UIElements.IPointerEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPointerEvent.html) pointerEvent); 
### Parameters
Parameter | Description  
---|---  
pointerEvent | The pointer event that sent this event.  
### Returns
**T** An initialized event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained using this method need to be released back to the pool. You can use `Dispose()` to release them. 
* * *
