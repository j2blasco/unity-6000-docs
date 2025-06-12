* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView-bindItem.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html).bindItem
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
bindItem; 
### Description
Callback for binding a data item to the visual element. 
The method called by this callback receives the VisualElement to bind, and the index of the element to bind it to.  
  
If this property and makeItem are not set, Unity will try to bind to a SerializedProperty if bound, or simply set text in the created Label.  
  
**Note:** : Setting this callback without also setting unbindItem might result in unexpected behavior. This is because the default implementation of unbindItem expects the default implementation of bindItem. 
* * *
