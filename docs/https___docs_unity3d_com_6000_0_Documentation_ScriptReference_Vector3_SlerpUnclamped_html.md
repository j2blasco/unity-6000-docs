* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.SlerpUnclamped.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).SlerpUnclamped
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) SlerpUnclamped([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, float t); 
### Description
Spherically interpolates between two vectors.
Interpolates between `a` and `b` by amount `t`. The difference between this and linear interpolation (aka, "lerp") is that the vectors are treated as directions rather than points in space. The direction of the returned vector is interpolated by the angle and its [magnitude](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3-magnitude.html) is interpolated between the magnitudes of `from` and `to`.  
  
**Note:** This static method can slerp beyond the `a` and `b` vectors. This means `t` can be less than zero or greater than one.  
  
Additional resources: [Slerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Slerp.html).
* * *
