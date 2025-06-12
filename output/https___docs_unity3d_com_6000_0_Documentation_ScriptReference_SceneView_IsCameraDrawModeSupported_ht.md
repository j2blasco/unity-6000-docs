* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.IsCameraDrawModeSupported.html

#  [SceneView](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.html).IsCameraDrawModeSupported
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
public bool IsCameraDrawModeSupported([SceneView.CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) mode); 
### Parameters
Parameter | Description  
---|---  
mode | A [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) to check.  
### Returns
**bool** Returns true if the current rendering configuration supports the [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html). 
### Description
Checks if the current rendering configuration supports the [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html). The check includes custom validators.
A rendering configuration might not support a [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) if the mode has a feature that the current render pipeline does not support. For example, if the render pipeline does not support Enlighten Realtime Global Illumination, and [CameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView.CameraMode.html) has a property [DrawCameraMode.RealtimeAlbedo](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DrawCameraMode.RealtimeAlbedo.html), this method returns false.  
  
To register support for a draw mode feature in a custom render pipeline, use [SceneView.onValidateCameraMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/SceneView-onValidateCameraMode.html) to add a draw mode validation callback.
* * *
