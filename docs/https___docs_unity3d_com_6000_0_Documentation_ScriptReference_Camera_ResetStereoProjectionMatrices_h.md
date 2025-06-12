* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.ResetStereoProjectionMatrices.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).ResetStereoProjectionMatrices
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
public void ResetStereoProjectionMatrices(); 
### Description
Reset the camera to using the Unity computed projection matrices for all stereoscopic eyes.
If Camera.SetStereoProjectionMatrices or [Camera.SetStereoProjectionMatrix](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.SetStereoProjectionMatrix.html) were used to provide custom projection matrices, this method reverts the camera back to using projection matrices provided by the VR SDK.
* * *
