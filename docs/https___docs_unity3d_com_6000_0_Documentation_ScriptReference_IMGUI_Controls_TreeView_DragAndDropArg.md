* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs.html

# DragAndDropArgs
struct in UnityEditor.IMGUI.Controls
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
### Description
Method arguments for the [HandleDragAndDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.HandleDragAndDrop.html) virtual method.
### Properties
Property | Description  
---|---  
[dragAndDropPosition](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs-dragAndDropPosition.html) | When dragging items the current drag can have the following 3 positions relative to the items: Upon an item, Between two items or Outside items.  
[insertAtIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs-insertAtIndex.html) | This index refers to the index in the children list of the parentItem where the current drag is positioned.  
[parentItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs-parentItem.html) | The parent item is set if the drag is either upon this item or between two of its children.  
[performDrop](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.DragAndDropArgs-performDrop.html) | This value is false as long as the mouse button is down, when the mouse button is released it is true.  
* * *
