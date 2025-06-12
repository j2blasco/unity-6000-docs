* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoNonJitteredProjectionMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).GetStereoNonJitteredProjectionMatrix
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
public [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) GetStereoNonJitteredProjectionMatrix([Camera.StereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
eye | Specifies the stereoscopic eye whose non-jittered projection matrix needs to be returned.  
### Returns
**Matrix4x4** The non-jittered projection matrix of the specified stereoscopic eye. 
### Description
Gets the non-jittered projection matrix of a specific left or right stereoscopic eye.
If you have configured the non-jittered stereo projection matrices with [Camera.CopyStereoDeviceProjectionMatrixToNonJittered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html), this function will return the VR device's original stereo projection matrices. If you have not used [Camera.CopyStereoDeviceProjectionMatrixToNonJittered](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html), this will return the same matrix as [Camera.GetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoProjectionMatrix.html).  
  
Use [Camera.GetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoProjectionMatrix.html) to get the jittered stereo projection matrices.  
  
For descriptions of jittered projection rendering see: [Camera.nonJitteredProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nonJitteredProjectionMatrix.html).
* * *
