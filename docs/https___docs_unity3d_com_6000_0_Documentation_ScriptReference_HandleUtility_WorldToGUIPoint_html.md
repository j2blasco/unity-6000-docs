* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.WorldToGUIPoint.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).WorldToGUIPoint
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
public static [Vector2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) WorldToGUIPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) world); 
### Parameters
Parameter | Description  
---|---  
world | Point in world space.  
### Description
Convert a world space point to a 2D GUI position.
Uses the current camera to calculate the projection.  
  
Additional resources: [GUIPointToWorldRay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.GUIPointToWorldRay.html), [RaySnap](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.RaySnap.html).
* * *
