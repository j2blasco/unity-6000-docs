* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.GetPositionAndRotation.html

#  [TransformAccess](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.html).GetPositionAndRotation
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
public void GetPositionAndRotation(out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, out [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Description
Gets the position and rotation of the transform in world space.
When getting both the position and rotation of a transform, calling this method is more efficient than querying to position and rotation individually.
* * *
