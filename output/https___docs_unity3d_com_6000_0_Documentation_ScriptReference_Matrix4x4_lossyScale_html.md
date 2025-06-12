* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4-lossyScale.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).lossyScale
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
[Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lossyScale; 
### Description
Attempts to get a scale value from the matrix. (Read Only)
Scale can only be represented correctly by a 3x3 matrix instead of a 3 component vector, if the given matrix has been skewed for example. `lossyScale` is a convenience property which attempts to match the scale from the matrix as much as possible. If the given matrix is orthogonal, the value will be correct.
* * *
