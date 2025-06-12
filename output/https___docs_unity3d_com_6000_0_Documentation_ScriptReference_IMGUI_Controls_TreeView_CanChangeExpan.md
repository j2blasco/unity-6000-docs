* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanChangeExpandedState.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).CanChangeExpandedState
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
protected bool CanChangeExpandedState([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
### Parameters
Parameter | Description  
---|---  
item | Can this item be expanded/collapsed.  
### Description
Override this method to control whether an item can be expanded or collapsed by key or mouse.
If this method returns false the foldout arrow for an item will not be shown. Default behavior: if a search is active this method returns false (for search results, no foldout is required since the the results are shown as a flat list). If no search is active then by default it returns true if the item has any children, and false if it has no children.
* * *
