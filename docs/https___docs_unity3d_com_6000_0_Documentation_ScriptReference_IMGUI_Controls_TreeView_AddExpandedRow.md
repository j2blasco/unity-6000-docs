* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.AddExpandedRows.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).AddExpandedRows
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
protected void AddExpandedRows([IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) root, IList<TreeViewItem> rows); 
### Parameters
Parameter | Description  
---|---  
root | Root of the TreeView.  
rows | Rows that will be refilled using the expanded state of TreeView.  
### Description
Adds the expanded rows of the full tree to the input list. Only use this method if a full tree was built in BuildRoot.
Note that the rows list will not be cleared before adding items.  
  
Additional resources: BuildRoot, BuildRows.
* * *
