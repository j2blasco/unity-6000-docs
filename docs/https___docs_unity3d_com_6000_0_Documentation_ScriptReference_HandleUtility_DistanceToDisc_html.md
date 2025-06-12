* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToDisc.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).DistanceToDisc
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
public static float DistanceToDisc([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) normal, float radius); 
### Description
Returns the distance in pixels from the mouse pointer to a 3D disc.
Calculates the screen space distance from the mouse pointer to the disc (circle) at given world space `position` with the given `radius` and `normal`.  
  
Uses the current camera to determine the distance.  
  
Additional resources: [DistanceToCircle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.DistanceToCircle.html).
* * *
