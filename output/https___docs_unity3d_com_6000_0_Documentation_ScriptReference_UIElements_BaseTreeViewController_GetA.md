* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.GetAllItemIds.html

#  [BaseTreeViewController](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UIElements.BaseTreeViewController.html).GetAllItemIds
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
public IEnumerable<int> GetAllItemIds(IEnumerable<int> rootIds); 
### Parameters
Parameter | Description  
---|---  
rootIds | Root IDs to start from. If null, will use the tree root ids.  
### Returns
**IEnumerable <int>** All items IDs in the tree, starting from the specified IDs. 
### Description
Returns all item IDs that can be found in the tree, optionally specifying root IDs from where to start. 
* * *
