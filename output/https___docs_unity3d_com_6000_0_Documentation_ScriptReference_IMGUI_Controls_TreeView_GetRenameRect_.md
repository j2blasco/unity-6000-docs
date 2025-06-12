* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetRenameRect.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetRenameRect
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
protected [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) GetRenameRect([Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) rowRect, int row, [IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
### Parameters
Parameter | Description  
---|---  
rowRect | Row rect for the item currently being renamed.  
row | Row index for the item currently being renamed.  
item | TreeViewItem that are currently being renamed.  
### Returns
**Rect** The rect where the rename overlay should appear. 
### Description
Override this method if custom GUI handling are used in [RowGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUI.html). This method for controls where the rename overlay appears.
By default the rename overlay matches the placement of the item's displayName text being rendered.
* * *
