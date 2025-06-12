* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.Dot.html

#  [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html).Dot
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
public static float Dot([Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) lhs, [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) rhs); 
### Description
Dot Product of two vectors.
Returns `lhs` `.` `rhs`.  
  
For normalized vectors Dot returns 1 if they point in exactly the same direction; -1 if they point in completely opposite directions; and a number in between for other cases (e.g. Dot returns zero if vectors are perpendicular).  
  
For vectors of arbitrary length the Dot return values are similar: they get larger when the angle between vectors decreases.
* * *
