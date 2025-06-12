* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.Contains.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).Contains
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
public bool Contains([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) child); 
### Parameters
Parameter | Description  
---|---  
child | The child element to test against.  
### Returns
**bool** Returns true if this element is a ancestor of the child element, false otherwise. 
### Description
Checks if this element is an ancestor of the specified child element. 
This method "walks up" the hierarchy of the child element until it reaches this element or the root of the visual tree. 
* * *
