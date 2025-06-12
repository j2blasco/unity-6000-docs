* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit.html

# WheelHit
struct in UnityEngine
/
Implemented in:[UnityEngine.VehiclesModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.VehiclesModule.html)
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
Contact information for the wheel, reported by [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html).
Friction for the [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html) is computed separately from the rest of the physics, using a slip based tire friction model. This allows for more realistic behaviour, but makes wheel colliders ignore standard [PhysicsMaterial](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PhysicsMaterial.html) settings.  
  
The way to simulate different ground materials is to query [WheelCollider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.html) for its collision information (see [WheelCollider.GetGroundHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetGroundHit.html)). Usually, you get the other collider the wheel is hitting, and modify the wheel's [WheelCollider.forwardFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-forwardFriction.html) and [WheelCollider.sidewaysFriction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider-sidewaysFriction.html) based on the physics material of the ground.  
  
The other members of the WheelHit structure are usually queried for information purposes or special effects. For example, a "slipping tire" sound can be played if [forwardSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-forwardSlip.html) or [sidewaysSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-sidewaysSlip.html) exceed some threshold.  
  
Additional resources: [WheelCollider.GetGroundHit](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelCollider.GetGroundHit.html).
### Properties
Property | Description  
---|---  
[collider](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-collider.html) | The other Collider the wheel is hitting.  
[force](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-force.html) | The magnitude of the force being applied for the contact.  
[forwardDir](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-forwardDir.html) | The direction the wheel is pointing in.  
[forwardSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-forwardSlip.html) | Tire slip in the rolling direction. Acceleration slip is negative, braking slip is positive.  
[normal](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-normal.html) | The normal at the point of contact.  
[point](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-point.html) | The point of contact between the wheel and the ground.  
[sidewaysDir](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-sidewaysDir.html) | The sideways direction of the wheel.  
[sidewaysSlip](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WheelHit-sidewaysSlip.html) | Tire slip in the sideways direction.  
* * *
