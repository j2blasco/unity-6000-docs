* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.FindItem.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).FindItem
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
protected [IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) FindItem(int id, [IMGUI.Controls.TreeViewItem](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeViewItem.html) searchFromThisItem); 
### Parameters
Parameter | Description  
---|---  
id | Find the TreeViewItem with this ID.  
searchFromThisItem | Sets the search to start from an item. Use 'rootItem' to search the entire tree.  
### Returns
**TreeViewItem** This search method returns the TreeViewItem found and returns null if not found. 
### Description
Finds a TreeViewItem by an ID.
Set the searchFromThisItem parameter to 'rootItem' to search the entire tree.
* * *
