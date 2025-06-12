* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html

# ContactPoint2D
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
Details about a specific point of contact involved in a 2D physics collision.
A contact point describes a point of intersection between two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html). [ContactPoint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D.html) can only exist on [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) that are not set to be triggers as triggers do not define contact points.  
  
Additional resources: [Collider2D.isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-isTrigger.html), [Physics2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Physics2D.GetContacts.html), [Rigidbody2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.GetContacts.html), [Collider2D.GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.GetContacts.html) and [Collision2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html).
### Properties
Property | Description  
---|---  
[bounciness](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-bounciness.html) | The effective bounciness used for the ContactPoint2D.  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-collider.html) | The incoming Collider2D involved in the collision with the otherCollider.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-enabled.html) | Indicates whether the collision response or reaction is enabled or disabled.  
[friction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-friction.html) | The effective friction used for the ContactPoint2D.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-normal.html) | Surface normal at the contact point.  
[normalImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-normalImpulse.html) | Gets the impulse applied at the contact point along the ContactPoint2D.normal.  
[otherCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-otherCollider.html) | The other Collider2D involved in the collision with the collider.  
[otherRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-otherRigidbody.html) | The other Rigidbody2D involved in the collision with the rigidbody.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-point.html) | The point of contact between the two colliders in world space.  
[relativeVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-relativeVelocity.html) | Gets the relative velocity of the two colliders at the contact point (Read Only).  
[rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-rigidbody.html) | The incoming Rigidbody2D involved in the collision with the otherRigidbody.  
[separation](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-separation.html) | Gets the distance between the colliders at the contact point.  
[tangentImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-tangentImpulse.html) | Gets the impulse applied at the contact point which is perpendicular to the ContactPoint2D.normal.  
* * *
