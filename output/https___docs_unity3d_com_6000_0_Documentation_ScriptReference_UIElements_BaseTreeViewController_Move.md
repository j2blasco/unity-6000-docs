* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.Move.html

#  [BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html).Move
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
public void Move(int id, int newParentId, int childIndex, bool rebuildTree); 
### Parameters
Parameter | Description  
---|---  
id | The ID of the item to move.  
newParentId | The new parent ID. -1 if moved at the root.  
childIndex | The child index to insert at under the parent. -1 will add as the last child.  
rebuildTree | Whether we need to rebuild tree data. Set to false when doing multiple operations.  
### Description
Moves an item by ID, to a new parent and child index. 
* * *
