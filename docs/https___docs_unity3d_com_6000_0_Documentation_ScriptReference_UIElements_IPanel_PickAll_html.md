* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.PickAll.html

#  [IPanel](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IPanel.html).PickAll
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
public [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) PickAll([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) point, List<VisualElement> picked); 
### Parameters
Parameter | Description  
---|---  
point | World coordinates.  
picked | All Visualelements overlapping this position.  
### Returns
**VisualElement** Top VisualElement at the position. Null if none was found. 
### Description
Returns all elements at this position. Will not return elements with pickingMode set to [PickingMode.Ignore](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.PickingMode.Ignore.html). 
* * *
