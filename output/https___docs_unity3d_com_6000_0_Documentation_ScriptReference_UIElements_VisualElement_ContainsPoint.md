* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.ContainsPoint.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).ContainsPoint
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
public bool ContainsPoint([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) localPoint); 
### Parameters
Parameter | Description  
---|---  
localPoint | The point in the local space of the element.  
### Returns
**bool** Returns true if the point is contained within the element's layout. Otherwise, returns false. 
### Description
Checks if the specified point intersects with this VisualElement's layout. 
Unity calls this method to find out what elements are under a cursor (such as a mouse). Do not rely on this method to perform invalidation, since Unity might cache results or skip some invocations of this method for performance reasons. By default, a VisualElement has a rectangular area. Override this method in your VisualElement subclass to customize this behaviour. 
* * *
