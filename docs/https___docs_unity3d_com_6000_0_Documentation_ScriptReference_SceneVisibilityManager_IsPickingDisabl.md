* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.IsPickingDisabled.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).IsPickingDisabled
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
public bool IsPickingDisabled([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeDescendants); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to check.  
includeDescendants | Specify true to check the GameObject and all its descendants. Set to false to check the GameObject.  
### Returns
**bool** When includeDescendants is true, this method returns true when the GameObject and all its descendants have picking disabled. When includeDescendants is false, this method returns true when the GameObject has picking disabled. 
### Description
Checks the picking state of a GameObject and, optionally, its descendants.
When includeDescendants is true, this method returns true when the GameObject and all its descendants have picking disabled. When includeDescendants is false, this method returns true when the GameObject is hidden.
* * *
