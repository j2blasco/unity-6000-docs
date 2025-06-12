* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.SetExpandedRecursive.html

#  [TreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/IMGUI.Controls.TreeView.html).SetExpandedRecursive
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
public void SetExpandedRecursive(int id, bool expanded); 
### Parameters
Parameter | Description  
---|---  
id | TreeViewItem ID.  
expanded | Expanded state: true expands, false collapses.  
### Description
Expand or collapse all items under item with id.
This is also used internally when Alt/Option + clicking an foldout arrow of an item to expand/collapse the entire sub-tree under this item.
* * *
