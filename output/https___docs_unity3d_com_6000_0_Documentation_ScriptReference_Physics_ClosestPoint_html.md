* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.ClosestPoint.html

#  [Physics](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.html).ClosestPoint
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClosestPoint([Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) point, [Collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.html) collider, [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) position, [Quaternion](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Quaternion.html) rotation); 
### Parameters
Parameter | Description  
---|---  
point | Location you want to find the closest point to.  
collider | The collider that you find the closest point on.  
position | The position of the collider.  
rotation | The rotation of the collider.  
### Returns
**Vector3** The point on the collider that is closest to the specified location. 
### Description
Returns a point on the given collider that is closest to the specified location.
Note that in case the specified location is inside the collider, or exactly on the boundary of it, the input location is returned instead.  
  
The collider can only be BoxCollider, SphereCollider, CapsuleCollider or a convex MeshCollider.  
  
Additional resources: [ClosestPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider.ClosestPoint.html).  
  

* * *
