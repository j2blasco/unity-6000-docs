* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.SortingButton.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).SortingButton
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
protected void SortingButton([IMGUI.Controls.MultiColumnHeaderState.Column](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.Column.html) column, [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) headerRect, int columnIndex); 
### Parameters
Parameter | Description  
---|---  
column | Column data.  
headerRect | Column header rect.  
columnIndex | Column index.  
### Description
Provides the button logic for a column header and the rendering of the sorting arrow (if visible).
Can be used if overriding [ColumnHeaderGUI](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ColumnHeaderGUI.html) to provide the default behavior when clicking a column header.
* * *
