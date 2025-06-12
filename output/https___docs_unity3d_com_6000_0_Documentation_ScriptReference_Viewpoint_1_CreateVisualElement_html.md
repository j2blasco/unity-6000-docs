* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.CreateVisualElement.html

#  [Viewpoint<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Viewpoint_1.html).CreateVisualElement
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
public [UIElements.VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) CreateVisualElement(); 
### Returns
**VisualElement** The VisualElement to attach to the Cameras Overlay when the associated camera is active. 
### Description
CreateVisualElement is called when a Viewpoint is selected in the Cameras Overlay.
Viewpoint sends visual information directly on to the Cameras overlay. Provide a reference of an instance of VisualElement and it attaches underneath the Cameras overlay toolbar when a Camera is being looked through.
* * *
