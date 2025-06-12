* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.CollapseItem.html

#  [BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html).CollapseItem
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
public void CollapseItem(int id, bool collapseAllChildren, bool refresh); 
### Parameters
Parameter | Description  
---|---  
id | The item ID.  
collapseAllChildren | Whether the whole hierarchy under that item will be collapsed.  
refresh | Whether to refresh items or not. Set to false when doing multiple operations on the tree, to only do one RefreshItems once all operations are done.  
### Description
Collapses the item with the specified ID, hiding its children. Allows to collapse the whole hierarchy under that item. 
* * *
