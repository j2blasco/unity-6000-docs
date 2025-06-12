* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.CalculateObliqueMatrix.html

#  [Camera](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Camera.html).CalculateObliqueMatrix
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
public [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) CalculateObliqueMatrix([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) clipPlane); 
### Parameters
Parameter | Description  
---|---  
clipPlane | Vector4 that describes a clip plane.  
### Returns
**Matrix4x4** Oblique near-plane projection matrix. 
### Description
Calculates and returns oblique near-plane projection matrix.
Given a clip plane vector, this function returns camera's projection matrix which has this clip plane set as its near plane.
* * *
