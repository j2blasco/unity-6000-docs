* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.GetLocalPositionAndRotation.html

#  [TransformAccess](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Jobs.TransformAccess.html).GetLocalPositionAndRotation
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
public void GetLocalPositionAndRotation(out [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) localPosition, out [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) localRotation); 
### Description
Gets the position and rotation of the transform in local space relative to its parent transform.
When getting both the position and rotation of a transform, calling this method is slightly more efficient than querying localPosition and localRotation individually.  
  
If the transform has no parent, then calling this is equivalent to calling GetPositionAndRotation.
* * *
