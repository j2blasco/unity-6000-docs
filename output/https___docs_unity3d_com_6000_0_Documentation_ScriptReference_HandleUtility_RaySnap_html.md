* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RaySnap.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).RaySnap
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
public static object RaySnap([Ray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Ray.html) ray); 
### Returns
**object** A boxed RaycastHit, null if nothing hit it. 
### Description
Casts `ray` against the Scene and reports whether an object lies in its path.
The `ray` only returns intersections with GameObjects that have a collider component attached to them.
* * *
