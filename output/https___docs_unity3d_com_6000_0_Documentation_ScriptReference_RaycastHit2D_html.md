* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D.html

# RaycastHit2D
struct in UnityEngine
/
Implemented in:[UnityEngine.Physics2DModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.Physics2DModule.html)
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
Returns information about 2D Colliders detected by a 2D physics query in the scene.
The RaycastHit2D struct is used to return results from many 2D physics queries. It contains many pieces of information about a detection result including the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) detected along with extra detail such as the contact point, the distance traversed to that contact point, the contact normal at that contact point etc.  
  
When using any physics query that returns a RaycastHit2D, you should always first check to see if it contains a valid result which indicates that a hit (intersection) was detected. You can do this by checking if the RaycastHit2D is `true` or `false` (see code examples). Also, when the result is invalid, all the RaycastHit2D fields will be at their default.  
  
**NOTE** : This type is also used by the following physics queries:  
  
Additional resources: [Physics2D.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Raycast.html), [Physics2D.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Linecast.html), [Physics2D.BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.BoxCast.html), [Physics2D.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CapsuleCast.html), [Physics2D.CircleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.CircleCast.html), [Physics2D.GetRayIntersection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetRayIntersection.html), [Collider2D.Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Cast.html), [Rigidbody2D.Cast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Cast.html), [PhysicsScene2D.Raycast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.Raycast.html), [PhysicsScene2D.Linecast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.Linecast.html), [PhysicsScene2D.BoxCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.BoxCast.html), [PhysicsScene2D.CapsuleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.CapsuleCast.html), [PhysicsScene2D.CircleCast](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.CircleCast.html) and [PhysicsScene2D.GetRayIntersection](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsScene2D.GetRayIntersection.html).
### Properties
Property | Description  
---|---  
[centroid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-centroid.html) | The world space centroid (center) of the physics query shape when it intersects.  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-collider.html) | The Collider2D detected by the physics query.  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-distance.html) | The distance the physics query traversed before it detected a Collider2D.  
[fraction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-fraction.html) | The fraction of the distance specified to the physics query before it detected a Collider2D.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-normal.html) | The surface normal of the detected Collider2D.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-point.html) | The world space position where the physics query shape intersected with the detected Collider2D surface.  
[rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-rigidbody.html) | The Rigidbody2D that the Collider2D detected by the physics query is attached to.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-transform.html) | The Transform on the GameObject that the Collider2D is attached to.  
### Operators
Operator | Description  
---|---  
[bool](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RaycastHit2D-operator_RaycastHit2D.html) | Implicit operator used to return a true or false result indicating if the result is valid or not.  
* * *
