* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ClosestPointToArc.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).ClosestPointToArc
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClosestPointToArc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) from, float angle, float radius); 
### Description
Get the point on an arc (in 3D space) which is closest to the current mouse position.
This function takes the arc defined by its parameters and "flattens" it into screen space. The closest point between the flattened arc and the current mouse position (also in screen space) is then found and converted back into a 3D point on the original 3D arc. This is useful for Handle GUIs that involve rotation of an object around the center of the arc; the 2D mouse movements are converted into 3D space in the familiar way used by Unity's built-in tools.
* * *
