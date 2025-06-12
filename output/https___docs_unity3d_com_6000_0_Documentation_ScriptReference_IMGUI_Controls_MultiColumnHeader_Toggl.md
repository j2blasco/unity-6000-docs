* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.ToggleVisibility.html

#  [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html).ToggleVisibility
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
protected void ToggleVisibility(int columnIndex); 
### Parameters
Parameter | Description  
---|---  
columnIndex | Toggle visibility for this column.  
### Description
Method for toggling the visibility of a column.
This is also called from the context menu of the MultiColumnHeader. This method toggles the visiblity state, calls ::ef::OnVisibleColumnsChanged which in turn dispatces the [visibleColumnsChanged](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader-visibleColumnsChanged.html) event.
* * *
