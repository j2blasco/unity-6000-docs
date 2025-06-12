* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetRowRect.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetRowRect
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
protected [Rect](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rect.html) GetRowRect(int row); 
### Parameters
Parameter | Description  
---|---  
row | Row index.  
### Returns
**Rect** Row rect. 
### Description
Get the rect for a row.
This rect is limited to the visible width of the scroll view. If the TreeView is using a [MultiColumnHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.MultiColumnHeader.html) then the total width of all the columns can be found by MultiColumnHeaderState.widthOfAllVisibleColumns  
  
Additional resources: [GetRows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetRows.html).
* * *
