* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController.IgnoreEvent.html

#  [FocusController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.FocusController.html).IgnoreEvent
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
public void IgnoreEvent([UIElements.EventBase](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.EventBase.html) evt); 
### Parameters
Parameter | Description  
---|---  
evt | The event to be ignored.  
### Description
Instructs the FocusController to ignore the given event. This will prevent the event from changing the current focused VisualElement or triggering focus events. 
In general this will have no effect if the event is not a [PointerDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PointerDownEvent.html), [MouseDownEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.MouseDownEvent.html), or [NavigationMoveEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.NavigationMoveEvent.html). 
* * *
