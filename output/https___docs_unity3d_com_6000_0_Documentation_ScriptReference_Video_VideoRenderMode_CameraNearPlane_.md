* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoRenderMode.CameraNearPlane.html

#  [VideoRenderMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoRenderMode.html).CameraNearPlane
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
### Description
Draw video content in front of a camera's scene.
Scene content is visible through any transparent areas of the video content.  
  
Use for cutscenes, splashscreens and videos that overlay the scene. Since the VideoPlayer has a transparency control, you can use this render mode to display the video on top of an active scene and still see as much of the scene as you want behind it. To control the transparency, use [VideoPlayer.targetCameraAlpha](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Video.VideoPlayer-targetCameraAlpha.html).  
  
The [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html) clipping planes determine where video content is rendered. Video content is offset by a factor of 0.00005. To render scene content on top of the video, you have to position it between [Camera.nearClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nearClipPlane.html) and [Camera.nearClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nearClipPlane.html) + ([Camera.farClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-farClipPlane.html) - [Camera.nearClipPlane](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nearClipPlane.html)) * 0.00005.
* * *
