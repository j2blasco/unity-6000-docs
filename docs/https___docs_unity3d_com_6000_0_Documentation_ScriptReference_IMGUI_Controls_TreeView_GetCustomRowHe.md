* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.GetCustomRowHeight.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).GetCustomRowHeight
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
protected float GetCustomRowHeight(int row, [IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) item); 
### Parameters
Parameter | Description  
---|---  
row | Row index.  
item | Item for given row.  
### Returns
**float** Height of row. 
### Description
Override to control individual row heights.
Override this method if custom row rects are needed for each row in the TreeView, for example if you have content that can vary in height depending on the content. This method is called internally by the TreeView for each row after BuildRows have been called. If this method is not overridden then the `rowHeight` property is used for all rows.  
  
This method should only be overridden if row heights can differ; if all rows have same height then use the `rowHeight` property as this is more performant for large data sets.  
  
The heights returned by this method are cached. To update the cache call [RefreshCustomRowHeights](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.RefreshCustomRowHeights.html).
* * *
