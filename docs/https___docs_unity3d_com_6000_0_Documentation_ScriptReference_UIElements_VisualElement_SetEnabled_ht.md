* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.SetEnabled.html

#  [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html).SetEnabled
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
public void SetEnabled(bool value); 
### Parameters
Parameter | Description  
---|---  
value | New enabled state  
### Description
Changes the [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) enabled state. A disabled visual element does not receive most events. 
The method disables the local flag of the VisualElement and implicitly disables its children. It does not affect the local enabled flag of each child.   
  
A disabled visual element does not receive most input events, such as mouse and keyboard events. However, it can still respond to Attach or Detach events, and geometry change events.   
  
When an element is disabled, its style changes to visually indicate it's inactive.   
  
Additional resources: [VisualElement.enabledSelf](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement-enabledSelf.html)
* * *
