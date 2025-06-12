* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.GetCombinedSceneCullingMaskForCamera.html

#  [Stage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneManagement.Stage.html).GetCombinedSceneCullingMaskForCamera
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
public ulong GetCombinedSceneCullingMaskForCamera(); 
### Returns
**ulong** The combined Scene culling mask for this Stage. Unity uses this mask on the Scene view Camera for renderer filtering. 
### Description
Gets the Scene culling mask from this Stage.
Depending on the currently open Stages, this can either be a Scene culling mask from a single Scene or a combined Scene culling mask from multiple Scenes. Unity uses the mask that this function returns on the Scene view Camera for renderer filtering.
* * *
