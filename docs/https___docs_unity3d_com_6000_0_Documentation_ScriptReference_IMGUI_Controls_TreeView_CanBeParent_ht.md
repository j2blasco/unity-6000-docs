* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanBeParent.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).CanBeParent
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
protected bool CanBeParent([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
### Parameters
Parameter | Description  
---|---  
item | Can this item be a parent?  
### Description
Override this method to control which items are allowed to be parents.
This is called internally by the TreeView to determine dragging behavior. For list views this function should just return false to prevent any reparenting.  
Default behavior: returns true.
* * *
