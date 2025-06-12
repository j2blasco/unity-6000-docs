* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles-currentCamera.html

#  [Handles](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.html).currentCamera
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
[Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) currentCamera; 
### Description
Gets or sets the camera that is currently rendering.
When set in the lifecycle of SceneView.OnGUI, Handles.currentCamera determines where 3D handles are drawn. Handles.currentCamera only sets the currently rendering camera, it does not set up the viewport. It is best practice to use [Handles.SetCamera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Handles.SetCamera.html) and not set the camera directly.
* * *
