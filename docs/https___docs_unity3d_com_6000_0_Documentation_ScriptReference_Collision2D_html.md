* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.html

# Collision2D
class in UnityEngine
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
Collision details returned by 2D physics callback functions.
The collisions details are returned by [MonoBehaviour.OnCollisionEnter2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionEnter2D.html), [MonoBehaviour.OnCollisionStay2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionStay2D.html) and [MonoBehaviour.OnCollisionExit2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.OnCollisionExit2D.html) callbacks. It details which [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) and [Rigidbody2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D.html) pairs are involved in the collision as well as contact points where the [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) meet. **Note:** During the `OnCollisionExit2D` event, there are no contacts to be retrieved.
### Properties
Property | Description  
---|---  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-collider.html) | The incoming Collider2D involved in the collision with the otherCollider.  
[contactCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-contactCount.html) | Gets the number of contacts for this collision.  
[contacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-contacts.html) | The specific points of contact with the incoming Collider2D. You should avoid using this as it produces memory garbage. Use GetContact or GetContacts instead.  
[enabled](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-enabled.html) | Indicates whether the collision response or reaction is enabled or disabled.  
[gameObject](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-gameObject.html) | The incoming GameObject involved in the collision.  
[otherCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-otherCollider.html) | The other Collider2D involved in the collision with the collider.  
[otherRigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-otherRigidbody.html) | The other Rigidbody2D involved in the collision with the rigidbody.  
[relativeVelocity](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-relativeVelocity.html) | The relative linear velocity of the two colliding objects (Read Only).  
[rigidbody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-rigidbody.html) | The incoming Rigidbody2D involved in the collision with the otherRigidbody.  
[transform](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D-transform.html) | The Transform of the incoming object involved in the collision.  
### Public Methods
Method | Description  
---|---  
[GetContact](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.GetContact.html) | Gets the contact point at the specified index.  
[GetContacts](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collision2D.GetContacts.html) | Retrieves all contact points for contacts between collider and otherCollider.  
* * *
