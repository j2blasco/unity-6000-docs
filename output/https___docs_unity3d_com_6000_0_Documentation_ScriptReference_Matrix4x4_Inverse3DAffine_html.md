* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.Inverse3DAffine.html

#  [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html).Inverse3DAffine
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
public static bool Inverse3DAffine([Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) input, ref [Matrix4x4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Matrix4x4.html) result); 
### Parameters
Parameter | Description  
---|---  
input | Input matrix to invert.  
result | The result of the inversion. Equal to the input matrix if the function fails.  
### Returns
**bool** Returns true and a valid result if the function succeeds, false and a copy of the input matrix if the function fails. 
### Description
Computes the inverse of a 3D affine matrix.
This function is dedicated to a non-singular matrix (typically, a transform matrix), otherwise, returns false and the result is a copy of the input matrix.
* * *
