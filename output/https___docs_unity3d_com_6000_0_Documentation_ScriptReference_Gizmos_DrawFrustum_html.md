* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.DrawFrustum.html

#  [Gizmos](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Gizmos.html).DrawFrustum
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
public static void DrawFrustum([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) center, float fov, float maxRange, float minRange, float aspect); 
### Parameters
Parameter | Description  
---|---  
center | The apex of the truncated pyramid.  
fov | Vertical field of view (ie, the angle at the apex in degrees).  
maxRange | Distance of the frustum's far plane.  
minRange | Distance of the frustum's near plane.  
aspect | Width/height ratio.  
### Description
Draw a camera frustum using the currently set Gizmos.matrix for its location and rotation.
* * *
