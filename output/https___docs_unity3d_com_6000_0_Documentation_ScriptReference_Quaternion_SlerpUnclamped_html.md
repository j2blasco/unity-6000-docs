* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SlerpUnclamped.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).SlerpUnclamped
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) SlerpUnclamped([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) a, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) b, float t); 
### Parameters
Parameter | Description  
---|---  
a | Start unit quaternion value, returned when t = 0.  
b | End unit quaternion value, returned when t = 1.  
t | Interpolation ratio. Value is unclamped.  
### Returns
**Quaternion** A unit quaternion spherically interpolated between unit quaternions `a` and `b`. 
### Description
Spherically linear interpolates between unit quaternions `a` and `b` by t.
Additional resources: [LerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LerpUnclamped.html), [Slerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Slerp.html).
* * *
