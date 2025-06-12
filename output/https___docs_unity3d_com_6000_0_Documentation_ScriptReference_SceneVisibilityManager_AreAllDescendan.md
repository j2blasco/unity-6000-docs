* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.AreAllDescendantsHidden.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).AreAllDescendantsHidden
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
public bool AreAllDescendantsHidden([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to check.  
### Returns
**bool** Returns true if all descendants are hidden. 
### Description
Checks whether all the descendants of a GameObject are hidden.
* * *
## Declaration
public bool AreAllDescendantsHidden([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | Scene to check.  
### Returns
**bool** Returns true if all root GameObjects of the Scene and all their descendants are hidden. 
### Description
Checks whether root GameObjects, and all their descendants, are hidden in a Scene.
* * *
