* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetExpanded.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).SetExpanded
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
public bool SetExpanded(int id, bool expanded); 
### Parameters
Parameter | Description  
---|---  
id | TreeViewItem ID.  
expanded | True expands item. False collapses item.  
### Returns
**bool** True if item changed expanded state, false if item already had the `expanded` state. 
### Description
Set a single TreeViewItem to be expanded or collapsed.
* * *
## Declaration
public void SetExpanded(IList<int> ids); 
### Parameters
Parameter | Description  
---|---  
ids | List of item IDs that should be expanded.  
### Description
Set the current expanded TreeViewItems of the TreeView. This will overwrite the previous expanded state.
* * *
