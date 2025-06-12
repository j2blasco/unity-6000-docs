* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.GetSceneCullingMask.html

#  [EditorSceneManager](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.EditorSceneManager.html).GetSceneCullingMask
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
public static ulong GetSceneCullingMask([SceneManagement.Scene](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Scene.html) scene); 
### Parameters
Parameter | Description  
---|---  
scene | The scene to get the culling mask from.  
### Returns
**ulong** The scene's current culling mask as a bitfield. 
### Description
Return the culling mask set on the given Scene.
The culling mask for a Scene is used by Cameras to determine which Scenes should appear in the Cameras final render target. Culling masks are stored as a bitfield.
* * *
