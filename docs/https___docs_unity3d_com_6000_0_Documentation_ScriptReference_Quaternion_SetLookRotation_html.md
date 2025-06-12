* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SetLookRotation.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).SetLookRotation
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Quaternion.html "Go to Quaternion Component in the Manual")
## Declaration
public void SetLookRotation([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) view, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) up = Vector3.up); 
### Parameters
Parameter | Description  
---|---  
view | The direction to look in.  
up | The vector that defines in which direction up is.  
### Description
Creates a rotation with the specified `forward` and `upwards` directions.
The result is applied to this quaternion. If used to orient a Transform, the Z axis will be aligned with `forward/` and the Y axis with `upwards`, assuming these vectors are orthogonal. Logs an error if the forward direction is zero.  
  
Additional resources: [LookRotation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LookRotation.html).
* * *
