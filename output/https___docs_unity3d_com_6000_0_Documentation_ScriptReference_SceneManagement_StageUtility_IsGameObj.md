* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.IsGameObjectRenderedByCameraAndPartOfEditableScene.html

#  [StageUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.StageUtility.html).IsGameObjectRenderedByCameraAndPartOfEditableScene
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
public static bool IsGameObjectRenderedByCameraAndPartOfEditableScene([GameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) gameObject, [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) camera); 
### Parameters
Parameter | Description  
---|---  
gameObject | The GameObject to check.  
camera | The Camera to check.  
### Returns
**bool** True if the GameObject is rendered by the camera and part of an editable scene. 
### Description
Specifies whether the given Camera currently renders the given GameObject and the GameObject is also part of an editable scene.
This is not related to culling, but simply checks if the stages of the GameObject and camera respectively means that the Camera is able to render the GameObject, and additionally that the scene the GameObject is in is editable, and not part of a visible but non-editable environment.
* * *
