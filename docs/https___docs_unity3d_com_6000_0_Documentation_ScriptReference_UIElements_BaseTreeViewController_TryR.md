* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.TryRemoveItem.html

#  [BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html).TryRemoveItem
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
public bool TryRemoveItem(int id, bool rebuildTree); 
### Parameters
Parameter | Description  
---|---  
id | The item id.  
rebuildTree | Whether we need to rebuild tree data. Set to <c>false</c> when doing multiple operations and call <see cref="TreeViewController.RebuildTree()" />.  
### Returns
**bool** Whether the item was successfully found and removed. 
### Description
Removes an item by id. 
* * *
