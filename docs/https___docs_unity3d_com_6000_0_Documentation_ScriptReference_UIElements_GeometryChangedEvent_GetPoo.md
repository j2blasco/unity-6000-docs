* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GeometryChangedEvent.GetPooled.html

#  [GeometryChangedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GeometryChangedEvent.html).GetPooled
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
public static [UIElements.GeometryChangedEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.GeometryChangedEvent.html) GetPooled([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) oldRect, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) newRect); 
### Parameters
Parameter | Description  
---|---  
oldRect | The old dimensions of the element.  
newRect | The new dimensions of the element.  
### Returns
**GeometryChangedEvent** An initialized event. 
### Description
Gets an event from the event pool, and initializes it with the specified values. Use this method instead of instancing new events. Use Dispose() to release events back to the event pool. 
* * *
