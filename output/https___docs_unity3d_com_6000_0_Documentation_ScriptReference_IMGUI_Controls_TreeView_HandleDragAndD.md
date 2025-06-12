* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.HandleDragAndDrop.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).HandleDragAndDrop
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
protected [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) HandleDragAndDrop([IMGUI.Controls.TreeView.DragAndDropArgs](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs.html) args); 
### Parameters
Parameter | Description  
---|---  
args | Drag and drop arguments.  
### Description
Override this function to control the drag and drop behavior of the TreeView.
This function is called continously when a drag and drop operation is active and the cursor is over the TreeView. Note that the drag and drop operation can have been initiated outside the TreeView.  
  
Use the state in [DragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDrop.html) to determine the objects for the drag and drop. This function returns a [DragAndDropVisualMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DragAndDropVisualMode.html) value that controls the cursor state.  
  
You control TreeView drag and drop in the following order:  
1) override [CanStartDrag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.CanStartDrag.html) to enable dragging TreeViewItems.  
2) override [SetupDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetupDragAndDrop.html) to set which TreeViewItems are dragged.  
3) override [HandleDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.HandleDragAndDrop.html) to control the drag and drop behavior of the TreeView.  

* * *
