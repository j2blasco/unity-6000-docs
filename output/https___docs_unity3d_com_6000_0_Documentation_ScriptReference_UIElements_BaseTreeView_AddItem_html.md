* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.AddItem.html

#  [BaseTreeView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeView.html).AddItem
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
public void AddItem(TreeViewItemData<T> item, int parentId, int childIndex, bool rebuildTree); 
### Parameters
Parameter | Description  
---|---  
item | Item to add.  
parentId | The parent id for the item.  
childIndex | The child index in the parent's children list.  
rebuildTree | Whether we should call RebuildTree and RefreshItems or not. Set to false when doing multiple additions to save a few rebuilds.  
### Description
Adds an item to the existing tree. 
* * *
