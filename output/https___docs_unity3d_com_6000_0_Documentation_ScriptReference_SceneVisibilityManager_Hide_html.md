* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.Hide.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).Hide
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
public void Hide([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeDescendants); 
## Declaration
public void Hide(GameObject[] gameObjects, bool includeDescendants); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to hide.  
gameObjects | Array of GameObjects to hide.  
includeDescendants | Whether to also hide descendants.  
### Description
Hides a GameObject, or an Array of GameObjects, and their descendants.
* * *
## Declaration
public void Hide([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | Scene containing GameObjects to hide.  
### Description
Hides all GameObjects in a scene.
* * *
