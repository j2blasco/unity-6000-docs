* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-cellMargin.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).cellMargin
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
cellMargin; 
### Description
When using a MultiColumnHeader this value adjusts the cell rects provided for all columns except the tree foldout column.
This value is used for all cell margins except the column with the tree view foldouts since that column uses [baseIndent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView-baseIndent.html) and assumes full width for rename overlay placement.  
  
Additional resources: [TreeView.RowGUIArgs.GetCellRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.GetCellRect.html).
* * *
