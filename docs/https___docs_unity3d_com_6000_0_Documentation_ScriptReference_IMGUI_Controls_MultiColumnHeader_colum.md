* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ColumnHeaderClicked.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).ColumnHeaderClicked
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
protected void ColumnHeaderClicked([IMGUI.Controls.MultiColumnHeaderState.Column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.Column.html) column, int columnIndex); 
### Parameters
Parameter | Description  
---|---  
column | Column clicked.  
columnIndex | Column index clicked.  
### Description
Override to customize the behavior when clicking a column header.
The default behavior toggles the [MultiColumnHeaderState.Column.sortedAscending](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.Column-sortedAscending.html) property for the column and calls [OnSortingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.OnSortingChanged.html) which in turns dispatches the [sortingChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-sortingChanged.html) event.  
  
Call base.ColumnHeaderClicked to ensure default handling.
* * *
