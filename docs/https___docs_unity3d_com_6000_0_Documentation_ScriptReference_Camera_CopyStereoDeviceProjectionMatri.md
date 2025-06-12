* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CopyStereoDeviceProjectionMatrixToNonJittered.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).CopyStereoDeviceProjectionMatrixToNonJittered
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
public void CopyStereoDeviceProjectionMatrixToNonJittered([Camera.StereoscopicEye](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.StereoscopicEye.html) eye); 
### Parameters
Parameter | Description  
---|---  
eye | Specifies the stereoscopic eye whose non-jittered projection matrix will be sourced from the VR SDK.  
### Description
Sets the non-jittered projection matrix, sourced from the VR SDK.
With traditional rendering, the application is responsible for generating the non-jittered and jittered projection matrices. However, in VR rendering, the projection matrices are sourced from the VR SDK. Therefore, if the intention is to jitter the VR projection matrices, that would indicate the non-jittered projection matrices are the ones provided by the VR SDK. This API provides this functionality by copying the VR SDK projection matrices directly into the non-jittered stereo projection matrix set.  
  
Use Camera.GetNonJitteredStereoProjectionMatrix to get the non-jittered stereo projection matrices.  
  
Use [Camera.SetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoProjectionMatrix.html) and [Camera.GetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.GetStereoProjectionMatrix.html) to set and get the jittered stereo projection matrices, respectively.  
  
For descriptions of jittered projection rendering see: [Camera.nonJitteredProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera-nonJitteredProjectionMatrix.html).
* * *
