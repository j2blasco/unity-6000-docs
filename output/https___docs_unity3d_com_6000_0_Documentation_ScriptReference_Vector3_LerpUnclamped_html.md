* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.LerpUnclamped.html

#  [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html).LerpUnclamped
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) LerpUnclamped([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) a, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) b, float t); 
### Description
Linearly interpolates between two vectors.
Interpolates between the vectors `a` and `b` by the interpolant `t`. This is most commonly used to find a point some fraction of the way along a line between two endpoints (e.g. to move an object gradually between those points).  
  
When `t` = 0 returns `a`. When `t` = 1 returns `b`. When `t` = 0.5 returns the point midway between `a` and `b`.  
  
Additional resources: [Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.Lerp.html).
* * *
