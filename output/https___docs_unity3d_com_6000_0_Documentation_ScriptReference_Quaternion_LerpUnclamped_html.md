* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.LerpUnclamped.html

#  [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html).LerpUnclamped
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
public static [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) LerpUnclamped([Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) a, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) b, float t); 
### Description
Interpolates between `a` and `b` by `t` and normalizes the result afterwards. The parameter `t` is not clamped.
This is faster than Slerp but looks worse if the rotations are far apart.  
  
Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.Lerp.html), [SlerpUnclamped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.SlerpUnclamped.html).
* * *
