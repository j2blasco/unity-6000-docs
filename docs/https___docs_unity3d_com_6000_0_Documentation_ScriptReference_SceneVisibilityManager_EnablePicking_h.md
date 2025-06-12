* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.EnablePicking.html

#  [SceneVisibilityManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneVisibilityManager.html).EnablePicking
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
public void EnablePicking([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, bool includeDescendants); 
## Declaration
public void EnablePicking(GameObject[] gameObjects, bool includeDescendants); 
### Parameters
Parameter | Description  
---|---  
includeDescendants | Whether to include descendants.  
gameObject | GameObject on which to enable picking.  
gameObjects | Array of GameObjects on which to enable picking.  
### Description
Enables picking on a GameObject, or an array of GameObjects, and its descendants.
* * *
## Declaration
public void EnablePicking([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | Scene containing GameObjects on which to enable picking.  
### Description
Enables picking on all GameObjects in a Scene.
* * *
