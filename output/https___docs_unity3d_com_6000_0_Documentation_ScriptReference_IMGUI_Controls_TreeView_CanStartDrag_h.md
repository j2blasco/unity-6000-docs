* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanStartDrag.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).CanStartDrag
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
protected bool CanStartDrag([IMGUI.Controls.TreeView.CanStartDragArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanStartDragArgs.html) args); 
### Description
This function is called whenever a TreeViewItem is clicked and dragged. It returns false by default.
Override this function so it returns true to enable drag and drop behavior for TreeViewItems.  
  
You control TreeView drag and drop in the following order:  
1) override [CanStartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanStartDrag.html) to enable dragging TreeViewItems.  
2) override [SetupDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDragAndDrop.html) to set which TreeViewItems are dragged.  
3) override [HandleDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.HandleDragAndDrop.html) to control the drag and drop behavior of the TreeView.  

* * *
