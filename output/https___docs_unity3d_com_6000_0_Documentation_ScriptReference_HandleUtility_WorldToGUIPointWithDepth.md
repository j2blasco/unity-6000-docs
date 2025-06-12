* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPointWithDepth.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).WorldToGUIPointWithDepth
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) WorldToGUIPointWithDepth([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) world); 
### Parameters
Parameter | Description  
---|---  
world | Point in world space.  
### Returns
**Vector3** A Vector3 where the x and y values relate to the 2D GUI position. The z value is the distance in world units from the camera. 
### Description
Convert a world space point to a 2D GUI position.
Uses the current camera to calculate the projection.  
  
Additional resources: [WorldToGUIPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPoint.html). [GUIPointToWorldRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToWorldRay.html), [RaySnap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RaySnap.html).
* * *
