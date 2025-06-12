* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.IsCameraDrawModeEnabled.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).IsCameraDrawModeEnabled
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
public bool IsCameraDrawModeEnabled([SceneView.CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
mode | A [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) to check.  
### Returns
**bool** Returns true if the [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) is available in this [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html). Returns false otherwise. 
### Description
Returns true if mode is enabled in the current rendering setup, including custom validators.
* * *
