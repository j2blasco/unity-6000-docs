* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoViewMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).GetStereoViewMatrix
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
public [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) GetStereoViewMatrix([Camera.StereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
eye | Specifies the stereoscopic eye whose view matrix needs to be returned.  
### Returns
**Matrix4x4** The view matrix of the specified stereoscopic eye. 
### Description
Gets the left or right view matrix of a specific stereoscopic eye.
The view matrix will be provided by the VR SDK unless [Camera.SetStereoViewMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoViewMatrix.html) or Camera.SetStereoViewMatrices have been used, in which case this method will return the value given to those methods. You can use [Camera.ResetStereoViewMatrices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoViewMatrices.html) to revert the camera to using view matrices provided by the VR SDK.
* * *
