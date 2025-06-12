* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.MoveTowards.html

#  [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html).MoveTowards
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
public static [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) MoveTowards([Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) current, [Vector4](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.html) target, float maxDistanceDelta); 
### Description
Moves a point `current` towards `target`.
This is essentially the same as [Vector4.Lerp](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector4.Lerp.html) but instead the function will ensure that the speed never exceeds `maxDistanceDelta`. Negative values of `maxDistanceDelta` pushes the vector away from `target`.
* * *
