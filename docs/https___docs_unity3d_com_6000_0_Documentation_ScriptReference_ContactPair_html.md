* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.html

# ContactPair
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
A pair of Colliders that belong to the bodies in the parent [ContactPairHeader](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairHeader.html) struct.
Contains an array of [ContactPairPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPairPoint.html)s that can be retrieved using the [GetContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.GetContactPoint.html) method.
### Properties
Property | Description  
---|---  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-collider.html) | The first Collider component of the ContactPair.  
[colliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-colliderInstanceID.html) | Instance ID of the first Collider in the ContactPair.  
[contactCount](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-contactCount.html) | The number of ContactPairPoints that this pair contains.  
[impulseSum](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-impulseSum.html) | Total impulse sum of the pair.  
[isCollisionEnter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-isCollisionEnter.html) | Whether or not this pair is equivalent to a pair reported in MonoBehaviour.OnCollisionEnter events.  
[isCollisionExit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-isCollisionExit.html) | Whether or not this pair is equivalent to a pair reported in MonoBehaviour.OnCollisionExit events.  
[isCollisionStay](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-isCollisionStay.html) | Whether or not this pair is equivalent to a pair reported in MonoBehaviour.OnCollisionStay events.  
[otherCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-otherCollider.html) | The second Collider component of the ContactPair.  
[otherColliderInstanceID](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair-otherColliderInstanceID.html) | Instance ID of the second Collider in the ContactPair.  
### Public Methods
Method | Description  
---|---  
[CopyToNativeArray](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.CopyToNativeArray.html) | Copies the internal ContactPairPoint buffer to the provided buffer.  
[GetContactPoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.GetContactPoint.html) | Gets the ContactPairPoint at the provided index of this pair.  
[GetContactPointFaceIndex](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPair.GetContactPointFaceIndex.html) | Get the index of a face that a particular contact point belongs to in this ContactPairPoint.  
* * *
