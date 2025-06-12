* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.html

# DistanceMetric
enumeration
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
### Description
Type of sorting to use while rendering.
By default, perspective cameras sort objects based on distance from camera position to the object center; and orthographic cameras sort based on distance along the view direction.  
  
If you're making a 2D game with a perspective camera, you might want to use [DistanceMetric.Orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.Orthographic.html) sort mode so that objects are sorted based on distance along the camera's view direction.
### Properties
Property | Description  
---|---  
[Perspective](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.Perspective.html) | Perspective sorting mode.  
[Orthographic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.Orthographic.html) | Orthographic sorting mode.  
[CustomAxis](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.DistanceMetric.CustomAxis.html) | Sort objects based on distance along a custom axis.  
* * *
