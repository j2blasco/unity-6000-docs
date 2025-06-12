* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.SetSceneCullingMask.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).SetSceneCullingMask
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
public static void SetSceneCullingMask([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene, ulong sceneCullingMask); 
### Parameters
Parameter | Description  
---|---  
scene | The scene to set the culling mask on.  
sceneCullingMask | The value of the culling mask, stored as a bitfield.  
### Description
Set the culling mask on this scene to this value. Cameras will only render objects in Scenes that have the same bits set in their culling mask.
* * *
