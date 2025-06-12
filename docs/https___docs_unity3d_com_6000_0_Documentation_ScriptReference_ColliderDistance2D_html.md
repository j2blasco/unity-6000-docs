* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html

# ColliderDistance2D
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
Represents the separation or overlap of two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
The [ColliderDistance2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D.html) primarily defines a point on the exterior of each [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) along with the [distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html) between those two points. The [distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html) between them can be positive indicating that the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) are separated (not overlapped), zero indicating that they are touching (but not overlapped) or negative indicating that they are overlapped.  
  
A [normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-normal.html) is provided that is a normalized vector that points from [pointB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-pointB.html) to [pointA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-pointA.html). This vector, when scaled with the [distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html), provide a vector that can be used to move the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) so that they are no longer overlapped (if the [distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html) is negative) or so they are touching (if the [distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html) is positive).  
  
A common use-case for this is solving overlaps between two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), particularly when attached to a [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) set to be [RigidbodyType2D.Kinematic](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html).  
  
Additional resources: [Physics2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.Distance.html), [Collider2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.Distance.html) and [Rigidbody2D.Distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.Distance.html).
### Properties
Property | Description  
---|---  
[distance](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-distance.html) | Gets the distance between two colliders.  
[isOverlapped](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-isOverlapped.html) | Gets whether the distance represents an overlap or not.  
[isValid](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-isValid.html) | Gets whether the distance is valid or not.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-normal.html) | A normalized vector that points from pointB to pointA.  
[pointA](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-pointA.html) | A point on a Collider2D that is a specific distance away from pointB.  
[pointB](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ColliderDistance2D-pointB.html) | A point on a Collider2D that is a specific distance away from pointA.  
* * *
