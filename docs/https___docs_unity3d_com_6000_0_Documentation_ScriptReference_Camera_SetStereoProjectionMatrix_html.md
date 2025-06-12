* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoProjectionMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).SetStereoProjectionMatrix
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Camera.html "Go to Camera Component in the Manual")
## Declaration
public void SetStereoProjectionMatrix([Camera.StereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.html) eye, [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) matrix); 
### Parameters
Parameter | Description  
---|---  
eye | Specifies the stereoscopic eye whose projection matrix needs to be set.  
matrix | The matrix to be set.  
### Description
Sets a custom projection matrix for a specific stereoscopic eye.
In general it is recommended to stick with the projection matrices provided by the VR SDK to ensure accurate stereoscopic rendering. However for some specific scenarios it can be useful to override the projection matrices to achieve specific effects. For example, custom projection matrices would be required to implement binoculars in VR. In order to process custom projection matrix per eye, [RenderingPath](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RenderingPath.html) has to be set to Multi Pass in player settings.  
  
Calling [Camera.ResetStereoProjectionMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoProjectionMatrices.html) will revert the camera to using projection matrices provided by the VR SDK.
* * *
