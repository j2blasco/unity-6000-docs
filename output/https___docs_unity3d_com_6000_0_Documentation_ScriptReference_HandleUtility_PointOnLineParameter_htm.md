* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.PointOnLineParameter.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).PointOnLineParameter
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
public static float PointOnLineParameter([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) linePoint, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) lineDirection); 
### Description
Returns the parameter for the projection of the `point` on the given line.
The return value can be negative if the projected point is in negative `lineDirection` relative to the `linePoint/` Additional resources: [ProjectPointLine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ProjectPointLine.html).
* * *
