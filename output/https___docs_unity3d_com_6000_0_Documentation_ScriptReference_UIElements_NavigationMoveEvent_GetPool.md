* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.GetPooled.html

#  [NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html).GetPooled
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
public static [UIElements.NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html) GetPooled([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) moveVector, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
moveVector | The move vector.  
modifiers | The modifier keys held down during the event.  
### Returns
**NavigationMoveEvent** An initialized navigation event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained from this method should be released back to the pool using Dispose(). 
* * *
## Declaration
public static [UIElements.NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html) GetPooled([UIElements.NavigationMoveEvent.Direction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.Direction.html) direction, [EventModifiers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EventModifiers.html) modifiers); 
### Parameters
Parameter | Description  
---|---  
direction | The logical direction of the navigation.  
modifiers | The modifier keys held down during the event.  
### Returns
**NavigationMoveEvent** An initialized navigation event. 
### Description
Gets an event from the event pool and initializes it with the given values. Use this function instead of creating new events. Events obtained from this method should be released back to the pool using Dispose(). 
This method doesn't set any move vector. See other overload of the method for more information. 
* * *
