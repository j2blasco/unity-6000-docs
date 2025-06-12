* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit.html

# RaycastHit
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
Structure used to get information back from a raycast.
Additional resources: [Physics.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Raycast.html), [Physics.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.Linecast.html), [Physics.RaycastAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics.RaycastAll.html).
### Properties
Property | Description  
---|---  
[articulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-articulationBody.html) | The ArticulationBody of the collider that was hit. If the collider is not attached to an articulation body then it is null.  
[barycentricCoordinate](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-barycentricCoordinate.html) | The barycentric coordinate of the triangle we hit.  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-collider.html) | The Collider that was hit.  
[colliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-colliderInstanceID.html) | Instance ID of the Collider that was hit.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-distance.html) | The distance from the ray's origin to the impact point.  
[lightmapCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-lightmapCoord.html) | The uv lightmap coordinate at the impact point.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-normal.html) | The normal of the surface the ray hit.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-point.html) | The impact point in world space where the ray hit the collider.  
[rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-rigidbody.html) | The Rigidbody of the collider that was hit. If the collider is not attached to a rigidbody then it is null.  
[textureCoord](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord.html) | The uv texture coordinate at the collision location.  
[textureCoord2](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-textureCoord2.html) | The secondary uv texture coordinate at the impact point.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-transform.html) | The Transform of the rigidbody or collider that was hit.  
[triangleIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit-triangleIndex.html) | The index of the triangle that was hit.  
* * *
