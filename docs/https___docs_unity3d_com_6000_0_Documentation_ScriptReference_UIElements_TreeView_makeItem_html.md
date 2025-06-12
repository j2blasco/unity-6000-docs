* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView-makeItem.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.TreeView.html).makeItem
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
makeItem; 
### Description
Callback for constructing the VisualElement that is the template for each recycled and re-bound element in the list. 
This callback needs to call a function that constructs a blank [VisualElement](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.VisualElement.html) that is bound to an element from the list.  
  
The collection view automatically creates enough elements to fill the visible area, and adds more if the area is expanded. As the user scrolls, the collection view cycles elements in and out as they appear or disappear.  
  
If this property and bindItem are not set, Unity will either create a PropertyField if bound to a SerializedProperty, or create an empty label for any other case. 
* * *
