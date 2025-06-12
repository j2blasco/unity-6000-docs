* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ResizeToFit.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).ResizeToFit
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
public void ResizeToFit(); 
### Description
Resizes the column widths of the columns that have auto-resize enabled to make all the columns fit to the width of the MultiColumnHeader render rect.
If no columns have [MultiColumnHeaderState.Column.autoResize](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeaderState.Column-autoResize.html) enabled then this method does nothing. This method is also called when selecting the 'Resize To Fit' context menu of the MultiColumnHeader.
* * *
