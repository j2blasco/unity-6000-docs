* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.Show.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).Show
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
public void Show([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeDescendants); 
## Declaration
public void Show(GameObject[] gameObjects, bool includeDescendants); 
### Parameters
Parameter | Description  
---|---  
gameObject | GameObject to show.  
gameObjects | Array of GameObjects to show.  
includeDescendants | Whether to include descendants.  
### Description
Shows a GameObject, or an array of GameObjects, and its descendants.
* * *
## Declaration
public void Show([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | Scene containing GameObjects to show.  
### Description
Shows all GameObjects in scene.
* * *
