* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementExtensions.StretchToParentSize.html

#  [VisualElementExtensions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElementExtensions.html).StretchToParentSize
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
public static void StretchToParentSize([UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) elem); 
### Parameters
Parameter | Description  
---|---  
elem | The element to be aligned with its parent  
### Description
Aligns a VisualElement's left, top, right and bottom edges with the corresponding edges of its parent. 
This method provides a way to set the following styles in one operation: - [IStyle.position](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-position.html) is set to [Position.Absolute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Position.Absolute.html) - [IStyle.left](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-left.html) is set to 0 - [IStyle.top](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-top.html) is set to 0 - [IStyle.right](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-right.html) is set to 0 - [IStyle.bottom](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.IStyle-bottom.html) is set to 0 
* * *
