* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetCellRectForTreeFoldouts.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetCellRectForTreeFoldouts
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
protected [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) GetCellRectForTreeFoldouts([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rowRect); 
### Parameters
Parameter | Description  
---|---  
rowRect | Rect for a row.  
### Returns
**Rect** Cell rect in a multi column setup. 
### Description
Utility for multi column setups. This method will clip the input rowRect against the column rect defined by columnIndexForTreeFoldouts to get the cell rect where the the foldout arrows appear.
Additional resources: [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).
* * *
