* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.ExpandItem.html

#  [BaseTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.html).ExpandItem
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
public void ExpandItem(int id, bool expandAllChildren, bool refresh); 
### Parameters
Parameter | Description  
---|---  
id | The TreeView item identifier.  
expandAllChildren | When true, all children will also get expanded. This is false by default.  
refresh | Whether to refresh items or not. Set to false when doing multiple operations on the tree, to only do one RefreshItems once all operations are done. This is true by default.  
### Description
Expands the specified TreeView item. 
* * *
