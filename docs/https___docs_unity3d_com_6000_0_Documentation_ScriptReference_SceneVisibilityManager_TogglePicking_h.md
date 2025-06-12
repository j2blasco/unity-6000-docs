* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.TogglePicking.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).TogglePicking
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
public void TogglePicking([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeDescendants); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject on which to toggle picking ability.  
includeDescendants | Whether to include descendants.  
### Description
Toggles the picking ability of a GameObject.
When includeDescendants is true, a descendant is set to the same picking state as the parent GameObject. When includeDescendants is false, the picking state of descendants are not affected.
* * *
