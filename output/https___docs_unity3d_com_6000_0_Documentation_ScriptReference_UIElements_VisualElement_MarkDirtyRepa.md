* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.MarkDirtyRepaint.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).MarkDirtyRepaint
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
public void MarkDirtyRepaint(); 
### Description
Triggers a repaint of the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) on the next frame. This method is called internally when a change occurs that requires a repaint, such as when UIElements.[BaseField_1.value](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/BaseField_1-value.html) is changed or the text in a [Label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.Label.html). If you are implementing a custom control, you can call this method to trigger a repaint when a change occurs that requires a repaint such as when using [generateVisualContent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-generateVisualContent.html) to render a mesh and the mesh data has now changed. 
* * *
