* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceReceiveLayers.html

#  [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).forceReceiveLayers
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
[LayerMask](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LayerMask.html) forceReceiveLayers; 
### Description
The Layers that this [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) can receive forces from during a Collision contact with another [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html).
When a collision occurs between two [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html), both Colliders would normally receive a force from each other that separates them. Both Colliders have a Layer assigned to them respectively, which can be the same or different Layer(s). For the forces to apply, each Collider must send a force to the Layer that is assigned to the other Collider, while also receiving a force on their own Layer from the other Collider. Thus, both Colliders must mutually agree on which Layers the forces are being sent and received.  
  
The [forceReceiveLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceReceiveLayers.html) property allows you to select which Layers that the Collider receives force from, while [forceSendLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceSendLayers.html) allows you to select which Layers the Collider sends a force to.  
  
**NOTES** : 
  * Because forces only relate to a Collision contact, this features does not apply when either [Collider2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D.html) is set to be a trigger via [Collider2D.isTrigger](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-isTrigger.html) and does not affect mutual forces applied by a [Joint2D](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Joint2D.html).
  * Any [Rigidbody2D.bodyType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rigidbody2D-bodyType.html) can send forces; however, only a [Dynamic Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Dynamic.html) can receive forces. Neither [Kinematic Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Kinematic.html) nor [Static Body Type](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/RigidbodyType2D.Static.html) can receive forces.
  * Forces being sent and received do not affect Collision callbacks which are still called even if no forces are applied.
  * During a Collision callback, any impulses reported by [ContactPoint2D.normalImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-normalImpulse.html) or [ContactPoint2D.tangentImpulse](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ContactPoint2D-tangentImpulse.html) will be the impulses that would have been applied if [forceSendLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceSendLayers.html) and [forceReceiveLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceReceiveLayers.html) were not used.


Additional resources: [Collider2D.forceSendLayers](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Collider2D-forceSendLayers.html).
* * *
