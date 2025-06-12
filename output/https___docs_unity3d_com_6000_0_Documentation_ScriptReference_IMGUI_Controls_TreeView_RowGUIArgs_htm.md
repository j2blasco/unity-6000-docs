* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.html

# RowGUIArgs
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
Method arguments for the virtual method [RowGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUI.html).
### Properties
Property | Description  
---|---  
[focused](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-focused.html) | This value is true only when the TreeView has keyboard focus and the TreeView's window has focus.  
[isRenaming](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-isRenaming.html) | This value is true when the ::item is currently being renamed.  
[item](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-item.html) | Item for the current row being handled in TreeView.RowGUI.  
[label](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-label.html) | Label used for text rendering of the item displayName. Note this is an empty string when isRenaming == true.  
[row](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-row.html) | Row index into the list of current rows.  
[rowRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-rowRect.html) | Row rect for the current row being handled.  
[selected](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs-selected.html) | This value is true when the current row's item is part of the current selection.  
### Public Methods
Method | Description  
---|---  
[GetCellRect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.GetCellRect.html) | If using a MultiColumnHeader for the TreeView this method can be used to get the cell rects of a row using the visible columns of the MultiColumnHeader.  
[GetColumn](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.GetColumn.html) | If using a MultiColumnHeader for the TreeView this method can be used to convert an index from the visible columns list to a index into the actual columns in the MultiColumnHeaderState.  
[GetNumVisibleColumns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RowGUIArgs.GetNumVisibleColumns.html) | If using a MultiColumnHeader for the TreeView use this method to get the number of visible columns currently being shown in the MultiColumnHeader.  
* * *
